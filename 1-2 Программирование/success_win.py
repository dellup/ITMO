# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'success.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(594, 365)
        Dialog.setStyleSheet(u"background-color: rgba(250,250,250,100);\n"
"font-family: Noto Sans;\n"
"color: black;\n"
"")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: black;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 25px; \n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: rgba(255,255,255,100);\n"
"color: black;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"background-color: rgba(255,255,255,100);")
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.name)

        self.weight = QLabel(self.frame)
        self.weight.setObjectName(u"weight")
        self.weight.setStyleSheet(u"background-color: rgba(255,255,255,100);")
        self.weight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.weight)

        self.length = QLabel(self.frame)
        self.length.setObjectName(u"length")
        self.length.setStyleSheet(u"background-color: rgba(255,255,255,100);")
        self.length.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.length)

        self.width = QLabel(self.frame)
        self.width.setObjectName(u"width")
        self.width.setStyleSheet(u"background-color: rgba(255,255,255,100);")
        self.width.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.width)

        self.height = QLabel(self.frame)
        self.height.setObjectName(u"height")
        self.height.setStyleSheet(u"background-color: rgba(255,255,255,100);")
        self.height.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.height)

        self.ok = QPushButton(self.frame)
        self.ok.setObjectName(u"ok")
        self.ok.setStyleSheet(u"height: 50px;\n"
"background-color: rgba(255,255,255,100);\n"
"border:none;")

        self.verticalLayout.addWidget(self.ok)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u044f\u0432\u043a\u0430 \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0430!", None))
        self.name.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442:", None))
        self.weight.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442:", None))
        self.length.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442:", None))
        self.width.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442:", None))
        self.height.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u0448 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442:", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
    # retranslateUi

