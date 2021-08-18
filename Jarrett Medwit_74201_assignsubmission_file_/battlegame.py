# The player will be able to choose between three characters: a Wizard, an Elf, and a Human.
# The chosen character will fight a Dragon, and the program will calculate and display the results.
# wizard = "Wizard"
wizard = {"name": "Steve the Wizard", "hp": 70, "damage": 150}
elf = {"name": "Jeffery the Elf", "hp": 100, "damage": 100}
human = {"name": "Josh the Human", "hp": 150, "damage": 20}
dragon = {"name": "Emily the Dragon", "hp": 300, "damage": 50}
death_knight = {"name": 'Stephanie the Death Knight',
                "hp": 190, "damage": 69.4}

while True:
    print(f"""
  1)  {wizard["name"]}
  2)  {elf["name"]}
  3)  {human["name"]}
  4)  {death_knight["name"]}
  5)  Exit
  """)
    choose = input("Choose Your Character:  ").lower()
    print(choose)

    # check input
    if choose == "1" or choose == "wizard" or choose == "steve" or choose == "steve the wizard":
        character = wizard
        break
    elif choose == "2" or choose == "elf" or choose == "jeffery" or choose == "jeffrey the elf":
        character = elf
        break
    elif choose == "3" or choose == "human" or choose == "josh" or choose == "josh the human":
        character = human
        break
    elif choose == "4" or choose == "death knight" or choose == "deathknight" or choose == "stephanie" or choose == "stephanie the death knight":
        character = death_knight
        break
    elif choose == "5":
        print("Ok fine then! Go away or you will die unexpectedly!")
        exit()
    else:
        print("Unknown Character")

print()
print(f"""
You have chosen the character: {character["name"]}
Health: {character["hp"]}
damage: {character["damage"]}
""")

while True:
    dragon["hp"] = dragon["hp"] - character["damage"]
    print(f"""
    {character['name']} damaged {dragon['name']}!
    {dragon['name']}'s hitpoints are now: {dragon['hp']}
  """)
    if dragon['hp'] <= 0:
        print(dragon['name'] + " has lost the battle")
        break

    character["hp"] = character["hp"] - dragon["damage"]
    print(f"""
    {dragon['name']} damaged {character['name']}!
    {character['name']}'s hitpoints are now: {character['hp']}
  """)
    if character['hp'] <= 0:
        print(character['name'] + " has died and therefore loses the battle. Please always remember the good times with " + character['name'])
        break
