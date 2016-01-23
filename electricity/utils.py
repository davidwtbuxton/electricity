import contextlib

import six


@contextlib.contextmanager
def open_filename(*args, **kwargs):
    """A context manager for open(..) for a filename OR a file-like object."""
    if isinstance(args[0], six.string_types):
        with open(*args, **kwargs) as fh:
            yield fh
    else:
        yield args[0]

        if kwargs.get('closing', False):
            args[0].close()
