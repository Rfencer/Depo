from functools import wraps


def type_logger(func):
    @wraps(func)
    def check_type(*args):
        for i in args:
            print(f'{i} is {type(i)}')
        return func(*args)
    return check_type

@type_logger
def calc_cube(*args):
    return [x**3 for x in args]


a = calc_cube(5,4.4,2,534.2)
print(calc_cube.__name__)
print(a)
