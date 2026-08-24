from _typeshed import Incomplete

class Map:
    pool: Incomplete
    args: Incomplete
    kwds: Incomplete
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''map instance with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, a builtins.map will be
        used with the returned iterator cast to a list.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's map

    Args:
        func: function object to map
        *args: positional arguments for map
        **kwds: keyword arguments for map

    Returns:
        results from execution of ``map(func, *args, **kwds)``

    NOTE: initializes a new worker pool with each call
        """
    def __cls__(self): ...
    def __meth__(self): ...
    def __attr__(self): ...
    __self__: Incomplete
    __func__: Incomplete
    __get__: Incomplete
    def close(self) -> None:
        """close the map to any new jobs"""
    def join(self) -> None:
        """reclaim the closed workers"""
    def clear(self) -> None:
        """remove pool singleton, if exists"""
    def __del__(self) -> None:
        """shutdown the worker pool and tidy up
        """

class Smap(Map):
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''starmap instance with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, an itertools.starmap will
        be used with the returned iterator cast to a list.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's starmap

    Args:
        func: function object to map
        *args: positional arguments for starmap
        **kwds: keyword arguments for starmap

    Returns:
        results from execution of ``starmap(func, *args, **kwds)``

    NOTE: initializes a new worker pool with each call
        """

class Imap(Map):
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''map iterator with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, a builtins.map will be
        used.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's map iterator

    Args:
        func: function object to map
        *args: positional arguments for map iterator
        **kwds: keyword arguments for map iterator

    Returns:
        results from execution of ``map(func, *args, **kwds)`` iterator

    NOTE: initializes a new worker pool with each call
        """

class Amap(Map):
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''async map instance with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, NotImplemented is returned
        upon use.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's async map

    Args:
        func: function object to map
        *args: positional arguments for async map
        **kwds: keyword arguments for async map

    Returns:
        results from execution of async ``map(func, *args, **kwds)``

    NOTE: initializes a new worker pool with each call
        """

class Asmap(Map):
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''async starmap instance with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, NotImplemented is returned
        upon use.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's async starmap

    Args:
        func: function object to map
        *args: positional arguments for async starmap
        **kwds: keyword arguments for async starmap

    Returns:
        results from execution of async ``starmap(func, *args, **kwds)``

    NOTE: initializes a new worker pool with each call
        """

class Uimap(Map):
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''unordered map iterator with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, NotImplemented is returned
        upon use.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's unordered map iterator

    Args:
        func: function object to map
        *args: positional arguments for unordered map iterator
        **kwds: keyword arguments for unordered map iterator

    Returns:
        results from execution of unordered ``map(func, *args, **kwds)`` iterator

    NOTE: initializes a new worker pool with each call
        """

class Ismap(Map):
    def __init__(self, pool: Incomplete | None = None, *args, **kwds) -> None:
        '''starmap iterator with internal lazy pool instantiation

    Args:
        pool: pool object (i.e. pathos.pools.ProcessPool)
        *args: positional arguments for pool initialization
        **kwds: keyword arguments for pool initialization
        close: if True, close the pool to any new jobs [Default: False] 
        join: if True, reclaim the pool\'s closed workers [Default: False]
        clear: if True, delete the pool singleton [Default: False]

    NOTE: if a pool object is not provided, an itertools.starmap will
        be used.
    NOTE: pools from both multiprocess and pathos.pools can be used,
        however the behavior is slightly different. Pools from both
        pathos and multiprocess have close and join methods, to close
        the pool to new jobs, and to shut down the pool\'s workers.
        Pools from pathos, however, are launched as singletons, so
        they also include a clear method that deletes the singleton.
        In either case, a pool that has been "closed" will throw a
        ValueError if map is then called, and similarly, a ValueError
        will be thrown if join is called before a pool is "closed".
        The major difference is that if a pathos.pool is closed, the
        map instance cannot run new jobs until "clear" is called,
        while a new multiprocess pool will be created each time the
        map is executed. This leads to pathos.pools generally being
        called with either ``clear=True`` or ``clear=False``, and pools
        from multprocess either using ``close=True`` or ``join=True`` or
        both. Some hierarchical parallel workflows are not allowed,
        and will result in an error being thrown; however, changing
        close, join, or clear can often remove the error.
        '''
    def __call__(self, func, *args, **kwds):
        """instantiate a pool and execute the pool's starmap iterator

    Args:
        func: function object to map
        *args: positional arguments for starmap iterator
        **kwds: keyword arguments for starmap iterator

    Returns:
        results from execution of ``starmap(func, *args, **kwds)`` iterator

    NOTE: initializes a new worker pool with each call
        """
