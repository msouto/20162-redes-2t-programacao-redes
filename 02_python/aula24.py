x = 99
def func1(y):
    z = x * y
    return z
def func2(y):
    x = 20           # variável local
    z = x * y
    return z

print(func1(2),"\n")
print(func2(2))
