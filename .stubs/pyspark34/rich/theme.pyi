from .default_styles import DEFAULT_STYLES as DEFAULT_STYLES
from .style import Style as Style, StyleType as StyleType
from _typeshed import Incomplete
from typing import Dict, IO, Mapping

class Theme:
    """A container for style information, used by :class:`~rich.console.Console`.

    Args:
        styles (Dict[str, Style], optional): A mapping of style names on to styles. Defaults to None for a theme with no styles.
        inherit (bool, optional): Inherit default styles. Defaults to True.
    """
    styles: Dict[str, Style]
    def __init__(self, styles: Mapping[str, StyleType] | None = None, inherit: bool = True) -> None: ...
    @property
    def config(self) -> str:
        """Get contents of a config file for this theme."""
    @classmethod
    def from_file(cls, config_file: IO[str], source: str | None = None, inherit: bool = True) -> Theme:
        """Load a theme from a text mode file.

        Args:
            config_file (IO[str]): An open conf file.
            source (str, optional): The filename of the open file. Defaults to None.
            inherit (bool, optional): Inherit default styles. Defaults to True.

        Returns:
            Theme: A New theme instance.
        """
    @classmethod
    def read(cls, path: str, inherit: bool = True, encoding: str | None = None) -> Theme:
        """Read a theme from a path.

        Args:
            path (str): Path to a config file readable by Python configparser module.
            inherit (bool, optional): Inherit default styles. Defaults to True.
            encoding (str, optional): Encoding of the config file. Defaults to None.

        Returns:
            Theme: A new theme instance.
        """

class ThemeStackError(Exception):
    """Base exception for errors related to the theme stack."""

class ThemeStack:
    """A stack of themes.

    Args:
        theme (Theme): A theme instance
    """
    get: Incomplete
    def __init__(self, theme: Theme) -> None: ...
    def push_theme(self, theme: Theme, inherit: bool = True) -> None:
        """Push a theme on the top of the stack.

        Args:
            theme (Theme): A Theme instance.
            inherit (boolean, optional): Inherit styles from current top of stack.
        """
    def pop_theme(self) -> None:
        """Pop (and discard) the top-most theme."""
