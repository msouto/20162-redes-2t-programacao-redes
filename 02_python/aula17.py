y=19009938080983209480325329053285283
x=y//2
while x > 1:
    if y%x == 0:
        print(y,'tem fator', x)
        break
    x-=1
else:
    print(y, 'eh primo')
