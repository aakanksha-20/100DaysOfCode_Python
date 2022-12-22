
first = input(
    "You're at an island with no supplies. You're despate to find a way to survive. There's a shore on the left and dense forest on the right. what would you choose? Left or Right?"
).lower()
# second = print(input("swim or wait"))
# third = print(input("Which door? Red, Blue, Yellow?"))

if first == "left":
    second = input(
        'You see s small lake at the edge. Type "swim" if you want to cross the lake or type  "wait" if want to wait to find a boat for it'
    ).lower()
    if second == "wait":
        third = input(
            "You now encounter 3 doors. Which door do you think could have the treasure? Red, Blue, Yellow?"
        ).lower()
        if third == "red":
            print("Burned by fire. Game Over.")
        elif third == "blue":
            print("Eaten by beasts. Game Over.")
        elif third == "yellow":
            print("You've found the treasure! You Win!")
        else:
            print("You stepped on quicksand. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game over.")
