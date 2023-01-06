# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import matplotlib as plt
import time

def diesix():#returns a random number integer between 1 and 6
    list = [1,2,3,4,5,6]
    return random.choice(list)

def roll(dice,current_player):#returns the total of the provided number of 6 sided dice, and prints the roll for the current player
    count = dice
    roll = 0
    while count > 0:
        roll = roll+diesix()
        count = count - 1
    print('player '+str(current_player)+' rolls '+str(dice)+' dice for a total of '+str(roll))
    return roll
        
  
def nextplayer(current_player,players):
    if current_player == len(players):
        current_player = 1
    else:
        current_player = current_player + 1         
    return current_player

def positioncheck(player,lastroll): #checks the current position of the current player and initiates the relevant choices (roll again, buy supply boat base etc). Also deducts rent, adds income etc if the relevant square has been passed
  
    print(str(playerpositions[player]))
          
    if playerpositions[player] == 35 or (playerpositions[player] - lastroll <0):
        player_cash[player] = player_cash[player] + player_headoffice[player]     
        print('player '+str(player+1)+' receives monthly income from head office of £'+str(player_headoffice[player]))
    if boardpos[playerpositions[player]] == 'chance factor':
        chance(player)
    return
        
def turnloop(current_player):    
    
    current_player = nextplayer(current_player,players)
    player = current_player-1
    print('it is player '+str(current_player)+"'s turn'\nplayer "+str(current_player)+' has £'+str(player_cash[player]))
    
    rollchoice = ''
    while rollchoice != "y":
        rollchoice = input("Type 'y' to roll for player "+str(current_player)+"\n")
        if rollchoice != 'y':
            print("That is not a valid input")

    lastroll = roll(2,current_player)
    time.sleep(sleeptime) # the delay in seconds between rolling and the turn being carried out    
    playerpositions[player] = playerpositions[player] + lastroll
    if playerpositions[player] > (len(boardpos) -1):
        playerpositions[player] = playerpositions[player] - lastroll
        playerpositions[player] = playerpositions[player] - len(boardpos) + lastroll
    print('player '+str(current_player)+" lands on "+str(boardpos[playerpositions[player]]))
    positioncheck(player,lastroll)
    turnloop(current_player)
    return

def chance(player):#applies a random chance card effect to the current player
    list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    names = ['explosion','government tax refund','production platform discount','good weather(pipe-laying barge)','hurricane(pipe-laying barge)','seamans strike','hurricane (exploration rig)','fire at refinery','storm damage to production platform','economic boom','refinery discount','pipe-laying barge option','reservoir difficulties','good weather(rig)','hurricane(production platform)','economic expansion program','government tax refund','good weather(supply boat)','government conservation','exploration rig option','legal action','economic recession','strike at refinery','field extension']
    effects = ['lose production platform on producing field(insurance provides free replacement at rig depot)','miss paying next monthly interest','the next production platform you buy will provide a 10% refund of 5000000','option to move a pipe-laying barge twice in a row, this ability is retained until used','if you have an active pipe-laying barge it is lost','all your supply boats are returned to your nearest base','if you have an exploration rig it is lost','the next two times you pass the production income square you do not receive income','next monthly income from head office reduced by 500000','next monthly income from head office is doubled','the next refinery you purchase will provide 10% refund of 5000000','you may acquire a pipe-laying barge at any time without use a decision, this ability is retained until it is used','one of your proven size 2 or 3 reservoirs(of your choice) is reduced by 1 size','option to move an exploration rig or production platform twice in a row, this ability is retained until used','one of your production platforms(your choice) is destroyed, insurance provides replacement at rig depot','the next monthly production income you collect is doubled','your next monthly running costs are free','option to move a supply boat twice in a row, this ability is retained until used','your next two monthly production incomes are halved','you may acquire an exploration rig at any time without use of a decision, this abilit is retained until it is used','next monthly income from head office reduced by 100000','your next monthly income from head office is reduced to 0','your next monthly production income is reduced to 0','one of your proven size 1 or 2 reservoirs(of your choice) is increased by 1 size']
    result = random.choice(list)
    print('player '+str(player + 1)+' draws the chance card '+str(names[result])+': '+str(effects[result]))

    # if result = 0:
    #     elif result = 1:
    #         elif result = 2:
    #             elif result = 3:
    #                 elif result = 4:
    #                     elif result = 5:
    #                         elif result = 6:
    #                             elif result = 7:
    #                                 elif result = 8:
    #                                     elif result = 9:
    #                                         elif result = 10:
    #                                             elif result = 11:
    #                                                 elif result = 12:
    #                                                     elif result = 13:
    #                                                         elif result = 14:
    #                                                             elif result = 15:
    #                                                                 elif result = 16:
    #                                                                     elif result = 17:
    #                                                                         elif result = 18:
    #                                                                             elif result = 19:
    #                                                                                 elif result = 20:
    #                                                                                     elif result = 21:
    #                                                                                         elif result = 22:
    #                                                                                             elif result = 23: 
    return

def moneychange(current_player,adjustment):#applies the provided financial change to the current_player
    
    return

def interestchange(current_player,adjustment):#adjusts the current players interest payments by the specified amount
    return



boardpos = ['rig depot','decision','supply depot 1','decision','chance factor','decision','decision','refinery 1','pay monthly running costs','decision','refinery 2','supply depot 2','decision','refinery 3','supply depot 3','chance factor','decision','collect monthly production income','decision','refinery 4','supply depot 4','chance factor','refinery 5','decision','decision','supply depot 5','pay monthly interest','decision','supply depot 6','decision','decision','chance factor','refinery 6','decision','pipe-laying barge depot','collect monthly income from head office'] #every square on the board in a list
#boardpos = range(1,37)
oilfields = [0,0,0,1,2,3,2,1,0,0,0,0] #every oilfield tile in order from 1,1 to 12,12 as a list, 0 = empty, 1 = low, 2 = medium, 3 =  high
explorepool = 2 # number of available exploration rigs
pipepool = 2 #number of available pipe laying barges
playercount = 3
sleeptime = 0

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
current_player = 0
lastroll = 0
turnloop(current_player)





