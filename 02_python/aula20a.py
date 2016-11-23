#uso do zip
L1=['a','b','c','d']
L2=[1,2,3,4]
a=zip(L1,L2)
print(a)
print(list(a))
for (x, y) in list(zip(L1, L2)):
    print(x,"-", y)
