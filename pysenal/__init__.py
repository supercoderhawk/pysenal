# -*- coding: utf-8 -*-

try:
    from importlib.metadata import PackageNotFoundError, version  # Python 3.8+
except Exception:  # pragma: no cover
    try:
        from importlib_metadata import PackageNotFoundError, version  # type: ignore[import-not-found]  # Python 3.6-3.7
    except Exception:  # pragma: no cover
        PackageNotFoundError = Exception

        def version(_dist_name):
            raise PackageNotFoundError


try:
    __version__ = version(__name__.split('.')[0])
except PackageNotFoundError:
    __version__ = 'unknown'

from pysenal.io import *
from pysenal.utils import *
