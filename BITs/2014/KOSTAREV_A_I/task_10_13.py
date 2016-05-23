#Задача №10, Вариант 13
#Напишите программу "Генератор персонажей" для игры. 
#Пользователю должно быть предоставлено 30 пунктов, 
#которые можно распределить между четырьмя 
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. 
#Надо сделать так, чтобы пользователь мог не только брать 
#эти пункты из общего "пула", но и возвращать их туда из 
#характеристик, которым он решил присвоить другие значения.

#Костарев Андрей
#16.05.2016

POINT = 30 
ochki = 30 
person = {"Сила":"0","Здоровье":"0","Ум":"0","Ловкость":"0"} 
points = 0 
choice = None 
while choice != 0: 
    print("""
0 - Выход
1 - Добавить пункты к характеристике
2 - Уменьшить пункты характеристики
3 - Просмотр характеристик
""")
    choice = int(input("Choose option: "))
    if choice == 1:
        print("Пожалуйста, введите характеристику для добавления пунктов. Для изменения доступны", len(person), "характеристики:")
        for item in person:
            print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Нет такой характеристики, проверьте введенные данные: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество пунктов для данной характеристики. У вас", ochki, "свободных пунктов")
            points = int(input("\n:"))
            while points > ochki or points < 0: 
                print("Вы не можете назначить такое количество пунктов", "Доступно", ochki, "свободных пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было добавлено к", char)
        ochki -= points 
    elif choice == 2:
        print("Пожалуйста, введите имя характеристики для снятия пунктов.", "Доступно изменение для: ")
        for item in person:
            if int(person[item]) > 0:  
                print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Нет такой характеристики, проверьте введенные данные: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество пунктов для характеристики. Доступно", person[char], "пунктов:")
            points = int(input("\n:"))
            while points > int(person[char]) or points < 0: 
                print("Невозможно удалить такое количество пунктов. Доступно", person[char], "пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было удалено")
        ochki += points 
    elif choice == 3:
        print("\nХарактеристики героя")
        for item in person:
            print(item, "\t\t", person[item])
        
    elif choice == 0:
        print("Пока!")
    else:
        print("В меню нет такого пункта")
input("\n\nНажмите Enter, чтобы выйти.")