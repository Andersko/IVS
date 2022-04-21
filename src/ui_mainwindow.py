# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QRegularExpression,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QRegularExpressionValidator,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 475)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(860, 475))
        MainWindow.setMaximumSize(QSize(860, 475))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 842, 544))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.OutputLabel = QLineEdit(self.verticalLayoutWidget)
        self.OutputLabel.setObjectName(u"OutputLabel")
        self.OutputLabel.setMinimumSize(QSize(840, 100))
        self.OutputLabel.setMaximumSize(QSize(840, 100))
        font = QFont()
        font.setPointSize(26)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setEchoMode(QLineEdit.Normal)
        self.OutputLabel.setReadOnly(False)
        self.OutputLabel.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.OutputLabel.setClearButtonEnabled(False)
        regexp = QRegularExpression(r'^(-?(\d+(\.\d+)?)|([\!\-\+\/\*\(\)\√\^\%]))*$')
        validator = QRegularExpressionValidator(regexp)
        self.OutputLabel.setValidator(validator)

        self.verticalLayout.addWidget(self.OutputLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.Button_Six = QPushButton(self.verticalLayoutWidget)
        self.Button_Six.setObjectName(u"Button_Six")
        font1 = QFont()
        font1.setPointSize(30)
        self.Button_Six.setFont(font1)
        self.Button_Six.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Six, 2, 2, 1, 1)

        self.Button_Sqrt = QPushButton(self.verticalLayoutWidget)
        self.Button_Sqrt.setObjectName(u"Button_Sqrt")
        self.Button_Sqrt.setFont(font1)
        self.Button_Sqrt.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Sqrt, 2, 5, 1, 1)

        self.Button_Three = QPushButton(self.verticalLayoutWidget)
        self.Button_Three.setObjectName(u"Button_Three")
        self.Button_Three.setFont(font1)
        self.Button_Three.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Three, 3, 2, 1, 1)

        self.Button_C = QPushButton(self.verticalLayoutWidget)
        self.Button_C.setObjectName(u"Button_C")
        self.Button_C.setFont(font1)
        self.Button_C.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_C, 3, 6, 1, 1)

        self.Button_Percent = QPushButton(self.verticalLayoutWidget)
        self.Button_Percent.setObjectName(u"Button_Percent")
        self.Button_Percent.setFont(font1)
        self.Button_Percent.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Percent, 2, 6, 1, 1)

        self.Button_One = QPushButton(self.verticalLayoutWidget)
        self.Button_One.setObjectName(u"Button_One")
        self.Button_One.setFont(font1)
        self.Button_One.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_One, 3, 0, 1, 1)

        self.Button_Four = QPushButton(self.verticalLayoutWidget)
        self.Button_Four.setObjectName(u"Button_Four")
        self.Button_Four.setFont(font1)
        self.Button_Four.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Four, 2, 0, 1, 1)

        self.Button_Two = QPushButton(self.verticalLayoutWidget)
        self.Button_Two.setObjectName(u"Button_Two")
        self.Button_Two.setFont(font1)
        self.Button_Two.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Two, 3, 1, 1, 1)

        self.Button_Dot = QPushButton(self.verticalLayoutWidget)
        self.Button_Dot.setObjectName(u"Button_Dot")
        self.Button_Dot.setFont(font1)
        self.Button_Dot.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Dot, 3, 4, 1, 1)

        self.Button_Factorial = QPushButton(self.verticalLayoutWidget)
        self.Button_Factorial.setObjectName(u"Button_Factorial")
        self.Button_Factorial.setFont(font1)
        self.Button_Factorial.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Factorial, 0, 6, 1, 1)

        self.Button_Seven = QPushButton(self.verticalLayoutWidget)
        self.Button_Seven.setObjectName(u"Button_Seven")
        self.Button_Seven.setFont(font1)
        self.Button_Seven.setAutoFillBackground(False)
        self.Button_Seven.setIconSize(QSize(15, 15))
        self.Button_Seven.setAutoDefault(False)

        self.gridLayout.addWidget(self.Button_Seven, 0, 0, 1, 1)

        self.Button_Five = QPushButton(self.verticalLayoutWidget)
        self.Button_Five.setObjectName(u"Button_Five")
        self.Button_Five.setFont(font1)
        self.Button_Five.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Five, 2, 1, 1, 1)

        self.Button_Power = QPushButton(self.verticalLayoutWidget)
        self.Button_Power.setObjectName(u"Button_Power")
        self.Button_Power.setFont(font1)
        self.Button_Power.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Power, 0, 5, 1, 1)

        self.Button_Minus = QPushButton(self.verticalLayoutWidget)
        self.Button_Minus.setObjectName(u"Button_Minus")
        self.Button_Minus.setFont(font1)
        self.Button_Minus.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Minus, 2, 3, 1, 1)

        self.Button_Eight = QPushButton(self.verticalLayoutWidget)
        self.Button_Eight.setObjectName(u"Button_Eight")
        self.Button_Eight.setFont(font1)
        self.Button_Eight.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Eight, 0, 1, 1, 1)

        self.Button_Times = QPushButton(self.verticalLayoutWidget)
        self.Button_Times.setObjectName(u"Button_Times")
        self.Button_Times.setFont(font1)
        self.Button_Times.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Times, 0, 4, 1, 1)

        self.Button_Hint = QPushButton(self.verticalLayoutWidget)
        self.Button_Hint.setObjectName(u"Button_Hint")
        self.Button_Hint.setFont(font1)
        self.Button_Hint.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Hint, 3, 5, 1, 1)

        self.Button_Plus = QPushButton(self.verticalLayoutWidget)
        self.Button_Plus.setObjectName(u"Button_Plus")
        self.Button_Plus.setFont(font1)
        self.Button_Plus.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Plus, 0, 3, 1, 1)

        self.Button_Zero = QPushButton(self.verticalLayoutWidget)
        self.Button_Zero.setObjectName(u"Button_Zero")
        self.Button_Zero.setFont(font1)
        self.Button_Zero.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Zero, 3, 3, 1, 1)

        self.Button_Divide = QPushButton(self.verticalLayoutWidget)
        self.Button_Divide.setObjectName(u"Button_Divide")
        self.Button_Divide.setFont(font1)
        self.Button_Divide.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Divide, 2, 4, 1, 1)

        self.Button_Nine = QPushButton(self.verticalLayoutWidget)
        self.Button_Nine.setObjectName(u"Button_Nine")
        self.Button_Nine.setFont(font1)
        self.Button_Nine.setIconSize(QSize(15, 15))

        self.gridLayout.addWidget(self.Button_Nine, 0, 2, 1, 1)

        self.Button_Equals = QPushButton(self.verticalLayoutWidget)
        self.Button_Equals.setObjectName(u"Button_Equals")
        self.Button_Equals.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_Equals.sizePolicy().hasHeightForWidth())
        self.Button_Equals.setSizePolicy(sizePolicy1)
        self.Button_Equals.setFont(font1)

        self.gridLayout.addWidget(self.Button_Equals, 3, 7, 1, 1)

        self.Button_Right_Parenthesis = QPushButton(self.verticalLayoutWidget)
        self.Button_Right_Parenthesis.setObjectName(u"Button_Right_Parenthesis")
        self.Button_Right_Parenthesis.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Button_Right_Parenthesis.sizePolicy().hasHeightForWidth())
        self.Button_Right_Parenthesis.setSizePolicy(sizePolicy1)
        self.Button_Right_Parenthesis.setFont(font1)

        self.gridLayout.addWidget(self.Button_Right_Parenthesis, 2, 7, 1, 1)

        self.Button_Left_Parenthesis = QPushButton(self.verticalLayoutWidget)
        self.Button_Left_Parenthesis.setObjectName(u"Button_Left_Parenthesis")
        self.Button_Left_Parenthesis.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Button_Left_Parenthesis.sizePolicy().hasHeightForWidth())
        self.Button_Left_Parenthesis.setSizePolicy(sizePolicy1)
        self.Button_Left_Parenthesis.setFont(font1)

        self.gridLayout.addWidget(self.Button_Left_Parenthesis, 0, 7, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.OutputLabel.setInputMask("")
        self.OutputLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.OutputLabel.setPlaceholderText("")
        self.Button_Six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Button_Sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.Button_Three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_Percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.Button_One.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Button_Four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button_Two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Button_Dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Button_Factorial.setText(QCoreApplication.translate("MainWindow", u"n!", None))
        self.Button_Seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Button_Five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Button_Power.setText(QCoreApplication.translate("MainWindow", u"x^", None))
        self.Button_Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Button_Eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Button_Times.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.Button_Hint.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.Button_Plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Button_Zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_Divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.Button_Nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Button_Equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Button_Right_Parenthesis.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.Button_Left_Parenthesis.setText(QCoreApplication.translate("MainWindow", u"(", None))
    # retranslateUi

