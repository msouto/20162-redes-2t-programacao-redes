#Convertendo de volta os objetos
arquivo = open(‘datafile.txt’,'r')
linha = arquivo.readline()
print(linha.rstrip())

linha = arquivo.readline()
lista_numeros = [int(p) for p in linha.split(‘,’)]
print(lista_numeros)

linha = arquivo.readline()
sequencias = [eval(p) for p in linha.split(‘$’)]
print(sequencias)
