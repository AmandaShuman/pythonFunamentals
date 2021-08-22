states = ["Washington", "Oregon", "California"]

'''#assessing list values
print(states[-1])  #last
print(states[-2])  #second to last item
print(states[-3])  #third to last item
'''

states[2] = "Arizona"
# print(states)
# print(len(states))
states.append("New York")
print(states)
states.pop()
print(states)
states.pop(1)
print(states)