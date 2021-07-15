from CommonTools.save_load.controller import Controller

from Designer.save_load.save_load import SaveLoad
from Designer.common_ import main_window


def main():
    save_load = SaveLoad()
    if save_load.filepath:
        save_load.save()
    else:
        instance = Controller(save_load.save, "Save", main_window(),
                              SaveLoad().root, SaveLoad().project, SaveLoad().buttons)
