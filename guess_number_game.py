import random
target=random.randint(1,100)

while True:
    userchoice=input("Guess a number(1-100) or Quit(Q):")
    if(userchoice=="Q"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("Successfull : correct guess")
        break
    elif(userchoice<target):
        print("your choice is too small. Take a bigger guess...")
    else:
        print("your choice is too large. Take a smaller guess...")

print("---Game Over---")
