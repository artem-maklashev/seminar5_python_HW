import os
from winlist import winlist
from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def DefoultNet():
    cell = []
    for i in range(1,10):
        cell.append(i)
    #print(cell)
    return cell

def DrawNet(net_list):
    cls()
    print('+---+---+---+')
    for i in range(0,len(net_list)):
        if net_list[i] in range(1,10):
            print(f'| \033[91m{net_list[i]} \033[0m', end='')
        elif net_list[i] == 'X' :
            print(f'| \033[32m{net_list[i]} \033[0m', end='')
        elif net_list[i] == 'O':
            print(f'| \033[36m{net_list[i]} \033[0m', end='')
        if i==2 or i == 5 or i==8:
            print (f'|\n+---+---+---+')
        
def turn(player):
    if player == 'human':
        player = 'bot'
        symbol = 'O'
    else:
        player = 'human'
        symbol = 'X'

    return player, symbol

def ChangeCell(index, net, symbol):
    net[index-1] = symbol
    # DrawNet(net)

def CheckWin(winlist, net):
    x_list = []
    o_list =[]
    for i in range(0,len(net)):
        if net[i]=='O':
            o_list.append(i+1)
        elif net[i]=='X':
            x_list.append(i+1)
    DrawNet(net)
    for i in range(len(winlist)):
        if len(set(x_list).intersection(set(winlist[i]))) == 3:
            # DrawNet(net)
            print('\033[32mТы выиграл :( \033[0m')
            return False
        elif len(set(o_list).intersection(set(winlist[i]))) == 3:
            # DrawNet(net)
            print('\033[36mМеня не победить \033[0m')
            return False
        elif len(x_list)+len(o_list) == 9:
            # DrawNet(net)
            print ('Похоже ничья')
            return False

# первая версия
# def Intelect(winlist, net):
#     step = None
#     x_list = []
#     for i in range(len(net)):
#         if net[i]=='X':
#             x_list.append(i+1)
#             print(x_list)
#     # if len(x_list) == 2:
#     #     for i in range(len(winlist)):
#     #         if len(set(x_list) & set(winlist[i])) == 2:
#     #             step = (set(winlist[i]).difference(set(x_list))).pop()
#     #             if net[step-1] in range(1,9):        
#     #                 ChangeCell(step, net, 'O')
#     #                 return
#     #             else:
#     #                 number = step
#     #                 while step in x_list and step == number: 
#     #                     step = randint(1,9)
#     #                 ChangeCell(step, net, 'O')
#     #                 return
#     if len(x_list) >= 2:
#         for i in range(len(x_list)):
#             for j in range(1, len(x_list)):
#                 for k in range(len(winlist)):
#                     if len(set([i, j]).intersection(winlist[k])) == 2:
#                         step = set(winlist[k]).difference(set([x_list[i], x_list[j]])).pop()
#                         if net[step-1].isdigit():
#                             ChangeCell(step, net, 'O')
#                             return
#                     # else:
#                     #     step = randint(1,10)
#                     #     while step not in list(filter(lambda x: type(x) is int, net)): 
#                     #         step = randint(1,10)
#                     #     ChangeCell(step, net, 'O')
#                     #     return
#                 if step == None: 
#                     step = randint(1,9)
#                     while step not in list(filter(lambda x: type(x) is int, net)): 
#                         step = randint(1,9)       
#                     ChangeCell(step, net, 'O')
#                     return
#                 else:
#                     ChangeCell(step, net, 'O')
#                     return
                
                    
#                 #     while step not in list(filter(lambda x: type(x) is int, net)): 
#                 #         step = randint(1,10)
#                 #     ChangeCell(step, net, 'O')
#                 #     return

#     else:
#         step = randint(1,9)
#         while step not in list(filter(lambda x: type(x) is int, net)): #in x_list: 
#             step = randint(1,9)
#         ChangeCell(step, net, 'O')
#         return

def EmptyCells(net):
    empty_list = list(filter(lambda x: type(x) is int, net))
    return empty_list

def PlayerCells(net, symbol):
    player_cells = []#list(filter(lambda x: x is symbol, net))
    for i in range(len(net)):
        if net[i] == symbol:
            player_cells.append(i+1)
    return player_cells

def ChekCell(number : int, net : list):
    if number in EmptyCells(net):
        return True
    else:
        return False    

def Intellect2(net, winlist: set):
    player_list = PlayerCells(net, 'X')
    bot_list = PlayerCells(net, 'O')
    empty_cells = EmptyCells(net)
    # if len(player_list) == 2:
    #     for item in winlist:
    #         if len(set(item).intersection(set(player_list))) == 2:
    #             step = set(item).difference(set(player_list)).pop()
    #             if step in empty_cells:
    #                 ChangeCell(step, net, 'O')
    #                 return
    
    if len(player_list) >= 2:
        # for i in range(len(player_list)):
        #     for j in range(1,len(player_list)):
        #         new_list = [player_list[i], player_list[j]]
        #         for k in range(len(winlist)):
        #             if len(set(winlist[k]).intersection(set(new_list))) == 2: # нужно остальное переделать так же
                        step = ChekList(bot_list, winlist, empty_cells)
                        if step != None:
                            ChangeCell(step, net, 'O')
                            return
                        else:
                            step = ChekList(player_list, winlist, empty_cells)
                            if step != None:
                                ChangeCell(step, net, 'O')
                                return
    # else:
    #     if len(bot_list) == 2:
    #         for item in winlist:
    #             if len(set(item).intersection(set(bot_list))) == 2:
    #                 step = set(item).difference(set(bot_list)).pop()
    #                 if step in empty_cells:
    #                     ChangeCell(step, net, 'O')
    #                     return
    #     elif len(bot_list) > 2:
    #         # for i in range(len(bot_list)):
    #         #     for j in range(len(bot_list)):
    #         #         for k in range(1,len(winlist)):
    #         #             if len(set(winlist[k]).intersection([i,j])) == 2:
    #                         step = ChekList(bot_list, winlist)
    #                         if step in empty_cells:
    #                             ChangeCell(step, net, 'O')
    #                             return
    #     # else:
    index = randint(0, len(empty_cells)-1)
    step = empty_cells[index]
    ChangeCell(step, net, 'O')
    return

# def ChekList(player_list, winlist, empty_list):
#     step = None
#     for i in range(len(player_list)):
#             for j in range(1,len(player_list)):
#                 new_list = [player_list[i], player_list[j]]
#                 for k in range(len(winlist)):
#                     if len(set(winlist[k]).intersection(set(new_list))) == 2: 
#                         step = set(winlist[k]).difference(set([i,j])).pop()
#                         if step in empty_list:
#                             return step
#                         step = None
#     return step

def ChekList(player_list, winlist, empty_list):
    step = None
    for k in range(len(winlist)):
        if len(set(winlist[k]).intersection(set(player_list))) == 2: 
            step = set(winlist[k]).difference(set(player_list)).pop()
            if step in empty_list:
                return step
            step = None
    return step

cell = DefoultNet()
DrawNet(cell)
# player = 'bot'
while True:
    #DrawNet(cell)
    #player, symbol = turn(player) 
    isEmpty = False
    while not isEmpty:
        
        # DrawNet(cell)
        x = input(f'Ходи кожаный -> X // Введи номер ячейки ')
        if x.isdigit():
            x = int(x)
            isEmpty = True
    ChangeCell(x, cell, 'X')   

    if CheckWin(winlist, cell) == False:
        break
    else: 
        Intellect2(cell, winlist)
        if CheckWin(winlist, cell) == False:
            break