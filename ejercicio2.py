def nota():
    x=float(input('Nota del Hito individual:  '))
    y=float(input('Nota del Hito Grupal:  '))
    z=float(input('Nota del Examen:  '))
    print(f'Tu nota es {round(x*0.3+y*0.2+z*0.5,2)}')
nota()