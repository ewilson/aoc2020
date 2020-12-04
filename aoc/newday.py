from sys import argv

day = argv[1]

names = [f'day{day}.py', f'input{day}.txt', f'test{day}.txt']

for name in names:
    open(name, 'w')
