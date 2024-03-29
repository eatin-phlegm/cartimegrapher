# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewFile = QtWidgets.QAction(MainWindow)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionViewCharacters = QtWidgets.QAction(MainWindow)
        self.actionViewCharacters.setObjectName("actionViewCharacters")
        self.actionViewLocations = QtWidgets.QAction(MainWindow)
        self.actionViewLocations.setObjectName("actionViewLocations")
        self.actionViewCivilizations = QtWidgets.QAction(MainWindow)
        self.actionViewCivilizations.setObjectName("actionViewCivilizations")
        self.actionViewEvents = QtWidgets.QAction(MainWindow)
        self.actionViewEvents.setObjectName("actionViewEvents")
        self.actionViewRecent_Edits = QtWidgets.QAction(MainWindow)
        self.actionViewRecent_Edits.setObjectName("actionViewRecent_Edits")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        self.action_Preferences.setObjectName("action_Preferences")
        self.actionProject_Metadata = QtWidgets.QAction(MainWindow)
        self.actionProject_Metadata.setObjectName("actionProject_Metadata")
        self.action_Minimize_Maximize = QtWidgets.QAction(MainWindow)
        self.action_Minimize_Maximize.setObjectName("action_Minimize_Maximize")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Manual = QtWidgets.QAction(MainWindow)
        self.action_Manual.setObjectName("action_Manual")
        self.actionAddEvent = QtWidgets.QAction(MainWindow)
        self.actionAddEvent.setObjectName("actionAddEvent")
        self.actionRemoveEvent = QtWidgets.QAction(MainWindow)
        self.actionRemoveEvent.setObjectName("actionRemoveEvent")
        self.actionAddCharacter = QtWidgets.QAction(MainWindow)
        self.actionAddCharacter.setObjectName("actionAddCharacter")
        self.actionRemoveCharacter = QtWidgets.QAction(MainWindow)
        self.actionRemoveCharacter.setObjectName("actionRemoveCharacter")
        self.actionAddTimeline = QtWidgets.QAction(MainWindow)
        self.actionAddTimeline.setObjectName("actionAddTimeline")
        self.actionRemoveTimeline = QtWidgets.QAction(MainWindow)
        self.actionRemoveTimeline.setObjectName("actionRemoveTimeline")
        self.actionAddLocation = QtWidgets.QAction(MainWindow)
        self.actionAddLocation.setObjectName("actionAddLocation")
        self.actionEditEvent = QtWidgets.QAction(MainWindow)
        self.actionEditEvent.setObjectName("actionEditEvent")
        self.actionEditTimeline = QtWidgets.QAction(MainWindow)
        self.actionEditTimeline.setObjectName("actionEditTimeline")
        self.actionEditCharacter = QtWidgets.QAction(MainWindow)
        self.actionEditCharacter.setObjectName("actionEditCharacter")
        self.actionRemoveLocation = QtWidgets.QAction(MainWindow)
        self.actionRemoveLocation.setObjectName("actionRemoveLocation")
        self.actionEditLocation = QtWidgets.QAction(MainWindow)
        self.actionEditLocation.setObjectName("actionEditLocation")
        self.actionNewCivilization = QtWidgets.QAction(MainWindow)
        self.actionNewCivilization.setObjectName("actionNewCivilization")
        self.actionRemoveCivilization = QtWidgets.QAction(MainWindow)
        self.actionRemoveCivilization.setObjectName("actionRemoveCivilization")
        self.actionEditCivilization = QtWidgets.QAction(MainWindow)
        self.actionEditCivilization.setObjectName("actionEditCivilization")
        self.actionViewEvent_Statistics = QtWidgets.QAction(MainWindow)
        self.actionViewEvent_Statistics.setObjectName("actionViewEvent_Statistics")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionCharacters = QtWidgets.QAction(MainWindow)
        self.actionCharacters.setObjectName("actionCharacters")
        self.actionLocations = QtWidgets.QAction(MainWindow)
        self.actionLocations.setObjectName("actionLocations")
        self.actionCivilizations = QtWidgets.QAction(MainWindow)
        self.actionCivilizations.setObjectName("actionCivilizations")
        self.actionTimelines = QtWidgets.QAction(MainWindow)
        self.actionTimelines.setObjectName("actionTimelines")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuEdit.addAction(self.actionAddEvent)
        self.menuEdit.addAction(self.actionEditEvent)
        self.menuEdit.addAction(self.actionRemoveEvent)
        self.menu_View.addAction(self.actionCharacters)
        self.menu_View.addAction(self.actionLocations)
        self.menu_View.addAction(self.actionCivilizations)
        self.menu_View.addAction(self.actionTimelines)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.actionNewFile.setText(_translate("MainWindow", "&New..."))
        self.actionNewFile.setToolTip(_translate("MainWindow", "Create a new timeline file."))
        self.actionNewFile.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "&Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionImport.setText(_translate("MainWindow", "&Import..."))
        self.actionImport.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save &As..."))
        self.actionExport.setText(_translate("MainWindow", "&Export..."))
        self.actionViewCharacters.setText(_translate("MainWindow", "&Characters"))
        self.actionViewLocations.setText(_translate("MainWindow", "&Locations"))
        self.actionViewCivilizations.setText(_translate("MainWindow", "Ci&vilizations"))
        self.actionViewEvents.setText(_translate("MainWindow", "&Timelines"))
        self.actionViewRecent_Edits.setText(_translate("MainWindow", "&Recent Edits"))
        self.action_Preferences.setText(_translate("MainWindow", "&Preferences..."))
        self.actionProject_Metadata.setText(_translate("MainWindow", "Project &Metadata.."))
        self.action_Minimize_Maximize.setText(_translate("MainWindow", "&Minimize / Maximize"))
        self.action_About.setText(_translate("MainWindow", "&About..."))
        self.action_Manual.setText(_translate("MainWindow", "&Manual..."))
        self.actionAddEvent.setText(_translate("MainWindow", "&New Event..."))
        self.actionRemoveEvent.setText(_translate("MainWindow", "&Remove Event..."))
        self.actionAddCharacter.setText(_translate("MainWindow", "&New..."))
        self.actionAddCharacter.setToolTip(_translate("MainWindow", "Add a new character."))
        self.actionRemoveCharacter.setText(_translate("MainWindow", "&Delete..."))
        self.actionRemoveCharacter.setToolTip(_translate("MainWindow", "Delete a character"))
        self.actionAddTimeline.setText(_translate("MainWindow", "&New..."))
        self.actionAddTimeline.setToolTip(_translate("MainWindow", "Create a new timeline."))
        self.actionRemoveTimeline.setText(_translate("MainWindow", "&Delete..."))
        self.actionRemoveTimeline.setToolTip(_translate("MainWindow", "Delete a timeline."))
        self.actionAddLocation.setText(_translate("MainWindow", "&New..."))
        self.actionAddLocation.setToolTip(_translate("MainWindow", "Create a new location."))
        self.actionEditEvent.setText(_translate("MainWindow", "&Edit / View Event..."))
        self.actionEditTimeline.setText(_translate("MainWindow", "&Edit / View..."))
        self.actionEditCharacter.setText(_translate("MainWindow", "&Edit / View..."))
        self.actionRemoveLocation.setText(_translate("MainWindow", "&Delete..."))
        self.actionEditLocation.setText(_translate("MainWindow", "&Edit / View..."))
        self.actionNewCivilization.setText(_translate("MainWindow", "&New..."))
        self.actionRemoveCivilization.setText(_translate("MainWindow", "&Delete..."))
        self.actionEditCivilization.setText(_translate("MainWindow", "&Edit / View..."))
        self.actionViewEvent_Statistics.setText(_translate("MainWindow", "&Event Statistics"))
        self.action_Close.setText(_translate("MainWindow", "&Close File"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCharacters.setText(_translate("MainWindow", "&Characters..."))
        self.actionLocations.setText(_translate("MainWindow", "&Locations..."))
        self.actionCivilizations.setText(_translate("MainWindow", "Ci&vilizations..."))
        self.actionTimelines.setText(_translate("MainWindow", "&Timelines..."))
