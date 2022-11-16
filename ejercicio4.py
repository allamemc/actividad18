def rectangulo():
    base =float(input('Base del rectángulo: '))
    altura =float(input('Altura del rectángulo: '))

    area = base*altura
    peri = base*2+altura*2

    print(f'La área es {area}cm2 y el perímetro {peri}cm')
rectangulo()