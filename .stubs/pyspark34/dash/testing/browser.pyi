from _typeshed import Incomplete
from dash.testing.consts import SELENIUM_GRID_DEFAULT as SELENIUM_GRID_DEFAULT
from dash.testing.dash_page import DashPageMixin as DashPageMixin
from dash.testing.errors import BrowserError as BrowserError, DashAppLoadingError as DashAppLoadingError, TestingTimeoutError as TestingTimeoutError
from dash.testing.wait import class_to_equal as class_to_equal, contains_class as contains_class, contains_text as contains_text, style_to_equal as style_to_equal, text_to_equal as text_to_equal, until as until

logger: Incomplete

class Browser(DashPageMixin):
    percy_runner: Incomplete
    def __init__(self, browser, remote: bool = False, remote_url: Incomplete | None = None, headless: bool = False, options: Incomplete | None = None, download_path: str = '', percy_run: bool = True, percy_finalize: bool = True, percy_assets_root: str = '', wait_timeout: int = 10, pause: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def visit_and_snapshot(self, resource_path, hook_id, wait_for_callbacks: bool = True, convert_canvases: bool = False, assert_check: bool = True, stay_on_page: bool = False, widths: Incomplete | None = None) -> None: ...
    def percy_snapshot(self, name: str = '', wait_for_callbacks: bool = False, convert_canvases: bool = False, widths: Incomplete | None = None) -> None:
        """percy_snapshot - visual test api shortcut to `percy_runner.snapshot`.
        It also combines the snapshot `name` with the Python version,
        args:
        - name: combined with the python version to give the final snapshot name
        - wait_for_callbacks: default False, whether to wait for Dash callbacks,
            after an extra second to ensure that any relevant callbacks have
            been initiated
        - convert_canvases: default False, whether to convert all canvas elements
            in the DOM into static images for percy to see. They will be restored
            after the snapshot is complete.
        - widths: a list of pixel widths for percy to render the page with. Note
            that this does not change the browser in which the DOM is constructed,
            so the width will only affect CSS, not JS-driven layout.
            Defaults to [1280]
        """
    def take_snapshot(self, name) -> None:
        """Hook method to take snapshot when a selenium test fails. The
        snapshot is placed under.

            - `/tmp/dash_artifacts` in linux
            - `%TEMP` in windows
        with a filename combining test case name and the
        running selenium session id
        """
    def find_element(self, selector, attribute: str = 'CSS_SELECTOR'):
        '''find_element returns the first found element by the attribute `selector`
        shortcut to `driver.find_element(By.CSS_SELECTOR, ...)`.
        args:
        - attribute: the attribute type to search for, aligns with the Selenium
            API\'s `By` class. default "CSS_SELECTOR"
            valid values: "CSS_SELECTOR", "ID", "NAME", "TAG_NAME",
            "CLASS_NAME", "LINK_TEXT", "PARTIAL_LINK_TEXT", "XPATH"
        '''
    def find_elements(self, selector, attribute: str = 'CSS_SELECTOR'):
        '''find_elements returns a list of all elements matching the attribute
        `selector`. Shortcut to `driver.find_elements(By.CSS_SELECTOR, ...)`.
        args:
        - attribute: the attribute type to search for, aligns with the Selenium
            API\'s `By` class. default "CSS_SELECTOR"
            valid values: "CSS_SELECTOR", "ID", "NAME", "TAG_NAME",
            "CLASS_NAME", "LINK_TEXT", "PARTIAL_LINK_TEXT", "XPATH"
        '''
    def wait_for_element(self, selector, timeout: Incomplete | None = None):
        """wait_for_element is shortcut to `wait_for_element_by_css_selector`
        timeout if not set, equals to the fixture's `wait_timeout`."""
    def wait_for_element_by_css_selector(self, selector, timeout: Incomplete | None = None):
        """Explicit wait until the element is present, timeout if not set,
        equals to the fixture's `wait_timeout` shortcut to `WebDriverWait` with
        `EC.presence_of_element_located`."""
    def wait_for_no_elements(self, selector, timeout: Incomplete | None = None):
        """Explicit wait until an element is NOT found. timeout defaults to
        the fixture's `wait_timeout`."""
    def wait_for_element_by_id(self, element_id, timeout: Incomplete | None = None):
        """Explicit wait until the element is present, timeout if not set,
        equals to the fixture's `wait_timeout` shortcut to `WebDriverWait` with
        `EC.presence_of_element_located`."""
    def wait_for_class_to_equal(self, selector, classname, timeout: Incomplete | None = None):
        """Explicit wait until the element's class has expected `value` timeout
        if not set, equals to the fixture's `wait_timeout` shortcut to
        `WebDriverWait` with customized `class_to_equal` condition."""
    def wait_for_style_to_equal(self, selector, style, val, timeout: Incomplete | None = None):
        """Explicit wait until the element's style has expected `value` timeout
        if not set, equals to the fixture's `wait_timeout` shortcut to
        `WebDriverWait` with customized `style_to_equal` condition."""
    def wait_for_text_to_equal(self, selector, text, timeout: Incomplete | None = None):
        """Explicit wait until the element's text equals the expected `text`.

        timeout if not set, equals to the fixture's `wait_timeout`
        shortcut to `WebDriverWait` with customized `text_to_equal`
        condition.
        """
    def wait_for_contains_class(self, selector, classname, timeout: Incomplete | None = None):
        """Explicit wait until the element's classes contains the expected `classname`.

        timeout if not set, equals to the fixture's `wait_timeout`
        shortcut to `WebDriverWait` with customized `contains_class`
        condition.
        """
    def wait_for_contains_text(self, selector, text, timeout: Incomplete | None = None):
        """Explicit wait until the element's text contains the expected `text`.

        timeout if not set, equals to the fixture's `wait_timeout`
        shortcut to `WebDriverWait` with customized `contains_text`
        condition.
        """
    def wait_for_page(self, url: Incomplete | None = None, timeout: int = 10) -> None:
        """wait_for_page navigates to the url in webdriver wait until the
        renderer is loaded in browser.

        use the `server_url` if url is not provided.
        """
    def select_dcc_dropdown(self, elem_or_selector, value: Incomplete | None = None, index: Incomplete | None = None) -> None: ...
    def toggle_window(self) -> None:
        """Switch between the current working window and the new opened one."""
    def switch_window(self, idx: int = 0) -> None:
        """Switch to window by window index shortcut to
        `driver.switch_to.window`."""
    def open_new_tab(self, url: Incomplete | None = None) -> None:
        """Open a new tab in browser url is not set, equals to `server_url`."""
    def get_webdriver(self): ...
    def multiple_click(self, elem_or_selector, clicks, delay: Incomplete | None = None) -> None:
        """multiple_click click the element with number of `clicks`."""
    def clear_input(self, elem_or_selector) -> None:
        """Simulate key press to clear the input."""
    def zoom_in_graph_by_ratio(self, elem_or_selector, start_fraction: float = 0.5, zoom_box_fraction: float = 0.2, compare: bool = True) -> None:
        """Zoom out a graph with a zoom box fraction of component dimension
        default start at middle with a rectangle of 1/5 of the dimension use
        `compare` to control if we check the svg get changed."""
    def click_at_coord_fractions(self, elem_or_selector, fx, fy) -> None: ...
    def get_logs(self):
        """Return a list of `SEVERE` level logs after last reset time stamps
        (default to 0, resettable by `reset_log_timestamp`.

        Chrome only
        """
    def reset_log_timestamp(self) -> None:
        """reset_log_timestamp only work with chrome webdriver."""
    @property
    def driver(self):
        """Expose the selenium webdriver as fixture property."""
    @property
    def session_id(self): ...
    @property
    def server_url(self): ...
    @server_url.setter
    def server_url(self, value) -> None:
        """Set the server url so the selenium is aware of the local server
        port.

        It also implicitly calls `wait_for_page`.
        """
    @property
    def download_path(self): ...
    @property
    def wait_timeout(self): ...
    @wait_timeout.setter
    def wait_timeout(self, value) -> None: ...
