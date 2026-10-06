import pytest
from calc import add,sub,mul,div

def test_add():
    assert add(10,20)==30

def test_sub():
    assert sub(40,20)==20

def test_mul():
    assert mul(5,5)==25

def test_div():
    assert div(20,10)==2
    
