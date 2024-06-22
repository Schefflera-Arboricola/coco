import warnings
from importlib.metadata import entry_points


__all__ = ["_dispatchable"]


def _get_backends(group):
    items = entry_points(group=group)
    rv = {}
    for ep in items:
        if ep.name in rv:
            warnings.warn(
                f"coco backend defined more than once: {ep.name}",
                RuntimeWarning,
                stacklevel=2,
            )
        else:
            rv[ep.name] = ep
    return rv


backends = _get_backends("coco.backends")


def _dispatchable(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if hasattr(arg, "__coco_backend__"):
                backend_name = arg.__coco_backend__
                if backend_name in backends:
                    backend_entry_point = backends[backend_name]
                    backend_module = backend_entry_point.load()
                    backend_func = getattr(backend_module, func.__name__, None)
                    if backend_func:
                        print(f"Running {func.__name__} using {backend_name} backend")
                        result = backend_func(*args, **kwargs)
                        return result

        return func(*args, **kwargs)

    return wrapper
