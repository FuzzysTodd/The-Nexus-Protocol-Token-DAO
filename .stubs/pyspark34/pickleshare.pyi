import collections as collections_abc
from _typeshed import Incomplete

__version__: str
string_types: Incomplete

def gethashfile(key): ...

class PickleShareDB(collections_abc.MutableMapping):
    """ The main 'connection' object for PickleShare database """
    root: Incomplete
    cache: Incomplete
    def __init__(self, root) -> None:
        """ Return a db object that will manage the specied directory"""
    def __getitem__(self, key):
        """ db['key'] reading """
    def __setitem__(self, key, value) -> None:
        """ db['key'] = 5 """
    def hset(self, hashroot, key, value) -> None:
        """ hashed set """
    def hget(self, hashroot, key, default=..., fast_only: bool = True):
        """ hashed get """
    def hdict(self, hashroot):
        """ Get all data contained in hashed category 'hashroot' as dict """
    def hcompress(self, hashroot) -> None:
        """ Compress category 'hashroot', so hset is fast again

        hget will fail if fast_only is True for compressed items (that were
        hset before hcompress).

        """
    def __delitem__(self, key) -> None:
        ''' del db["key"] '''
    def keys(self, globpat: Incomplete | None = None):
        """ All keys in DB, or all keys matching a glob"""
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def uncache(self, *items) -> None:
        """ Removes all, or specified items from cache

        Use this after reading a large amount of large objects
        to free up memory, when you won't be needing the objects
        for a while.

        """
    def waitget(self, key, maxwaittime: int = 60):
        ''' Wait (poll) for a key to get a value

        Will wait for `maxwaittime` seconds before raising a KeyError.
        The call exits normally if the `key` field in db gets a value
        within the timeout period.

        Use this for synchronizing different processes or for ensuring
        that an unfortunately timed "db[\'key\'] = newvalue" operation
        in another process (which causes all \'get\' operation to cause a
        KeyError for the duration of pickling) won\'t screw up your program
        logic.
        '''
    def getlink(self, folder):
        """ Get a convenient link for accessing items  """

class PickleShareLink:
    """ A shortdand for accessing nested PickleShare data conveniently.

    Created through PickleShareDB.getlink(), example::

        lnk = db.getlink('myobjects/test')
        lnk.foo = 2
        lnk.bar = lnk.foo + 5

    """
    def __init__(self, db, keydir) -> None: ...
    def __getattr__(self, key): ...
    def __setattr__(self, key, val) -> None: ...

def main() -> None: ...
