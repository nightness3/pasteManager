# -*- coding: utf-8 -*-

import os
import sys

def getPastes():
    global pastes
    pastes = baseOfData.readlines()

def getNames():
    global names
    names = baseOfNames.readlines()

def add():
    global baseOfData
    global baseOfNames
    global countPastes
    print("Введите название пасты, которую собираетесь добавить, или введите '!Назад!', если хотите вернуться в главное меню")
    name = input("Ввод: ")
    if name == "!Назад!":
        begin()
    else:
        baseOfNames.write(name+"\n")
        countPastes = countPastes + 1
        print("Введите саму пасту, которую собираетесь добавить")
        text = input("Ввод: ")
        baseOfData.write(text+"\n")
        print("Паста добавлена","\n\n")
        baseOfData.close()
        baseOfNames.close()
        baseOfData = open('pastes.txt', 'r+')
        baseOfNames = open('names.txt', 'r+')
        getPastes()
        getNames()
        begin()

def search():
    global countPastes
    global baseOfData
    global baseOfNames
    print("Выберите как вы будете искать пасту: ")
    print("1. По имени \n2. По нескольким словам из пасты ('!Назад!', если нужно в главное меню)")
    choice = input("Ввод: ")
    if choice == '1':
        print("Введите название пасты (ВАЖНО! ввести название пасты полностью, сохраняя изначальную орфографию и пунктуацию)")
        searchWords = input("Ввод: ")
        for i in range(countPastes):
            if (names[i].lower()) == (searchWords.lower()+"\n"):
                print("\n")
                print("ID пасты: ", i+1)
                print("Название пасты: ", names[i])
                print("Паста: ")
                print(pastes[i])
    elif choice == '2':
        print("Введите несколько слов из пасты (ВАЖНО! ввести слова идущие в пасте подряд и как они написаны в пасте, сохраняя орфографию и пунктуацию)")
        searchWords = input("Ввод: ")
        searchWords = searchWords.split()
        for i in range(countPastes):
            splitPaste = pastes[i].split()
            for j in range(len(splitPaste)-len(searchWords)+1):
                str = ""
                for k in range(len(searchWords)):
                    str += splitPaste[j+k]
                if str.lower() == (''.join(searchWords)).lower():
                    print("\n")
                    print("ID пасты: ", i+1)
                    print("Название пасты: ", names[i])
                    print("Паста: ")
                    print(pastes[i])
                    break;
    begin()

def delete():
    global baseOfData
    global baseOfNames
    global countPastes
    print("Введите ID (число) пасты, которую вы хотите удалить (ID узнается во вкладке ПОИСК). '!Назад!', чтобы вернутся в главное меню.")
    choice = input()
    if choice == "!Назад!":
        begin()
    else:
        id = int(choice) - 1
        del pastes[id]
        del names[id]
        baseOfData.close()
        baseOfNames.close()
        os.remove("pastes.txt")
        os.remove("names.txt")
        baseOfData = open('pastes.txt', 'w+')
        baseOfNames = open('names.txt', 'w+')
        for paste in pastes:
            baseOfData.write(paste)
        for name in names:
            baseOfNames.write(name)
        print("Элемент удален","\n\n")
        countPastes = countPastes - 1
        begin()

def all_remove():
    global baseOfData
    global baseOfNames
    print("Вы уверены?")
    print("1. Да \n2. Вернуться назад")
    choice = int(input("Ввод: "))
    if choice == 1:
        baseOfData.close()
        baseOfNames.close()
        os.remove("pastes.txt")
        os.remove("names.txt")
        baseOfData = open('pastes.txt', 'w+')
        baseOfNames = open('names.txt', 'w+')
    elif choice == 2:
        begin()
    else:
        print("Неправильный ввод")
        all_remove()

def main():
    global countPastes
    global baseOfData
    global baseOfNames

    file_path = "pastes.txt"

    if not(os.path.exists(file_path)):
        baseOfData = open('pastes.txt', 'w+')
        baseOfNames = open('names.txt', 'w+')
    else:
        baseOfData = open('pastes.txt', 'r+')
        baseOfNames = open('names.txt', 'r+')

    global pastes
    global names
    pastes = []
    names = []

    getPastes()
    getNames()
    print(names)
    countPastes = len(pastes)

    print("╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭━╮╭━╮")
    print("╱╱╱╱╱╱╱╱╭╯╰╮╱╱┃┃╰╯┃┃")
    print("╭━━┳━━┳━┻╮╭╋━━┫╭╮╭╮┣━━┳━╮╭━━┳━━┳━━┳━╮")
    print("┃╭╮┃╭╮┃━━┫┃┃┃━┫┃┃┃┃┃╭╮┃╭╮┫╭╮┃╭╮┃┃━┫╭╯")
    print("┃╰╯┃╭╮┣━━┃╰┫┃━┫┃┃┃┃┃╭╮┃┃┃┃╭╮┃╰╯┃┃━┫┃")
    print("┃╭━┻╯╰┻━━┻━┻━━┻╯╰╯╰┻╯╰┻╯╰┻╯╰┻━╮┣━━┻╯")
    print("┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃")
    print("╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯")
    print("Привет, это менеджер паст от nightness3. Количество паст: ", countPastes)
    begin()

def begin():
    global baseOfNames
    global baseOfData
    print("Выберите что вы хотите сделать: \n1. Добавить новую пасту \n2. Поиск по пастам \n3. Удалить пасту (сначала нужно узнать id пасты с помощью поиска по пастам) \n4. Полностью удалить базу данных \n5. Узнать количество паст \n6. Закрыть программу \n7. Указания для добавления пасты \n8. О создателях")
    choice = input("Ваш выбор: ")
    if choice == '1':
        add()
    elif choice == '2':
        search()
    elif choice == '3':
        delete()
    elif choice == '4':
        all_remove()
    elif choice == '5':
        print("Количество паст: ", countPastes,"\n\n")
        begin()
    elif choice == '6':
        baseOfData.close()
        baseOfNames.close()
        sys.exit()
    elif choice == '7':
        print("Важно называть пасту уникально, не допускать дублирования названия паст, нужно чтобы в названии содержалась хотя бы одна буква. Сами пасты могут быть какими угодно, однако лучше, чтобы они содеражил хотя бы одно слово (паста была не пустая)")
        begin()
    elif choice == '8':
        print("Создатель: nightness3")
        print("Создал просто так, за несколько часов работы. Иногда буду делать обновления. В планах: добавить категории, улучшить поиск по пастам.")
        print("vk: vk.com/trollface_2003")
        begin()
    else:
        print("Неправильный ввод","\n\n")
        begin()


if __name__ == "__main__":
    main()
