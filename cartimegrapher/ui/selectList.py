# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectList.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 299)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.list_widget = QtWidgets.QListWidget(Dialog)
        self.list_widget.setGeometry(QtCore.QRect(5, 11, 281, 281))
        self.list_widget.setObjectName("list_widget")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class SelectListDialog(QtWidgets.QDialog):
    def __init__(self, list_to_query, title='Select from the list...', multiple_select=False):
        super().__init__()
        # set up the main window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.ui.list_widget.addItems(list_to_query)
        self.ui.list_widget.update()
        if multiple_select:
            self.ui.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        else:
            self.ui.list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    def get_data(self):
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return list([l.text() for l in self.ui.list_widget.selectedItems()])
        else:
            return None
