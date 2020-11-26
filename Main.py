from Snakes import Snakes
from Members import Members
from Chatbot import chatbot

import time

memberlist = list()
snakelist = list()

def addMember():
    chatbot(text = "What is the name of the member?")
    memberName = input()
    m = Members(memberName)
    memberlist.append(m)
    print("Member added successfully as: " + m.getMemName() + " with id " + str(m.getMemNumber()))
    while True:
        again = input("Add more members? Y/N: ").lower()
        if (again == "y"):
            addMember()
        elif (again == "n"):
            break
        else:
            chatbot(text = "Enter Y or N")
            continue
        break


def addSnake():
    chatbot(text = "What is the name of the snake?")
    snakeName = input()
    snakelist.append(snakeName)
    print("Snake added successfully as: " + snakeName)

chatbot(text = "Welcome to the \"Friends of a snake\" association!")
chatbot(text = "What would you like to do?")
chatbot(text = "Press 1 if you would like to add a member, or 2 if you would like to add a snake and link it to an existing member.")
while True:
    snake_or_member = input()
    try:
        snake_or_member = int(snake_or_member)
    except:
        chatbot(text = "Sorry I didn't get that. Enter either 1 or 2.")
        continue
    if (snake_or_member == 1 ):
        chatbot(text = "Add a member")
        addMember()
    elif (snake_or_member == 2):
        chatbot(text = "Add a snake")
        # AddSnake()
    else:
        chatbot(text = "You can only enter the number 1 or 2. Try again.")
        continue
    break