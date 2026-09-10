from .base import ListFormatter as ListFormatter
from _typeshed import Incomplete
from cliff import columns as columns

class CSVLister(ListFormatter):
    QUOTE_MODES: Incomplete
    def add_argument_group(self, parser) -> None: ...
    def emit_list(self, column_names, data, stdout, parsed_args) -> None: ...
