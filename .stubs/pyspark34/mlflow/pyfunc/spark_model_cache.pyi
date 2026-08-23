class SparkModelCache:
    """Caches models in memory on Spark Executors, to avoid continually reloading from disk.

    This class has to be part of a different module than the one that _uses_ it. This is
    because Spark will pickle classes that are defined in the local scope, but relies on
    Python's module loading behavior for classes in different modules. In this case, we
    are relying on the fact that Python will load a module at-most-once, and can therefore
    store per-process state in a static map.
    """
    def __init__(self) -> None: ...
    @staticmethod
    def add_local_model(spark, model_path):
        '''Given a SparkSession and a model_path which refers to a pyfunc directory locally,
        we will zip the directory up, enable it to be distributed to executors, and return
        the "archive_path", which should be used as the path in get_or_load().
        '''
    @staticmethod
    def get_or_load(archive_path):
        """Given a path returned by add_local_model(), this method will return a tuple of
        (loaded_model, local_model_path).
        If this Python process ever loaded the model before, we will reuse that copy.
        """
