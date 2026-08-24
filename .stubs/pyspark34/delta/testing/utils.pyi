from _typeshed import Incomplete
from pyspark import SparkConf as SparkConf
from pyspark.testing.sqlutils import ReusedSQLTestCase

class DeltaTestCase(ReusedSQLTestCase):
    """Test class base that sets up a correctly configured SparkSession for querying Delta tables.
    """
    @classmethod
    def conf(cls) -> SparkConf: ...
    tempPath: Incomplete
    tempFile: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
