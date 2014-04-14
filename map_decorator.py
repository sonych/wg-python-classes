# coding: utf-8

import time


# task 1
# custom map

def map_rq(func, sequence):
    if sequence:
        return [func(sequence[0])] + map_rq(func, sequence[1:]) #<<<< would not works with generators
    else:
        return []


def map_yield(func, sequence):
    for item in sequence:
        yield func(item)


def map_rq_yield(func, sequence):
    if sequence:
        yield [func(sequence[0])] + list(map_rq_yield(func, sequence[1:]))
    else:
        yield []

#In [17]: for i in map_rq_yield(str, range(10)):
#   ....:     print i
#   ....:
#['0', ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', []]]]]]]]]]]

# Task 2
# Profiling decorator

def time_me(time_func, statistic):
    statistic['num_calls'] = 0
    statistic['cum_time'] = 0

    def decorator(func):
        def wrapper(*args, **kwargs):
            t1 = time_func()
            return func(*args, **kwargs)
            t2 = time_func()
            statistic['cum_time'] += t2 - t1
            statistic['num_calls'] += 1
        return wrapper
    return decorator
