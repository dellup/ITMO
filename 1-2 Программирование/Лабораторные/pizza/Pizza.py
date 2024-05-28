import time, math, datetime, sqlite3, asyncio
from threading import Thread
from abc import ABC, ABCMeta, abstractmethod, abstractproperty
with sqlite3.connect("base.db") as db:
    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(40),
        price INTEGER NOT NULL DEFAULT 500
    )
    """
    cursor.executescript(query)

async def sleep(sec):
    await asyncio.sleep(sec)
class Pizza(ABC):
    def __init__(self, price, dough="Пшеничное тесто", sauce="Томатный соус", filling=["Колбаски","Сыр"]):
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.__price = price

    def __str__(self):
        return "Цена: {0}".format(self.__price)
    
    def __add__(self, other):
        return Pizza(self.__price + other.getCoast())
    
    def __sub__(self, other):
        return Pizza(abs(self.__price - other.getCoast()))

    def getCoast(self):
        return self.__price


class PizzaMixin():

    def bake(self, vremya):
       print("Испечем пиццу " + self.name)
       asyncio.run(sleep(vremya))

    def cut(self):
        print("Порежем ингредиенты пиццы " + self.name)
        asyncio.run(sleep(3))

    def pack(self):
        print("Пицца " + self.name + " упакована")
        asyncio.run(sleep(1))

    def prepare(self):
        print("Замесим " + self.dough)
        print(f"Подготовим {self.sauce} и {self.filling}")
        self.cut()
        print("Раскатаем тесто, расположим подготовленный соус и ингредиенты на нем")
        asyncio.run(sleep(4))

    def cook_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Пицца начала готовиться в {formatted_datetime}")
            result = func(*args, **kwargs)
            end_time = time.time()
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Пицца закончила готовиться в {formatted_datetime}")
            print(f"Пицца готовилась {math.floor((end_time - start_time))} секунд")
            return result
        return wrapper
    
    @cook_time
    def start(self, vremya):
        self.prepare()
        self.bake(vremya)
        self.pack()



class PizzaBBQ(Pizza, PizzaMixin):
    def __init__(self, price, dough="Пшеничное тесто", sauce="Барбекю соус", filling=["Колбаски","Сыр"]):
        super().__init__(price, dough, sauce, filling)
        self.name = "BBQ"
    def moremeat(self):
        print("Добавляем больше мяса")
    def getName(self):
        return self.name
    def moremeat(self, typeofmeat):
        print(f"Добавляем больше мяса {typeofmeat}")
    


class PizzaGiftsOfTheSea(Pizza, PizzaMixin):
    def __init__(self, price, dough="Пшеничное тесто", sauce="Томатный соус", filling=["Колбаски","Сыр","Лобстер"]):
        super().__init__(price, dough, sauce, filling)
        self.name = "Дары моря"
    def morelobster(self):
        print("Добавляем больше лобстера")
    def getName(self):
        return self.name
    def morelobster(self, typeoflobster):
        print(f"Добавляем больше лобстера {typeoflobster}")


class PizzaPepperoni(Pizza, PizzaMixin):
    def __init__(self, price, dough="Пшеничное тесто", sauce="Томатный соус", filling=["Колбаски","Сыр","Мясо"]):
        super().__init__(price, dough, sauce, filling)
        self.name = "Пепперони"
    def morecheeze(self):
        print("Добавляем больше сыра")
    def getName(self):
        return self.name
    def morecheeze(self, typeofcheeze):
        print(f"Добавляем больше сыра {typeofcheeze}")  



class Order:
    def __init__(self, listOfPizzas):
        self.listOfPizzas = listOfPizzas
        self.count = 0
        self.order = self.doOrder()
        
    def doOrder(self):
        try:
            lstNames = ["пепперони", "барбекю", "дары моря"]
            pizzas = []
            for i in range(len(self.listOfPizzas)):
                if self.listOfPizzas[i].lower() == lstNames[0]:
                    pepperoni = PizzaPepperoni(500)
                    thread1 = Thread(target=pepperoni.start, args=(10,))
                    thread1.start()
                    pizzas.append(pepperoni)
                elif self.listOfPizzas[i].lower() == lstNames[1]:
                    bbq = PizzaBBQ(550)
                    thread2 = Thread(target=bbq.start, args=(15,))
                    thread2.start()
                    pizzas.append(bbq)
                elif self.listOfPizzas[i].lower() == lstNames[2]:
                    giftsofsea = PizzaGiftsOfTheSea(600)
                    thread3 = Thread(target=giftsofsea.start, args=(7,))
                    thread3.start()
                    pizzas.append(giftsofsea)
            
            db = sqlite3.connect("base.db")
            cursor = db.cursor()
            for i in range(len(pizzas)):
                name = pizzas[i].getName()
                coast = pizzas[i].getCoast()
                values = [name, coast]
                cursor.execute("INSERT INTO orders(name, price) VALUES(?, ?)", values)
                db.commit()
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close
        return pizzas
    def countOfCoast(self):
        for i in range(len(self.order)):
            self.count+=self.order[i].getCoast()
        return self.count

class Rejection(Exception):
    def __init__(self, lst):
        self.lst = lst
        super().__init__()
    def __str__(self) -> str:
        print(f"Ваш заказ был {self.lst}, но вы отказались от него. Сделайте заказ заново")

class Terminal:
    def menu(self):
        menu = [["Пепперони", "Цена: 500"], ["Барбекю", "Цена: 550"], ["Дары моря", "Цена: 600"]]
        print("Наше меню: ")
        for i in range(len(menu)):
            for j in range(len(menu[i])):
                print(menu[i][j])
            print("----------------------")
    def takeOrder(self):
        while True:
            self.menu()
            lst = []
            while True:
                a = input("Введите пиццу('stop' для завершения заказа'): ")
                if a=='stop':
                    break
                lst.append(a)
            print(f"Ваш заказ: {lst}")
            b = input("Согласны ли вы с заказом? ")
            try:
                if b.lower() == "да":
                    order = Order(lst)
                    print(f"Стоимость заказа: {order.countOfCoast()}")
                    print("Заказ успешно создан.")
                    return order
                raise(Rejection(lst))
            except Rejection as error:
                error.__str__()

terminal = Terminal()
terminal.takeOrder()