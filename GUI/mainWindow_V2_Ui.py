# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow_V2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 666)
        MainWindow.setStyleSheet(u"background-image: url(:/backgroud/background/background.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: transparent;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 16777215))
        self.title_label.setStyleSheet(u"\n"
"font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.title_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_label = QLabel(self.centralwidget)
        self.frame_label.setObjectName(u"frame_label")
        self.frame_label.setMinimumSize(QSize(640, 480))
        self.frame_label.setStyleSheet(u"")
        self.frame_label.setAlignment(Qt.AlignCenter)
        self.frame_label.setMargin(0)

        self.horizontalLayout_4.addWidget(self.frame_label)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_Button_ico = QPushButton(self.groupBox)
        self.start_Button_ico.setObjectName(u"start_Button_ico")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_Button_ico.sizePolicy().hasHeightForWidth())
        self.start_Button_ico.setSizePolicy(sizePolicy)
        self.start_Button_ico.setMinimumSize(QSize(100, 40))
        self.start_Button_ico.setStyleSheet(u"background-image:url(:/images/images/play.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: transparent;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.start_Button_ico)

        self.start_Button = QPushButton(self.groupBox)
        self.start_Button.setObjectName(u"start_Button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_Button.sizePolicy().hasHeightForWidth())
        self.start_Button.setSizePolicy(sizePolicy1)
        self.start_Button.setMinimumSize(QSize(100, 40))
        self.start_Button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.start_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stop_Button_ico = QPushButton(self.groupBox)
        self.stop_Button_ico.setObjectName(u"stop_Button_ico")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stop_Button_ico.sizePolicy().hasHeightForWidth())
        self.stop_Button_ico.setSizePolicy(sizePolicy2)
        self.stop_Button_ico.setMinimumSize(QSize(100, 40))
        self.stop_Button_ico.setStyleSheet(u"background-image:url(:/images/images/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: transparent;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.stop_Button_ico)

        self.stop_Button = QPushButton(self.groupBox)
        self.stop_Button.setObjectName(u"stop_Button")
        sizePolicy1.setHeightForWidth(self.stop_Button.sizePolicy().hasHeightForWidth())
        self.stop_Button.setSizePolicy(sizePolicy1)
        self.stop_Button.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_2.addWidget(self.stop_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stop_label_3 = QLabel(self.groupBox)
        self.stop_label_3.setObjectName(u"stop_label_3")
        sizePolicy1.setHeightForWidth(self.stop_label_3.sizePolicy().hasHeightForWidth())
        self.stop_label_3.setSizePolicy(sizePolicy1)
        self.stop_label_3.setMinimumSize(QSize(100, 40))
        self.stop_label_3.setStyleSheet(u"background-image:url(:/images/images/photo-camera.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: transparent;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.stop_label_3)

        self.captureIndex_lineEdit = QLineEdit(self.groupBox)
        self.captureIndex_lineEdit.setObjectName(u"captureIndex_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.captureIndex_lineEdit.sizePolicy().hasHeightForWidth())
        self.captureIndex_lineEdit.setSizePolicy(sizePolicy3)
        self.captureIndex_lineEdit.setMinimumSize(QSize(90, 40))
        self.captureIndex_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.captureIndex_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stop_label_2 = QLabel(self.groupBox)
        self.stop_label_2.setObjectName(u"stop_label_2")
        sizePolicy1.setHeightForWidth(self.stop_label_2.sizePolicy().hasHeightForWidth())
        self.stop_label_2.setSizePolicy(sizePolicy1)
        self.stop_label_2.setMinimumSize(QSize(100, 40))
        self.stop_label_2.setStyleSheet(u"background-image:url(:/images/images/setting.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: transparent;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.stop_label_2)

        self.fps_lineEdit = QLineEdit(self.groupBox)
        self.fps_lineEdit.setObjectName(u"fps_lineEdit")
        sizePolicy3.setHeightForWidth(self.fps_lineEdit.sizePolicy().hasHeightForWidth())
        self.fps_lineEdit.setSizePolicy(sizePolicy3)
        self.fps_lineEdit.setMinimumSize(QSize(90, 40))
        self.fps_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.fps_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(180, 40))
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.verticalLayout.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameshow_label = QLabel(self.groupBox)
        self.nameshow_label.setObjectName(u"nameshow_label")
        self.nameshow_label.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")
        self.nameshow_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.nameshow_label, 0, 0, 1, 1)

        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.name_label, 0, 1, 1, 1)

        self.emotionshow_label = QLabel(self.groupBox)
        self.emotionshow_label.setObjectName(u"emotionshow_label")
        self.emotionshow_label.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")
        self.emotionshow_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.emotionshow_label, 1, 0, 1, 1)

        self.emotion_label = QLabel(self.groupBox)
        self.emotion_label.setObjectName(u"emotion_label")
        self.emotion_label.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.emotion_label, 1, 1, 1, 1)

        self.ageshow_label = QLabel(self.groupBox)
        self.ageshow_label.setObjectName(u"ageshow_label")
        self.ageshow_label.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")
        self.ageshow_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ageshow_label, 2, 0, 1, 1)

        self.age_label = QLabel(self.groupBox)
        self.age_label.setObjectName(u"age_label")
        self.age_label.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.age_label, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u591a\u7b97\u6cd5\u878d\u5408\u7684\u4eba\u8138\u8bc6\u522b\u7cfb\u7edf", None))
        self.frame_label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Setings and information", None))
        self.start_Button_ico.setText("")
        self.start_Button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_Button_ico.setText("")
        self.stop_Button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.stop_label_3.setText("")
        self.captureIndex_lineEdit.setText("")
        self.captureIndex_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Capture Index", None))
        self.stop_label_2.setText("")
        self.fps_lineEdit.setText("")
        self.fps_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Based on Facial feature", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Based on Facial feature and PCA", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Based on YOLOv8", None))

        self.nameshow_label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.name_label.setText("")
        self.emotionshow_label.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u7eea", None))
        self.emotion_label.setText("")
        self.ageshow_label.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None))
        self.age_label.setText("")
    # retranslateUi

