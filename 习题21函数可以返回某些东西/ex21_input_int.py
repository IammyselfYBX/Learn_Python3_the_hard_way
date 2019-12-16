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

a = int(input("The first int: "), 10)
b = int(input("The second int: "), 10)
age = add(a, b)

print(f"Age: {age}")