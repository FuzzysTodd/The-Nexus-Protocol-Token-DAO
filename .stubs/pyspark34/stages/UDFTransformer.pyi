from pyspark.ml.param.shared import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer

basestring = str

class UDFTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:

        inputCol (str): The name of the input column (default: )
        outputCol (str): The name of the output column
        udf (object): User Defined Python Function to be applied to the DF input col
        udfScala (object): User Defined Function to be applied to the DF input col
    """
    inputCol: Incomplete
    inputCols: Incomplete
    outputCol: Incomplete
    udf: Incomplete
    def __init__(self, inputCol: Incomplete | None = None, inputCols: Incomplete | None = None, outputCol: Incomplete | None = None, udf: Incomplete | None = None) -> None: ...
    def setInputCol(self, value):
        """

        Args:

            inputCol (str): The name of the input column (default: )

        """
    def getInputCol(self):
        """

        Returns:

            str: The name of the input column (default: )
        """
    def setInputCols(self, value):
        """

        Args:

            inputCols (list): The names of the input columns (default: )

        """
    def getInputCols(self):
        """

        Returns:

            str: The name of the input column (default: )
        """
    def setOutputCol(self, value):
        """

        Args:

            outputCol (str): The name of the output column

        """
    def getOutputCol(self):
        """

        Returns:

            str: The name of the output column
        """
    def setUDF(self, udf): ...
    def getUDF(self): ...
    @classmethod
    def read(cls):
        """Returns an MLReader instance for this class."""
    @staticmethod
    def getJavaPackage():
        """Returns package name String."""
