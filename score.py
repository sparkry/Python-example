socre = int(input('请输入你的成绩: '))
if socre < 90:
    print('优秀')
elif socre < 80:
    print('较好')
elif socre < 70:
    print('良好')
elif socre < 60:
    print('及格')
else:
    print('不及格')