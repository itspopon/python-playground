'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**options):
    result = 0
    operation = options.get('operation')
    first = options.get('first')
    second = options.get('second')

    if operation == 'add':
        result = first + second
    if operation == 'subtract':
        result = first - second
    if operation == 'multiply':
        result = first * second
    if operation == 'divide':
        result = first / second
    if options.get('make_float'):
        result *= 1.0
    if options.get('message'):
        return options.get('message') + ' {}'.format(result)
    else:
        return 'The result is {}'.format(result)


print(calculate(make_float=False, operation='add',
                message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
