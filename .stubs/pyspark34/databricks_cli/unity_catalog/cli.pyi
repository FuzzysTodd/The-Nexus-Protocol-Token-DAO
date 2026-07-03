from databricks_cli.unity_catalog.catalog_cli import register_catalog_commands as register_catalog_commands
from databricks_cli.unity_catalog.cred_cli import register_cred_commands as register_cred_commands
from databricks_cli.unity_catalog.delta_sharing_cli import register_delta_sharing_commands as register_delta_sharing_commands
from databricks_cli.unity_catalog.ext_loc_cli import register_ext_loc_commands as register_ext_loc_commands
from databricks_cli.unity_catalog.lineage_cli import register_lineage_commands as register_lineage_commands
from databricks_cli.unity_catalog.metastore_cli import register_metastore_commands as register_metastore_commands
from databricks_cli.unity_catalog.perms_cli import register_perms_commands as register_perms_commands
from databricks_cli.unity_catalog.schema_cli import register_schema_commands as register_schema_commands
from databricks_cli.unity_catalog.table_cli import register_table_commands as register_table_commands
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS
from databricks_cli.version import print_version_callback as print_version_callback, version as version

def unity_catalog_group() -> None:
    """
    Utility to interact with Databricks Unity Catalog.
    """
