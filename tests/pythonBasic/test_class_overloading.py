def successor(number):
    return number+1

def test_succssor():
    assert successor(1)==1
    assert successor(1.6) ==1.6

def f(n):
    return n+42
def f(n,m):
    return n+m +42

def f(n, m=None):
    if m:
        return n+m +42
    else:
        return n+42
def f(*x):
    if len(x) ==1:
        return x[0] + 42
    else:
        return x[0]+x[1]+42
def test_overloading():
    assert f(3,4)== 49
    # as f was must has 2 parameers ,so following will throw an error
    assert f(3) ==45

