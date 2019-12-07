import random

num = random.randint(1, 100)
counter = 0

while counter < 5:
    mynum = int(input('请输入任意输入(1~100)数: '))
    if mynum < num:
        print('猜小了')
    elif mynum > num:
        print('猜大了')
    else:
        print('猜对了')
        break
    counter += 1
else:
    print('没机会啦!正确数字是%s' % num)
