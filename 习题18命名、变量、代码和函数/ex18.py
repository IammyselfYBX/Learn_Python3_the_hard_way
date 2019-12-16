# this one is like your script with argv
def print_two(*args):
    argv1, argv2 = args
    print(f"arg1: {argv1}, argv2: {argv2}")

# ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this just takes no argument
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")    
print_one("First!")
print_none()
