# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEvent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_event_dialog(object):
    def setupUi(self, event_dialog):
        event_dialog.setObjectName("event_dialog")
        event_dialog.resize(521, 603)
        event_dialog.setToolTip("")
        self.buttonBox = QtWidgets.QDialogButtonBox(event_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(430, 540, 81, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(event_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, -1, 411, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.v_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setObjectName("v_layout")
        self.event_title = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.event_title.setObjectName("event_title")
        self.v_layout.addWidget(self.event_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.day = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.day.setMaximum(365)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.year = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.year.setMaximum(999999999)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.v_layout.addLayout(self.horizontalLayout)
        self.event_description = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.event_description.setObjectName("event_description")
        self.v_layout.addWidget(self.event_description)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timeline = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.timeline.setToolTipDuration(-1)
        self.timeline.setObjectName("timeline")
        self.horizontalLayout_4.addWidget(self.timeline)
        self.new_timeline_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_timeline_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.new_timeline_btn.setObjectName("new_timeline_btn")
        self.horizontalLayout_4.addWidget(self.new_timeline_btn)
        self.v_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.location = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.location.setCurrentText("")
        self.location.setObjectName("location")
        self.horizontalLayout_5.addWidget(self.location)
        self.new_loc_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_loc_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.new_loc_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.new_loc_btn.setBaseSize(QtCore.QSize(90, 0))
        self.new_loc_btn.setObjectName("new_loc_btn")
        self.horizontalLayout_5.addWidget(self.new_loc_btn)
        self.v_layout.addLayout(self.horizontalLayout_5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.v_layout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.characters = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.characters.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.characters.setObjectName("characters")
        self.horizontalLayout_2.addWidget(self.characters)
        self.new_char_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_char_btn.setObjectName("new_char_btn")
        self.horizontalLayout_2.addWidget(self.new_char_btn)
        self.v_layout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.v_layout.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.civilizations = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.civilizations.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.civilizations.setObjectName("civilizations")
        self.horizontalLayout_3.addWidget(self.civilizations)
        self.new_civ_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_civ_btn.setObjectName("new_civ_btn")
        self.horizontalLayout_3.addWidget(self.new_civ_btn)
        self.v_layout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(event_dialog)
        self.buttonBox.accepted.connect(event_dialog.accept)
        self.buttonBox.rejected.connect(event_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(event_dialog)

    def retranslateUi(self, event_dialog):
        _translate = QtCore.QCoreApplication.translate
        event_dialog.setWindowTitle(_translate("event_dialog", "Composing event..."))
        self.event_title.setToolTip(_translate("event_dialog", "Event title, which will be seen in the timeline"))
        self.event_title.setPlaceholderText(_translate("event_dialog", "Event Title"))
        self.label_2.setText(_translate("event_dialog", "Day:"))
        self.label.setText(_translate("event_dialog", "Year:"))
        self.event_description.setToolTip(_translate("event_dialog", "A supplemental description for the event."))
        self.event_description.setPlaceholderText(_translate("event_dialog", "Event Summary..."))
        self.timeline.setToolTip(_translate("event_dialog", "The timeline in which this event occurs."))
        self.new_timeline_btn.setText(_translate("event_dialog", "New Timeline"))
        self.location.setToolTip(_translate("event_dialog", "Location at which the event occurred."))
        self.new_loc_btn.setText(_translate("event_dialog", "New Location"))
        self.label_3.setText(_translate("event_dialog", "Select characters involved in the event..."))
        self.characters.setToolTip(_translate("event_dialog", "Characters involved in the event..."))
        self.characters.setSortingEnabled(True)
        self.new_char_btn.setText(_translate("event_dialog", "New\nCharacter"))
        self.label_4.setText(
            _translate("event_dialog", "Select Civilizations / Peoples / Groups / Institutions involved..."))
        self.civilizations.setToolTip(_translate("event_dialog", "Civilizations surrounding the event."))
        self.civilizations.setSortingEnabled(True)
        self.new_civ_btn.setText(_translate("event_dialog", "New\nCivilization"))


class EventDialog(QtWidgets.QDialog):
    def __init__(self, unique_time, unique_loc, unique_chars, unique_civs):
        super().__init__()
        # set up the main window
        self.ui = Ui_event_dialog()
        self.ui.setupUi(self)
        self.title = 'Composing event...'

        # set up lists
        if unique_time.any():
            self.ui.timeline.addItems(unique_time)
        if unique_loc.any():
            self.ui.location.addItems(unique_loc)
        if unique_chars:
            self.ui.characters.addItems(unique_chars)
        if unique_civs:
            self.ui.civilizations.addItems(unique_civs)

        # set up button functionality
        self.ui.new_timeline_btn.clicked.connect(self._new_timeline)
        self.ui.new_loc_btn.clicked.connect(self._new_loc)
        self.ui.new_char_btn.clicked.connect(self._new_char)
        self.ui.new_civ_btn.clicked.connect(self._new_civ)

    def _new_timeline(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "New timeline...", "Timeline name:",
                                                          QtWidgets.QLineEdit.Normal, '')
        if ok_pressed and text != '':
            self.ui.timeline.addItem(text)

    def _new_loc(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "New location...", "Location name:",
                                                          QtWidgets.QLineEdit.Normal, '')
        if ok_pressed and text != '':
            self.ui.location.addItem(text)

    def _new_char(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "New character...", "Character name:",
                                                          QtWidgets.QLineEdit.Normal, '')
        if ok_pressed and text != '':
            self.ui.characters.addItem(text)

    def _new_civ(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "New civilization...", "Civilization name:",
                                                          QtWidgets.QLineEdit.Normal, '')
        if ok_pressed and text != '':
            self.ui.civilizations.addItem(text)

    @property
    def get_event_data(self):
        #          [0] - title,                 [1] is description
        return (self.ui.event_title.text(), self.ui.event_description.toPlainText(),
                float(int(self.ui.year.text())+(float(self.ui.day.text())/365.0)),  # [2] is date
                list(s.text() for s in self.ui.characters.selectedItems()),  # [3] is characters
                self.ui.location.currentText(),  # [4] is location
                list(s.text() for s in self.ui.civilizations.selectedItems()),  # [5] is civs
                self.ui.timeline.currentText())  # [6] is timeline
