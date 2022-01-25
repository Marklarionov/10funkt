spis=["Один","два","3","Четыре","lOl","6","сЕМЬ"]
text=["estonia"]
while True:
    Answ=input("Хотите узнать функции списков? (1 - да / 0 - нет)")
    print(spis)
    if Answ=="1":
        print("1-Вывести список")
        print("2-Сделать список в верхнем регистре")
        print("3-Сделать список в нижнем регистре")
        print("4-Показывает наибольшое значение в списке")
        print("5-Перевернуть список")
        print("6-Колличество символов в списке")
        print("7-Сортировать список от меньшего к большему")
        print("8-Удалить элемент в конце списка")
        print("9-Добавить элемент в конец списка")
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
            print(len(spis))
        elif Answ2=="7":
            spis.sort()
            print(spis)
        elif Answ2=="8":  
            spis.pop()
            print(spis)
        elif Answ2=="9":
            spis.append(input("Добавить элемент: "))
            print(spis)
        elif Answ2=="10":
            spis.clear()
            print(spis)
        break
    elif Answ=="0":
        quit()