from distutils.command import upload as orig
from setuptools.errors import RemovedCommandError as RemovedCommandError

class upload(orig.upload):
    """Formerly used to upload packages to PyPI."""
    def run(self) -> None: ...
