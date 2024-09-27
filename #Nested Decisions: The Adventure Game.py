#Nested Decisions: The Adventure Game

#Task 1: Code Correction
place = input("Choose a place: forest or cave?")
action = input("climb a tree or cross a river?") if place == "forest" else input("light a torch or proceed in the dark")


if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else:
    if place == "cave": #Task 2: Setting the Scene
        if action == "light a torch":
            print("You found a town!")
    elif action == "proceed in the dark":
        print("You've fell into a hole!")

    else: 
     pass   #Task 3: Default Path
   
   
