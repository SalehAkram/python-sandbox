# from example_1 import Add,Subtract,Multiply,Divide
#
# operations = {"add": Add(), "subtract": Subtract(), "multiply": Multiply(), "divide": Divide()}
#
# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))
# print("Operation list: ")
# for key in operations:
#     print(key)
# selected_operation_key = input("Type in the name of the operation: ").lower()
#
# operation = operations[selected_operation_key]
#
# print(f"result of the {num1} {selected_operation_key} {num2} is: {operation.calculate(num1,num2)}")


# from example_2 import Calculator
#
# calculator = Calculator()
#
#
# print(calculator.calculate("divide", 5, 6))

import numpy

a = numpy.zeros([3, 2])
a[2, 1] = 1
print(a)





