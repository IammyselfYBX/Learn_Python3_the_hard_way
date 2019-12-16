from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv #解包,将argv的各个选项对应赋值

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)