# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QGridLayout,
    QGroupBox, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetPlotContainer = QWidget(self.centralwidget)
        self.widgetPlotContainer.setObjectName(u"widgetPlotContainer")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlotContainer.sizePolicy().hasHeightForWidth())
        self.widgetPlotContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widgetPlotContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.valuePlot = QLabel(self.widgetPlotContainer)
        self.valuePlot.setObjectName(u"valuePlot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.valuePlot.sizePolicy().hasHeightForWidth())
        self.valuePlot.setSizePolicy(sizePolicy1)
        self.valuePlot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.valuePlot)


        self.verticalLayout.addWidget(self.widgetPlotContainer)

        self.groupData = QGroupBox(self.centralwidget)
        self.groupData.setObjectName(u"groupData")
        sizePolicy1.setHeightForWidth(self.groupData.sizePolicy().hasHeightForWidth())
        self.groupData.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.groupData)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelStatistic = QLabel(self.groupData)
        self.labelStatistic.setObjectName(u"labelStatistic")

        self.gridLayout.addWidget(self.labelStatistic, 1, 0, 1, 1)

        self.labelPValue = QLabel(self.groupData)
        self.labelPValue.setObjectName(u"labelPValue")

        self.gridLayout.addWidget(self.labelPValue, 1, 2, 1, 1)

        self.valueStatistic = QLabel(self.groupData)
        self.valueStatistic.setObjectName(u"valueStatistic")
        sizePolicy1.setHeightForWidth(self.valueStatistic.sizePolicy().hasHeightForWidth())
        self.valueStatistic.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.valueStatistic, 1, 1, 1, 1)

        self.valuePValue = QLabel(self.groupData)
        self.valuePValue.setObjectName(u"valuePValue")
        sizePolicy1.setHeightForWidth(self.valuePValue.sizePolicy().hasHeightForWidth())
        self.valuePValue.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.valuePValue, 1, 3, 1, 1)

        self.valueHypothesis = QLabel(self.groupData)
        self.valueHypothesis.setObjectName(u"valueHypothesis")
        self.valueHypothesis.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.valueHypothesis, 2, 0, 1, 4)

        self.labelSignificance = QLabel(self.groupData)
        self.labelSignificance.setObjectName(u"labelSignificance")

        self.gridLayout.addWidget(self.labelSignificance, 0, 0, 1, 1)

        self.inputSignificance = QComboBox(self.groupData)
        self.inputSignificance.addItem("")
        self.inputSignificance.addItem("")
        self.inputSignificance.addItem("")
        self.inputSignificance.setObjectName(u"inputSignificance")

        self.gridLayout.addWidget(self.inputSignificance, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupData)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.controlWidget = QWidget()
        self.controlWidget.setObjectName(u"controlWidget")
        self.dockWidget.setWidget(self.controlWidget)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)

        self.retranslateUi(MainWindow)

        self.inputSignificance.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crimer-Von Mises criterion test", None))
        self.valuePlot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.groupData.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.labelStatistic.setText(QCoreApplication.translate("MainWindow", u"Statistic", None))
        self.labelPValue.setText(QCoreApplication.translate("MainWindow", u"p-value", None))
        self.valueStatistic.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.valuePValue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.valueHypothesis.setText(QCoreApplication.translate("MainWindow", u"Samples do not match distribution", None))
        self.labelSignificance.setText(QCoreApplication.translate("MainWindow", u"Significance", None))
        self.inputSignificance.setItemText(0, QCoreApplication.translate("MainWindow", u"0.01", None))
        self.inputSignificance.setItemText(1, QCoreApplication.translate("MainWindow", u"0.05", None))
        self.inputSignificance.setItemText(2, QCoreApplication.translate("MainWindow", u"0.10", None))

    # retranslateUi

