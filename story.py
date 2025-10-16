def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "ceneter":
        ceneter_path()    
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("The hero steps onto the left path.")
    print("A fierce dragon appears!")
def ceneter_path():
    print("You walk ceneter and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("The Hero takes the right path.")
    print("A dark curse overtakes them.") 
    0

if __name__ == "__main__":
    intro()
