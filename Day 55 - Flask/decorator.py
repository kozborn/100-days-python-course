

class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False



def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            func()
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print("Creating Blog Post")


# TODO: Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"You called {func.__name__}({', '.join(str(argument).strip() for argument in args)})")
        print(f"It returned: {result}")
        return result
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
a_function(4, 5, 6)