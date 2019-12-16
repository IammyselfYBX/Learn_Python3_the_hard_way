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

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(1000, 1)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")