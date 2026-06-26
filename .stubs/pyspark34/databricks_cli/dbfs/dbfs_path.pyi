from _typeshed import Incomplete
from click import ParamType
from databricks_cli.utils import error_and_quit as error_and_quit

class DbfsPath:
    absolute_path: Incomplete
    def __init__(self, absolute_path, validate: bool = True) -> None: ...
    @classmethod
    def from_api_path(cls, path): ...
    @classmethod
    def is_valid(cls, path): ...
    def validate(self) -> None:
        '''
        Checks that the path is a proper DbfsPath. it must have a prefix of
        "dbfs:" and must be an absolute path.
        '''
    def join(self, file_name):
        """
        Returns a new extended DBFS path with a file_name.
        :param: file_name
        :type: str
        :rtype: DbfsPath
        """
    def relpath(self, dbfs_path_prefix):
        """
        Strips the prefix of this DbfsPath. Behaves very similar to os.path.relpath
        """
    @property
    def basename(self):
        """
        This function is like the basename utility and is unlike os.path.basename.
        >>> assert DbfsPath('dbfs:/').basename == ''
        >>> assert DbfsPath('dbfs:/test').basename == 'test'
        >>> assert DbfsPath('dbfs:/test/').basename == 'test'
        """
    @property
    def is_absolute_path(self): ...
    @property
    def is_root(self): ...
    def __eq__(self, other): ...

class DbfsPathClickType(ParamType):
    name: str
    def convert(self, value, param, ctx): ...
