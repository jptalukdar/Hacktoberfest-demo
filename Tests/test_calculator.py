import pytest
from PythonCalculator import calculator

def test_testcase1():
    assert calculator.add(3,4) == 7

def test_testcase2():
    assert calculator.add('3','4') == 7

