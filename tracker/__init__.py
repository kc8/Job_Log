from configparser import ConfigParser as _ConfigParser


# Version of package
__version__ = "0.1"

# Read URL of feed from config file
"""
_cfg = _ConfigParser()
with _resources.path("reader", "config.cfg") as _path:
    _cfg.read(str(_path))
URL = _cfg.get("feed", "url")
"""