import pytest
from app.calculator import Calculator

class TestCalc: # тестируем весь калькулятор нажатием на стрелку
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): # умножение
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self): # деление
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_calculate_correctly(self): # вычитание
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_adding_calculate_correctly(self): # сложение
        assert self.calc.adding(self, 7, 2) == 9



    def test_multiply_calculation_failed(self): # умножение
        assert self.calc.multiply(self, 2, 2) == 5 # негативный

    def test_division_calculation_failed(self): # деление
        assert self.calc.division(self, 9, 3) == 5 # негативный

    def test_subtraction_calculation_failed(self):  # вычитание
        assert self.calc.subtraction(self, 5, 3) == 5  # негативный

    def test_adding_calculation_failed(self): # сложение
        assert self.calc.adding(self, 7, 2) == 5 # негативный
