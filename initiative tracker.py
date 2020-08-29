print("Copyright 2020. Please feel free to use the code. However, please give credit to user under the following Discord application username: SirNeil email: sk992@live.com\n")
character_listname = []
character_listinitiative = []
aclist = []
hplist = []
round = 0


while True:
    try:
        characters = int(input("How many character(s) are there?: "))
        if characters <= 0:
            print("There must be characters to create a scene!")
            continue
    except ValueError:
        print("Please enter a value preferably more than 0")
        continue
    else:
        break

for num in range(characters):
    while True:
        try:
            nam_char = (input("Enter character name: "))
            initiative = int(input("Character's initiative: "))
            ac = int(input("Enter AC: "))
            hp = int(input("Enter HP: "))
        except ValueError:
            print("Please enter integers only and don't leave blanks! Programme will now restart.")
            continue
        except NameError:
            print("Please enter names using letters only! Programme will now restart")
            continue
        else:
            character_listname.append(nam_char)
            character_listinitiative.append(initiative)
            aclist.append(ac)
            hplist.append(hp)
            break

character_listinitiative, character_listname, aclist, hplist = (list(t) for t in zip(*reversed(sorted(zip(character_listinitiative, character_listname, aclist, hplist)))))
# Merges the lists and sorts them in reverse order. The function ensures they don't become tuples.




while 1:
    round+=1
    print("\nRound ", round)
    for  num in range(0,characters):
        print(
            f"Next position at {num+1}\nname: {character_listname[num]}\nThe AC: {aclist[num]}\nThe HP: {hplist[num]}\ninitiative: {character_listinitiative[num]}\n")
        (input("press enter to continue \n"))

