# Task 3

# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules
# ' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def arg_check(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            my_func = func(*args, **kwargs)
            name = ''.join(args)
            if len(name) > max_length:
                return f'User name must be no longer than {max_length} characters'
            if not isinstance(name, type_):
                return f'Type of your name must be{type_}'
            for word in contains:
                if word not in name:
                    return f'Should contain following characters {contains}'
            return my_func

        return wrap

    return arg_check


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan('johndoe05@gmail.com'))
    print(create_slogan('S@SH05'))
