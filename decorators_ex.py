def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper


@start_end_decorator  # print_name = start_end_decorator(print_name)
def print_name():
    print('serkan')


print_name()

import functools


def sum_of_digits(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        total_sum = 0
        func_result = func(*args, **kwargs)
        for digit in str(func_result):
            total_sum += int(digit)
        return total_sum

    return wrapper


@sum_of_digits
def add_five(x):
    return x + 5


x = add_five(11)
print(x)
print(help(add_five))
print(add_five.__name__)


# Decorator function arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet('Alex')






# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


def start_end_decorator_2(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('End')
    return wrapper



@debug
@start_end_decorator_2
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')

import functools


class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")

@CountCalls
def say_hello(num):
    print("Hello!")


say_hello(5)
say_hello(5)