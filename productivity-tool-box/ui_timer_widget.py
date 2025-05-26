# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(475, 176)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 451, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 410, 115))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.current_task_input = QLabel(self.widget)
        self.current_task_input.setObjectName(u"current_task_input")
        font1 = QFont()
        font1.setPointSize(10)
        self.current_task_input.setFont(font1)

        self.horizontalLayout_2.addWidget(self.current_task_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.timer_input = QLabel(self.widget)
        self.timer_input.setObjectName(u"timer_input")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(37)
        font2.setBold(False)
        self.timer_input.setFont(font2)
        self.timer_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.timer_input)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.restart_button = QPushButton(self.widget)
        self.restart_button.setObjectName(u"restart_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restart_button.sizePolicy().hasHeightForWidth())
        self.restart_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.restart_button)

        self.settings_button = QPushButton(self.widget)
        self.settings_button.setObjectName(u"settings_button")

        self.horizontalLayout.addWidget(self.settings_button)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.start_button = QPushButton(self.widget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy1)
        self.start_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.start_button, 2, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Current Task:", None))
        self.current_task_input.setText(QCoreApplication.translate("Form", u"Homework", None))
        self.timer_input.setText(QCoreApplication.translate("Form", u"60:00", None))
        self.restart_button.setText(QCoreApplication.translate("Form", u"r", None))
        self.settings_button.setText(QCoreApplication.translate("Form", u"S", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

