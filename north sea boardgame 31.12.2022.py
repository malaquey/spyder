# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import random
import matplotlib as plt
import time

def diesix():
    list = [1,2,3,4,5,6]
    return random.choice(list)

def roll(dice,current_player):
    count = dice
    roll = 0
    while count > 0:
        roll = roll+diesix()
        count = count - 1
    print(str(current_player)+' rolls '+str(dice)+' dice for a total of '+str(roll))
    
    return roll
        
def move():
    roll(2)    
    
def nextplayer(current_player,players):
    if current_player == players[len(players) - 1]:
        current_player = players[0]
    else:
        current_player = players[players.index(current_player)+1]     
        
    return current_player

def positioncheck(player): #checks the current position of the current player and initiates the relevant choices (roll again, buy supply boat base etc). Also deducts rent, adds income etc if the relevant square has been passed
    if playerpositions[player] - lastroll + 12 > 22 and playerpositions[player] > 34 or playerpositions[player] < 11:
        player_cash[player] = player_cash[player] + player_headoffice[player]     
    return
        
def turnloop(current_player):    
    
    current_player = nextplayer(current_player,players)
    print('it is '+str(current_player)+"'s turn'")

    rollchoice = ''
    while rollchoice != "yes":
        rollchoice = input("Type 'yes' to roll for "+str(current_player)+"\n")
        if rollchoice != 'yes':
            print("That is not a valid input")

    lastroll = roll(2,current_player)
    time.sleep(0) # the delay in seconds between rolling and the turn being carried out
    player = int(current_player[-1])-1
    playerpositions[player] = playerpositions[player] + lastroll
    if playerpositions[player] > (len(boardpos) - 1):
        playerpositions[player] = playerpositions[player] - lastroll
        playerpositions[player] = playerpositions[player] - len(boardpos) + lastroll
    print(str(current_player)+" lands on "+str(boardpos[playerpositions[player]]))
    positioncheck(player)
    turnloop(current_player)
    return



boardpos = ['rig depot','supply depot 1',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35] #every square on the board in a list
chance = [] #every chance card as a list
oilfields = [0,0,0,1,2,3,2,1,0,0,0,0] #every oilfield tile in order from 1,1 to 12,12 as a list, 0 = empty, 1 = low, 2 = medium, 3 =  high
explorepool = 2 # number of available exploration rigs
pipepool = 2 #number of available pipe laying barges
playercount = 3

#all players start at position 1 (rig depot)
playerpositions = []
count = playercount
while count > 0:
    playerpositions.append(0)
    count = count - 1

#starting money for each player
player_cash = []
count = playercount
while count > 0:
    player_cash.append(500000)
    count = count - 1

#monthly running costs for each player, starts at 0
player_running_costs = []
count = playercount
while count > 0:
    player_running_costs.append(0)
    count = count - 1

#monthly interest for each player, start at 0
player_interest = []
count = playercount
while count > 0:
    player_interest.append(0)
    count = count - 1

#monthly income from head office for each player, starts at 500,000
player_headoffice = []
count = playercount
while count > 0:
    player_headoffice.append(500000)
    count = count - 1

#monthly production income for each player, starts at 0
player_production = []
count = playercount
while count > 0:
    player_production.append(0)
    count = count - 1

players = []
count = playercount
player = 1
while count > 0:
    players.append('player '+str(player))
    player = player + 1
    count = count - 1
current_player = players[len(players)-1]
lastroll = 0
turnloop(current_player)