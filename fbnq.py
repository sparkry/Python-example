fb = [0,1]
n = int(input('请输入长度: '))
for i in range(n-2):
    fb.append(fb[-1]+fb[-2])
print(fb)
