# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_vehicle.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(574, 533)
        Dialog.setStyleSheet(u"background-color: rgba(250,250,250,100);\n"
"font-family: Noto Sans;\n"
"color: black;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
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

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"height:30px;\n"
"background-color: rgba(255,255,255,100);\n"
"border: none;")
        self.comboBox.setFrame(True)

        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(255,255,255,100);")

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"height: 30px;\n"
"background-color: rgba(255,255,255,100);\n"
"border: none;")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"height: 30px;\n"
"background-color: rgba(255,255,255,100);\n"
"border: none;")

        self.verticalLayout.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.frame)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"height: 30px;\n"
"background-color: rgba(255,255,255,100);\n"
"border:none;\n"
"")

        self.verticalLayout.addWidget(self.comboBox_4)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"height: 50px;\n"
"background-color: rgba(255,255,255,100);\n"
"border:none;")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u043c\u0430\u0448\u0438\u043d\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0413\u0430\u0437\u0435\u043b\u044c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0411\u044b\u0447\u043e\u043a", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"MAN-10", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u0424\u0443\u0440\u0430", None))

#if QT_CONFIG(whatsthis)
        self.comboBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.comboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u043c\u0430\u0448\u0438\u043d\u0443", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0443\u0437\u043e\u043f\u043e\u0434\u044a\u0435\u043c\u043d\u043e\u0441\u0442\u044c, \u0442\u043e\u043d\u043d", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

