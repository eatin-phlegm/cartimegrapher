import sys
from ast import literal_eval as l_eval

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout

from logbook import Logbook
from ui.mainWindow import Ui_MainWindow
from ui.newEvent import EventDialog
from ui.selectList import SelectListDialog
from ui.view import ViewDialog, TimelineFigure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set up the main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.title = '[CARTimeGRAPHER]'
        self.setWindowTitle(self.title)
        layout = QVBoxLayout(self.centralWidget())

        # set up dataframe
        self.logbook = Logbook()

        # -- set up actions on top menubar
        # file menu
        self.ui.actionOpen.triggered.connect(self._open_logbook)
        self.ui.actionSave.triggered.connect(self._save_logbook)
        self.ui.actionSave_As.triggered.connect(self._save_as_logbook)
        self.ui.actionImport.triggered.connect(self._import)
        self.ui.actionExport.triggered.connect(self._export)
        self.ui.action_Quit.triggered.connect(self._quit)
        # edit menu
        self.ui.actionAddEvent.triggered.connect(self._add_event)
        self.ui.actionEditEvent.triggered.connect(self._edit_event)
        self.ui.actionRemoveEvent.triggered.connect(self._remove_event)
        # view menu
        self.ui.actionCharacters.triggered.connect(lambda: self._view_dialog('Characters Involved'))
        self.ui.actionCivilizations.triggered.connect(lambda: self._view_dialog('Civilizations Involved'))
        self.ui.actionLocations.triggered.connect(lambda: self._view_dialog('Location'))
        self.ui.actionTimelines.triggered.connect(lambda: self._view_dialog('Timeline'))

        # -- set up event timeline figure
        self._event_timeline = TimelineFigure("[Event Timeline]", figsize=(8.8, 4), main_window=self)
        layout.addWidget(self._event_timeline)
        self.addToolBar(self._event_timeline.tool_bar)

    # -- ui handle of logbook functionality
    def _setup_logbook(self):
        self.logbook = Logbook()
        self._update_event_timeline()

    def _open_logbook(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        fname, _ = dlg.getOpenFileName(caption='Open Project...',
                                       filter=dlg.tr("Excel File (*.xlsx)"), options=dlg.Options())
        if fname:
            self.logbook.load(filename=fname)
            self._update_event_timeline()
            self.setWindowTitle(self.logbook.filename)

    def _save_logbook(self):
        self.logbook.save_excel()

    def _save_as_logbook(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        fname, _ = dlg.getSaveFileName(caption='Save As...',
                                       filter="Excel File (*.xlsx)", options=dlg.Options())
        if fname:
            if not fname.endswith('.xlsx'):
                fname += '.xlsx'
            self.logbook.save_as_excel(filename=fname)
            self.setWindowTitle(self.logbook.filename)

    def _import(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.setWindowTitle('Import project into this one...')
        fname, _ = dlg.getOpenFileName(caption='Join an external project into this one...',
                                       filter=dlg.tr("Excel File (*.xlsx)"), options=dlg.Options())
        if fname:
            self.logbook.import_excel(filename=fname)
            self._update_event_timeline()

    def _export(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.setWindowTitle('Export project into another project...')
        fname, _ = dlg.getOpenFileName(caption="Join this project into an external one...",
                                       filter=dlg.tr("Excel File (*.xlsx)"), options=dlg.Options())
        if fname:
            self.logbook.export_to_excel(filename=fname)

    # utility functions for add event and edit, used to write event to the logbook
    # connected to the accept button of a new event dialog
    def _new_event(self, event_dlg):
        data = event_dlg.get_event_data
        self.logbook.new_event(data)
        self._update_event_timeline()

    def _change_event(self, old_name, event_dlg):
        data = event_dlg.get_event_data
        self.logbook.edit_event(old_name, data)
        self._update_event_timeline()

    # updates the main event timeline on the main window
    def _update_event_timeline(self):
        names, dates = self.logbook.get_event_timeline()
        self._event_timeline.render_canvas(names, dates)

    # connected to the 'add event' qaction on the edit menubar option
    def _add_event(self):
        dlg = EventDialog(self.logbook.get_unique_timelines(), self.logbook.get_unique_locs(),
                          self.logbook.get_unique_chars(), self.logbook.get_unique_civs())
        dlg.accepted.connect(lambda: self._new_event(dlg))
        dlg.exec_()

    def _edit_event(self):
        # select an event to edit
        event_list, _ = self.logbook.get_event_timeline()
        selected = self._select_list(event_list, title="Select events to edit/view...",
                                     multiple_select=False)
        # edit event selected
        dlg = EventDialog(self.logbook.get_unique_timelines(), self.logbook.get_unique_locs(),
                          self.logbook.get_unique_chars(), self.logbook.get_unique_civs())

        event_data = self.logbook.get_event_data(selected)[0]  # get event data to view / edit
        dlg.ui.event_title.setText(event_data[1])
        dlg.ui.event_description.setPlainText(event_data[2])
        dlg.ui.day.setValue(int((event_data[3] % 1)*365))
        dlg.ui.year.setValue(int(event_data[3]))
        dlg.ui.timeline.setCurrentText(event_data[7])  # set the timeline to match the event's
        dlg.ui.location.setCurrentText(event_data[5])

        # prep character list
        char_list = event_data[4]
        if isinstance(char_list, str):
            char_list = l_eval(char_list)
        for character in char_list:  # check characters
            matching_items = dlg.ui.characters.findItems(character, Qt.MatchContains)
            for item in matching_items:
                item.setSelected(True)

        civ_list = event_data[6]
        if isinstance(civ_list, str):
            civ_list = l_eval(civ_list)
        for civ in civ_list:
            matching_items = dlg.ui.civilizations.findItems(civ, Qt.MatchContains)
            for item in matching_items:
                item.setSelected(True)

        dlg.accepted.connect(lambda: self._change_event(selected, dlg))
        dlg.exec_()

    def _remove_event(self):
        event_list, _ = self.logbook.get_event_timeline()
        selected = self._select_list(event_list, title="Select events to remove...",
                                     multiple_select=True)
        self.logbook.remove_event(selected)
        self._update_event_timeline()

    def _view_dialog(self, category):
        dlg = ViewDialog(category, self.logbook)
        dlg.exec_()

    # returns the items selected
    @staticmethod
    def _select_list(list_to_query, title='Select from the list...', multiple_select=False):
        dlg = SelectListDialog(list_to_query, title, multiple_select)
        return dlg.get_data()

    @staticmethod
    def _quit():
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
