# Task 1
# Write a decorator that prints a function with arguments passed to it.

# NOTE! It should print the function, not the result of its execution!
# For example:

# "add called with 4, 5"
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapped_func(*args):
        return f'Function {func.__name__} was called .Function takes following arguments {args}'

    return wrapped_func


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    print(square_all(1, 2, 3, 4, 5, ))
    print(add(5, 6))
