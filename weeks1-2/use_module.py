#first way to import and use modules
'''
import my_module

my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)
'''


#second way to import module - this way you only import the code you need to use
from my_module import greet, flavor

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)
