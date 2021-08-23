state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}
'''for state in state_capitals:  # prints the keys
    print(state)'''

'''for city in state_capitals.values():  # prints the values
    print(city)'''

# iterating with both keys and values
""" for state in state_capitals:  
    print(state_capitals[state], "is the capital of", state) """

for state, city in state_capitals.items():
    print(city, "is the capital of", state)
