go = input("Where do you want to go? Left or Right:  ").lower()
if go == "right":
    print("Ooops, That was quick, Game Over")
elif go == "left":
    water = input("Do you want to swim or wait? Enter swim or wait:  ").lower()
    if water == "swim":
        print("Sorry, it's time to go, Game Over")
    elif water =="wait":
        door = input("Choose a door, be wise about it, Enter Red, Blue or Yellow: ").lower()
        if door == "yellow": 
            print("You did choose wisely, You won!!!!")
        else:
            print("Yikes, Almost made it, Game Over")


