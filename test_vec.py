import numpy as np

from vector import Vec


def inerror(val1, val2, error = 1e-10):
    return abs(val2 - val2) < error



def test_len():
    
    a = Vec([1, 2, 3])
    assert len(a) == 3
    return


def test_getitem():
    a = Vec([1, 2, 3, 4, 5])
    
    assert a[3] == 4
    
    assert a[-1] == 5
    
    assert len(a[0:2]) == 2
    
    return

def test_setitem():
    a = Vec([1, 2, 3, 4, 5])
    
    a[0] = 0
    a[1:3] = [1, 2]
    
    assert a[0] == 0 and a[1] == 1 and a[2] == 2
    
def test_abs():
    a = Vec([0, 2, 0])
    assert inerror(abs(a), 2)
    return
    
def test_bool():
    
    assert bool(Vec([])) == False
    
    assert bool(Vec([1, 2, 4, 5]))
    return
    
def test_add():
    
    a = Vec([1, 2, 3])
    b = Vec([4, 5, 6])
    
    c = a + b
    
    assert inerror(c[0], 5) and inerror(c[1], 7) and inerror(c[2], 9)
    
    c+=a
    
    assert inerror(c[0], 6) and inerror(c[1], 9) and inerror(c[2], 12)
    
    return

def test_sub():
    
    a = Vec([1, 2, 3])
    b = Vec([4, 5, 6])
    
    c = a - b
    
    assert inerror(c[0], -3) and inerror(c[1], -3) and inerror(c[2], -3)
    
    c-=a
    
    assert inerror(c[0], -4) and inerror(c[1], -5) and inerror(c[2], -6)
    
    return


def test_mul():
    
    a = Vec([1, 2, 3])
    b = Vec([4, 5, 6])
    
    c = 2 * a
    assert inerror(c[0], 2) and inerror(c[1], 4) and inerror(c[2], 6)
    
    c = a * 2
    assert inerror(c[0], 2) and inerror(c[1], 4) and inerror(c[2], 6)
    
    c = a * b
    assert inerror(c[0], 4) and inerror(c[1], 10) and inerror(c[2], 18)
    
    c*=2
    assert inerror(c[0], 8) and inerror(c[1], 20) and inerror(c[2], 36)
    
    return

def test_div():
    
    a = Vec([1, 2, 3])
    b = Vec([4, 5, 6])
    
    c = a / 2
    assert inerror(c[0], 1/2) and inerror(c[1], 2/2) and inerror(c[2], 3/6)
    
    c = a / b
    assert inerror(c[0], 1/4) and inerror(c[1], 2/5) and inerror(c[2], 3/6)
    
    c/=2
    assert inerror(c[0], 1/2) and inerror(c[1], 2/2) and inerror(c[2], 3/6)
    
    return
    
def test_pow():
    
    a = Vec([1, 2, 3])
    
    c = a ** 2
    
    assert inerror(c[0], 1) and inerror(c[1], 2 ** 2) and inerror(c[2], 3 ** 2)
    
    return

def test_matmul():
    
    a = Vec([[1], [2], [3]])
    b = Vec([[4, 5, 6]])
    
    c = a @ b
    
    assert inerror(c[0][0], 4) and inerror(c[0][1], 5) and inerror(c[0][2], 6)
    assert inerror(c[1][0], 8) and inerror(c[1][1], 10) and inerror(c[1][2], 12)
    assert inerror(c[2][0], 12) and inerror(c[2][1], 15) and inerror(c[2][2], 18)
    
    return

def test_dot_prod():
    
    a = Vec([1, 2, 3])
    b = Vec([4, 5, 6])
    
    c = a ^ b
    
    assert inerror(c, 4 + 10 + 18)
    
    
def test_state_same():
    
    a = Vec([1, 2, 3])
    b = Vec([4, 5, 6])
    
    c = a + b
    assert inerror(a[0], 1) and inerror(a[1], 2) and inerror(a[2], 3)
    assert inerror(b[0], 4) and inerror(b[1], 5) and inerror(b[2], 6)
    
    c = a - b
    assert inerror(a[0], 1) and inerror(a[1], 2) and inerror(a[2], 3)
    assert inerror(b[0], 4) and inerror(b[1], 5) and inerror(b[2], 6)
    
    c = a * b
    assert inerror(a[0], 1) and inerror(a[1], 2) and inerror(a[2], 3)
    assert inerror(b[0], 4) and inerror(b[1], 5) and inerror(b[2], 6)
    
    c = a ^ b
    assert inerror(a[0], 1) and inerror(a[1], 2) and inerror(a[2], 3)
    assert inerror(b[0], 4) and inerror(b[1], 5) and inerror(b[2], 6)
    
    c = a / b
    assert inerror(a[0], 1) and inerror(a[1], 2) and inerror(a[2], 3)
    assert inerror(b[0], 4) and inerror(b[1], 5) and inerror(b[2], 6)
    
    return

def test_for():
    
    a = Vec([1, 2, 3])
    a_list = [1, 2, 3]
    
    for i, val in enumerate(a):
        assert inerror(val, a_list[i])
        assert inerror(val, a[i])