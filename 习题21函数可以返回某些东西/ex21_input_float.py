def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRUCT {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b   
    
def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b

print("let's do some math with just function!")

a = float(input("The first int: "))
b = float(input("The second int: "))
age = add(a, b)

print(f"Age: {age}")