from Designer.designer.save_file.source import core


class Controller(object):

    def __init__(self, ui, parent=None):

        self.filepath = core.filepath()

        self.ui = ui(self, parent)

        self.first_save_or_not()

        self.asset_type = "CHARA"
        self.asset_name = ""
        self.dpt = "SHD"

        self.chara_btn = self.ui.chara_btn
        self.props_btn = self.ui.props_btn
        self.save_btn = self.ui.save_btn
        self.close_btn = self.ui.close_btn

        self.library_box = self.ui.library_combobox
        self.get_asset(self.asset_type)
        self.update_asset_name()

        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)

        self.init_btn_connections()

    def first_save_or_not(self):
        if not self.filepath:
            self.show()
        else:
            self.filepath = core.save(self.filepath)

    def show(self):
        self.ui.show()

    def save_file(self):

        choice, save_choice = self.ui.message_box()
        if choice == save_choice:
            self.filepath = core.first_save(self.asset_type, self.asset_name, self.dpt)

            self.ui.close()

    def init_btn_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)

        self.library_box.currentTextChanged.connect(self.update_asset_name)

        self.save_btn.clicked.connect(self.save_file)
        self.close_btn.clicked.connect(self.close_action)

    def chara_action(self):
        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.asset_type = "CHARA"
        self.get_asset(self.asset_type)

    def props_action(self):
        self.props_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.asset_type = "PROPS"
        self.get_asset(self.asset_type)

    def get_asset(self, asset_type):
        assets = core.find_assets(asset_type)
        if assets:
            assets.sort()

            self.library_box.clear()
            self.library_box.addItems(assets)

    def update_asset_name(self):
        self.asset_name = self.library_box.currentText()

    def close_action(self):
        self.ui.close()
