import random

all = ['石头', '剪刀', '布']
win = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
option = """[0]石头
[1]剪刀
[2]布
请选择(0/1/2):"""
computer = random.choice(all)
myid = int(input(option))
player = all[myid]

print('Your choice: %s,Computer choice: %s ' % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
