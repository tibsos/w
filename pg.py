import random


letters = 'asdfghjklqwertyuiopzxcvbnm'
numbers = '1234567890'
symbols = "!@#$-_^&*()[]\|/?~`.,'"

all_symbols = []

all_symbols += [letters]
all_symbols += [letters.upper()]
all_symbols += [numbers]
all_symbols += [symbols]

password_length = 100

password = []

for i in range(password_length):

    symbol_type = all_symbols[random.randint(0, 3)]

    symbol = symbol_type[random.randint(0, len(symbol_type) - 1)]

    password.append(symbol)


password = "".join(password)

print('Password: ' + password)