import os
from winlist import winlist
from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def DefoultNet():
    cell = []
    for i in range(1,10):
        cell.append(i)
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

def EmptyCells(net):
    empty_list = list(filter(lambda x: type(x) is int, net))
    return empty_list

def PlayerCells(net, symbol):
    player_cells = []
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
    if len(player_list) >= 2:
        step = ChekList(bot_list, winlist, empty_cells)
        if step != None:
            ChangeCell(step, net, 'O')
            return
        else:
            step = ChekList(player_list, winlist, empty_cells)
            if step != None:
                ChangeCell(step, net, 'O')
                return
    index = randint(0, len(empty_cells)-1)
    step = empty_cells[index]
    ChangeCell(step, net, 'O')
    return

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
while True:
    isEmpty = False
    while not isEmpty:
        x = input(f'Ходи кожаный -> X // Введи номер ячейки ')
        if x.isdigit(): 
            if int(x) > 0 and int(x) < 10:
                x = int(x)
                isEmpty = True
        DrawNet(cell)
    ChangeCell(x, cell, 'X')   

    if CheckWin(winlist, cell) == False:
        break
    else: 
        Intellect2(cell, winlist)
        if CheckWin(winlist, cell) == False:
            break