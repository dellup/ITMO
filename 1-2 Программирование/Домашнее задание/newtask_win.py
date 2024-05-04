# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_task.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(523, 471)
        Dialog.setStyleSheet(u"background-color: rgba(250,250,250,100);\n"
"font-family: Noto Sans;\n"
"color: black;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: black;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 25px; \n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: rgba(255,255,255,100);\n"
"color: black;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineWeight = QLineEdit(self.frame)
        self.lineWeight.setObjectName(u"lineWeight")
        self.lineWeight.setStyleSheet(u"background-color: rgba(255,255,255,100);\n"
"")

        self.verticalLayout.addWidget(self.lineWeight)

        self.lineLength = QLineEdit(self.frame)
        self.lineLength.setObjectName(u"lineLength")
        self.lineLength.setStyleSheet(u"background-color: rgba(255,255,255,100);\n"
"")

        self.verticalLayout.addWidget(self.lineLength)

        self.lineWidth = QLineEdit(self.frame)
        self.lineWidth.setObjectName(u"lineWidth")
        self.lineWidth.setStyleSheet(u"background-color: rgba(255,255,255,100);\n"
"")

        self.verticalLayout.addWidget(self.lineWidth)

        self.lineHeight = QLineEdit(self.frame)
        self.lineHeight.setObjectName(u"lineHeight")
        self.lineHeight.setStyleSheet(u"background-color: rgba(255,255,255,100);\n"
"")

        self.verticalLayout.addWidget(self.lineHeight)

        self.buttonOK = QPushButton(self.frame)
        self.buttonOK.setObjectName(u"buttonOK")
        self.buttonOK.setStyleSheet(u"height: 50px;\n"
"background-color: rgba(255,255,255,100);\n"
"border:none;")

        self.verticalLayout.addWidget(self.buttonOK)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443", None))
        self.lineWeight.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438 \u0432\u0435\u0441 \u0433\u0440\u0443\u0437\u0430", None))
        self.lineLength.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438 \u0434\u043b\u0438\u043d\u0443 \u0433\u0440\u0443\u0437\u0430", None))
        self.lineWidth.setText("")
        self.lineWidth.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438 \u0448\u0438\u0440\u0438\u043d\u0443 \u0433\u0440\u0443\u0437\u0430", None))
        self.lineHeight.setText("")
        self.lineHeight.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438 \u0432\u044b\u0441\u043e\u0442\u0443 \u0433\u0440\u0443\u0437\u0430", None))
        self.buttonOK.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442", None))
    # retranslateUi

