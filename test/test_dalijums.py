import pytest
from src.dalijums import dali
def test_dalijums(a,b):
    assert dali(0,1) == 0
    assert dali(1,0) == 0
    assert dali(6,2) == 3
    assert dali(6,-2) == -3
    assert dali(-6,2) == -3
    assert round(dali(5,2),1) == pytest.approx(2.5)
    assert round(dali(5,-2),1) == pytest.approx(-2.5)
    assert round(dali(-5,2),1) == pytest.approx(-2.5)

"""Funkcija akceptē divus argumentus - skaiļus a un b,
aprēķina to dalījumu un atgriež to. Ja skaiļus dalīt nedrīkst,
atgriež 0.

Argumenti:
    a {int vai float} -- pirmais skaitlis
    b {int vai float} -- otrais skaitlis
Atgriež:
    int vai float -- rezultāts
"""