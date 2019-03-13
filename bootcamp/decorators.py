# Decorators

from functools import wraps


def log_function(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''I AM I WRAPPER FUNCTION'''
        print(f'Executing: {fn.__name__}{args}')
        print(f'Docstring: {fn.__doc__}')
        return f'Result:    {fn(*args, **kwargs)}'

    return wrapper


@log_function
def add(x, y):
    '''Adds two numbers together'''
    return x + y


@log_function
def square(x):
    '''Returns the square of a number'''
    return x*x


@ log_function
def divide(x, y):
    '''Divides the first number by the second number'''
    return x / y


# print(divide(75,12))
# print(add(4566, 1659))
# print(square(1748))
# help(divide)


# Speed Test

from time import time
from time import sleep
from datetime import datetime as dt

def speed_test(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        print(f'Executing: {fn.__name__}{args, kwargs}')
        print(f'Docstring: {fn.__doc__}')
        start_time = round(time(), 2)
        result = fn(*args, **kwargs)
        end_time = round(time(), 2)
        print(f'Duration:  {end_time - start_time}')
        print(f'Result:    {result}')

        return result

    return wrapper


@speed_test
def test_list(n):
    '''Uses a list comprehension to calculate the sum of n in range n'''
    return sum([x for x in range(n)])


@speed_test
def test_generator(n):
    '''Uses a generator to calculate the sum of n in range n'''
    return sum(x for x in range(n))


# Enforcing types with a decorator

def enforce(*types):

    def decorator(fn):

        def new_func(*args, **kwargs):
            
            # Converts args into something mutable and explicity casts to types
            new_args = []
            for (a, t) in zip(args, types):
                new_args.append(t(a))

            return fn(*new_args, **kwargs)

        return new_func

    return decorator


@enforce(str, int)
def repeat_msg(msg, times):

    for i in range(times):
        print(msg)


# repeat_msg('Ohai Mark', '3')


def delay(t):

    def decorator(fn):

        @wraps(fn)
        def delay(*args, **kwargs):

            print(f'There will be a delay of {t} seconds before executing {fn.__name__}{args}{kwargs}')
            sleep(t)

            return fn(*args, **kwargs)

        return delay

    return decorator


@delay(5)
def get_time():

    print(f'The current date and time is {dt.now()}')


get_time()