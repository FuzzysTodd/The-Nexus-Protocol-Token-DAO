__all__ = ['SparkFiles']

class SparkFiles:
    """
    Resolves paths to files added through :meth:`SparkContext.addFile`.

    SparkFiles contains only classmethods; users should not create SparkFiles
    instances.
    """
    def __init__(self) -> None: ...
    @classmethod
    def get(cls, filename: str) -> str:
        '''
        Get the absolute path of a file added through
        :meth:`SparkContext.addFile` or :meth:`SparkContext.addPyFile`.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        filename : str
            file that are added to resources

        Returns
        -------
        str
            the absolute path of the file

        See Also
        --------
        :meth:`SparkFiles.getRootDirectory`
        :meth:`SparkContext.addFile`
        :meth:`SparkContext.addPyFile`
        :meth:`SparkContext.listFiles`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> from pyspark import SparkFiles

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path1 = os.path.join(d, "test.txt")
        ...     with open(path1, "w") as f:
        ...         _ = f.write("100")
        ...
        ...     sc.addFile(path1)
        ...     file_list1 = sorted(sc.listFiles)
        ...
        ...     def func1(iterator):
        ...         path = SparkFiles.get("test.txt")
        ...         assert path.startswith(SparkFiles.getRootDirectory())
        ...         return [path]
        ...
        ...     path_list1 = sc.parallelize([1, 2, 3, 4]).mapPartitions(func1).collect()
        ...
        ...     path2 = os.path.join(d, "test.py")
        ...     with open(path2, "w") as f:
        ...         _ = f.write("import pyspark")
        ...
        ...     # py files
        ...     sc.addPyFile(path2)
        ...     file_list2 = sorted(sc.listFiles)
        ...
        ...     def func2(iterator):
        ...         path = SparkFiles.get("test.py")
        ...         assert path.startswith(SparkFiles.getRootDirectory())
        ...         return [path]
        ...
        ...     path_list2 = sc.parallelize([1, 2, 3, 4]).mapPartitions(func2).collect()
        >>> file_list1
        [\'file:/.../test.txt\']
        >>> set(path_list1)
        {\'.../test.txt\'}
        >>> file_list2
        [\'file:/.../test.py\', \'file:/.../test.txt\']
        >>> set(path_list2)
        {\'.../test.py\'}
        '''
    @classmethod
    def getRootDirectory(cls) -> str:
        """
        Get the root directory that contains files added through
        :meth:`SparkContext.addFile` or :meth:`SparkContext.addPyFile`.

        .. versionadded:: 0.7.0

        Returns
        -------
        str
            the root directory that contains files added to resources

        See Also
        --------
        :meth:`SparkFiles.get`
        :meth:`SparkContext.addFile`
        :meth:`SparkContext.addPyFile`

        Examples
        --------
        >>> from pyspark.files import SparkFiles
        >>> SparkFiles.getRootDirectory()  # doctest: +SKIP
        '.../spark-a904728e-08d3-400c-a872-cfd82fd6dcd2/userFiles-648cf6d6-bb2c-4f53-82bd-e658aba0c5de'
        """
