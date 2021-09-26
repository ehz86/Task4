cathet1 = float(input ("Введите длину первого катета: "))
cathet2 = float(input ("Введите длину второго катета: "))
hypotenuse = (cathet1 ** 2 + cathet2 ** 2) ** 0.5
perimeter = (cathet1 + cathet2 + hypotenuse)
square = (cathet1 * cathet2) / 2
print ("Площадь прямоугольного треугольника: " + str(square))
print ("Периметр прямоугольного треугольника: " + str(perimeter))