from importlib.resources import path
import sys
import time

def intro():
    print()
    print("Why hello there, are you awake? Good, you might be wondering who I am? ")
    print("Well, there is no time for that as THEY are closing in.")
    print("Oh don't worry, the choice will not have a large impact, only which door you'll go through.")
    print("Now, will you pick the red or blue door?")
    print()
    print()
    print("Blue door: a door as blue as the ocean on a clear day")
    print("Red door: a door as red as your bloodshot eyes")
    print()
    firstPath = input("Which door do you pick? Red or Blue?: ")
    if firstPath == 'Red':
        print()
        path1()
    elif firstPath == 'Blue':
        print()
        path2()


def path1():
    print("The door opens effertlessly as a blast of hot air hits you in the face, the smell of cheap Chinese food hitting your nostrils.")
    print("You weren't expecting this, how did you end up in a place like this?")
    print("You turn around only to see the red door door fade away into the flames of a stove.")
    print()
    print("Now what?")
    print()
    print("Do you look around?")
    print("Grab sime dim sum?")
    print("Leave the kitchen?")
    print("Talk to one of the cooks.")
    print("Stick your hand in the flame to see if the door opens.")
    print()
    secondPath = input("What do you do? (look/eat/leave/talk/flame): ")
    if secondPath == 'leave':
        path1_1()
    elif secondPath == 'look':
        path1_2()
    elif secondPath == 'talk':
        path1_3()
    elif secondPath == 'Flame':
        print("Well that was stupid, you burn your hand as the flames quickly spreads acorss your body")
    elif secondPath == 'eat':
        print("Oh no, the cook did not like that as you find a cleaver in your back.")
    else:
        print("Hey don't just stand there, do something dumbass.")

def path1_1():
    print()

def path1_2():
    print()

def path1_3():
    print()

def path2():
    print()

def path2_1():
    print()

def path2_2():
    print()

def path2_3():
    print()

print()
print()
print("              ####################")
print("              #                  #")
print("              #     work         #")
print("              #       in         #")
print("              #     progress     #")
print("              #                  #")
print("              ####################")
print()

startGame = input("Would you like to wake up? (Y/N): ")
if startGame == 'n' or startGame == 'N':
    print("Sweet dreams")
elif startGame == 'y' or startGame == 'Y':
    intro()