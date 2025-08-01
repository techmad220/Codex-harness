import importlib
import logging
import pkgutil

logger = logging.getLogger(__name__)


def load_plugins():
    """Load available plugin modules.

    Returns a dict mapping plugin names to loaded modules. Any plugin that
    fails to import will be skipped and a warning will be logged.
    """
    loaded = {}
    for finder, name, ispkg in pkgutil.iter_modules(__path__):
        full_name = f"{__name__}.{name}"
        try:
            module = importlib.import_module(full_name)
        except Exception as exc:  # catch broad because dependency issues vary
            logger.warning("Failed to load plugin %s: %s", name, exc)
            continue
        loaded[name] = module
    return loaded


__all__ = ["load_plugins"]
