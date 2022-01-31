spis=["Один","два","3","Четыре","lOl","6","сЕМЬ"]
text=["ESTonia"]
while True:
    Answ=input("Хотите узнать функции списков? (1 - да / 0 - нет)")
    print(spis)
    if Answ=="1":
        print("1-Вывести список")
        print("2-Сделать список в верхнем регистре")
        print("3-Сделать список в нижнем регистре")
        print("4-Показывает наибольшое значение в списке")
        print("5-Перевернуть список")
        print("6-Выводит символ по его числовому значению")
        print("7-Выводит число по значению его символа")
        print("8-Первую букву слова переводит в верхний регистр")
        print("9-Преобразовывает список в строку")
        print("10-Очищает список")
        Answ2=input("Выбери число: ")
        if Answ2=="1":
            print(spis)
        elif Answ2=="2":               
            print(text.upper())
        elif Answ2=="3":      
            print(text.lower())
        elif Answ2=="4":
            print(max(spis))
        elif Answ2=="5":                
            spis.reverse()
            print(spis)
        elif Answ2=="6": 
            a=chr(43)
            print(a)
        elif Answ2=="7":
            a=ord("+")
            print(a)
        elif Answ2=="8":
            strspis=" ".join(spis)
            strspis.title()
            print(strspis)
        elif Answ2=="9":
            strspis="".join(spis)
            print(strspis)
        elif Answ2=="10":
            spis.clear()
            print(spis)
        break
    elif Answ=="0":
        quit()
