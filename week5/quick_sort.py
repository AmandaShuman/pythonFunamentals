my_list = [5, 4, 1, 2, 3]

def sort_part(the_list, low_idx, pivot_idx):
    pivot_val = the_list[pivot_idx]

    while pivot_idx != low_idx:  # for iterating through list
        low_val = the_list[low_idx]  # value stored at lowest index

        print(the_list, low_val, pivot_val)
        # Let's start sorting!
        if low_val <= pivot_val:  # two are already sorted
            low_idx += 1
        else:
            the_list[low_idx] = the_list[pivot_idx - 1]  # moves pivot-1 val to low
            the_list[pivot_idx] = low_val  # moves low val to pivot
            the_list[pivot_idx - 1] = pivot_val  # moves pivot down one
            pivot_idx -= 1  # decrement pivot by one to follow pivot

    return pivot_idx

def quicksort(the_list, low_idx, high_idx):
    # this function will be used recursively
    if low_idx > high_idx:  # base case where no recursion happens
        return

    pivot_idx = sort_part(the_list, low_idx, high_idx)  
    quicksort(the_list, low_idx, pivot_idx-1)  # apply divide & conquer to left 1/2
    quicksort(the_list, pivot_idx+1, high_idx) # to then conquer right 1/2
    # recursive calls will divide and sort list over and over until finished
    
quicksort(my_list, 0, len(my_list) - 1)
print("my list:", my_list)

# output:
"""
[5, 4, 1, 2, 3] 5 3
[2, 4, 1, 3, 5] 2 3
[2, 4, 1, 3, 5] 4 3
[2, 1, 3, 4, 5] 1 3 - this is where sort_part ends
[2, 1, 3, 4, 5] 2 1 - this is where the recursion comes in for left 1/2
[1, 2, 3, 4, 5] 4 5 - then recursion comes in for right 1/2
my list: [1, 2, 3, 4, 5]
"""
