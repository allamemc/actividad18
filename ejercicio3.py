# • Se pide calcular la nota de tu examen tipo test.
# • Serán 20 preguntas
# • Las preguntas correctas sumarán 0,5
# • Las preguntas incorrectas restarán 0,25
# • Las preguntas sin contestar tendrán 0

# Datos de entrada
# Las preguntas correctas
# Preguntas incorrectas
# Preguntas sin contestar

# Datos de salida
# Nota del examen

# Proceso
# C = int numero de correctas
# I = int numero de incorrectas
# SC = int numero de sin contestar

pc= int(input('Numero de correctas: '))
pi= int(input('Numero de incorrectas: '))
ps = int(input('Numero sin contestar: '))

if pc+pi+ps != 20:
    print('Introduzca un numero valido de preguntas: ')

nota=pc*0.5-pi*0.25
print(round(nota))



