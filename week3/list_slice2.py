lst = ['Ajay', 'Bobby','Ashok', 'Vijay', 'Anil', 'Rahul','Alex', 'Christopher']
print (lst[1:])  # prints all but 1st element
# displays ['Bobby', 'Ashok', 'Vijay', 'Anil', 'Rahul', 'Alex', 'Christopher']

print (lst[0:])  # prints all elements
# displays ['Ajay', 'Bobby', 'Ashok', 'Vijay', 'Anil', 'Rahul', 'Alex', 'Christopher']

print (lst[2:-2]) # all elements starting from third element but skips the last two elements.
# displays ['Ashok', 'Vijay', 'Anil', 'Rahul']

print (lst[::2])  # this will print all alternate elements (begin to end in steps of 2)
# displays ['Ajay', 'Ashok', 'Anil', 'Alex']

print (lst[::-1]) # this will print all but last element
# displays ['Christopher', 'Alex', 'Rahul', 'Anil', 'Vijay', 'Ashok', 'Bobby', 'Ajay']

print (lst [-1])  #prints the last element 
#displays Christopher - note this is not a list, but only a single element

print (lst[0:3])
