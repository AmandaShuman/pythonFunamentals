unsorted_list = [101, 49, 3, 12, 56]

# list sort
"""
first iteration [49, 3, 12, 56, 101]
second iteration [3, 12, 49, 56, 101]
third iteration [3, 12, 49, 56, 101] - no changes so done!
"""


def bubblesort(the_list):
    high_idx = len(the_list) - 1
    for i in range(high_idx):  # number of adj. pairs = highest index
        list_changed = False
        for j in range(high_idx):  # run once for each adj. pair
            item = the_list[j]
            next = the_list[j+1]

            if item > next:  # this is where the swap occurs if needed
                the_list[j+1] = item
                the_list[j] = next
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break

bubblesort(unsorted_list)