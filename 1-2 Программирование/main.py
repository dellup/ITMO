import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from main_win import Ui_MainWindow
from PySide6.QtSql import QSqlTableModel
from vehicle import Ui_Dialog
from connection import Data
import success_win
import newtask_win

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.view_data_2()
        self.reload_data()
        self.reload_data_2()


        self.ui.add_car.clicked.connect(self.open_vehicle_window)
        self.ui.delete_car.clicked.connect(self.delete_vehicle)
        self.ui.create_task.clicked.connect(self.open_task_window)

    def reload_data(self):
        self.ui.free_car_count.setText(self.conn.get_count("free_cars"))
    def reload_data_2(self):
        self.ui.busy_car_count.setText(self.conn.get_count("busy_cars"))

    def open_vehicle_window(self):
        self.vehicle_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.vehicle_window)
        self.ui_window.comboBox.currentIndexChanged.connect(self.update_combobox_options)

        self.vehicle_window.show()
        sender = self.sender()
        if sender.text() == "Добавить машину":
            self.ui_window.pushButton.clicked.connect(self.add_new_vehicle)

    def open_task_window(self):
        self.task_window = QtWidgets.QDialog()
        self.uiTask_window = newtask_win.Ui_Dialog()
        self.uiTask_window.setupUi(self.task_window)
        # self.task_window.comboBox.currentIndexChanged.connect(self.update_combobox_options)

        self.task_window.show()
        sender = self.sender()
        if sender.text() == "Создать заявку":
            self.uiTask_window.buttonOK.clicked.connect(self.open_success)


    def open_success(self):
        weight = self.uiTask_window.lineWeight.text()
        length = self.uiTask_window.lineLength.text()
        width = self.uiTask_window.lineWidth.text()
        height = self.uiTask_window.lineHeight.text()
        self.task_window.close()

        freeCars = self.conn.get_all_info()
        freeCars.sort(key=lambda x: x[2])
        for i in range(len(freeCars)):
            try:
                if self.check_conclution(freeCars[i], weight, length, width, height):
                    id = freeCars[i][0]
                    self.conn.replace_query(id)
                    self.view_data_2()
                    self.reload_data_2()
                    self.reload_data()
                    self.view_data()
                    self.success_window = QtWidgets.QDialog()
                    self.uiSuccess_window = success_win.Ui_Dialog()
                    self.uiSuccess_window.setupUi(self.success_window)
                    self.success_window.show()
                    self.uiSuccess_window.name.setText(f"Ваш транспорт: {freeCars[i][1]}")
                    self.uiSuccess_window.weight.setText(f"Грузоподъемность: {freeCars[i][2]}")
                    self.uiSuccess_window.length.setText(f"Длина транспорта: {freeCars[i][3]}")
                    self.uiSuccess_window.width.setText(f"Ширина транспорта: {freeCars[i][4]}")
                    self.uiSuccess_window.height.setText(f"Высота транспорта: {freeCars[i][5]}")
                    self.uiSuccess_window.ok.clicked.connect(self.close_success)
                    break
            except:
                QtWidgets.QMessageBox.critical(None, "Ошибка ввода",
                                               "Нажмите Cancel, чтобы выйти", QtWidgets.QMessageBox.Cancel)
                break
        else:
            QtWidgets.QMessageBox.critical(None, "Не могу найти транспорт",
                                    "Нажмите Cancel, чтобы выйти", QtWidgets.QMessageBox.Cancel)


    def check_conclution(self, freeCars, weight, length, width, height):
        if float(freeCars[2]) >= float(weight) and float(freeCars[3]) >= float(length) and float(freeCars[4]) >= float(width) and float(freeCars[5]) >= float(height):
            return True
        if float(freeCars[2]) >= float(weight) and float(freeCars[3]) >= float(length) and float(freeCars[4]) >= float(height) and float(freeCars[5]) >= float(width):
            return True
        if float(freeCars[2]) >= float(weight) and float(freeCars[3]) >= float(height) and float(freeCars[4]) >= float(width) and float(freeCars[5]) >= float(length):
            return True
        if float(freeCars[2]) >= float(weight) and float(freeCars[3]) >= float(height) and float(freeCars[4]) >= float(length) and float(freeCars[5]) >= float(width):
            return True
        if float(freeCars[2]) >= float(weight) and float(freeCars[3]) >= float(width) and float(freeCars[4]) >= float(height) and float(freeCars[5]) >= float(length):
            return True
        if float(freeCars[2]) >= float(weight) and float(freeCars[3]) >= float(width) and float(freeCars[4]) >= float(length) and float(freeCars[5]) >= float(height):
            return True





    def close_success(self):
        self.success_window.close()

    def update_combobox_options(self):
        selected_value = self.ui_window.comboBox.currentText()

        self.ui_window.comboBox_2.clear()
        self.ui_window.comboBox_3.clear()
        self.ui_window.comboBox_4.clear()

        if selected_value == "Газель":
            self.ui_window.label_2.setText("2")
            self.ui_window.comboBox_2.addItems(["2"])
            self.ui_window.comboBox_2.setCurrentIndex(0)
            self.ui_window.comboBox_3.addItems(["3"])
            self.ui_window.comboBox_3.setCurrentIndex(0)
            self.ui_window.comboBox_4.addItems(["1.7", "2.2"])
            self.ui_window.comboBox_4.setCurrentIndex(0)
        elif selected_value == "Бычок":
            self.ui_window.label_2.setText("3")
            self.ui_window.comboBox_2.addItems(["4.2", "5"])
            self.ui_window.comboBox_2.setCurrentIndex(0)
            self.ui_window.comboBox_3.addItems(["2", "2.2"])
            self.ui_window.comboBox_3.setCurrentIndex(0)
            self.ui_window.comboBox_4.addItems(["2", "2.4"])
            self.ui_window.comboBox_4.setCurrentIndex(0)
        elif selected_value == "MAN-10":
            self.ui_window.label_2.setText("10")
            self.ui_window.comboBox_2.addItems(["6", "8"])
            self.ui_window.comboBox_2.setCurrentIndex(0)
            self.ui_window.comboBox_3.addItems(["2.45"])
            self.ui_window.comboBox_3.setCurrentIndex(0)
            self.ui_window.comboBox_4.addItems(["2.3", "2.7"])
            self.ui_window.comboBox_4.setCurrentIndex(0)
        elif selected_value == "Фура":
            self.ui_window.label_2.setText("20")
            self.ui_window.comboBox_2.addItems(["13.6"])
            self.ui_window.comboBox_2.setCurrentIndex(0)
            self.ui_window.comboBox_3.addItems(["2.48"])
            self.ui_window.comboBox_3.setCurrentIndex(0)
            self.ui_window.comboBox_4.addItems(["2.5", "2.7"])
            self.ui_window.comboBox_4.setCurrentIndex(0)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("free_cars")
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSortingEnabled(True)

    def view_data_2(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("busy_cars")
        self.model.select()
        self.ui.tableView_2.setModel(self.model)
        self.ui.tableView_2.setSortingEnabled(True)



    def add_new_vehicle(self):
        type = self.ui_window.comboBox.currentText()
        load = self.ui_window.label_2.text()
        length = self.ui_window.comboBox_2.currentText()
        weight = self.ui_window.comboBox_3.currentText()
        height = self.ui_window.comboBox_4.currentText()
        self.conn.add_new_query(type, load, length, weight, height, "free_cars")
        self.view_data()
        self.reload_data()
        self.vehicle_window.close()

    def delete_vehicle(self):
        try:
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(index))
            self.conn.delete_query(id, "free_cars")
            self.reload_data()
            self.view_data()
        except:
            index2 = self.ui.tableView_2.selectedIndexes()[0]
            id = str(self.ui.tableView_2.model().data(index2))
            self.conn.delete_query(id, "busy_cars")
            self.reload_data_2()
            self.view_data_2()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
