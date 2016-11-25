x = 99
def func2(y):
    global x
    x = 20           # variável local
    z = x * y
    return z

print(func2(2),"\n")
print(x)
