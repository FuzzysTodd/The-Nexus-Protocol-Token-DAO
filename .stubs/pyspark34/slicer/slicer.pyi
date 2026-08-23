from .slicer_internal import Alias as Alias, AliasLookup as AliasLookup, AtomicSlicer as AtomicSlicer, Obj as Obj, Tracked as Tracked, UnifiedDataHandler as UnifiedDataHandler, reduced_o as reduced_o, resolve_dim as resolve_dim, unify_slice as unify_slice

class Slicer:
    """ Provides unified slicing to tensor-like objects. """
    def __init__(self, *args, **kwargs) -> None:
        """ Wraps objects in args and provides unified numpy-like slicing.

        Currently supports (with arbitrary nesting):

        - lists and tuples
        - dictionaries
        - numpy arrays
        - pandas dataframes and series
        - pytorch tensors

        Args:
            *args: Unnamed tensor-like objects.
            **kwargs: Named tensor-like objects.

        Examples:

            Basic anonymous slicing:

            >>> from slicer import Slicer as S
            >>> li = [[1, 2, 3], [4, 5, 6]]
            >>> S(li)[:, 0:2].o
            [[1, 2], [4, 5]]
            >>> di = {'x': [1, 2, 3], 'y': [4, 5, 6]}
            >>> S(di)[:, 0:2].o
            {'x': [1, 2], 'y': [4, 5]}

            Basic named slicing:

            >>> import pandas as pd
            >>> import numpy as np
            >>> df = pd.DataFrame({'A': [1, 3], 'B': [2, 4]})
            >>> ar = np.array([[5, 6], [7, 8]])
            >>> sliced = S(first=df, second=ar)[0, :]
            >>> sliced.first
            A    1
            B    2
            Name: 0, dtype: int64
            >>> sliced.second
            array([5, 6])

        """
    @classmethod
    def from_slicer(cls, *args, **kwargs):
        """ Alternative to SUPER SLICE
        Args:
            *args:
            **kwargs:

        Returns:

        """
    def __getitem__(self, item): ...
    def __getattr__(self, item):
        """ Override default getattr to return tracked attribute.

        Args:
            item: Name of tracked attribute.
        Returns:
            Corresponding object.
        """
    def __setattr__(self, key, value):
        """ Override default setattr to sync tracking of slicer.

        Args:
            key: Name of tracked attribute.
            value: Either an Obj, Alias or Python Object.
        """
    def __delattr__(self, item):
        """ Override default delattr to remove tracked attribute.

        Args:
            item: Name of tracked attribute to delete.
        """
