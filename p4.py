years = int(input("Количество лет: "))
exhibits = years*365*96
print("Кол-во экспонатов: "+ str(exhibits))
exhibits2 = int(input("Количество просмотренных экспонатов: "))
minutes = exhibits2*5
hours = minutes/60
days = hours/8
years2 = days/365
print("Кол-во лет: " + str(years2))

