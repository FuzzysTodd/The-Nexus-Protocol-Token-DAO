from IPython.core.error import UsageError as UsageError
from IPython.core.magic import Magics as Magics, line_magic as line_magic, magics_class as magics_class
from IPython.testing.skipdoctest import skip_doctest as skip_doctest
from _typeshed import Incomplete

def restore_aliases(ip, alias: Incomplete | None = None) -> None: ...
def refresh_variables(ip) -> None: ...
def restore_dhist(ip) -> None: ...
def restore_data(ip) -> None: ...

class StoreMagics(Magics):
    """Lightweight persistence for python variables.

    Provides the %store magic."""
    autorestore: Incomplete
    def __init__(self, shell) -> None: ...
    def store(self, parameter_s: str = '') -> None:
        """Lightweight persistence for python variables.

        Example::

          In [1]: l = ['hello',10,'world']
          In [2]: %store l
          Stored 'l' (list)
          In [3]: exit

          (IPython session is closed and started again...)

          ville@badger:~$ ipython
          In [1]: l
          NameError: name 'l' is not defined
          In [2]: %store -r
          In [3]: l
          Out[3]: ['hello', 10, 'world']

        Usage:

        * ``%store``          - Show list of all variables and their current
                                values
        * ``%store spam bar`` - Store the *current* value of the variables spam
                                and bar to disk
        * ``%store -d spam``  - Remove the variable and its value from storage
        * ``%store -z``       - Remove all variables from storage
        * ``%store -r``       - Refresh all variables, aliases and directory history
                                from store (overwrite current vals)
        * ``%store -r spam bar`` - Refresh specified variables and aliases from store
                                   (delete current val)
        * ``%store foo >a.txt``  - Store value of foo to new file a.txt
        * ``%store foo >>a.txt`` - Append value of foo to file a.txt

        It should be noted that if you change the value of a variable, you
        need to %store it again if you want to persist the new value.

        Note also that the variables will need to be pickleable; most basic
        python types can be safely %store'd.

        Also aliases can be %store'd across sessions.
        To remove an alias from the storage, use the %unalias magic.
        """

def load_ipython_extension(ip) -> None:
    """Load the extension in IPython."""
