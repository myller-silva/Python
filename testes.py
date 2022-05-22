lista = []
str = "12345"
len = len(str)
c = 0
if(len%2!=0): 
  lista += str[c]
  c+=1
lista += ( (str[i:i+2]) for i in range( c, len, 2 ))
print(lista)
