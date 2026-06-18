from _typeshed import Incomplete
from pyspark.ml import Transformer
from pyspark.sql import DataFrame as DataFrame
from typing import List

class ComplementAccessTransformer(Transformer):
    partitionKey: Incomplete
    indexedColNamesArr: Incomplete
    complementsetFactor: Incomplete
    def __init__(self, partition_key: str | None, indexed_col_names_arr: List[str], complementset_factor: int) -> None: ...
