import sd


def test():
    print("Hello World!")


def app():
        return sd.getContext().getSDApplication()


def package():
    return app().getPackageMgr().getPackages().getItem(0)


def qt_instance():
    return app().getQtForPythonUIMgr()


def main_window():
    return qt_instance().getMainWindow()


def get_filepath():
    return package().getFilePath()


def save_as(filepath_):
    print(123)
    app().getPackageMgr().savePackageAs(package(), filepath_)


def open_file(filepath_):
    app().getPackageMgr().loadUserPackage(filepath_)
