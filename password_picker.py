import random
import string

print("Wlcome to password picker")

while True:
    for num in range(3):
        adjective=["Sleepy","slow","smelly","wet","fat","red","orange","yellow","green","blue","purple","white","proud","brave"]
        nouns=["apple","dinosaur","ball","toaster","goat","dragon","hammer","duck","panda"]

        adjective=random.choice(adjective)
        noun=random.choice(nouns)
        number=random.randrange(0,100)
        special_char=random.choice(string.punctuation)
        password=adjective+noun+str(number)+special_char
        print("Your new password is: %s" %password)

    response=input("Would ou like another password? Type y or n: ")
    if(response=='n'):
        break
