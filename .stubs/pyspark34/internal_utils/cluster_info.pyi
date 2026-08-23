from _typeshed import Incomplete

class ClusterMetaData:
    cluster_name: Incomplete
    cluster_type: Incomplete
    healing_service_end_point_uri: Incomplete
    region: Incomplete
    msi_client_id: Incomplete
    environment_name: Incomplete
    environment_type: Incomplete
    workspace_name: Incomplete
    workspace_subscription_id: Incomplete
    pool_name: Incomplete
    vhd_id: Incomplete
    onelake_endpoint: Incomplete
    trident_environment_name: Incomplete
    enable_olc: Incomplete
    cloud_type: Incomplete
    def __init__(self, cluster_name: str = '', cluster_type: str = '', healing_service_end_point_uri: str = '', region: str = '', msi_client_id: str = '', environment_name: str = '', environment_type: str = '', workspace_name: str = '', workspace_subscription_id: str = '', pool_name: str = '', vhd_id: str = '', onelake_endpoint: str = '', trident_environment_name: str = '', enable_olc: bool = False, cloud_type: str = '') -> None: ...

class ClusterInfo:
    schema_version: Incomplete
    manifest_version: Incomplete
    cluster_metadata: Incomplete
    def __init__(self, cluster_metadata: ClusterMetaData, schema_version: str = '', manifest_version: int = 0) -> None: ...

def read_cluster_info() -> ClusterInfo | None: ...
def is_olc_enabled() -> bool: ...
