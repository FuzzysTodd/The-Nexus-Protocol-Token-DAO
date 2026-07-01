class _SparkDirectoryDistributor:
    """Distribute spark directory from driver to executors."""
    def __init__(self) -> None: ...
    @staticmethod
    def add_dir(spark, dir_path):
        '''Given a SparkSession and a model_path which refers to a pyfunc directory locally,
        we will zip the directory up, enable it to be distributed to executors, and return
        the "archive_path", which should be used as the path in get_or_load().
        '''
    @staticmethod
    def get_or_extract(archive_path):
        """Given a path returned by add_local_model(), this method will return a tuple of
        (loaded_model, local_model_path).
        If this Python process ever loaded the model before, we will reuse that copy.
        """
