from .module_2 import f1, f2

def f3(a, b, c):
    if c=='sum':
        return f1(a, b)
    elif c=='division':
        try:
            result = f2(a, b)
        except ZeroDivisionError as e:
            print("'b' is zero!'")
        else:
            return result
    else:
        print("'c' must be one 'sum' or 'division'")