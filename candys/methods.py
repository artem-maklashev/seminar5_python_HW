from random import randint


def GetNumber(message, min_number, max_number):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            if min_number <= number <= max_number:
                isCorrect = True
            else:
                print(f'Значение должно быть от {min_number} до {max_number}')
        except ValueError:
            print("Введено не целое число. Повторите ввод ")
    return number


def coin(player):
    print('Бросим жребий!')
    heads_tails = GetNumber(
        f'{player}, введите 1 если выбираете "орел" или 0 если "решка": ', 0, 1)
    coin = randint(0, 1)
    message = 'орел' if coin == 1 else 'решка'
    print(f'Выпал(а) --> {message}')
    return 2 if heads_tails != coin else 1


def switch_turn(x): return 2 if x == 1 else 1

def logic(candies):
    if candies % 29 != 0:
        number = candies % 29
    else:
        number = candies if candies <= 28 else randint(1, 28)
    return number

def GameVariant():
    variant = GetNumber('Выберите вариант игры (1 - человек против человека, 2 - человек против бота)',1 ,2)
    return 'pve' if variant == 2 else 'pvp'


def GameProcess(player1, player2, pve=True):
    player_1 = player1
    player_2 = player2
    turn = coin(player_1)
    remains = 325
    stop_game = False

    while stop_game == False:
        player = player_1 if turn == 1 else player_2
        print(f'Остаток конфет --> {remains}')
        print(f'Ход игрока {player}')
        candies = logic(remains) if pve and turn ==2 else GetNumber(
            'Какое количество конфет вы берете (1...28): ', 1, 28)
        if candies < remains:
            remains -= candies
            print(f'Игрок {player} забрал {candies} конфет')
            turn = switch_turn(turn)
        else:
            print(f'Победил игрок {player}')
            stop_game = True



