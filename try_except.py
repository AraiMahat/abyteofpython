try:
    text = input('Enter something --> ')
except EOFError:
    print('\nWhy did you do an EOF on me?')
except KeyboardInterrupt:
    print('\nYou cancelled the operation.')
else:
    print('You entered {}'.format(text))