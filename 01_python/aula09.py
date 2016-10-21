#Exemplo de script para armazenamento
x, y, z = 43, 44, 45
s = 'spam'
d = {'a':1, 'b':2}
l = [1, 2, 3]
f = open('datafile.txt', 'w')
f.write(s + '\n')
f.write('%s, %s, %s\n' % (x, y, z))
f.write(str(l) + '$' + str(d) + '\n')
f.close()
