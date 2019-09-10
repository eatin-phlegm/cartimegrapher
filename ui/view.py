# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import numpy as np
from PyQt5 import QtCore, QtWidgets
from logbook import Logbook

import matplotlib
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

matplotlib.use('QT5Agg')


# a plot specifically for timelines featured in the MainWindow
class TimelineFigure(FigureCanvas):
    def __init__(self, title, figsize, main_window):
        super().__init__(Figure(figsize))
        self.title = title
        self.tool_bar = NavigationToolbar(self, main_window)
        self._ax = self.figure.subplots()

    def render_canvas(self, notes, dates):
        self._ax.clear()
        if notes.any() and dates.any():
            # Choose some nice levels
            levels = np.tile([-5, 5, -3, 3, -1, 1],
                             int(np.ceil(len(dates) / 6)))[:len(dates)]

            # Create figure and plot a stem plot with the date
            self._ax.set(title=self.title)
            self._ax.stem(dates, levels, linefmt="C3-", basefmt="k-", use_line_collection=True)

            # annotate lines
            vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
            for d, l, r, va in zip(dates, levels, notes, vert):
                self._ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3),
                                  textcoords="offset points", va=va, ha="right")

            # remove y axis and spines
            self._ax.get_yaxis().set_visible(False)
            for spine in ["left", "top", "right"]:
                self._ax.spines[spine].set_visible(False)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(871, 501)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 281, 481))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter_list_widget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.filter_list_widget.setObjectName("filter_list_widget")
        self.horizontalLayout.addWidget(self.filter_list_widget)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 10, 561, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.timeline_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.timeline_layout.setContentsMargins(0, 0, 0, 0)
        self.timeline_layout.setObjectName("timeline_layout")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Filtered Timelines..."))


class ViewDialog(QtWidgets.QDialog):
    def __init__(self, category_name, logbook_copy):
        assert isinstance(logbook_copy, Logbook)
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Viewing " + category_name + " Timelines...")
        self.ui.filter_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ui.filter_list_widget.clicked.connect(self._update_timeline_pane)
        self._category = category_name
        self._logbook_copy = logbook_copy
        # set up selectable items to view timelines for
        if self._category == 'Characters Involved':
            self.ui.filter_list_widget.addItems(self._logbook_copy.get_unique_chars())
        elif self._category == 'Civilizations Involved':
            self.ui.filter_list_widget.addItems(self._logbook_copy.get_unique_civs())
        elif self._category == 'Location':
            self.ui.filter_list_widget.addItems(self._logbook_copy.get_unique_locs())
        elif self._category == 'Timeline':
            self.ui.filter_list_widget.addItems(self._logbook_copy.get_unique_timelines())
        # set up timeline figure
        self._timeline_figure = TimelineFigure('Timeline of ' + self._category, figsize=(8.8, 4), main_window=self)
        main_window = QtWidgets.QMainWindow()
        main_window.setCentralWidget(self._timeline_figure)
        self.ui.timeline_layout.addWidget(main_window)
        main_window.addToolBar(self._timeline_figure.tool_bar)

    def _update_timeline_pane(self):
        selected = list([qitem.text() for qitem in self.ui.filter_list_widget.selectedItems()])
        filtered_events, filtered_dates = self._logbook_copy.get_filtered_event_timeline(self._category, selected)

        self._timeline_figure.render_canvas(filtered_events, filtered_dates)
