from random import choice

emojis = ['🌨', '❌', '🙀', '🏦', '😽', '🕧', '💵', '🏯', '💀', '📗', '🍭', '🚱', '🔒',
          '😗', '📢', '🏊‍', '⏭', '🚬', '⏬', '💠', '💍', '🙃', '📵', '♎', '🗼', '😋']

playing = True
while playing:
    # Getting the desired size
    size = input('How tall should the pyramid be? (q to quit)  ')
    # If its a q, quit
    if size[0].lower() == 'q':
        playing = False
        break
    # Turn it into int and check if its between 1 and 80
    size = int(size)
    if not (size > 0 and size <= 80):
        print('Invalid size, a random value will be selected for you')
        # If its a invalid size pick a number from 5 to 20
        size = choice(range(5, 21))
        input()

    count = 1  # current count
    max = size  # max size
    down = False  # if its going down
    emoji = choice(emojis)  # random emoji

    while count > 0:
        # print the mojis count times
        print(f' {emoji}' * count)

        # count up or down
        if down:
            count -= 1
        else:
            count += 1

        # If hit the max start to go down
        if count == max:
            down = True
        if max == 1:
            count = 0
