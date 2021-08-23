my_string = "alpha"
'''multiline_string = """bravo
charlie"""
print(my_string)
print(multiline_string)

print(my_string[0])
print(my_string[3])

print(my_string[0:3])  # prints index 0 to 2
print(my_string[:2])   # prints index 0 to 1 
print(my_string[2:])  # prints index 2 to end
print(my_string)

for char in my_string:
    print(char)
'''
print("pha" in my_string)
print("z" not in my_string)