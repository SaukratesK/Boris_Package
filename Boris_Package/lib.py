from termcolor import colored, cprint

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def try_me():
    name = input('Whats your name ? ')

    while has_numbers(name):
        name = input('Invalid Name. Try again! ')

    #print(type(name))
    text = colored(f'Hello {name} ! How are you ?', 'red', attrs=['reverse', 'blink'])
    print(text)

    #print(f'Bonjour {name}')
