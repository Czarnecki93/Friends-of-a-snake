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
    fw = open("mymembers.txt", "a")
    fw.write("\nMember id: " + str(m.getMemNumber()) + ". Member name: " + m.getMemName() + ".")
    fw.close()
    chatbot(text = "Member added successfully as: " + m.getMemName() + " with id " + str(m.getMemNumber()))
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
    while True:
        chatbot(text = "What type of snake is it? \"Mamba\" or \"Anaconda\"?")
        snakeType = input()
        if (snakeType.lower() == "anaconda"):
            chatbot(text = "Whoops. Bad news! This type of snake is protected, and cannot be added!")
            continue
        elif (snakeType.lower() == "mamba"):
            break
        else:
            chatbot(text = "Hmm.. Don't know that type of snake.. Try again with another type of snake.")
            continue
        break
    chatbot(text = "Who is the owner of the snake?")
    snakeOwner = input()
    s = Snakes(snakeName, snakeType, snakeOwner)
    fw = open("mysnakes.txt", "a")
    fw.write("\nSnake id: " + str(s.getSnakeNumber()) + ". Snake name: " + s.getSnakeName() + ". Snake type: " + s.getSnakeType() + ". Owner of the snake: " + s.getMember() + ".")
    fw.close()
    chatbot(text = "Snake added successfully")
    while True:
        again = input("Add more snakes? Y/N: ").lower()
        if (again == "y"):
            addSnake()
        elif (again == "n"):
            break
        else:
            chatbot(text = "Enter Y or N")
            continue
        break

chatbot(text = "Welcome to the \"Friends of a snake\" association!")
while True:
    chatbot(text = "What would you like to do?")
    chatbot(text = "Press 1 if you would like to add a member, \nPress 2 if you would like to add a snake, \nPress 3 if you would like to see the list of members, \nPress 4 if you would like to see the list of snakes, \nPress 0 if you want to break free.")
    while True:
        snake_or_member = input()
        try:
            snake_or_member = int(snake_or_member)
        except:
            chatbot(text = "Sorry I didn't get that. You have to enter a number between 0 and 4 to make a choice.")
            continue
        if (snake_or_member == 1 ):
            chatbot(text = "You chose: Add a member")
            addMember()
        elif (snake_or_member == 2):
            chatbot(text = "You chose: Add a snake")
            addSnake()
        elif (snake_or_member == 3):
            chatbot(text = "You chose: See list of members")
            f = open("mymembers.txt", "r")
            chatbot(text = f.read())
            chatbot(text = "Allright! That was an interesting list! What's next?")
        elif (snake_or_member == 4):
            chatbot(text = "You chose: See list of snakes")
            f = open("mysnakes.txt", "r")
            chatbot(text = f.read())
            chatbot(text = "Allright! That was an interesting list! What's next?")
        elif (snake_or_member == 0):
            exit(0)
        else:
            chatbot(text = "You can only enter the numbers 0-4. Try again.")
            continue
        break
    continue