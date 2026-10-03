Name = input("Hello Adventurer, what is your name? ")
print(f"Welcome {Name} ...... to the ULTIMATTTTTE ADVENTURE!")
Path_A = "The Spoooooooooooky Path"
Path_B = "The Nice and Friendly path"
Choice_Of_Path = input(f"Please choose your path {Name}! '1' = {Path_A} '2' = {Path_B} ")
if Choice_Of_Path == '1':
    print("Welcome to the spooky path.      You Win!")
    Loot = input(f"You can have anything in the world {Name} so what do you want? ")
    print(f" You really want a {Loot} {Name}? well thats weird but here you go you can have your {Loot}")
elif Choice_Of_Path == '2':
    print(f"you died {Name}. haha")
elif Choice_Of_Path == 'no':
    print(f"The heck you mean no {Name}?")
else:
    print(f"That isnt a choice {Name}")

#Thanks for viewing!..... i probably shoudve added more documentation
