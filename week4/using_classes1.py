""" # class names are capitalized
class Player: 
    # inside are class attributes and/or methods
    max_hp = 4000

# purpose of class is to make objects (instantiate an object)

# how to make objects from classes
player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)

Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp) """


#instance attributes - stored per instance rather than on class - can change instance attribute without affecting other instances
    #initialize like this. Constructor method __init__
    #parameter list - 1st object being created, others can be added too
class Player:
    def __init__(self, name, hp):  # don't need to parameterize all attributes. Only need to pass in att. we want to set value dynamically. Can also set them up with initial value without putting in parameter list.
        self.name = name
        self.hp = hp
        self.score = 0

player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, "-- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, "-- HP:", player2.hp, "-- SCORE: ", player2.score)

player1.hp += 500
player1.score += 10
print("P1:", player1.name, "-- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, "-- HP:", player2.hp, "-- SCORE: ", player2.score)
