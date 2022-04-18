from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QRegularExpression,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QRegularExpressionValidator)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget, QLabel,QHBoxLayout)

class Ui_HintWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_HintWindow, self).__init__(parent)
    
    def setupUi(self, HintWindow):
        # if not HintWindow.objectName():
        #     HintWindow.setObjectName(u"Hint window")
        # HintWindow.resize(860, 400)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(HintWindow.sizePolicy().hasHeightForWidth())
        # HintWindow.setSizePolicy(sizePolicy)
        # HintWindow.setMinimumSize(QSize(400, 400))
        # HintWindow.setMaximumSize(QSize(400, 400))


        # HintWindow.centralwidget = QWidget(HintWindow)
        # HintWindow.centralwidget.setObjectName(u"centralwidget")
        # HintWindow.horizontalLayoutWidget = QWidget(HintWindow.centralwidget)
        # HintWindow.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        # HintWindow.horizontalLayout = QHBoxLayout(HintWindow.horizontalLayoutWidget)
        # HintWindow.horizontalLayout.setObjectName(u"horizontalLayout")

        # HintWindow.label1 = QLabel("Help text1")
        # HintWindow.label1.setText("Help text1")
        # HintWindow.label2 = QLabel("Help text2")
        # HintWindow.label2.setText("Help text2")
        # HintWindow.label3 = QLabel("Help text3")
        # HintWindow.label3.setText("Help text3")
        # HintWindow.label4 = QLabel("Help text4")
        # HintWindow.label4.setText("Help text4")

        # HintWindow.horizontalLayout.addWidget(HintWindow.label1)
        # HintWindow.horizontalLayout.addWidget(HintWindow.label2)
        # HintWindow.horizontalLayout.addWidget(HintWindow.label3)
        # HintWindow.horizontalLayout.addWidget(HintWindow.label4)

        
        # HintWindow.setWindowTitle("Hint")
        # HintWindow.setLayout(HintWindow.horizontalLayout)

        # HintWindow.setCentralWidget(HintWindow.centralwidget)
        
        if not HintWindow.objectName():
            HintWindow.setObjectName(u"Hint window")
        HintWindow.resize(860, 400)
        HintWindow.setMinimumSize(QSize(860, 400))
        HintWindow.setMaximumSize(QSize(860, 400))
        self.verticalLayoutWidget = QWidget(HintWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 748, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Hint_Label = QLabel(self.verticalLayoutWidget)
        self.Hint_Label.setObjectName(u"Hint_Label")
        font = QFont()
        font.setPointSize(12)
        self.Hint_Label.setFont(font)
        self.Hint_Label.setScaledContents(False)
        self.Hint_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Hint_Label.setWordWrap(True)

        self.verticalLayout.addWidget(self.Hint_Label)


        self.retranslateUi(HintWindow)

        QMetaObject.connectSlotsByName(HintWindow)
    # setupUi

    def retranslateUi(self, HintWindow):
        HintWindow.setWindowTitle(QCoreApplication.translate("HintWindow", u"HintWindow", None))
        self.Hint_Label.setText(QCoreApplication.translate("HintWindow", u"<html><head/><body><p>Calculator help:<br/>- Use negative numbers in form of &quot;-number&quot;, in expression etc. &quot;-number&quot; &quot;operator -&quot; &quot;-number&quot; =&gt; -5--5<br/>- Hit &quot;=&quot; to see result</p></body></html>", None))
    # retranslateUi