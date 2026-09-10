from . import authentication as authentication
from ._version import __version__ as __version__
from .report import Report as Report
from .utils import MODULE_NAME as MODULE_NAME, get_access_token_details as get_access_token_details, is_dataset_create_config_valid as is_dataset_create_config_valid
from _typeshed import Incomplete
from ipywidgets import DOMWidget
from traitlets import HasTraits

class QuickVisualize(DOMWidget, HasTraits):
    """Power BI quick visualization widget"""
    EMBED_CONFIG_DEFAULT_STATE: Incomplete
    REGISTERED_EVENT_HANDLERS_DEFAULT_STATE: Incomplete
    EVENT_DATA_DEFAULT_STATE: Incomplete
    INIT_ERROR_DEFAULT_STATE: str
    SAVED_REPORT_ID_DEFAULT_STATE: str
    TOKEN_EXPIRED_DEFAULT_STATE: bool
    SUPPORTED_EVENTS: Incomplete
    container_height: Incomplete
    container_width: Incomplete
    def __init__(self, dataset_create_config, auth: Incomplete | None = None, **kwargs) -> None:
        """Create an instance of Quick Visualization in Power BI

        Args:
            dataset_create_config (object): Required.
                A dict representing the data used to create the report, formatted as IDatasetCreateConfiguration
                (See: https://learn.microsoft.com/en-us/javascript/api/overview/powerbi/embed-quick-report#step-11---create-a-dataset-without-a-data-source)

            auth (string or object): Optional.
                We have 3 authentication options to embed Power BI quick visualization:
                 - Access token (string)
                 - Authentication object (object) - instance of AuthenticationResult (DeviceCodeLoginAuthentication or InteractiveLoginAuthentication)
                 - If not provided, Power BI user will be authenticated using Device Flow authentication

        Returns:
            object: QuickVisualize object
        """
    def set_access_token(self, access_token) -> None:
        """Set an access token for the Power BI quick visualization

        Args:
            access_token (string)
        """
    def get_saved_report(self):
        """Returns the saved report associated with this QuickVisualize instance.

        Returns:
            Report: The saved report object.

        Raises:
            Exception: If no saved report is found.
        """
    def on(self, event, callback) -> None:
        """Register a callback to execute when the Power BI quick visualization emits the target event

        Args:
            event (string): Name of Power BI event (supported events: 'loaded', 'rendered', 'saved')
            callback (function): User defined function. Callback function is invoked with event details as parameter
        """
    def off(self, event) -> None:
        """Unregisters a callback on target event

        Args:
            event (string): Name of Power BI event (supported events: 'loaded', 'rendered', 'saved')
        """
    def set_size(self, container_height, container_width) -> None:
        """Set height and width of Power BI quick visualization in px

        Args:
            container_height (float)
            container_width (float)
        """
