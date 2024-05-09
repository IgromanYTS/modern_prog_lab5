from calc import add, subtract, multiply, division
import pytest


def test_add():
    assert add(2, 4) == 6
    assert add("Dima", "cool") == "Dimacool"
