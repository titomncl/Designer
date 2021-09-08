from Designer.common_ import qt_instance
from Designer.menu.custom_menu import CustomMenu

from Designer.save_load import save, load
from Designer.publish import publish


def save_action():
    save.main()


def load_action():
    load.main()


def publish_action():
    publish.save_and_publish()


def initializeSDPlugin():
    menu()


def uninitializeSDPlugin():
    pass


def menu():

    menu_ = CustomMenu(qt_instance(), "VSPA_TOOLS", "vspa.menu")
    menu_.add_actions("Save", save_action)
    menu_.add_actions("Load", load_action)
    menu_.add_separator()
    menu_.add_actions("Publish", publish_action)
