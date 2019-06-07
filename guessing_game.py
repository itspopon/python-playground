from random import randint

playing = True

while playing:
    print('Choose a number between 1 and 10')
    number = randint(1, 10)

    response = None
    while playing:
        response = int(input())
        if response == number:
            print('You got it! Yayyy!')
            break
        elif response < number:
            print('Too low, try again.')
        else:
            print('Too high, try again.')

    response = input('Do you want to play again? (y/n) ')
    if response[0].lower() == 'n':
        playing = False
