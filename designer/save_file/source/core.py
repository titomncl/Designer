import os

from CommonTools.concat import concat

from Designer.designer.globals import PFE_PATH
from Designer.designer.common_ import get_package, get_filepath, save_as

def filepath():
    try:
        package = get_package()
        filepath = get_filepath(package)
        return filepath
    except RuntimeError:
        return None

def save(filepath):

    path, filename = os.path.split(filepath)

    files = os.listdir(path)

    if "desktop.ini" in files:
        files.remove("desktop.ini")

    files.sort()

    last_file, _ = os.path.splitext(files[-1])

    new_filename = next_version(last_file)

    new_filepath = concat(path, new_filename + ".sbs", separator="/")

    save_as(get_package(), new_filepath)

    return new_filepath


def next_version(file_):
    """
    Get the next version from the given file
    Args:
        file_:

    Raises:
        ValueError: if the filename is not correct

    Returns:
        str: file with last version

    """
    splited_file = file_.rsplit("_", 1)
    name_file = splited_file[0]
    version = splited_file[-1]
    padding = len(version)

    if version.isdigit():
        next_version = int(version) + 1
        next_version = str(next_version).zfill(padding)

        return concat(name_file, next_version, separator="_")
    else:
        e = concat(file_, " is incorrect.")
        raise ValueError(e)


# def publish(filepath):
#     path, name = os.path.split(filepath)
#
#     publish_path = path.rsplit("/", 1)[0]
#     publish_path = concat(publish_path, "PUBLISH", separator="/")
#
#     name, ext = os.path.splitext(name)
#     publish_name = name.rsplit("_", 1)[0] + ext
#
#     publish = concat(publish_path, publish_name, separator="/")
#
#     copyfile(filepath, publish)


def first_save(type, name, task):
    """

    Args:
        type (str): chara, props, set
        name (str): name of the asset
        task (str): departement of the file: MOD, RIG, SHD, ANIM

    Returns:
        str, str: versionned and published filepath

    """
    filename = concat(name, task, "001.sbs", separator="_")
    filepath = concat(PFE_PATH, "DATA/LIB", type, name, task, "SCENE/OLD", filename, separator="/")

    save_as(get_package(), filepath)

    return filepath

def find_assets(type_):
    """

    Args:
        project (str):
        type_ (str): CHARACTER, PROPS, MODULE folder

    Returns:
        list(str): assets found in the folder

    """
    path = concat(PFE_PATH, "DATA/LIB", type_, separator="\\")

    assets = next(os.walk(path))[1]

    return assets
