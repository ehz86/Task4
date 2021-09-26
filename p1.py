a = str (input ("Введите имя студента: "))
b = str (input ("Введите фамилию студента: "))
c = int (input ("Введите год рождения студента: "))
print (a + ' ' + b +' ' + str(c))
d = a
a = b
b = d
c = c + 60
print (a + ' ' + b +' ' + str(c))