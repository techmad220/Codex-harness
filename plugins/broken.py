import importlib

# This plugin depends on a package that does not exist. Importing it will
# raise ModuleNotFoundError which should be gracefully handled by the loader.
importlib.import_module('nonexistent_dependency')
