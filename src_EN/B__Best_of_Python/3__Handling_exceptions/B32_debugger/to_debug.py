
def f1(a, b, c):
    print("Entering f1")
    a = min(a, 5)
    print("After first instruction")
    d = a * b + c
    print("After second instruction")
    idx = 0
    while d < 100:
        d += 1
        f2(a, d)
        idx += 1
    print("Exiting f1")


def f2(a, d):
    print("Entering f2")
    e = a ** (d%5)
    f3()
    print(f"Conditionnal breakpoint: `e`>50")
    print("Exiting f2")
    

def f3():
    print("Entering f3")
    print("Still in f3")
    print("Exiting f3")


f1(7, 8, 4)