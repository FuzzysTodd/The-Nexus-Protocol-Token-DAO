from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, to_graph as to_graph

def list_table_lineages_cli(api_client, table_name, level) -> None:
    '''
    List table lineage by table name.
    :table_name str: name of the table with 3L format. E.g catalog.schema.table

    example response:

    digraph "lineage graph of main.lineage.user_account" {
        "main.lineage.user_account" -> "main.lineage.user_transaction";
        "main.lineage.dinner_price" -> "main.lineage.price_entry","main.lineage.user_account";
    }

    Returns the specified levels of downstream/upstream

    '''
def list_column_lineages_cli(api_client, table_name, column_name) -> None:
    '''
    List column lineage by table name and column name.
    :table_name str: name of the table with 3L format. E.g catalog.schema.table
    :column_name str: name of the column

    example response:
    {
      "downstream_cols": [
        {
          "workspace_id": 6051921418418893,
          "table_type": "TABLE",
          "catalog_name": "main",
          "table_name": "dinner_price",
          "schema_name": "lineage",
          "name": "full_menu"
        }
      ],
      "upstream_cols": [
        {
          "workspace_id": 6051921418418893,
          "table_type": "TABLE",
          "catalog_name": "main",
          "table_name": "menu",
          "schema_name": "lineage",
          "name": "app"
        },
        {
          "workspace_id": 6051921418418893,
          "table_type": "TABLE",
          "catalog_name": "main",
          "table_name": "menu",
          "schema_name": "lineage",
          "name": "desert"
        },
        {
          "workspace_id": 6051921418418893,
          "table_type": "TABLE",
          "catalog_name": "main",
          "table_name": "menu",
          "schema_name": "lineage",
          "name": "main"
        }
      ]
    }

    Returns the downstream/upstream of a given column
    '''
def lineage_group() -> None: ...
def register_lineage_commands(cmd_group) -> None: ...
def get_table_name(table_node): ...
def list_table_lineages_recursive_cli(api_client, table_name, level): ...
def connect_upstream_tables(upstream_tables, current_table, node_to_downstream) -> None:
    """
    fill node_to_downstream dict based with give upstreams and current table
    """
