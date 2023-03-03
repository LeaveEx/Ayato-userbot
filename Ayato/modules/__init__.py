import glob
from os.path import basename, dirname, isfile

from config import *
from Ayato import *
from Ayato.helpers import *
from Ayato.helpers.SQL import *
from Ayato.resources import *
from Ayato.utils import *


def __list_all_modules():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")

    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
