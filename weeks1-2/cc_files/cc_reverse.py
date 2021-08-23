def reverse(str):
    # [::-1] means start at the end of the string and end at position 0, move with the step -1
    return str [::-1]

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))

# helpful more info
#https://stackoverflow.com/questions/509211/understanding-slice-notation

'''
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
'''
