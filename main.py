#very cool test terminal game

#Imports
import os
import json
import random
import platform

#include functions
from Game.functions.draw import draw
from Game.functions.clearconsole import clearconsole
from Game.functions.dodgeresult import dodgeresult


#SUPER DUPER IMPORTANT MAIN VARIABLES
userinput = "null"
enemy = None
enemydodgesuccess = False
dodgesuccess = False

#loads objects from json
def importjson(file, name):
    with open(file, "r") as f:
        data = json.load(f)
    globals()[name] = data

#Creating Objects
def loadalljson():
    importjson("./Game/data/player.json", "player")
    importjson("./Game/data/zombie.json", "zombie")
    importjson("./Game/data/George.json", "george")
    importjson("./Game/data/skeleton.json", "skeleton")

#choose ennemy
def selectenemy():
    loadalljson()
    global enemy
    data = [zombie, skeleton]
    enemy = random.choice(data)

selectenemy()

#Draws terminal screen
draw(enemy, player)

#Main funtcion where code goes
def main():
    global enemydodgesuccess
    global dodgesuccess
    #processing user input
    userinput = input("Option: ")
    match userinput:
        #Exiting Program
        case "0":
            exit(0)
        #Attacking enemy
        case "1":
            if enemydodgesuccess != True:
                attackvalue = random.randint(1, player["attack"])
                enemy["health"] -= attackvalue
                print("You dealt: ", attackvalue, " damage")
                input("press enter to continue")
            else:
                print(enemy["name"], " dodged attack")
                input("press enter to continue")
                enemydodgesuccess = False
        #Dodging
        case "2":
            dodge = random.randint(1, 100)
            if dodge < player["speed"]:
                dodgeresult("player", "failed") 
            else:
                dodgeresult("player", "succeded")
                dodgesuccess = True
        #Error Handeling
        case _:
            clearconsole()
            print("Not VALID")
            input("")
            draw()
            main()
    #Checking and updating enemy stats
    enemydodgesuccess = False
    if enemy["health"] == 0 or enemy["health"] < 0:
        print("you defeated the enemy!!")
        input("press enter to continue")
        gameloop()
    else:
        #Enemy Choices
            #setting enemy chances
        enemydodge = random.randint(1, 100)
        enemyattack = random.randint(1, enemy["attack"])
        enemychoices = random.randint(1, 2)
        #Enemy attack
        if enemychoices == 1:
            if dodgesuccess != True:
                clearconsole()
                print(enemy["name"]," dealt ",enemyattack, "damage")
                player["health"] -= enemyattack
                input("press enter to contine")
            else:
                clearconsole()
                print("You dodged ", enemy["name"], "'s attack")
                input("press enter to contine")
                dodgesuccess = False
        #Enemy dodge
        else:
            if enemydodge < enemy["speed"]:
                dodgeresult("enemy","failed")
            else:
                dodgeresult("enemy", "failed")
                enemydodgesuccess = True

#Keeps the game running
def gameloop():
    selectenemy()
    while True:
        clearconsole()
        if enemy["health"] < 0 or enemy["health"] == 0:
            print("you defeated the enemy!!")
            input("press enter to continue")
            gameloop()
        elif player["health"] < 0 or player["health"] == 0:
            print("you died...")
            exit(0)
        elif player["health"] == 67.41:
            print ("THE ONE AND ONLY...")
            print("GEORGE FENTDROID")
        else:
            draw(enemy,player)
            main()
            clearconsole()

#init game
gameloop()
