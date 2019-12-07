#1+...100的和
num = 0
counter = 0
while counter < 101:
    num += counter
    counter += 1
print(num)


#9*9乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print('%d*%d=%d' % (y,x,y*x),end=' ')
    print()


#拓展.输入任意n,1+...n
num = 0
counter = 1
n = int(input('请输入要加到的数: '))
while counter < n+1:
    num += counter
    counter += 1
print(num)



n = int(input('请输入数字：'))
for x in range(1,n+1):
    for y in range(1,x+1):
        print('%d*%d=%d' % (y,x,y*x),end=' ')
    print()