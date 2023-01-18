weapon = False
hp = 4
const = "Please enter a valid option"
option = "Options: left/right/backward/forward"

def introScene():
    directions = ["left", "right", "forward", "backward"]
    print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print(option)
        userInput = input()
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "forward":
            hauntedRoom()
        elif userInput == "backward":
            print("You find that this door opens into a wall. You turn back.")
            introScene()
        else:
            print(const)

def showShadowFigure():
    directions = ["right", "backward"]
    print("You see a dark shadowy figure appar in the distance. You have an unsettling feeling about it. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print(option)
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "backward":
      introScene()
    else:
      print(const)

def cameraScene():
  directions = ["forward","backward"]
  print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print(option)
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print(const)

def hauntedRoom():
  directions = ["right","left","backward"]
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print(option)
    userInput = input()
    if userInput == "right":
      print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print(const)

def showSkeletons():
  directions = ["backward","forward"]
  global weapon
  print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print(option)
    userInput = input()
    if userInput == "left":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "right":
      print("You encounterd a wall")
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print(const)

def strangeCreature():
  actions = ["fight","flee"]
  global weapon
  print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
      else:
        print("The goul-like creature has killed you.")
      quit()
    elif userInput == "flee":
      showSkeletons()
    else:
      print(const)

if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()