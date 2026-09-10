from .core import XGBoostError as XGBoostError, build_info as build_info, c_str as c_str

def run_federated_server(port: int, world_size: int, server_key_path: str = '', server_cert_path: str = '', client_cert_path: str = '') -> None:
    """Run the Federated Learning server.

    Parameters
    ----------
    port : int
        The port to listen on.
    world_size: int
        The number of federated workers.
    server_key_path: str
        Path to the server private key file. SSL is turned off if empty.
    server_cert_path: str
        Path to the server certificate file. SSL is turned off if empty.
    client_cert_path: str
        Path to the client certificate file. SSL is turned off if empty.
    """
