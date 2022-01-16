from sys import argv

script, filename = argv

target = open(filename, 'r')

context = target.read()

print(context)

target.close()

