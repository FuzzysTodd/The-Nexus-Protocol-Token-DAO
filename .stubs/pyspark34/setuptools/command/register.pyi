import distutils.command.register as orig
from setuptools.errors import RemovedCommandError as RemovedCommandError

class register(orig.register):
    """Formerly used to register packages on PyPI."""
    def run(self) -> None: ...
