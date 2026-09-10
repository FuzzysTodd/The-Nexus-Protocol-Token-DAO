import logging
from _typeshed import Incomplete

class mds_handler(logging.Handler):
    synapse_workspace_name: Incomplete
    synapse_pool_name: Incomplete
    cluster_name: Incomplete
    cluster_region: Incomplete
    cluster_env_type: Incomplete
    cluster_env_name: Incomplete
    cluster_node_name: Incomplete
    application_id: Incomplete
    kusto_table_name: Incomplete
    def __init__(self, kusto_table, application_id: Incomplete | None = None, level=...) -> None: ...
    def emit(self, record) -> None: ...
    def get_log_entry(self, record): ...
    def send_log_entry(self, log_entry) -> None: ...
