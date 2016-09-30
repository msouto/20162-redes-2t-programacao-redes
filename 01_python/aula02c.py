#Não pode somar diretamente uma string com um inteiro
#s='42'
#s+5
#>>> Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: must be str, not int

#conversao de string para inteiro
s='42'
y=int(s)+5
print(y)

#conversao de inteiro para string
y=s+str(5)
print(y)
