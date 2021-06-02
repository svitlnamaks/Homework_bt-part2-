# Task 2
# Write a decorator that takes a list of stop words and replaces them with *inside the decorated function

from functools import wraps


def stop_words_list(words: list, space='=( '):
    def stop_words_inner(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            our_func = func(*args, **kwargs)
            rep = ''

            for word in str(our_func).split():
                if word in words:
                    rep += space
                else:
                    rep += word + ' '
            return rep

        return wrap

    return stop_words_inner


@stop_words_list(['pepsi', 'Volvo'])
def create_slogan(name: str):
    return f'{name} drinc pepsi in his brand new Volvo'


if __name__ == '__main__':
    my_slogan = create_slogan('Oleksandr')
    print(my_slogan)
