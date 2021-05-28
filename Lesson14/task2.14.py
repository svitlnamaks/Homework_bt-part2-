# Task 2
# Write a decorator that takes a list of stop words and replaces them with *inside the decorated function

def stop_words(words: list):
    words = []

    def my_func(func): ...

    return my_func(func)


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    a = f"{name} drinks pepsi in his brand new BMW!"
    return a


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
