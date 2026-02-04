def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return "Cannot divide by zero" if b ==0 else a // b
###### solution 1 ####################
'''
operations = {
    "1": ("Addition", add),
    "2": ("Subtract", sub),
    "3": ("Multiply", mul),
    "4": ("Divide", div),
}
print("select a operation: \n1: Add\n2: Subtract\n3: Multiply\n4: Divide ")

choice = input("Enter your choice(1/2/3/4): ")

if choice in operations:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator, func = operations[choice]
    print(f"{operator} of {num1} and {num2} is {func(num1, num2)}")
else:
    print("Invalid choice")

'''
######### solution 2 #################
operation = {
    "+" : (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: "can not divided zero" if b == 0 else a / b),
}

choice = input("Enter your choice('+'/'-'/'*'/'/'): ")
if choice in operation:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    func = operation[choice]
    print(func(num1, num2))
else:
    print("Invalid choice")


