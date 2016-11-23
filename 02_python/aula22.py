#Uso do enumerate
s = 'spam'
print(enumerate(s))
print(list(enumerate(s)))

for (offset, valor) in enumerate(s):
    print(offset, valor)
