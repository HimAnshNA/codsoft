# Rock Paper Scissor game by himanshu


import random

def play(comp, user):
    
    if comp == user:
        return None

    elif comp == 'r':
        if user=='s':
            return False
        elif user=='p':
            return True
    
    elif comp == 'p':
        if user=='r':
            return False
        elif user=='s':
            return True
    
    elif comp == 's':
        if user=='p':
            return False
        elif user=='r':
            return True

print("Comp Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

user = input("Your Turn: Rock(r) Paper(p) or scissor(s)?")
a = play(comp, user)

print(f"Computer chose {comp}")
print(f"You chose {user}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")