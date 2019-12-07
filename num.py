# #打印1~100的循环数字
# for a in range(100):
#     print(a,end=' ') #end=表示此次循环后不回车
# print() #回车
#
# #打印1~100的奇数
# for b in range(100):
#     if b %2 !=0:
#         print(b,end=' ')
# print()
#
# #打印1~100的偶数
# for c in range(100):
#     if c %2 == 0:
#         print(c,end=' ')
# print()
#
# #打印1~100的偶数并整齐排列
# for d in range(100):
#     if d %2 == 0:
#         print(d,end='\t')
#     if(d+1) %10 == 0:
#         print("\n")


# 计算1~100偶数之和
number = 0
counter = 0
while counter < 101:
    counter += 1
    if counter % 2 == 0:
        number += counter
    else:
        continue
print(number)
