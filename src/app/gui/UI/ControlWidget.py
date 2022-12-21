# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ControlWidget(object):
    def setupUi(self, ControlWidget):
        if not ControlWidget.objectName():
            ControlWidget.setObjectName(u"ControlWidget")
        ControlWidget.resize(390, 568)
        self.verticalLayout_2 = QVBoxLayout(ControlWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupControls = QGroupBox(ControlWidget)
        self.groupControls.setObjectName(u"groupControls")
        self.verticalLayout = QVBoxLayout(self.groupControls)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelDistribution = QLabel(self.groupControls)
        self.labelDistribution.setObjectName(u"labelDistribution")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDistribution)

        self.inputDistribution = QComboBox(self.groupControls)
        self.inputDistribution.addItem("")
        self.inputDistribution.addItem("")
        self.inputDistribution.setObjectName(u"inputDistribution")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputDistribution)

        self.labelN = QLabel(self.groupControls)
        self.labelN.setObjectName(u"labelN")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelN)

        self.inputN = QSpinBox(self.groupControls)
        self.inputN.setObjectName(u"inputN")
        self.inputN.setMinimum(2)
        self.inputN.setMaximum(1000000000)
        self.inputN.setValue(3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputN)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelMean = QLabel(self.groupControls)
        self.labelMean.setObjectName(u"labelMean")

        self.horizontalLayout_2.addWidget(self.labelMean)

        self.valueMean = QLabel(self.groupControls)
        self.valueMean.setObjectName(u"valueMean")

        self.horizontalLayout_2.addWidget(self.valueMean)

        self.labelStd = QLabel(self.groupControls)
        self.labelStd.setObjectName(u"labelStd")

        self.horizontalLayout_2.addWidget(self.labelStd)

        self.valueStd = QLabel(self.groupControls)
        self.valueStd.setObjectName(u"valueStd")

        self.horizontalLayout_2.addWidget(self.valueStd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.inputCustomDistribution = QLineEdit(self.groupControls)
        self.inputCustomDistribution.setObjectName(u"inputCustomDistribution")
        self.inputCustomDistribution.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputCustomDistribution)

        self.valueError = QLabel(self.groupControls)
        self.valueError.setObjectName(u"valueError")
        self.valueError.setWordWrap(True)

        self.verticalLayout.addWidget(self.valueError)


        self.verticalLayout_2.addWidget(self.groupControls)

        self.tableWidget = QTableWidget(ControlWidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(3)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.groupSample = QGroupBox(ControlWidget)
        self.groupSample.setObjectName(u"groupSample")
        self.horizontalLayout = QHBoxLayout(self.groupSample)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonImport = QPushButton(self.groupSample)
        self.buttonImport.setObjectName(u"buttonImport")

        self.horizontalLayout.addWidget(self.buttonImport)

        self.buttonExport = QPushButton(self.groupSample)
        self.buttonExport.setObjectName(u"buttonExport")

        self.horizontalLayout.addWidget(self.buttonExport)


        self.verticalLayout_2.addWidget(self.groupSample)


        self.retranslateUi(ControlWidget)

        QMetaObject.connectSlotsByName(ControlWidget)
    # setupUi

    def retranslateUi(self, ControlWidget):
        ControlWidget.setWindowTitle(QCoreApplication.translate("ControlWidget", u"ControlWidget", None))
        self.groupControls.setTitle(QCoreApplication.translate("ControlWidget", u"Controls", None))
        self.labelDistribution.setText(QCoreApplication.translate("ControlWidget", u"Distribution", None))
        self.inputDistribution.setItemText(0, QCoreApplication.translate("ControlWidget", u"Custom", None))
        self.inputDistribution.setItemText(1, QCoreApplication.translate("ControlWidget", u"Normal", None))

        self.labelN.setText(QCoreApplication.translate("ControlWidget", u"Samples", None))
        self.labelMean.setText(QCoreApplication.translate("ControlWidget", u"Mean:", None))
        self.valueMean.setText(QCoreApplication.translate("ControlWidget", u"0", None))
        self.labelStd.setText(QCoreApplication.translate("ControlWidget", u"Stand. dev.", None))
        self.valueStd.setText(QCoreApplication.translate("ControlWidget", u"0", None))
        self.inputCustomDistribution.setText("")
        self.inputCustomDistribution.setPlaceholderText(QCoreApplication.translate("ControlWidget", u"Input distribution expression", None))
        self.valueError.setText(QCoreApplication.translate("ControlWidget", u"No errors", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ControlWidget", u"Sample", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ControlWidget", u"CDF", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ControlWidget", u"-1", None));
        ___qtablewidgetitem3 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ControlWidget", u"0", None));
        ___qtablewidgetitem4 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ControlWidget", u"1", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupSample.setTitle(QCoreApplication.translate("ControlWidget", u"Sample", None))
        self.buttonImport.setText(QCoreApplication.translate("ControlWidget", u"Import", None))
        self.buttonExport.setText(QCoreApplication.translate("ControlWidget", u"Export", None))
    # retranslateUi

