nombre = input("Ingrese su nombre")
edad = int(input("Ingrese su edad"))
hora = 19
#Ingresar un nombre y su edad.
#Si es menor de edad que indique que dependiendo de la hora (si es mas de las 6pm) 
#debe ir a dormir y si no hacer la tarea.
#Si es mayor de edad que indique que no esta obligado a hacer nada.
if edad <18 :
  if hora>18:
    print ('Hola ', nombre ,' debes ir a domir')
  else:
    print('Hola ', nombre ,' debes hacer la tarea')
else:
  print('Hola ', nombre ,' no estás obligado a hacer nada')