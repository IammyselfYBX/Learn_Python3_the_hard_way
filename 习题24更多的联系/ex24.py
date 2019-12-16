print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and reqires an explantion
\n\t\twhere there is none.
"""

print("-------------------------")
print(poem)
print("-------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jerry_beans = started * 500
    jars = jerry_beans / 1000
    creates = jars / 100
    return jerry_beans, jars, creates

start_point = 1000
beans, jars, creates = secret_formula(start_point)  # 使用三个变量分别对应

# return that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#It's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {creates} creates")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)               # 使用 *formula 表示全部 —— 见习题18
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} creates.".format(*formula))