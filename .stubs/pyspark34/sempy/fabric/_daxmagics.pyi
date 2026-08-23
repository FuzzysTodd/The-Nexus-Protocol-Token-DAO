from IPython.core.interactiveshell import InteractiveShell as InteractiveShell
from IPython.core.magic import Magics

def unquote(arg) -> str | None: ...

class DAXMagics(Magics):
    def __init__(self, shell: InteractiveShell) -> None: ...
    def dax(self, line: str, cell: str):
        """
        Evaluate a DAX query and return the results as a FabricDataFrame.
        """
