astr = 'hello'
alist = [10,20,'tom','limin']
atuple = (20,60,'jerry','lihong')
adict = {'name':'spark','age':22,'home':'shannxi'}

print(astr)
print(alist)
print(atuple)
print(adict)



for a in astr:
    print(a)



for b in alist:
    print(b)


for c in atuple:
    print(c)


for d  in adict:
    print('%s:%s' % (d,adict[d]))