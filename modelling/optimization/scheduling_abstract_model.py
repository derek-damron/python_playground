import pyomo.environ as pyo

def create():
    workers = (
        "Adam",
        "Bob",
        "Cynthia",
    )

    customers = (
        "Frank",
        "Ginny",
        "Hannah",
    )

    days = (
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    )
    
    model = pyo.AbstractModel()
    
    # Define sets
    model.workers = pyo.Set(initialize=workers)
    model.customers = pyo.Set(initialize=customers)
    model.days = pyo.Set(initialize=days)
    
    # Define parameters
    model.worker_schedules = pyo.Param(
        model.workers * model.days,
        initialize = 0,
        within = pyo.Binary
    )
    model.customer_requests = pyo.Param(
        model.customers * model.days,
        initialize = 0,
        within = pyo.Binary
    )
    
    # Define variables
    model.assignments = pyo.Var(
        model.workers * model.customers * model.days,
        domain = pyo.Binary,
        initialize = 0
    )
    
    # Define constraints
    #    1) Each customer assigned to exactly 1 worker
    #    1.1) Each customer assigned to at most 1 worker (allows for partial solutions if 1 is deactivated)
    #    2) Each customer only assigned on a requested day
    #    3) Each worker only assigned on a scheduled day
    
    def exactly_one_worker_per_customer(model, customer):
        n_workers_assigned_to_customer = sum(
            model.assignments[worker, customer, day]
            for worker in model.workers
            for day in model.days
        )
        return n_workers_assigned_to_customer == 1
    model.exactly_one_worker_per_customer = pyo.Constraint(
        model.customers,
        rule = exactly_one_worker_per_customer
    )
    
    def at_most_one_worker_per_customer(model, customer):
        n_workers_assigned_to_customer = sum(
            model.assignments[w, customer, d]
            for w in model.workers
            for d in model.days
        )
        return n_workers_assigned_to_customer <= 1
    model.at_most_one_worker_per_customer = pyo.Constraint(
        model.customers,
        rule = at_most_one_worker_per_customer
    )
    
    def at_most_one_customer_per_worker(model, worker):
        n_customers_assigned_to_worker = sum(
            model.assignments[worker, c, d]
            for c in model.customers
            for d in model.days
        )
        return n_customers_assigned_to_worker <= 1
    model.at_most_one_customer_per_worker = pyo.Constraint(
        model.workers,
        rule = at_most_one_customer_per_worker
    )

    def customer_assigned_on_nonrequested_day(model, customer):
        assigned_on_nonrequested_day = sum(
            model.assignments[w, customer, d] * (1 - model.customer_requests[customer, d])
            for w in model.workers
            for d in model.days
        )
        return assigned_on_nonrequested_day == 0
    model.customer_assigned_on_nonrequested_day = pyo.Constraint(
        model.customers,
        rule = customer_assigned_on_nonrequested_day
    )

    def worker_assigned_on_nonscheduled_day(model, worker):
        assigned_on_nonscheduled_day = sum(
            model.assignments[worker, c, d] * (1 - model.worker_schedules[worker, d])
            for c in model.customers
            for d in model.days
        )
        return assigned_on_nonscheduled_day == 0
    model.worker_assigned_on_nonscheduled_day = pyo.Constraint(
        model.workers,
        rule = worker_assigned_on_nonscheduled_day
    )
    
    # Define our objective
    # -> Total number of matches
    def get_legit_matches(model):
        # Multiply assignments by the 
        legit_matches = [
            model.assignments[w, c, d] * model.worker_schedules[w, d] * model.customer_requests[c, d]
            for (w, c, d), p in model.assignments.items()
        ]
        return sum(legit_matches)
    
    model.objective = pyo.Objective(
        rule = get_legit_matches,
        sense = pyo.maximize
    )
    
    return model

def get_matches(model):
    matches = set()
    for combo, matched in model.assignments.get_values().items():
        if matched == 1:
            matches.add(combo)
    return matches

def get_all_solutions(model):
    solver = pyo.SolverFactory("glpk")
    
    model.c = pyo.ConstraintList()
    solutions = set()

    while True:
        expr = 0
        for j in model.assignments:
            if pyo.value(model.assignments[j]) == 0:
                expr += model.assignments[j]
            else:
                expr += (1 - model.assignments[j])
        model.c.add( expr >= 1 )
        results = solver.solve(model)
        if get_matches(model) in solutions:
            break
        solutions.add(frozenset(get_matches(model)))

    return solutions