from _typeshed import Incomplete
from os.path import basename as basename
from unittest import case as case, loader

class TestLoader(loader.TestLoader):
    def __init__(self, topleveldir: Incomplete | None = None) -> None: ...
