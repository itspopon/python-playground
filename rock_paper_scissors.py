from random import choice


def choice_to_text(c):
    i = c - 1
    return ['Rock', 'Paper', 'Scissors'][i]


def who_wins(aiChoice, playerChoice):
    if aiChoice == 1:
        if playerChoice == 1:
            return 'Draw!'
        if playerChoice == 2:
            return 'You win!'
        if playerChoice == 3:
            return 'You lose!'
    if aiChoice == 2:
        if playerChoice == 1:
            return 'You lose!'
        if playerChoice == 2:
            return 'Draw!'
        if playerChoice == 3:
            return 'You win!'
    if aiChoice == 3:
        if playerChoice == 1:
            return 'You win!'
        if playerChoice == 2:
            return 'You lose!'
        if playerChoice == 3:
            return 'Draw!'


playing = True

while playing:
    ai = choice([1, 2, 3])

    print()
    print('Choose one:')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    print('(Type quit to quit)')

    pick = input()

    if pick:
        if pick[0] == '1' or pick.lower() == 'rock':
            print(f'You picked Rock and the AI picked {choice_to_text(ai)}')
            print(who_wins(ai, 1))
        elif pick[0] == '2' or pick.lower() == 'paper':
            print(f'You picked Paper and the AI picked {choice_to_text(ai)}')
            print(who_wins(ai, 2))
        elif pick[0] == '3' or pick.lower() == 'scissors':
            print(
                f'You picked Scissors and the AI picked {choice_to_text(ai)}')
            print(who_wins(ai, 3))
        elif pick[0].lower() == 'q':
            playing = False
        else:
            print('Not a valid choice, the AI wins!')
    else:
        print('You didn\'t pick, the AI wins!')

    input()
