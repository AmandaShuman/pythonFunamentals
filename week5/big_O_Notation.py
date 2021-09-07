import timeit
# complexitites in time consumption least to greatest

# constant time complexity
# like declaring a variable or appending or popping to end of a list


# log time complexity
# example is a binary search b/c dividing list by 2 each time

# linear complexity
print(timeit.timeit("[x for x in range(1000000)]", number =1))
print(timeit.timeit("[x for x in range(10000000)]", number=1))
print(timeit.timeit("[x for x in range(100000000)]", number=1))

# linearithmic complexity is combo of linear and exponential time
# example is quicksort - O(n * log2(n))

# quadratic complexity - O(n^2)
# considered inefficient like Bubblesort - (n-1)(n-1) but can simplify to n^2
