states = ["Washington", "Oregon", "California"]

'''for state in states:
    state = state.lower()
    print(state)
    
print("Washington" in states)  # checks to see if washington in states list T/F
print("Tennessee" in states)
print("Washington" not in states)
'''
states2 = ["Arizona", "Ohio", "Michigan", "Texas"]
best_states = states + states2
print(best_states)
print(best_states[1:3])  #grab all items index 1 up to index 3 (not including 3)
print(best_states[:2])  #grab all items up to certain index (not including index 2)
print(best_states[4:])  #grap index 4 until end of list