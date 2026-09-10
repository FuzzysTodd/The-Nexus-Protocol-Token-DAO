from pyspark.ml.util import JavaMLReadable as JavaMLReadable, JavaMLReader, MLReadable

basestring = str

def from_java(java_stage, stage_name):
    """
    Given a Java object, create and return a Python wrapper of it.
    Used for ML persistence.
    Meta-algorithms such as Pipeline should override this method as a classmethod.

    Args:
        java_stage (str):
        stage_name (str):

    Returns:
        object: The python wrapper
    """

class JavaMMLReadable(MLReadable):
    """
    (Private) Mixin for instances that provide JavaMLReader.
    """
    @classmethod
    def read(cls):
        """Returns an MLReader instance for this class."""

class ComplexParamsMixin(MLReadable): ...

class JavaMMLReader(JavaMLReader):
    """
    (Private) Specialization of :py:class:`MLReader` for :py:class:`JavaParams` types
    """
    def __init__(self, clazz) -> None: ...
