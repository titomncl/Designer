import sd


def test():
    print("Hello World!")

def get_app():
    context = sd.getContext()
    return context.getSDApplication()

def get_package():
    app = get_app()
    package = app.getPackageMgr().getPackages().getItem(0)

    return package


def get_main_window():
    app = get_app()
    ui_mgr = app.getUIMgr()

    qt_wrapper = sd.api.qtforpythonuimgrwrapper.QtForPythonUIMgrWrapper(ui_mgr)
    main_window = qt_wrapper.getMainWindow()


def get_filepath(package):
    return package.getFilePath()

def save_as(package, filepath):
    app = get_app()
    app.getPackageMgr().savePackageAs(package, filepath)
