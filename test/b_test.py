import pytest
from src.u_laukums import laukums

def test_vesel_pozitivi():
    assert laukums(2, 3) == 2

def test_poz_dala():
    assert laukums(2,4.2) == 4.2

def test_abi_dalas():
    assert laukums(3.2,4.4)==7.04