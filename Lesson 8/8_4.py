from functools import wraps


def val_checker(arg):
    def decorator(func):
        @wraps(func)
        def check_value(x):
            if not arg(x):
                raise ValueError('cant be negative')
            return func(x)

        return check_value

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(calc_cube.__name__)
print(a)

a = calc_cube(-5)
