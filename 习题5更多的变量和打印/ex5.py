my_name = 'Zed A.Shaw'
my_age = 35 # not a lie
my_height = 74  # inches
my_weight = 160 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending ont the coffee.")

# thie line tricky, try to get exactly right
total = my_age  + my_height + my_weight
print(f"If I add {my_age}, {my_height}, {my_weight} I get {total}.")

# 浮点数四舍五入
a = round(1.7333)
print("1.7333 is", a)