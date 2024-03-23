def wrap_text(beginning_symbol, end_symbol, text):
    return f"{beginning_symbol}{text}{end_symbol}"


def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return wrap_text("<b>", "</b>", result)

    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return wrap_text("<i>", "</i>", result)

    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return wrap_text("<u>", "</u>", result)

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))

print()


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
