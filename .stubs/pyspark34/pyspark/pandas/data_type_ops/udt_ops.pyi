from pyspark.pandas.data_type_ops.base import DataTypeOps as DataTypeOps

class UDTOps(DataTypeOps):
    """
    The class for binary operations of pandas-on-Spark objects with Spark type:
    UserDefinedType or its subclasses.
    """
    @property
    def pretty_name(self) -> str: ...
