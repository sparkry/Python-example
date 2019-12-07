import getpass
user = input('请输入用户名: ')
passwd = getpass.getpass('password: ')

if user == 'bob' and passwd == '123456':
    print('登录成功')
else:
    print('登录失败！')


