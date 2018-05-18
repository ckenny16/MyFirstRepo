import pyautogui as pg
import time

points = 0




#question
answer = pg.prompt(
"""
Where do you usually land?

a)greasy every time
b)to the closest area
c)very far from the bus

"""
    )
#answer
pg.alert("you chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


#question
answer = pg.prompt(
"""
Which would you rather pick up?

a)Sheild Potion
b)mini shield
c)Med kit

"""
    )
#answer
pg.alert("you chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3








#question
answer = pg.prompt(
"""
What is your favorite weapon?

a)Classic AR
b)purple tactical shotgun
c)sniper

"""
    )
#answer
pg.alert("you chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


#question
answer = pg.prompt(
"""
What is the first thing you do when you land after you find loot?

a)gather materials
b)Find people
c)Hide
"""
    )
#answer
pg.alert("you chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    

#question
answer = pg.prompt(
"""
What type of gernade is better?

a)Gernades are terrible
b)Reg gernade
c)smoke gernade

"""
    )
#answer
pg.alert("you chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



#END OF SURVEY
pg.alert("you are...")


#Agressive Player
if points >=8 and points <=11
pg.alert("Your an agressive player")

#Noob Player
if points >=12 and points <=15
pg.alert("You are a noob")

#Smart Player
if points >=5 and points <=7
pg.alert("you are a smart player")

