# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 511)
        MainWindow.setStyleSheet(u"background-color: rgba(250,250,250,100);\n"
"font-family: Noto Sans;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.free_car = QLabel(self.frame)
        self.free_car.setObjectName(u"free_car")
        self.free_car.setStyleSheet(u"font-size: 15px; \n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: rgba(255,255,255,100);\n"
"color: black;")

        self.verticalLayout.addWidget(self.free_car)

        self.free_car_count = QLabel(self.frame)
        self.free_car_count.setObjectName(u"free_car_count")
        self.free_car_count.setStyleSheet(u"font-size:20px; \n"
"border: none;\n"
"background-color: rgba(255,255,255,100);\n"
"color: black;\n"
"padding-left: 1px;")

        self.verticalLayout.addWidget(self.free_car_count)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.busy_car = QLabel(self.frame)
        self.busy_car.setObjectName(u"busy_car")
        self.busy_car.setStyleSheet(u"font-size: 15px; \n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: rgba(255,255,255,100);\n"
"color:black;")

        self.verticalLayout_2.addWidget(self.busy_car)

        self.busy_car_count = QLabel(self.frame)
        self.busy_car_count.setObjectName(u"busy_car_count")
        self.busy_car_count.setStyleSheet(u"font-size:20px; \n"
"border: none;\n"
"background-color: rgba(255,255,255,100);\n"
"color: black;")

        self.verticalLayout_2.addWidget(self.busy_car_count)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_car = QPushButton(self.centralwidget)
        self.add_car.setObjectName(u"add_car")
        self.add_car.setStyleSheet(u"color: black;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_car.setIcon(icon)
        self.add_car.setIconSize(QSize(24, 16))

        self.horizontalLayout_2.addWidget(self.add_car)

        self.delete_car = QPushButton(self.centralwidget)
        self.delete_car.setObjectName(u"delete_car")
        self.delete_car.setStyleSheet(u"color:black;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_car.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.delete_car)

        self.create_task = QPushButton(self.centralwidget)
        self.create_task.setObjectName(u"create_task")
        self.create_task.setStyleSheet(u"color:black;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_task.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.create_task)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"text-align: center;\n"
"color:black;\n"
"display: flex;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:black;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"\n"
"QTableView {\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"color: black;\n"
"QTableView::section {\n"
"color:black;\n"
"border: none;\n"
"height: 50px;\n"
"}\n"
"QTableView::item {\n"
"border-style:none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"color:black;\n"
"}\n"
"QTableView::item:selected {\n"
"color:black;\n"
"border:none;\n"
"color:rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.tableView.setShowGrid(False)

        self.horizontalLayout_3.addWidget(self.tableView)

        self.tableView_2 = QTableView(self.centralwidget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setStyleSheet(u"\n"
"QTableView {\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView::section {\n"
"border: none;\n"
"height: 50px;\n"
"}\n"
"QTableView::item {\n"
"border-style:none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"QTableView::item:selected {\n"
"border:none;\n"
"color:rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.tableView_2.setShowGrid(False)

        self.horizontalLayout_3.addWidget(self.tableView_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Homatask", None))
        self.free_car.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0445 \u043c\u0430\u0448\u0438\u043d", None))
        self.free_car_count.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.busy_car.setText(QCoreApplication.translate("MainWindow", u" \u0417\u0430\u043d\u044f\u0442\u044b\u0445 \u043c\u0430\u0448\u0438\u043d", None))
        self.busy_car_count.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.add_car.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0430\u0448\u0438\u043d\u0443", None))
        self.delete_car.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043c\u0430\u0448\u0438\u043d\u0443", None))
        self.create_task.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0435 \u043c\u0430\u0448\u0438\u043d\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u044b\u0435 \u043c\u0430\u0448\u0438\u043d\u044b", None))
    # retranslateUi

