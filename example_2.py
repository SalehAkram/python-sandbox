class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, n1, n2):
        if n2 == 0:
            print("cannot divide by zero")
            return
        return n1 / n2

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    def calculate(self, operation_name, num1, num2):
        if operation_name in self.operations:
            operation = self.operations[operation_name]
            return operation(self, num1, num2)
        else:
            print("Invalid operation name")
