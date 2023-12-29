# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMdiArea, QMenu, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1834, 929)
        MainWindow.setMinimumSize(QSize(450, 300))
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionShow_Webcam_View = QAction(MainWindow)
        self.actionShow_Webcam_View.setObjectName(u"actionShow_Webcam_View")
        self.actionShow_Webcam_View.setCheckable(True)
        self.actionShow_Tracking_Mask = QAction(MainWindow)
        self.actionShow_Tracking_Mask.setObjectName(u"actionShow_Tracking_Mask")
        self.actionShow_Tracking_Mask.setCheckable(True)
        self.actionShow_3D_Visualisation = QAction(MainWindow)
        self.actionShow_3D_Visualisation.setObjectName(u"actionShow_3D_Visualisation")
        self.actionShow_3D_Visualisation.setCheckable(True)
        self.actionShow_Remote_View = QAction(MainWindow)
        self.actionShow_Remote_View.setObjectName(u"actionShow_Remote_View")
        self.actionShow_Remote_View.setCheckable(True)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionDefault = QAction(MainWindow)
        self.actionDefault.setObjectName(u"actionDefault")
        self.actionOneDark = QAction(MainWindow)
        self.actionOneDark.setObjectName(u"actionOneDark")
        self.actionOneLight = QAction(MainWindow)
        self.actionOneLight.setObjectName(u"actionOneLight")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(240, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(150, 0))
        self.lineEdit.setMaximumSize(QSize(240, 16777215))

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMaximumSize(QSize(240, 16777215))

        self.verticalLayout.addWidget(self.pushButton)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(240, 16777215))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(240, 16777215))
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(240, 16777215))

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMaximumSize(QSize(240, 16777215))

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMaximumSize(QSize(105, 16777215))

        self.verticalLayout.addWidget(self.radioButton_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMaximumSize(QSize(240, 16777215))
        icon = QIcon()
        icon.addFile(u"../../../../../Desktop/Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(240, 16777215))
        self.label_5.setFont(font)
        self.label_5.setIndent(-4)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(240, 16777215))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(240, 16777215))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(240, 16777215))
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(0, 200))
        self.scrollArea.setMaximumSize(QSize(240, 16777215))
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 16, 16))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy3)
        self.mdiArea.setMaximumSize(QSize(16777215, 16777215))
        self.mdiArea.setSizeIncrement(QSize(100, 0))
        self.mdiArea.setFrameShadow(QFrame.Plain)
        self.mdiArea.setTabShape(QTabWidget.Rounded)

        self.verticalLayout_2.addWidget(self.mdiArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1834, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTheme = QMenu(self.menuFile)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuSelect_Video_Device = QMenu(self.menuOptions)
        self.menuSelect_Video_Device.setObjectName(u"menuSelect_Video_Device")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.menuTheme.menuAction())
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)
        self.menuTheme.addAction(self.actionOneDark)
        self.menuTheme.addAction(self.actionOneLight)
        self.menuOptions.addAction(self.menuSelect_Video_Device.menuAction())
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionShow_Webcam_View)
        self.menuOptions.addAction(self.actionShow_Tracking_Mask)
        self.menuOptions.addAction(self.actionShow_3D_Visualisation)
        self.menuOptions.addAction(self.actionShow_Remote_View)
        self.menuSelect_Video_Device.addAction(self.actionDefault)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionShow_Webcam_View.setText(QCoreApplication.translate("MainWindow", u"Show Webcam View", None))
        self.actionShow_Tracking_Mask.setText(QCoreApplication.translate("MainWindow", u"Show Tracking Mask", None))
        self.actionShow_3D_Visualisation.setText(QCoreApplication.translate("MainWindow", u"Show 3D Visualisation", None))
        self.actionShow_Remote_View.setText(QCoreApplication.translate("MainWindow", u"Show Remote View", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionDefault.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.actionOneDark.setText(QCoreApplication.translate("MainWindow", u"OneDark", None))
        self.actionOneLight.setText(QCoreApplication.translate("MainWindow", u"OneLight", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Status: Disconnected", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Address", u"IP Address"))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LED Colour", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Rainbow", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Reactive", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Custom Colour", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Select Colour", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LED Brightness", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuSelect_Video_Device.setTitle(QCoreApplication.translate("MainWindow", u"Select Video Device", None))
    # retranslateUi

