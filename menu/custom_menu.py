from PySide2 import QtWidgets as Qw


class CustomMenu(object):
    def __init__(self, ui, title, menu_object_name):
        """

        Args:
            ui (PySide2.QtWidgets.QMainWindow): substance painter main window
            title (str): Title seen in the UI
            menu_object_name (str): Name of the object in the code
        """

        self.menu = ui.newMenu(menuTitle=title, objectName=menu_object_name)

    def add_actions(self, title, action):
        act = Qw.QAction(title, self.menu)
        act.triggered.connect(action)

        self.menu.addAction(act)

    def add_separator(self):
        self.menu.addSeparator()
