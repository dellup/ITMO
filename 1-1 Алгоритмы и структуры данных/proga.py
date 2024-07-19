
from calendar import isleap
import sys

print("Программа для контроля собственных денежных средств")
flag = True
def isFloat(num):
    try:
        float(num)
    except (ValueError):
        return False
    return True


def sortByPrice(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-i-1):
            if matrix[j][2] > matrix[j+1][2]:
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
    outputlst(matrix)


def sortByPriceReverse(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-i-1):
            if matrix[j][2] < matrix[j+1][2]:
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
    outputlst(matrix)


def outputlst(matrix):
    count = 1
    print("-"*43+"Корзина продуктов"+"-"*43)
    print('|'+'Имя'.ljust(35, ' ')+"|"+"Категория".ljust(21, ' ')+'|'
          +"Стоимость".ljust(21, ' ')+'|'+"Дата".ljust(21, ' ')+'|')
    for i in range(len(matrix)):
        print('|'+str(count)+'. ',end='')
        for j in range(4):
            if j == 0:
                print((str(matrix[i][j]).ljust(32, ' ')+'|'), end='')
            else:
                print((str(matrix[i][j]).ljust(21, ' ')+'|'), end='')
        count+=1
        print()


def searchByDate(matrix, date):
    a = []
    for i in range(len(matrix)):
        if matrix[i][3].strip() != date:
            a.append(i)
    a.sort(reverse=True)
    print(a)
    for i in range(len(a)):
        matrix.pop(a[i])
    return matrix

def searchByCategory(matrix, category):
    a = []
    for i in range(len(matrix)):
        if matrix[i][1].strip() != category:
            a.append(i)
    a.sort(reverse=True)
    print(a)
    for i in range(len(a)):
        matrix.pop(a[i])
    return matrix

def tests():
    flag2 = True
    while flag2:
        price_of_product = input("Введите стоимость продукта(макс 999999999999999): ").strip()
        if isFloat(price_of_product):
            if float(price_of_product) >= 0 and float(price_of_product) <= 999999999999999:
                price_of_product = round(float(price_of_product), 5)
                flag2 = False
            else:
                print("Ввели неверную стоимость. Попробуйте снова.")
        else:
            print("Ввели неверную стоимость. Попробуйте снова.")
    flag3 = True
    while flag3:
        date_of_product = input("Введите дату реализации продукта(формат хх.хх.хххх): ").strip()
        if (len(date_of_product) == 10 and date_of_product[:2].isdigit() and date_of_product[3:5].isdigit()
        and date_of_product[6:].isdigit()):
            if (1 <= int(date_of_product[:2]) <= 31 and 1 <= int(date_of_product[3:5]) <= 12 
                and 1900 <= int(date_of_product[6:]) <= 2023 
                and checkDate(int(date_of_product[:2]), int(date_of_product[3:5]), int(date_of_product[6:]))):
                flag3 = False  
            else:
                print("Вы ввели неверную дату. Попробуйте снова") 
        else:
            print("Вы ввели неверную дату. Попробуйте снова")
    return (price_of_product, date_of_product)


def checkDate(day, month, year):
    a = [(1, 31), [2, 28], (3, 31), (4, 30), (5, 31), (6, 30), (7,31), (8, 31), (9, 30), (10, 31), 
        (11, 30), (12, 30)]
    if month == 2:
        if isleap(year):
            a[1][1] = 29
    if a[month-1][1] >= day:
        return True




cart = []
while flag:
    flag0 = True
    while flag0:
        print("Возможные действия: \n1. Добавить продукт в корзину.\n", end='')
        print("2. Просматривать список продуктов.\n3. Просматривать покупки по дате и категории.\n", end='')
        print("4. Сортировка и вывод по возрастанию стоимости.\n",end='')
        print("5. Сортировка и вывод по убыванию стоимости.\n6. Удалить товар из списка.\n",end='')
        print("7. Выйти из программы")
        num = input("Введите номер действия: ").strip()
        if num.isdigit() and (num in ['1', '2', '3', '4', '5', '6', '7']):
            flag0 = False
        else:
            print("Введите корректный номер: ")
    if num == '1':
        name_of_product = input("Введите имя продукта: ").strip().lower()
        category_of_product = input("Введите категорию продукта: ").strip().lower()
        result = tests()
        price_of_product, date_of_product = result[0], result[1]
        ls = [name_of_product, category_of_product, price_of_product, date_of_product]        
        cart.append(ls)
        print("Продукт добавлен в корзину.")
    elif num == '2':
        outputlst(cart)
    elif num == "3":
        flag4 = True
        while flag4:
            com = input("Что вы хотите сделать? Введите команду. \n 1. Просмотр по дате."+ 
                        "\n 2. Просмотр по категории\n").strip()
            if com in ['1', '2']:
                flag4 = False
            else:
                print("Неверная команда. Попробуйте ещё раз.")
        flag4 = True
        if com == '1':
            while flag4:
                inp = input("Введите дату реализации продукта(формат хх.хх.хххх): ").strip()
                if len(inp) == 10 and inp[:2].isdigit() and inp[3:5].isdigit() and inp[6:].isdigit():
                    if (1 <= int(inp[:2]) <= 31 and 1 <= int(inp[3:5]) <= 31 and 1900 <= int(inp[6:]) <= 2023
                    and checkDate(int(inp[:2]), int(inp[3:5]), int(inp[6:]))):
                        flag4 = False  
                    else:
                        print("Вы ввели неверную дату. Попробуйте снова") 
                else:
                    print("Вы ввели неверную дату. Попробуйте снова")
            lst = cart.copy()
            z = searchByDate(lst, inp)
            print("Список продуктов по дате")
            outputlst(z)
        if com == '2':
            category = input("Введите категорию товара: ").strip().lower()
            lis = cart.copy()
            x = searchByCategory(lis, category)
            outputlst(x)
            
    elif num == '4':
        sortByPrice(cart)
    elif num == '5':
        sortByPriceReverse(cart)
    elif num == '6':
        a = [str(i) for i in range(1, len(cart)+1)]
        flag1 = True
        while flag1:
            result = input("Введите номер продукта в корзине, который хотите удалить: ").strip()
            if (result in a):
                cart.pop(int(result)-1)
                break
            else:
                print("Введите корректный номер продукта в таблице")
        
        outputlst(cart)
    elif num == '7':
        flag = False


sys.stdout = open("text.txt", "w")
outputlst(cart)
