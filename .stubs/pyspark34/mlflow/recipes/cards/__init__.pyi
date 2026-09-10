from _typeshed import Incomplete
from mlflow.exceptions import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException

CARD_PICKLE_NAME: str
CARD_HTML_NAME: str

class CardTab:
    name: Incomplete
    template: Incomplete
    def __init__(self, name: str, template: str) -> None:
        """
        Construct a step card tab with supported HTML template.

        :param name: a string representing the name of the tab.
        :param template: a string representing the HTML template for the card content.
        """
    def add_html(self, name: str, html_content: str) -> CardTab:
        """
        Adds html to the CardTab.

        :param name: String, name of the variable in the Jinja2 template
        :param html_content: String, the html to replace the named template variable
        :return: the updated card instance
        """
    def add_markdown(self, name: str, markdown: str) -> CardTab:
        """
        Adds markdown to the card replacing the variable name in the CardTab template.

        :param name: name of the variable in the CardTab Jinja2 template
        :param markdown: the markdown content
        :return: the updated card tab instance
        """
    def add_image(self, name: str, image_file_path: str, width: int = None, height: int = None) -> None: ...
    def add_pandas_profile(self, name: str, profile: str) -> CardTab:
        """
        Add a new tab representing the provided pandas profile to the card.

        :param name: name of the variable in the Jinja2 template
        :param profile: html string to render profile in the step card
        :return: the updated card instance
        """
    def to_html(self) -> str:
        """
        Returns a rendered HTML representing the content of the tab.

        :return: a HTML string
        """

class BaseCard:
    def __init__(self, recipe_name: str, step_name: str) -> None:
        """
        BaseCard Constructor

        :param recipe_name: a string representing name of the recipe.
        :param step_name: a string representing the name of the step.
        """
    def add_tab(self, name, html_template) -> CardTab:
        """
        Add a new tab with arbitrary content.

        :param name: a string representing the name of the tab.
        :param html_template: a string representing the HTML template for the card content.
        """
    def get_tab(self, name) -> CardTab | None:
        """
        Returns an existing tab with the specified name. Returns None if not found.

        :param name: a string representing the name of the tab.
        """
    def add_text(self, text: str) -> BaseCard:
        """
        Add text to the textual representation of this card.

        :param text: a string text
        :return: the updated card instance
        """
    def to_html(self) -> str:
        """
        This funtion renders the Jinja2 template based on the provided context so far.

        :return: a HTML string
        """
    def to_text(self) -> str:
        """
        :return: the textual representation of the card.
        """
    def save_as_html(self, path) -> None: ...
    def save(self, path: str) -> None: ...
    @staticmethod
    def load(path): ...
    @staticmethod
    def render_table(table, columns: Incomplete | None = None, hide_index: bool = True):
        """
        Renders a table-like object as an HTML table.

        :param table: Table-like object (e.g. pandas DataFrame, 2D numpy array, list of tuples).
        :param columns: Column names to use. If `table` doesn't have column names, this argument
            provides names for the columns. Otherwise, only the specified columns will be included
            in the output HTML table.
        :param hide_index: Hide index column when rendering.
        """

class FailureCard(BaseCard):
    """
    Step card providing information about a failed step execution, including a stacktrace.

    TODO: Migrate the failure card to a tab-based card, removing this class and its associated
          HTML template in the process.
    """
    def __init__(self, recipe_name: str, step_name: str, failure_traceback: str, output_directory: str) -> None: ...
