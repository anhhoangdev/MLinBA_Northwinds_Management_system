# Form implementation generated from reading ui file 'E:\Ml_in_BA\Final\MlInBA_FinalProject\View\ManagementPage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from Service.Base.TableService import TableViewService


class Ui_WizardManagementPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(1060, 540)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=WizardPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1041, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_filter = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_filter.setObjectName("label_filter")
        self.gridLayout.addWidget(self.label_filter, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 0, 6, 1, 1)
        self.pushButton_insert = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.gridLayout.addWidget(self.pushButton_insert, 0, 7, 1, 1)
        self.TableView =TableViewService(parent=self.gridLayoutWidget)
        self.TableView.setObjectName("TableView")
        self.gridLayout.addWidget(self.TableView, 1, 0, 1, 8)
        self.comboBox_filter = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_filter.setObjectName("comboBox_filter")
        self.gridLayout.addWidget(self.comboBox_filter, 0, 3, 1, 2)
        self.lineEdit_filter = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.gridLayout.addWidget(self.lineEdit_filter, 0, 1, 1, 2)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        _translate = QtCore.QCoreApplication.translate
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage"))
        self.label_filter.setText(_translate("WizardPage", "Filter: "))
        self.pushButton_delete.setText(_translate("WizardPage", "Delete"))
        self.pushButton_insert.setText(_translate("WizardPage", "Insert"))
        self.lineEdit_filter.setPlaceholderText(_translate("WizardPage", "Insert filter content"))
