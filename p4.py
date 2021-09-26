years = int(input("Количество лет:"))
exhibits = int(input("Количество просмотренных экспонатов: "))
minutes = exhibits*5
hours = minutes/60
days = hours/8
years2 = days/365
print("Кол-во лет: " + str(years2))
exhibits2 = years*365*96
print("Кол-во экспонатов"+ str(exhibits2))
