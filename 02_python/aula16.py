x=10 #não pode alterar o valor
while x: #não pode mudar essa condição
    x-=1
    if x % 2 != 0:
        continue
    print(x, end=' ')
    print("o valor de x:%d" % x)
#p/ próxima aula
#não pode haver instrução duplicada
#não pode haver loop infinito
