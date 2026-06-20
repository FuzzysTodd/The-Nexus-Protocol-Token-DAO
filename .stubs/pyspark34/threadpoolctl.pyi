import abc
import ctypes
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from contextlib import ContextDecorator

__all__ = ['threadpool_limits', 'threadpool_info', 'ThreadpoolController', 'LibController', 'register']

class _dl_phdr_info(ctypes.Structure): ...

class LibController(ABC, metaclass=abc.ABCMeta):
    '''Abstract base class for the individual library controllers

    A library controller must expose the following class attributes:
        - user_api : str
            Usually the name of the library or generic specification the library
            implements, e.g. "blas" is a specification with different implementations.
        - internal_api : str
            Usually the name of the library or concrete implementation of some
            specification, e.g. "openblas" is an implementation of the "blas"
            specification.
        - filename_prefixes : tuple
            Possible prefixes of the shared library\'s filename that allow to
            identify the library. e.g. "libopenblas" for libopenblas.so.

    and implement the following methods: `get_num_threads`, `set_num_threads` and
    `get_version`.

    Threadpoolctl loops through all the loaded shared libraries and tries to match
    the filename of each library with the `filename_prefixes`. If a match is found, a
    controller is instantiated and a handler to the library is stored in the `dynlib`
    attribute as a `ctypes.CDLL` object. It can be used to access the necessary symbols
    of the shared library to implement the above methods.

    The following information will be exposed in the info dictionary:
      - user_api : standardized API, if any, or a copy of internal_api.
      - internal_api : implementation-specific API.
      - num_threads : the current thread limit.
      - prefix : prefix of the shared library\'s filename.
      - filepath : path to the loaded shared library.
      - version : version of the library (if available).

    In addition, each library controller may expose internal API specific entries. They
    must be set as attributes in the `set_additional_attributes` method.
    '''
    prefix: Incomplete
    filepath: Incomplete
    dynlib: Incomplete
    version: Incomplete
    def __init__(self, *, filepath: Incomplete | None = None, prefix: Incomplete | None = None) -> None:
        """This is not meant to be overriden by subclasses."""
    def info(self):
        """Return relevant info wrapped in a dict

        This is not meant to be overriden by subclasses.
        """
    def set_additional_attributes(self) -> None:
        """Set additional attributes meant to be exposed in the info dict"""
    @property
    def num_threads(self):
        """Exposes the current thread limit as a dynamic property

        This is not meant to be used or overriden by subclasses.
        """
    @abstractmethod
    def get_num_threads(self):
        """Return the maximum number of threads available to use"""
    @abstractmethod
    def set_num_threads(self, num_threads):
        """Set the maximum number of threads to use"""
    @abstractmethod
    def get_version(self):
        """Return the version of the shared library"""

class OpenBLASController(LibController):
    """Controller class for OpenBLAS"""
    user_api: str
    internal_api: str
    filename_prefixes: Incomplete
    check_symbols: Incomplete
    threading_layer: Incomplete
    architecture: Incomplete
    def set_additional_attributes(self) -> None: ...
    def get_num_threads(self): ...
    def set_num_threads(self, num_threads): ...
    def get_version(self): ...

class BLISController(LibController):
    """Controller class for BLIS"""
    user_api: str
    internal_api: str
    filename_prefixes: Incomplete
    check_symbols: Incomplete
    threading_layer: Incomplete
    architecture: Incomplete
    def set_additional_attributes(self) -> None: ...
    def get_num_threads(self): ...
    def set_num_threads(self, num_threads): ...
    def get_version(self): ...

class MKLController(LibController):
    """Controller class for MKL"""
    user_api: str
    internal_api: str
    filename_prefixes: Incomplete
    check_symbols: Incomplete
    threading_layer: Incomplete
    def set_additional_attributes(self) -> None: ...
    def get_num_threads(self): ...
    def set_num_threads(self, num_threads): ...
    def get_version(self): ...

class OpenMPController(LibController):
    """Controller class for OpenMP"""
    user_api: str
    internal_api: str
    filename_prefixes: Incomplete
    def get_num_threads(self): ...
    def set_num_threads(self, num_threads): ...
    def get_version(self) -> None: ...

def register(controller) -> None:
    """Register a new controller"""
def threadpool_info():
    '''Return the maximal number of threads for each detected library.

    Return a list with all the supported libraries that have been found. Each
    library is represented by a dict with the following information:

      - "user_api" : user API. Possible values are {USER_APIS}.
      - "internal_api": internal API. Possible values are {INTERNAL_APIS}.
      - "prefix" : filename prefix of the specific implementation.
      - "filepath": path to the loaded library.
      - "version": version of the library (if available).
      - "num_threads": the current thread limit.

    In addition, each library may contain internal_api specific entries.
    '''

class _ThreadpoolLimiter:
    """The guts of ThreadpoolController.limit

    Refer to the docstring of ThreadpoolController.limit for more details.

    It will only act on the library controllers held by the provided `controller`.
    Using the default constructor sets the limits right away such that it can be used as
    a callable. Setting the limits can be delayed by using the `wrap` class method such
    that it can be used as a decorator.
    """
    def __init__(self, controller, *, limits: Incomplete | None = None, user_api: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    @classmethod
    def wrap(cls, controller, *, limits: Incomplete | None = None, user_api: Incomplete | None = None):
        """Return an instance of this class that can be used as a decorator"""
    def restore_original_limits(self) -> None:
        """Set the limits back to their original values"""
    unregister = restore_original_limits
    def get_original_num_threads(self):
        """Original num_threads from before calling threadpool_limits

        Return a dict `{user_api: num_threads}`.
        """

class _ThreadpoolLimiterDecorator(_ThreadpoolLimiter, ContextDecorator):
    """Same as _ThreadpoolLimiter but to be used as a decorator"""
    def __init__(self, controller, *, limits: Incomplete | None = None, user_api: Incomplete | None = None) -> None: ...
    def __enter__(self): ...

class threadpool_limits(_ThreadpoolLimiter):
    '''Change the maximal number of threads that can be used in thread pools.

    This object can be used either as a callable (the construction of this object
    limits the number of threads), as a context manager in a `with` block to
    automatically restore the original state of the controlled libraries when exiting
    the block, or as a decorator through its `wrap` method.

    Set the maximal number of threads that can be used in thread pools used in
    the supported libraries to `limit`. This function works for libraries that
    are already loaded in the interpreter and can be changed dynamically.

    This effect is global and impacts the whole Python process. There is no thread level
    isolation as these libraries do not offer thread-local APIs to configure the number
    of threads to use in nested parallel calls.

    Parameters
    ----------
    limits : int, dict, \'sequential_blas_under_openmp\' or None (default=None)
        The maximal number of threads that can be used in thread pools

        - If int, sets the maximum number of threads to `limits` for each
          library selected by `user_api`.

        - If it is a dictionary `{{key: max_threads}}`, this function sets a
          custom maximum number of threads for each `key` which can be either a
          `user_api` or a `prefix` for a specific library.

        - If \'sequential_blas_under_openmp\', it will chose the appropriate `limits`
          and `user_api` parameters for the specific use case of sequential BLAS
          calls within an OpenMP parallel region. The `user_api` parameter is
          ignored.

        - If None, this function does not do anything.

    user_api : {USER_APIS} or None (default=None)
        APIs of libraries to limit. Used only if `limits` is an int.

        - If "blas", it will only limit BLAS supported libraries ({BLAS_LIBS}).

        - If "openmp", it will only limit OpenMP supported libraries
          ({OPENMP_LIBS}). Note that it can affect the number of threads used
          by the BLAS libraries if they rely on OpenMP.

        - If None, this function will apply to all supported libraries.
    '''
    def __init__(self, limits: Incomplete | None = None, user_api: Incomplete | None = None) -> None: ...
    @classmethod
    def wrap(cls, limits: Incomplete | None = None, user_api: Incomplete | None = None): ...

class ThreadpoolController:
    """Collection of LibController objects for all loaded supported libraries

    Attributes
    ----------
    lib_controllers : list of `LibController` objects
        The list of library controllers of all loaded supported libraries.
    """
    lib_controllers: Incomplete
    def __init__(self) -> None: ...
    def info(self):
        """Return lib_controllers info as a list of dicts"""
    def select(self, **kwargs):
        '''Return a ThreadpoolController containing a subset of its current
        library controllers

        It will select all libraries matching at least one pair (key, value) from kwargs
        where key is an entry of the library info dict (like "user_api", "internal_api",
        "prefix", ...) and value is the value or a list of acceptable values for that
        entry.

        For instance, `ThreadpoolController().select(internal_api=["blis", "openblas"])`
        will select all library controllers whose internal_api is either "blis" or
        "openblas".
        '''
    def limit(self, *, limits: Incomplete | None = None, user_api: Incomplete | None = None):
        '''Change the maximal number of threads that can be used in thread pools.

        This function returns an object that can be used either as a callable (the
        construction of this object limits the number of threads) or as a context
        manager, in a `with` block to automatically restore the original state of the
        controlled libraries when exiting the block.

        Set the maximal number of threads that can be used in thread pools used in
        the supported libraries to `limits`. This function works for libraries that
        are already loaded in the interpreter and can be changed dynamically.

        This effect is global and impacts the whole Python process. There is no thread
        level isolation as these libraries do not offer thread-local APIs to configure
        the number of threads to use in nested parallel calls.

        Parameters
        ----------
        limits : int, dict, \'sequential_blas_under_openmp\' or None (default=None)
            The maximal number of threads that can be used in thread pools

            - If int, sets the maximum number of threads to `limits` for each
              library selected by `user_api`.

            - If it is a dictionary `{{key: max_threads}}`, this function sets a
              custom maximum number of threads for each `key` which can be either a
              `user_api` or a `prefix` for a specific library.

            - If \'sequential_blas_under_openmp\', it will chose the appropriate `limits`
              and `user_api` parameters for the specific use case of sequential BLAS
              calls within an OpenMP parallel region. The `user_api` parameter is
              ignored.

            - If None, this function does not do anything.

        user_api : {USER_APIS} or None (default=None)
            APIs of libraries to limit. Used only if `limits` is an int.

            - If "blas", it will only limit BLAS supported libraries ({BLAS_LIBS}).

            - If "openmp", it will only limit OpenMP supported libraries
              ({OPENMP_LIBS}). Note that it can affect the number of threads used
              by the BLAS libraries if they rely on OpenMP.

            - If None, this function will apply to all supported libraries.
        '''
    def wrap(self, *, limits: Incomplete | None = None, user_api: Incomplete | None = None):
        '''Change the maximal number of threads that can be used in thread pools.

        This function returns an object that can be used as a decorator.

        Set the maximal number of threads that can be used in thread pools used in
        the supported libraries to `limits`. This function works for libraries that
        are already loaded in the interpreter and can be changed dynamically.

        Parameters
        ----------
        limits : int, dict or None (default=None)
            The maximal number of threads that can be used in thread pools

            - If int, sets the maximum number of threads to `limits` for each
              library selected by `user_api`.

            - If it is a dictionary `{{key: max_threads}}`, this function sets a
              custom maximum number of threads for each `key` which can be either a
              `user_api` or a `prefix` for a specific library.

            - If None, this function does not do anything.

        user_api : {USER_APIS} or None (default=None)
            APIs of libraries to limit. Used only if `limits` is an int.

            - If "blas", it will only limit BLAS supported libraries ({BLAS_LIBS}).

            - If "openmp", it will only limit OpenMP supported libraries
              ({OPENMP_LIBS}). Note that it can affect the number of threads used
              by the BLAS libraries if they rely on OpenMP.

            - If None, this function will apply to all supported libraries.
        '''
    def __len__(self) -> int: ...
