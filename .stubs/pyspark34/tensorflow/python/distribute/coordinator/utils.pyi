from tensorflow.python.training import server_lib as server_lib

def start_server(cluster_resolver, protocol) -> None:
    """Start a server and block the process from exiting."""
