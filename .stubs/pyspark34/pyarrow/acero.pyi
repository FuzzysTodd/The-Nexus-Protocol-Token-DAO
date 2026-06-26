from pyarrow._acero import AggregateNodeOptions as AggregateNodeOptions, Declaration as Declaration, ExecNodeOptions as ExecNodeOptions, FilterNodeOptions as FilterNodeOptions, HashJoinNodeOptions as HashJoinNodeOptions, OrderByNodeOptions as OrderByNodeOptions, ProjectNodeOptions as ProjectNodeOptions, TableSourceNodeOptions as TableSourceNodeOptions
from pyarrow._dataset import ScanNodeOptions as ScanNodeOptions
from pyarrow.compute import Expression as Expression, field as field
from pyarrow.lib import Table as Table

class DatasetModuleStub:
    class Dataset: ...
    class InMemoryDataset: ...
ds = DatasetModuleStub
