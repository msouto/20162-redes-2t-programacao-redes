#O zip pode ser usado também para construir dicionário a partir de listas
chaves = ['a', 'b', 'c', 'd']
valores = [1, 2, 3, 4]
D1 = dict(zip(chaves, valores))
print(D1)

#outra sintaxe
D2 = {k: v for (k, v) in zip(chaves, valores)}
print(D2)
