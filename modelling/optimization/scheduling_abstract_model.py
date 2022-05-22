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
    #    1) Each customer assigned to only 1 worker
    def at_most_one_worker_per_customer(model, customer):
        n_workers_assigned_to_customer = sum(
            model.assignments[worker, customer, day]
            for worker in model.workers
            for day in model.days
        )
        return n_workers_assigned_to_customer <= 1
    
    model.at_most_one_worker_per_customer = pyo.Constraint(
        model.customers,
        rule = at_most_one_worker_per_customer
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
