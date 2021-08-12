while True:
    #declare variables
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    ogre = "Ogre"
    centaur = "Centaur"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    ogre_hp = 90
    centaur_hp = 130

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    ogre_damage = 45
    centaur_damage = 95

    #all characters will fight dragon
    dragon_hp = 300
    dragon_damage = 50

    #Allow player to choose character
    print("1)   " + wizard)
    print("2)   " + elf)
    print("3)   " + human)
    print("4)   " + ogre)
    print("5)   " + centaur)
    print("6)   Exit")
    player = input("Choose your character: ")
    player = player.capitalize()

    if (player == "1" or player == "Wizard"):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if (player == "2" or player == "Elf"):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if (player == "3" or player == "Human"):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if (player == "4" or player == "Ogre"):
        character = ogre
        my_hp = ogre_hp
        my_damage = ogre_damage
        break
    if (player == "5" or player == "Centaur"):
        character = centaur
        my_hp = centaur_hp
        my_damage = centaur_damage
        break
    if (player == "6"):
        exit("Ok, goodbye!")
    else:
        print("Unknown character")

#show player their character stats
print("You have chosen the character:", character)
print("Health:", my_hp)
print("Damage:", my_damage)
print()

#time to battle the dragon
while True:
    dragon_hp = dragon_hp - my_damage
    print(f"The {character} damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    print()
    if (dragon_hp <= 0):
        print("The Dragon has lost the battle.")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strickes back at", character)
    print(f"The {character}'s hitpoints are now: {my_hp}")
    print()
    if (my_hp <= 0):
        print(f"The {character} has lost the battle.")
        break
