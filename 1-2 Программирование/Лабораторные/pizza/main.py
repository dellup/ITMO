import os
from abc import ABC, abstractmethod
from datetime import time, datetime
import random
from tkinter import ttk, messagebox

import db_connect
import Exceptions
from db_connect import Clients, Orders, Sauces, Dough, Fillings, Products
import time
import tkinter as tk
import threading


class MainApp:
    def __init__(self, root):
        self.order_id = self.make_order()
        self.root = root
        self.create_main_screen()
        self.pizza_quantities = {}

    def update(self):
        new_text = random.randint(1, 100)  # Генерируем случайное число
        self.label.config(text="Выберите действие:")  # Обновляем текст на метке

    @classmethod
    def make_order(self):

        new_order = Orders(client_id=1)
        session.add(new_order)
        session.commit()

        return new_order.order_id

    def create_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.root, text="Выберите действие:")
        self.label.pack()

        self.button_menu = tk.Button(self.root, text="Перейти к меню", command=self.go_to_menu)
        self.button_menu.pack()

        self.button_view_order = tk.Button(self.root, text="Просмотреть заказ", command=self.view_order)
        self.button_view_order.pack()

        # self.button_cancel_item = tk.Button(self.root, text="Отменить позицию", command=self.cancel_item)
        # self.button_cancel_item.pack()

        self.button_exit = tk.Button(self.root, text="Завершить работу", command=self.quit_app)
        self.button_exit.pack()
    def quit_app(self):

        if session.query(db_connect.Order_products).filter_by(order_id=self.order_id).count() == 0:
            order_to_delete = session.query(Orders).filter_by(order_id=self.order_id).first()

            if order_to_delete:
                session.delete(order_to_delete)
                session.commit()
        self.root.quit()
    def go_to_menu(self):
        self.clear_screen()

        self.label = tk.Label(self.root, text="Выберите категорию:")
        self.label.pack()

        self.button_pizza = tk.Button(self.root, text="Пицца", command=self.show_menu_pizza)
        self.button_pizza.pack()

        self.button_back = tk.Button(self.root, text="Назад", command=self.create_main_screen)
        self.button_back.pack()

    def view_order(self):
        self.clear_screen()

        entry_label = tk.Label(self.root, text="Введите номер заказа:")
        entry_label.pack()

        order_entry = tk.Entry(self.root)
        order_entry.pack()


        def show_order():
            order_id = order_entry.get()
            try:
                session = db_connect.session_db()
                order = session.query(db_connect.Order_products).filter(
                    db_connect.Order_products.order_id == order_id).all()

                self.clear_screen()

                if order:
                    label = tk.Label(self.root, text=f'Информация о заказе {order_id}:')
                    label.pack()
                    for i in order:
                        label_product_type = tk.Label(self.root, text=f'{i.product_info}')

                        label_product_type.pack()



                else:
                    label = tk.Label(self.root, text=f'Заказ с номером {order_id} не найден.')
                    label.pack()
                self.button_back = tk.Button(self.root, text="Назад", command=self.create_main_screen)
                self.button_back.pack()

            except Exception as e:
                label = tk.Label(self.root, text=f'Ошибка при доступе к базе данных: {e}')
                label.pack()

            finally:
                session.commit()
                session.close()

        button_show_order = tk.Button(self.root, text="Показать заказ", command=show_order)
        button_show_order.pack()



    def show_menu_pizza(self):
        try:
            session = db_connect.session_db()
            pizzas = session.query(Products).filter(Products.category == 'Пицца').all()
            self.clear_screen()

            label = tk.Label(self.root, text="Меню пиццы:")
            label.pack()

             # словарь для хранения количества пицц каждого вида

            for pizza in pizzas:
                frame = tk.Frame(self.root)
                frame.pack()

                label_name = tk.Label(frame, text=f'{pizza.product_id}. {pizza.product_name}')
                label_name.pack(side=tk.LEFT)

                quantity = tk.IntVar()
                quantity.set(0)

                self.pizza_quantities[pizza.product_id] = quantity  # сохраняем переменную количества для каждой пиццы

                # Создадим список для временного хранения экземпляров пицц
                temp_pizzas = []

                def change_ingredients(product_id, product_type):
                    compound_window = tk.Toplevel(self.root)
                    compound_window.title('Изменить состав пиццы')

                    available_sauces = session.query(Sauces).all()
                    available_fillings = session.query(Fillings).all()
                    available_dough = session.query(Dough).all()

                    label = tk.Label(compound_window,
                                     text=f'Выберите компоненты для пиццы {product_type.name}:')
                    label.pack()


                    sauce_combobox = ttk.Combobox(compound_window,
                                                  values=[sauce.sauce_name for sauce in available_sauces])
                    sauce_combobox.pack()

                    filling_combobox = ttk.Combobox(compound_window,
                                                    values=[filling.fillings_name for filling in available_fillings])
                    filling_combobox.pack()

                    dough_combobox = ttk.Combobox(compound_window,
                                                  values=[dough.dough_name for dough in available_dough])
                    dough_combobox.pack()

                    def save_changes():
                        new_pizza = product_type
                        new_pizza.filling = filling_combobox.get()
                        new_pizza.dough = dough_combobox.get()
                        new_pizza.sauce = sauce_combobox.get()

                        temp_pizzas.append(new_pizza)

                        compound_window.destroy()

                    save_button = tk.Button(compound_window, text="Сохранить изменения", command=save_changes)
                    save_button.pack()

                    current_quantity = self.pizza_quantities[product_id].get()
                    self.pizza_quantities[product_id].set(current_quantity + 1)
                    compound_window.mainloop()



                def manage_quantity(change_type, product_id):
                    current_quantity = self.pizza_quantities[product_id].get()
                    if change_type == 'increment':
                        self.pizza_quantities[product_id].set(current_quantity + 1)
                        temp_pizzas.append(
                            session.query(Products.type_product).filter(Products.product_id == product_id).first()[0])
                    elif change_type == 'decrement' and current_quantity > 0:
                        self.pizza_quantities[product_id].set(current_quantity - 1)

                button_plus = tk.Button(frame, text="+",
                                        command=lambda id=pizza.product_id: manage_quantity('increment', id))
                button_plus.pack(side=tk.LEFT)

                quantity_label = tk.Label(frame, textvariable=self.pizza_quantities[pizza.product_id])
                quantity_label.pack(side=tk.LEFT)

                button_minus = tk.Button(frame, text="-",
                                         command=lambda id=pizza.product_id: manage_quantity('decrement', id))
                button_minus.pack(side=tk.LEFT)

                button_change = tk.Button(frame, text="Изменить состав", command=lambda id=pizza.product_id,
                                                                                        type_product=pizza.type_product: change_ingredients(
                    id, type_product))
                button_change.pack(side=tk.LEFT)

            def add_to_order(order_id):

                if len(temp_pizzas) != 0:
                    for i in temp_pizzas:
                        # Получаем информацию о пицце из сохраненных данных
                        new_order_product = db_connect.Order_products(order_id=order_id, product_info=i)
                        session.add(new_order_product)
                        session.commit()
                    tk.messagebox.showinfo(title="Заказ", message=f"Спасибо за заказ! Номер заказа: {order_id} ")
                    self.create_main_screen()
                else:
                    # Обработка случая, когда пицца с заданным product_id не найдена в сохраненных данных
                    # Можно вывести сообщение об ошибке или выполнить другие действия
                    return None

            button_add_to_order = tk.Button(self.root, text="Добавить к заказу",
                                            command=lambda: add_to_order(order_id=self.order_id))
            button_add_to_order.pack()

        except Exception as e:
            print(e)



    def show_drinks_menu(self):
        try:
            session = db_connect.session_db()
            drinks = session.query(Products).filter(Products.category == 'Напиток').all()
            self.clear_screen()

            label = tk.Label(self.root, text="Меню напитков:")
            label.pack()

            for drink in drinks:
                label = tk.Label(self.root, text=f'{drink.product_id}. {drink.name}')
                label.pack()
            self.button_back = tk.Button(self.root, text="Назад", command=self.go_to_menu)
            self.button_back.pack()
        except Exception as e:
            label = tk.Label(self.root, text=f'Ошибка бд: {e}')
            label.pack()

        finally:
            session.commit()
            session.close()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def cancel_item(self):

        pass


class Mixin_Spicy:
    @staticmethod
    def attention():
        print("Это пицца острая!!!!!")


class Pizza(ABC):
    name = None

    def __init__(self, dough=None, sauce=None, filling=None, size=None):
        self.__dough = dough
        self.__sauce = sauce
        self.__filling = filling
        self.__size = size

    # @abstractmethod
    # def get_size(self):
    #     return self.__size

    def __repr__(self):
        return f"------------------- \n Название: {self.name} \n Состав: \n Тесто: {self.dough} \n Добавка: {self.filling} \n Соус: {self.sauce} \n Размер: {self.__size} \n -------------------"

    def track_time(f):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Прошло {execution_time} секунд")
            return result

        return wrapper

    # Сравнение пицц по тесту
    def __eq__(self, other):
        if isinstance(other, Pizza):
            return self.__size == other.__size
        return False

    def __lt__(self, other):
        if isinstance(other, Pizza):
            return self.__size < other.__size
        return False

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        self.__dough = dough

    @property
    def sauce(self):
        return self.__sauce

    @sauce.setter
    def sauce(self, sauce):
        self.__sauce = sauce

    @property
    def filling(self):
        return self.__filling

    @filling.setter
    def filling(self, filling):
        self.__filling = filling

    @track_time
    def make_pizza(self):
        time.sleep(2)
        print(f"Замешено тесто для пиццы {self.name}")
        time.sleep(2)
        print("Подготовились ингредиенты")
        time.sleep(2)
        print("Пицца испеклась")
        time.sleep(1)
        print("Пицца нарезалась")
        time.sleep(1)
        print("Пицца упаковалась")


class BBQ_Pizza(Pizza, Mixin_Spicy):
    name = 'Барбекю'

    def __init__(self):
        super().__init__(dough="Thin", sauce="Soy", filling="Beef", size=25)

    def get_size(self):
        super().get_size()


class Pepperoni(Pizza, Mixin_Spicy):
    name = 'Пепперони'

    def __init__(self):
        super().__init__(dough="Thick", sauce="Tomato sauce", filling="Pepperoni sausage", size=30)

    def get_size(self):
        super().get_size()
        print('Вызван абстрактный метод в Pepperoni')


class Seafood(Pizza):
    name = 'Дары моря'

    def __init__(self):
        super().__init__(dough="Medium", sauce="Cream sauce", filling="Squid", size=35)

    def get_size(self):
        super().get_size()
        print('Вызван абстрактный метод в Seafood')


if __name__ == "__main__":
    db_connect.create_db()
    session = db_connect.session_db()


    def start_gui():
        root = tk.Tk()
        root.geometry('600x400+200+100')
        root.title("Приложение пицца")
        app = MainApp(root)

        # Запускаем метод update каждые 1000 миллисекунд (1 секунда)
        root.after(1000, app.update)

        root.mainloop()


    def start_gui_thread():
        gui_thread = threading.Thread(target=start_gui)
        gui_thread.start()


    start_gui_thread()



