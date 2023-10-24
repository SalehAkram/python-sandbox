from abc import ABC, abstractmethod


class ICalculator(ABC):
    @abstractmethod
    def calculate(self, n1, n2):
        pass


class Add(ICalculator):

    def calculate(self, n1, n2):
        return n1 + n2


class Subtract(ICalculator):

    def calculate(self, n1, n2):
        return n1 - n2


class Multiply(ICalculator):

    def calculate(self, n1, n2):
        return n1 * n2


class Divide(ICalculator):

    def calculate(self, n1, n2):
        if n2 == 0:
            print("cannot divide by zero")
            return
        return n1 / n2



