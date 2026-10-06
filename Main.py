#Asks the players name and then greets them
Name = input("Hello Adventurer, what is your name? ")
print(f"\n Welcome {Name} ...... to the ULTIMATTTTTE ADVENTURE!")


#This is a list that stores the items a player has collected
Backpack = []

#The loop starts after player greeting
while True:

     #Informs the player on the path chocies then asks them which one they choose.
    Path_A = "The Spoooooooooooky Path"
    Path_B = "The Nice and Friendly path"
    Choice_Of_Path = input(f"\n Please choose your path {Name}\n '1' = {Path_A}\n '2' = {Path_B}. ")

    #These are the differnt endings for the player

    #Choice 1 is the correct path. The players gets to choose what loot they want. Adds loot to players backpack.
    if Choice_Of_Path == '1':
        print("\n Welcome to the spooky path.      You Win!")
        Loot = input(f"\n You can have anything in the world {Name} so what do you want? ")
        print(f"\n You really want a {Loot} {Name}? well thats weird but here you go you can have your {Loot}")
        Backpack.append(f"{Loot}")
    
    #Choice 2 is ironically the incorrect path. The player  loses and gets trolled.
    elif Choice_Of_Path == '2':
        print(f"\n you died {Name}. haha")

    #This is the secret ending.
    elif Choice_Of_Path.lower() == 'no':
        print(f"\n The heck you mean no {Name}?")

    #If the players says something else the game restarts.
    else:
        print(f"\n That isnt a choice {Name}")
    
    #Tells the player what items they have
    if Backpack:
        print("\n Inventory so far:")
        for loot in Backpack:
            print(f" {loot}")
    
    Play_Again = input(f"\n Do you want to play again {Name}? (yes/no) ") 
    if Play_Again.lower() != 'yes':
        print(f"\n Thanks for playing, {Name}! Goodbye.")
        break 

#This ones alot better than my last one, alot more organized also.
