import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def insertion_sort(l, log=False):
    if l == []:
        return l
    l_len = len(l)
    i = 0
    while i < l_len:
        j = i
        while 0 < j and l[j] < l[j-1]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
        i += 1
        if log:
            logging.info('[%s]' % ', '.join(str(x) for x in l))
    return l

def bubble_sort(l, log=False):
    if l == []:
        return l
    i = 0
    j = len(l)
    while 0 < j:
        while i < (j-1):
            if l[i+1] < l[i]:
                l[i], l[i+1] = l[i+1], l[i]
            i += 1
        i = 0
        j -= 1
        if log:
            logging.info('[%s]' % ', '.join(str(x) for x in l))
    return l

def selection_sort(l, log=False):
    if l == []:
        return l
    l_len = len(l)
    i = 0
    while i < l_len:
        j = i+1
        j_min = i
        while j < l_len:
            if l[j] < l[j_min]:
                j_min = j
            j += 1
        if i != j_min:
            l[i], l[j_min] = l[j_min], l[i]
        i += 1
        if log:
            logging.info('[%s]' % ', '.join(str(x) for x in l))
    return l

def quicksort(l, lo=None, hi=None, log=False):
    if l == []:
        return l
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(l) - 1
    p = _quicksort_partition_around_pivot(l, lo, hi)
    if log:
        logging.info('[%s]' % ', '.join(str(x) for x in l))
    if lo < p:
        quicksort(l, lo, p, log)
    if p + 1 < hi:
        quicksort(l, p+1, hi, log)
    return l
    
def _quicksort_partition_around_pivot(l, lo, hi):
    pivot = l[hi]
    i = lo
    j = hi - 1
    while i <= j:
        if pivot < l[i]:
            l[i:(hi+1)] = l[(i+1):(hi+1)] + [l[i]]
            j -= 1
        else:
            i += 1
    return i - 1
        