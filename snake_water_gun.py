import random

def gameWin(comp, you):
    if comp == 's':
        if you =="w":
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you == 'w':
            return True
        elif you=='s':
            return False




print("comp Turn: Snake(s) water(w) or gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) water(w) or gun(g)?")

a = gameWin(comp,you)

print(f"Computer chose :{comp}")
print(f"YOu chose : {you}")

if a == None:
    print("The game is a tie")
elif a:
    print("YOu win!")
else:
    print("YOu lose")