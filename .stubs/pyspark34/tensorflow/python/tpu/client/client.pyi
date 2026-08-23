from _typeshed import Incomplete

FLAGS: Incomplete

class Client:
    """Client for working with the Cloud TPU API.

  This client is intended to be used for resolving tpu name to ip addresses.

  It's recommended to use this library as a contextlib to utilize all
  functionality.
  """
    def __init__(self, tpu: Incomplete | None = None, zone: Incomplete | None = None, project: Incomplete | None = None, credentials: str = 'default', service: Incomplete | None = None, discovery_url: Incomplete | None = None) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def recoverable(self):
        """Returns true if the TPU is in a state where training should eventually resume.

    If false the TPU is in a unrecoverable state and should be recreated.
    """
    def symptoms(self):
        """Return Cloud TPU Symptoms of the TPU."""
    def state(self):
        """Return state of the TPU."""
    def health(self):
        """Return health of the TPU."""
    def runtime_version(self):
        """Return runtime version of the TPU."""
    def accelerator_type(self):
        """Return accelerator type of the TPU."""
    def api_available(self):
        """Return if the Cloud TPU API is available, if not certain features will not work."""
    def name(self):
        """Return the name of the tpu, or the ip address if name is not provided."""
    def get_local_ip(self):
        """Return the local ip address of the Google Cloud VM the workload is running on."""
    def network_endpoints(self):
        """Return a list of tpu endpoints."""
    def wait_for_healthy(self, timeout_s: int = 1200, interval: int = 30) -> None:
        """Wait for TPU to become healthy or raise error if timeout reached.

    Args:
      timeout_s (int): The timeout in seconds for waiting TPU to become healthy.
      interval (int): The interval in seconds to poll the TPU for health.

    Raises:
      RuntimeError: If the TPU doesn't become healthy by the timeout.
    """
    def configure_tpu_version(self, version, restart_type: str = 'always') -> None:
        """Configure TPU software version.

    Args:
      version (string): Version of software to configure the TPU with.
      restart_type (string): Restart behaviour when switching versions,
        defaults to always restart. Options are 'always', 'ifNeeded'.

    """
