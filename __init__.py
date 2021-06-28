from Designer.designer import save
from Designer.designer import common_

from functools import partial
import weakref

from PySide2 import QtWidgets as Qw
# from PySide2 import QtCore as Qc
#
#
# def on_new_graph_view_created(ui_mgr):
#
#     main_window = ui_mgr.getMainWindow()
#     children = main_window.children()
#
#     print(main_window.findChildren(Qc.QObject, "Open..."))
#     # for i, child in enumerate(children):
#     #     try:
#     #         print(i, child.text(), 123456)
#     #     except AttributeError:
#     #         pass
#
#
#
# def initializeSDPlugin():
#     app = common_.get_app()
#     ui_mgr = app.getQtForPythonUIMgr()
#
#     if ui_mgr:
#         on_new_graph_view_created(ui_mgr=ui_mgr)
#
#
# def uninitializeSDPlugin():
#     app = common_.get_app()
#     ui_mgr = app.getQtForPythonUIMgr()
#
#     if ui_mgr:
#         # ui_mgr.unregisterCallback(graph_view_created_callback_id)
#         pass


class VspaTools(Qw.QToolBar):
    __toolbar_list = {}

    def __init__(self, graph_view_id, ui_mgr):
        Qw.QToolBar.__init__(self, parent=ui_mgr.getMainWindow())

        self.__graph_view_id = graph_view_id
        self.__ui_mgr = ui_mgr

        self.save_file()
        self.publish_file()

        self.__toolbar_list[graph_view_id] = weakref.ref(self)
        self.destroyed.connect(partial(VspaTools.__on_toolbar_deleted, graph_view_id=graph_view_id))

    def save_file(self):
        action = self.addAction("Save_File")
        action.setToolTip(self.tr("Save the graph."))
        action.triggered.connect(save)

    def publish_file(self):
        action = self.addAction("Publish_File")
        action.setToolTip(self.tr("Save the graph."))
        action.triggered.connect(save)

    @classmethod
    def __on_toolbar_deleted(cls, graph_view_id):
        del cls.__toolbar_list[graph_view_id]

    @classmethod
    def remove_all_toolbars(cls):
        for toolbar in cls.__toolbar_list.values():
            if toolbar():
                toolbar().deleteLater()


def on_new_graph_view_created(graph_view_id, ui_mgr):
    toolbar = VspaTools(graph_view_id, ui_mgr)

    ui_mgr.addToolbarToGraphView(graph_view_id, toolbar)


graph_view_created_callback_id = 0

def initializeSDPlugin():
    app = common_.get_app()
    ui_mgr = app.getQtForPythonUIMgr()

    if ui_mgr:
        global graph_view_created_callback_id
        graph_view = partial(on_new_graph_view_created, ui_mgr=ui_mgr)
        graph_view_created_callback_id = ui_mgr.registerGraphViewCreatedCallback(graph_view)


def uninitializeSDPlugin():
    app = common_.get_app()
    ui_mgr = app.getQtForPythonUIMgr()

    if ui_mgr:
        global graph_view_created_callback_id
        ui_mgr.unregisterCallback(graph_view_created_callback_id)
