import abc

class AbstractBaseFormat(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def supported(fn): ...
    @staticmethod
    @abc.abstractmethod
    def extract(fn, dest_dir, **kw): ...
    @staticmethod
    @abc.abstractmethod
    def create(prefix, file_list, out_fn, out_folder=..., **kw): ...
    @staticmethod
    @abc.abstractmethod
    def get_pkg_details(in_file): ...
