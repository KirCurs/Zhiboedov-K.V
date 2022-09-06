# -- coding: utf-8 --
#import sys
#print("Курс Основы программирования начался")
#print(16823 * 12302 % 3092)
#age = int(input("Сколько вам лет"))
#name = input("Введите имя ")
#if name != "Иван" or "Ваня":
#    if 0 < age < 75:
#        if age < 16: 
#            print("Сначала нужно окончить школу!")
#            years = 18 - age 
#            print("Вам осталось учится " + str(years))
#        elif 16 < age < 75: print("Поздравляем вы поступили в ВГУИТ")
#else: quit() #Не понимаю почему не прерывается цикл

sec = int(input("Введите кол-во секунд"))

day = sec // 86400
sec %= 86400
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60

print(str(day), str(hour), str(min), str(sec),sep = ":" )