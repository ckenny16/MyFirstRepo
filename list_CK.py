name = "Chris Kenny"

subjects = ["Math","History","Science","Chinese","English"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)

characters = ["Markitha","Cus Anime","Cken16","Rygy"]

for i in characters:
    print("One person that go to GCDS is " + i)
    if i == "Markitha":
        print(i + " has blond hair and barely plays fort dog.")
    elif i == "Cus Anime":
        print(i + " plays too much fort and has brown hair.")
    elif i == "Cken16":
        print(i + " Is a legend and plays a good amount of fort.")
    elif i == "Rygy":
        print(i + " plays basketball and is not as good as cken16.")

sports = []

while True:
    print("What's your favorite sport? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        sports.append(answer)

for i in sports:
    print("One of you favorite sports is " + i)
 
