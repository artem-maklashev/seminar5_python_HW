from methods import *
variant = GameVariant()
if variant == 'pvp':
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')
    GameProcess(player_1, player_2, False)
else:
    player_1 = input('Введите имя игрока: ')
    player_2 = 'SkyNet'
    GameProcess(player_1, player_2, True)
