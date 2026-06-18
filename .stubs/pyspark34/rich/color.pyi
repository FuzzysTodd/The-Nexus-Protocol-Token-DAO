from ._palettes import EIGHT_BIT_PALETTE as EIGHT_BIT_PALETTE, STANDARD_PALETTE as STANDARD_PALETTE, WINDOWS_PALETTE as WINDOWS_PALETTE
from .color_triplet import ColorTriplet as ColorTriplet
from .repr import Result as Result, rich_repr as rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME as DEFAULT_TERMINAL_THEME, TerminalTheme as TerminalTheme
from .text import Text as Text
from _typeshed import Incomplete
from enum import IntEnum
from typing import NamedTuple, Tuple

WINDOWS: Incomplete

class ColorSystem(IntEnum):
    """One of the 3 color system supported by terminals."""
    STANDARD: int
    EIGHT_BIT: int
    TRUECOLOR: int
    WINDOWS: int

class ColorType(IntEnum):
    """Type of color stored in Color class."""
    DEFAULT: int
    STANDARD: int
    EIGHT_BIT: int
    TRUECOLOR: int
    WINDOWS: int

ANSI_COLOR_NAMES: Incomplete

class ColorParseError(Exception):
    """The color could not be parsed."""

RE_COLOR: Incomplete

class Color(NamedTuple):
    """Terminal color definition."""
    name: str
    type: ColorType
    number: int | None = ...
    triplet: ColorTriplet | None = ...
    def __rich__(self) -> Text:
        """Displays the actual color if Rich printed."""
    def __rich_repr__(self) -> Result: ...
    @property
    def system(self) -> ColorSystem:
        """Get the native color system for this color."""
    @property
    def is_system_defined(self) -> bool:
        """Check if the color is ultimately defined by the system."""
    @property
    def is_default(self) -> bool:
        """Check if the color is a default color."""
    def get_truecolor(self, theme: TerminalTheme | None = None, foreground: bool = True) -> ColorTriplet:
        """Get an equivalent color triplet for this color.

        Args:
            theme (TerminalTheme, optional): Optional terminal theme, or None to use default. Defaults to None.
            foreground (bool, optional): True for a foreground color, or False for background. Defaults to True.

        Returns:
            ColorTriplet: A color triplet containing RGB components.
        """
    @classmethod
    def from_ansi(cls, number: int) -> Color:
        """Create a Color number from it's 8-bit ansi number.

        Args:
            number (int): A number between 0-255 inclusive.

        Returns:
            Color: A new Color instance.
        """
    @classmethod
    def from_triplet(cls, triplet: ColorTriplet) -> Color:
        """Create a truecolor RGB color from a triplet of values.

        Args:
            triplet (ColorTriplet): A color triplet containing red, green and blue components.

        Returns:
            Color: A new color object.
        """
    @classmethod
    def from_rgb(cls, red: float, green: float, blue: float) -> Color:
        """Create a truecolor from three color components in the range(0->255).

        Args:
            red (float): Red component in range 0-255.
            green (float): Green component in range 0-255.
            blue (float): Blue component in range 0-255.

        Returns:
            Color: A new color object.
        """
    @classmethod
    def default(cls) -> Color:
        """Get a Color instance representing the default color.

        Returns:
            Color: Default color.
        """
    @classmethod
    def parse(cls, color: str) -> Color:
        """Parse a color definition."""
    def get_ansi_codes(self, foreground: bool = True) -> Tuple[str, ...]:
        """Get the ANSI escape codes for this color."""
    def downgrade(self, system: ColorSystem) -> Color:
        """Downgrade a color system to a system with fewer colors."""

def parse_rgb_hex(hex_color: str) -> ColorTriplet:
    """Parse six hex characters in to RGB triplet."""
def blend_rgb(color1: ColorTriplet, color2: ColorTriplet, cross_fade: float = 0.5) -> ColorTriplet:
    """Blend one RGB color in to another."""
