from ._version import __version__ as __version__
from .models import EmbedMode as EmbedMode, ExportDataType as ExportDataType, TokenType as TokenType
from .utils import MODULE_NAME as MODULE_NAME, get_access_token_details as get_access_token_details
from _typeshed import Incomplete
from ipywidgets import DOMWidget
from traitlets import HasTraits

class Report(DOMWidget, HasTraits):
    """PowerBI report embedding widget"""
    EMBED_CONFIG_DEFAULT_STATE: Incomplete
    VISUAL_DATA_DEFAULT_STATE: str
    EXPORT_VISUAL_DATA_REQUEST_DEFAULT_STATE: Incomplete
    REGISTERED_EVENT_HANDLERS_DEFAULT_STATE: Incomplete
    EVENT_DATA_DEFAULT_STATE: Incomplete
    GET_FILTERS_REQUEST_DEFAULT_STATE: bool
    REPORT_FILTERS_DEFAULT_STATE: Incomplete
    REPORT_FILTER_REQUEST_DEFAULT_STATE: Incomplete
    GET_PAGES_REQUEST_DEFAULT_STATE: bool
    REPORT_PAGES_DEFAULT_STATE: Incomplete
    GET_VISUALS_DEFAULT_PAGE_NAME: str
    PAGE_VISUALS_DEFAULT_STATE: Incomplete
    GET_BOOKMARKS_REQUEST_DEFAULT_STATE: bool
    REPORT_BOOKMARKS_DEFAULT_STATE: Incomplete
    REPORT_BOOKMARK_DEFAULT_NAME: str
    TOKEN_EXPIRED_DEFAULT_STATE: bool
    CLIENT_ERROR_DEFAULT_STATE: str
    INIT_ERROR_DEFAULT_STATE: str
    REPORT_ACTIVE_PAGE_DEFAULT_NAME: str
    REPORT_NOT_EMBEDDED_MESSAGE: str
    PROCESS_EVENTS_ITERATION: int
    POLLING_INTERVAL: float
    ALLOWED_EVENTS: Incomplete
    SUPPORTED_EVENTS: Incomplete
    container_height: Incomplete
    container_width: Incomplete
    def __init__(self, group_id: Incomplete | None = None, report_id: Incomplete | None = None, auth: Incomplete | None = None, view_mode=..., permissions: Incomplete | None = None, dataset_id: Incomplete | None = None, **kwargs) -> None:
        """Create an instance of a Power BI report. 
        Provide a report ID for viewing or editing an existing report, or a dataset ID for creating a new report.

        Args:
            group_id (string): Optional.
                Id of Power BI Workspace where your report resides. If value is not provided, My workspace will be used.

            report_id (string): Optional.
                Id of Power BI report. Must be provided to view or edit an existing report.

            access_token (string): Optional.
                Access token, which will be used to embed a Power BI report.
                If not provided, authentication object will be used (to be provided using `auth` parameter).

            auth (string or object): Optional.
                We have 3 authentication options to embed a Power BI report:
                 - Access token (string)
                 - Authentication object (object) - instance of AuthenticationResult (DeviceCodeLoginAuthentication or InteractiveLoginAuthentication)
                 - If not provided, Power BI user will be authenticated using Device Flow authentication

            view_mode (number): Optional.
                Mode for embedding Power BI report (VIEW: 0, EDIT: 1, CREATE: 2).
                To be provided if user wants to edit or create a report.
                (Default = VIEW)

            permissions (number): Optional.
                Permissions required while embedding report in EDIT mode.
                Required when the report is embedded in EDIT mode by passing `1` in `view_mode` parameter.
                Values for permissions:
                `READWRITE` - Users can view, edit, and save the report.
                `COPY` - Users can save a copy of the report by using Save As.
                `CREATE` - Users can create a new report.
                `ALL` - Users can create, view, edit, save, and save a copy of the report.

            dataset_id (string): Optional.
                Create a new report using this dataset in the provided Power BI workspace. 
                Must be provided to create a new report from an existing dataset if report_id is not provided.

        Returns:
            object: Report object
        """
    def set_access_token(self, access_token) -> None:
        """Set access token for Power BI report

        Args:
            access_token (string): report access token
        """
    def set_size(self, container_height, container_width) -> None:
        """Set height and width of Power BI report in px

        Args:
            container_height (float): report height
            container_width (float): report width
        """
    def export_visual_data(self, page_name, visual_name, rows: Incomplete | None = None, export_data_type=...):
        """Returns the data of given visual of the embedded Power BI report

        Args:
            page_name (string): Page name of the report's page containing the target visual
            visual_name (string): Visual's unique name 
            rows (int, optional): Number of rows of data to export (default - exports all rows)
            export_data_type (number, optional): Type of data to be exported (SUMMARIZED: 0, UNDERLYING: 1).
                (Default = SUMMARIZED)

        Returns:
            string: visual's exported data
        """
    def on(self, event, callback) -> None:
        """Register a callback to execute when the report emits the target event

        Args:
            event (string): Name of Power BI event (supported events: 'loaded', 'rendered')
            callback (function): User defined function. Callback function is invoked with event details as parameter
        """
    def off(self, event) -> None:
        """Unregisters a callback on target event

        Args:
            event (string): Name of Power BI event (supported events: 'loaded', 'rendered')
        """
    def get_filters(self):
        """Returns the list of filters applied on the report level

        Returns:
            list: list of filters
        """
    def update_filters(self, filters) -> None:
        """Update report level filters in the embedded report.
            Currently supports models.FiltersOperations.Replace: Replaces an existing filter or adds it if it doesn't exist. 

        Args:
            filters ([models.ReportLevelFilters]): List of report level filters

        Raises:
            Exception: When report is not embedded
        """
    def remove_filters(self) -> None:
        """Remove all report level filters from the embedded report

        Raises:
            Exception: When report is not embedded
        """
    def get_pages(self):
        """Returns pages list of the embedded Power BI report

        Returns:
            list: list of pages
        """
    def visuals_on_page(self, page_name):
        """Returns visuals list of the given page of the embedded Power BI report

        Args:
            page_name (string): Page name of the embedded report

        Returns:
            list: list of visuals
        """
    def set_bookmark(self, bookmark_name) -> None:
        """Applies a bookmark by name on the embedded report.

        Args:
            bookmark_name (string) : Bookmark Name
        Raises:
            Exception: When report is not embedded
        """
    def get_bookmarks(self):
        """Returns the list of bookmarks of the embedded Power BI report

        Returns:
            list: list of bookmarks

        Raises:
            Exception: When report is not embedded
        """
    def set_active_page(self, page_name) -> None:
        """Sets the provided page as active

        Args:
            page_name (string): name of the page you want to set as active

        Raises:
            Exception: When report is not embedded
        """
