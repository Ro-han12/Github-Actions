from src.math_ops import add,sub

def test_add():
    assert add(5,3) == 8
    assert add(-1,1) == 0

def test_sub():
    assert sub(5,1)==4
    assert sub(3,3)==0
    
    