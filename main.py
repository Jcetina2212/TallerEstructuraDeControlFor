archivo = open('paises2.txt','r')
#imprima la posicion de colombia
#for i in archivo:
  #print(i)
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")  
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la letra B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
c=0
for i in ciudad:
  if(i[0]=="M"):
    c+=1
    print(i)
print(c)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
#c1=0
for i in pais:
  #c1+=1
  if (i[0]=="U"):
    print(i)
    #print(c1)
#c=0
for i in ciudad:
  #c+=1
  if(i[0]=="U"):
    print(i)
    #print(c)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  print(i)
print(len(paises))
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
c=0
for i in ciudad:
  c+=1
  if(i=="Singapur"):
    print(i)
    print(c)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="Venezuela"):
    print(i)
    #print(c)
    print(ciudad[c-1])
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
c=0
for i in pais:
  c=+1
  if(i=="E"):
    print(i)
    print(c)
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="Colombia"):
    #print(i)
    print(ciudad[c-1])
    #print(c)
"""
#imprima la posicion del pais de Uganda
"""
lista=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
c=0
for i in pais:
  c+=1
  if(i=="Uganda"):
    print(i)
    print(c)
"""
#imprima la posicion del pais de México
"""
lista=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="México"):
    print(i)
    print(c)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
c=0
for i in pais:
  c+=1
  if (i=="Madagascar"):
    ciudad.insert(c-1,"Antananarivo")
    print(pais[c-1],":",ciudad[c-1])
    print(c)
"""
#Agregue un país que no esté en la lista
"""
lista=[]
ciudad=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for p in range(0,a):
    lista.append(i[p])
  a="".join(lista)
  pais.append(a)
  lista=[]
  b=i.index(":")
  for c in range(b+2,len(i)-1):
    lista.append(i[c])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
pais.append("Kosovo")
pais.sort()
c=0
listac=[]
for i in pais:
  c+=1
  if(i=="Kosovo"):
    ciudad.insert(c-1,"Pristina")
    print(pais[c-1],":",ciudad[c-1])
    print(c)
"""