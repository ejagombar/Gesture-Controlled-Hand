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
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1446, 942)
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
        self.actionDefault.setCheckable(True)
        self.actionOneDark = QAction(MainWindow)
        self.actionOneDark.setObjectName(u"actionOneDark")
        self.actionOneDark.setCheckable(True)
        self.actionOneLight = QAction(MainWindow)
        self.actionOneLight.setObjectName(u"actionOneLight")
        self.actionOneLight.setCheckable(True)
        self.actionDefault2 = QAction(MainWindow)
        self.actionDefault2.setObjectName(u"actionDefault2")
        self.actionDefault2.setCheckable(True)
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
        self.SettingsLayout = QVBoxLayout()
        self.SettingsLayout.setSpacing(2)
        self.SettingsLayout.setObjectName(u"SettingsLayout")
        self.SettingsLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.ConnectionStatusLabel = QLabel(self.centralwidget)
        self.ConnectionStatusLabel.setObjectName(u"ConnectionStatusLabel")
        self.ConnectionStatusLabel.setMaximumSize(QSize(240, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.ConnectionStatusLabel.setFont(font)
        self.ConnectionStatusLabel.setTextFormat(Qt.PlainText)

        self.SettingsLayout.addWidget(self.ConnectionStatusLabel)

        self.IPAddrLineEdit = QLineEdit(self.centralwidget)
        self.IPAddrLineEdit.setObjectName(u"IPAddrLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IPAddrLineEdit.sizePolicy().hasHeightForWidth())
        self.IPAddrLineEdit.setSizePolicy(sizePolicy1)
        self.IPAddrLineEdit.setMinimumSize(QSize(150, 0))
        self.IPAddrLineEdit.setMaximumSize(QSize(240, 16777215))

        self.SettingsLayout.addWidget(self.IPAddrLineEdit)

        self.ConnectButton = QPushButton(self.centralwidget)
        self.ConnectButton.setObjectName(u"ConnectButton")
        sizePolicy1.setHeightForWidth(self.ConnectButton.sizePolicy().hasHeightForWidth())
        self.ConnectButton.setSizePolicy(sizePolicy1)
        self.ConnectButton.setMaximumSize(QSize(240, 16777215))

        self.SettingsLayout.addWidget(self.ConnectButton)

        self.LEDLine = QFrame(self.centralwidget)
        self.LEDLine.setObjectName(u"LEDLine")
        self.LEDLine.setMaximumSize(QSize(240, 16777215))
        self.LEDLine.setFrameShape(QFrame.HLine)
        self.LEDLine.setFrameShadow(QFrame.Sunken)

        self.SettingsLayout.addWidget(self.LEDLine)

        self.LEDColourLabel = QLabel(self.centralwidget)
        self.LEDColourLabel.setObjectName(u"LEDColourLabel")
        self.LEDColourLabel.setMaximumSize(QSize(240, 16777215))
        self.LEDColourLabel.setFont(font)

        self.SettingsLayout.addWidget(self.LEDColourLabel)

        self.RainbowRadioButton = QRadioButton(self.centralwidget)
        self.RainbowRadioButton.setObjectName(u"RainbowRadioButton")
        self.RainbowRadioButton.setMaximumSize(QSize(240, 16777215))

        self.SettingsLayout.addWidget(self.RainbowRadioButton)

        self.ReactiveRadioButton = QRadioButton(self.centralwidget)
        self.ReactiveRadioButton.setObjectName(u"ReactiveRadioButton")
        self.ReactiveRadioButton.setMaximumSize(QSize(240, 16777215))

        self.SettingsLayout.addWidget(self.ReactiveRadioButton)

        self.CustomRadioButton = QRadioButton(self.centralwidget)
        self.CustomRadioButton.setObjectName(u"CustomRadioButton")
        self.CustomRadioButton.setMaximumSize(QSize(105, 16777215))

        self.SettingsLayout.addWidget(self.CustomRadioButton)

        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.SettingsLayout.addItem(self.verticalSpacer)

        self.ColourButton = QPushButton(self.centralwidget)
        self.ColourButton.setObjectName(u"ColourButton")
        sizePolicy1.setHeightForWidth(self.ColourButton.sizePolicy().hasHeightForWidth())
        self.ColourButton.setSizePolicy(sizePolicy1)
        self.ColourButton.setMaximumSize(QSize(240, 16777215))
        icon = QIcon()
        icon.addFile(u"../../../../../Desktop/Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ColourButton.setIcon(icon)

        self.SettingsLayout.addWidget(self.ColourButton)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.SettingsLayout.addItem(self.verticalSpacer_2)

        self.LEDBrightnessLabel = QLabel(self.centralwidget)
        self.LEDBrightnessLabel.setObjectName(u"LEDBrightnessLabel")
        self.LEDBrightnessLabel.setMaximumSize(QSize(240, 16777215))
        self.LEDBrightnessLabel.setFont(font)
        self.LEDBrightnessLabel.setIndent(-4)

        self.SettingsLayout.addWidget(self.LEDBrightnessLabel)

        self.BrightnessSlider = QSlider(self.centralwidget)
        self.BrightnessSlider.setObjectName(u"BrightnessSlider")
        self.BrightnessSlider.setMaximumSize(QSize(240, 16777215))
        self.BrightnessSlider.setOrientation(Qt.Horizontal)

        self.SettingsLayout.addWidget(self.BrightnessSlider)

        self.LogLine = QFrame(self.centralwidget)
        self.LogLine.setObjectName(u"LogLine")
        self.LogLine.setMaximumSize(QSize(240, 16777215))
        self.LogLine.setFrameShape(QFrame.HLine)
        self.LogLine.setFrameShadow(QFrame.Sunken)

        self.SettingsLayout.addWidget(self.LogLine)

        self.LogLabel = QLabel(self.centralwidget)
        self.LogLabel.setObjectName(u"LogLabel")
        self.LogLabel.setMaximumSize(QSize(240, 16777215))
        self.LogLabel.setFont(font)

        self.SettingsLayout.addWidget(self.LogLabel)

        self.LogScrollArea = QScrollArea(self.centralwidget)
        self.LogScrollArea.setObjectName(u"LogScrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LogScrollArea.sizePolicy().hasHeightForWidth())
        self.LogScrollArea.setSizePolicy(sizePolicy2)
        self.LogScrollArea.setMinimumSize(QSize(0, 200))
        self.LogScrollArea.setMaximumSize(QSize(240, 16777215))
        self.LogScrollArea.setFrameShadow(QFrame.Plain)
        self.LogScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.LogScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LogScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.LogScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 16, 16))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.LogScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.SettingsLayout.addWidget(self.LogScrollArea)

        self.SettingsVerticleSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SettingsLayout.addItem(self.SettingsVerticleSpacer)


        self.horizontalLayout_2.addLayout(self.SettingsLayout)

        self.ViewsTabWidget = QTabWidget(self.centralwidget)
        self.ViewsTabWidget.setObjectName(u"ViewsTabWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ViewsTabWidget.sizePolicy().hasHeightForWidth())
        self.ViewsTabWidget.setSizePolicy(sizePolicy3)
        self.ViewsTabWidget.setTabPosition(QTabWidget.North)
        self.ViewsTabWidget.setTabShape(QTabWidget.Rounded)
        self.ViewsTabWidget.setUsesScrollButtons(False)
        self.ViewsTabWidget.setDocumentMode(False)
        self.ViewsTabWidget.setTabsClosable(False)
        self.ViewsTabWidget.setMovable(True)
        self.ViewsTabWidget.setTabBarAutoHide(True)
        self.WebcamTab = QWidget()
        self.WebcamTab.setObjectName(u"WebcamTab")
        self.WebcamLabel = QLabel(self.WebcamTab)
        self.WebcamLabel.setObjectName(u"WebcamLabel")
        self.WebcamLabel.setGeometry(QRect(10, 10, 1241, 841))
        sizePolicy3.setHeightForWidth(self.WebcamLabel.sizePolicy().hasHeightForWidth())
        self.WebcamLabel.setSizePolicy(sizePolicy3)
        self.WebcamLabel.setFrameShape(QFrame.Box)
        self.ViewsTabWidget.addTab(self.WebcamTab, "")
        self.RemoteTab = QWidget()
        self.RemoteTab.setObjectName(u"RemoteTab")
        self.ViewsTabWidget.addTab(self.RemoteTab, "")

        self.horizontalLayout_2.addWidget(self.ViewsTabWidget)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1446, 22))
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

        self.ViewsTabWidget.setCurrentIndex(0)


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
        self.actionDefault2.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.ConnectionStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Status: Disconnected", None))
        self.IPAddrLineEdit.setInputMask("")
        self.IPAddrLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Address", u"IP Address"))
        self.ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.LEDColourLabel.setText(QCoreApplication.translate("MainWindow", u"LED Colour", None))
        self.RainbowRadioButton.setText(QCoreApplication.translate("MainWindow", u"Rainbow", None))
        self.ReactiveRadioButton.setText(QCoreApplication.translate("MainWindow", u"Reactive", None))
        self.CustomRadioButton.setText(QCoreApplication.translate("MainWindow", u"Custom Colour", None))
        self.ColourButton.setText(QCoreApplication.translate("MainWindow", u"Select Colour", None))
        self.LEDBrightnessLabel.setText(QCoreApplication.translate("MainWindow", u"LED Brightness: 25%", None))
        self.LogLabel.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.WebcamLabel.setText("")
        self.ViewsTabWidget.setTabText(self.ViewsTabWidget.indexOf(self.WebcamTab), QCoreApplication.translate("MainWindow", u"Webcam", None))
        self.ViewsTabWidget.setTabText(self.ViewsTabWidget.indexOf(self.RemoteTab), QCoreApplication.translate("MainWindow", u"Robot Cam", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuSelect_Video_Device.setTitle(QCoreApplication.translate("MainWindow", u"Select Video Device", None))
    # retranslateUi

