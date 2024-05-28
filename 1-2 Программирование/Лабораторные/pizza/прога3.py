import tkinter as tk  
from tkinter import messagebox, Menu

class CalculatorApp(tk.Tk):  
    def __init__(self):  
        super().__init__()  
        self.title("Графический Калькулятор")  
        self.create_widgets()
        self.create_menu()
        # self.geometry("600x600")
        self.menu_bar = Menu(self)
        
        # Создаем пункт меню "Справка"
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="О программе", command=self.show_about_dialog)
        
        # Создаем пункт меню "Выход"
        self.menu_bar.add_cascade(label="Справка", menu=help_menu)
        self.menu_bar.add_command(label="Выход", command=self.quit)
        
        self.config(menu=self.menu_bar)

    def show_about_dialog(self):
        messagebox.showinfo("О программе", "уипщупщолптахьт кцаьтхззцскцсльзцъулщзщхлык ыкзщлцк зльцкацлзьцклзьцуклз")

    def create_widgets(self):  
        self.label_arg1 = tk.Label(self, text="Аргумент 1:")
        self.label_arg1.grid(row=0, column=0, sticky="e")

        self.label_arg2 = tk.Label(self, text="Аргумент 2:")
        self.label_arg2.grid(row=1, column=0, sticky="e")

        self.label_result = tk.Label(self, text="Результат:")
        self.label_result.grid(row=3, column=0, sticky="e")

        self.entry_arg1 = tk.Entry(self)
        self.entry_arg1.grid(row=0, column=1)

        self.entry_arg2 = tk.Entry(self)
        self.entry_arg2.grid(row=1, column=1)

        self.result_var = tk.StringVar()
        self.label_result_value = tk.Label(self, textvariable=self.result_var)
        self.label_result_value.grid(row=3, column=1)

        self.calculation_type = tk.StringVar()
        self.calculation_type.set("calculator")

        self.radio_calculator = tk.Radiobutton(self, text="Калькулятор", variable=self.calculation_type, value="calculator", command=self.toggle_entries)
        self.radio_calculator.grid(row=2, column=0)

        self.radio_rectangle = tk.Radiobutton(self, text="Прямоугольник", variable=self.calculation_type, value="rectangle", command=self.toggle_entries)
        self.radio_rectangle.grid(row=2, column=1)

        self.checkbutton = tk.Button(self, text="Вычислить", command=self.calculate)
        self.checkbutton.grid(row=4, columnspan=2)

        self.button_swap = tk.Button(self, text="Поменять местами", command=self.swap_arguments)
        self.button_swap.grid(row=5, column=0)

        self.button_clear = tk.Button(self, text="Очистить форму", command=self.clear_form)
        self.button_clear.grid(row=5, column=1)


        self.button_exit = tk.Button(self, text="Выход", command=self.quit)
        self.button_exit.grid(row=6, columnspan=2)

        self.canvas = tk.Canvas(self, width=200, height=100)
        self.canvas.grid(row=7, columnspan=2)

        self.canvas.grid_remove()

    def create_menu(self):  
        menubar = tk.Menu(self)  
        self.config(menu=menubar)  

    def toggle_entries(self):  
        if self.calculation_type.get() == "rectangle":  
            self.entry_arg1.config(state="normal")  
            self.entry_arg2.config(state="normal")
            self.checkbutton.config(state="normal")  
            self.canvas.grid()  
        else:  
            self.entry_arg1.config(state="normal")  
            self.entry_arg2.config(state="normal")
            self.checkbutton.config(state="normal")  
            self.canvas.grid_remove()  

    def swap_arguments(self):  
        arg1 = self.entry_arg1.get()
        arg2 = self.entry_arg2.get()
        self.entry_arg1.delete(0, tk.END)
        self.entry_arg1.insert(0, arg2)
        self.entry_arg2.delete(0, tk.END)
        self.entry_arg2.insert(0, arg1)

    def clear_form(self): 
        self.entry_arg1.delete(0, tk.END)
        self.entry_arg2.delete(0, tk.END)
        self.result_var.set("")

    def add(self, arg1, arg2): 
        return arg1 + arg2

    def subtract(self, arg1, arg2): 
        return arg1 - arg2

    def multiply(self, arg1, arg2):  
        return arg1 * arg2

    def divide(self, arg1, arg2):  
        if arg2 == 0:  
            messagebox.showerror("Ошибка", "Деление на ноль невозможно.")
            return
        else:
            return arg1 / arg2

    def calculate(self):  
        try:
            arg1 = float(self.entry_arg1.get())
            arg2 = float(self.entry_arg2.get())

            if self.calculation_type.get() == "calculator":  
                addition = self.add(arg1, arg2)
                subtraction = self.subtract(arg1, arg2)
                multiplication = self.multiply(arg1, arg2)
                division = self.divide(arg1, arg2)
                self.result_var.set(f"Сложение: {addition}, Вычитание: {subtraction}, Умножение: {multiplication}, Деление: {division}")
            elif self.calculation_type.get() == "rectangle":  
                if arg1 <= 0 or arg2 <= 0:  
                    messagebox.showerror("Ошибка", "Значения сторон прямоугольника должны быть положительными и больше нуля.")
                    return
                perimeter = round(2 * (arg1 + arg2), 2)
                area = round(arg1 * arg2, 2)
                self.result_var.set(f"Периметр: {perimeter}, Площадь: {area}")
               
                self.canvas.delete("all")
                self.canvas.create_rectangle(10, 10, arg1*8, arg2*8, outline="pink", fill="violet")
        except ValueError:  
            messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения для аргументов.")

if __name__ == "__main__": 
    app = CalculatorApp()  
    app.mainloop()  
