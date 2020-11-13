import pytest
from src.c_uzd import kelvini

def test_neg():
    assert kelvini(-289) == 0
def test_pozVes():
    assert kelvini(45) == 318.15
def test_nulle():
    assert kelvini(0) == 273.15
def test_dalas():
    assert kelvini(67.55) ==340.7