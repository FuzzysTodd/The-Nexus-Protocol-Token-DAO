from _typeshed import Incomplete
from enum import Enum
from typing import Any, IO

ESC: str
CSI: Incomplete
OSC: Incomplete
BEL: str

class AllowStyle(Enum):
    """Values for ``cmd2.ansi.allow_style``"""
    ALWAYS: str
    NEVER: str
    TERMINAL: str

allow_style: Incomplete
ANSI_STYLE_RE: Incomplete
STD_FG_RE: Incomplete
STD_BG_RE: Incomplete
EIGHT_BIT_FG_RE: Incomplete
EIGHT_BIT_BG_RE: Incomplete
RGB_FG_RE: Incomplete
RGB_BG_RE: Incomplete

def strip_style(text: str) -> str:
    """
    Strip ANSI style sequences from a string.

    :param text: string which may contain ANSI style sequences
    :return: the same string with any ANSI style sequences removed
    """
def style_aware_wcswidth(text: str) -> int:
    """
    Wrap wcswidth to make it compatible with strings that contain ANSI style sequences.
    This is intended for single line strings. If text contains a newline, this
    function will return -1. For multiline strings, call widest_line() instead.

    :param text: the string being measured
    :return: The width of the string when printed to the terminal if no errors occur.
             If text contains characters with no absolute width (i.e. tabs),
             then this function returns -1. Replace tabs with spaces before calling this.
    """
def widest_line(text: str) -> int:
    """
    Return the width of the widest line in a multiline string. This wraps style_aware_wcswidth()
    so it handles ANSI style sequences and has the same restrictions on non-printable characters.

    :param text: the string being measured
    :return: The width of the string when printed to the terminal if no errors occur.
             If text contains characters with no absolute width (i.e. tabs),
             then this function returns -1. Replace tabs with spaces before calling this.
    """
def style_aware_write(fileobj: IO[str], msg: str) -> None:
    """
    Write a string to a fileobject and strip its ANSI style sequences if required by allow_style setting

    :param fileobj: the file object being written to
    :param msg: the string being written
    """
def set_title(title: str) -> str:
    """
    Generate a string that, when printed, sets a terminal's window title.

    :param title: new title for the window
    :return: the set title string
    """
def clear_screen(clear_type: int = 2) -> str:
    """
    Generate a string that, when printed, clears a terminal screen based on value of clear_type.

    :param clear_type: integer which specifies how to clear the screen (Defaults to 2)
                       Possible values:
                       0 - clear from cursor to end of screen
                       1 - clear from cursor to beginning of the screen
                       2 - clear entire screen
                       3 - clear entire screen and delete all lines saved in the scrollback buffer
    :return: the clear screen string
    :raises: ValueError if clear_type is not a valid value
    """
def clear_line(clear_type: int = 2) -> str:
    """
    Generate a string that, when printed, clears a line based on value of clear_type.

    :param clear_type: integer which specifies how to clear the line (Defaults to 2)
                       Possible values:
                       0 - clear from cursor to the end of the line
                       1 - clear from cursor to beginning of the line
                       2 - clear entire line
    :return: the clear line string
    :raises: ValueError if clear_type is not a valid value
    """

class AnsiSequence:
    """Base class to create ANSI sequence strings"""
    def __add__(self, other: Any) -> str:
        '''
        Support building an ANSI sequence string when self is the left operand
        e.g. Fg.LIGHT_MAGENTA + "hello"
        '''
    def __radd__(self, other: Any) -> str:
        '''
        Support building an ANSI sequence string when self is the right operand
        e.g. "hello" + Fg.RESET
        '''

class FgColor(AnsiSequence):
    """Base class for ANSI Sequences which set foreground text color"""
class BgColor(AnsiSequence):
    """Base class for ANSI Sequences which set background text color"""

class Cursor:
    """Create ANSI sequences to alter the cursor position"""
    @staticmethod
    def UP(count: int = 1) -> str:
        """Move the cursor up a specified amount of lines (Defaults to 1)"""
    @staticmethod
    def DOWN(count: int = 1) -> str:
        """Move the cursor down a specified amount of lines (Defaults to 1)"""
    @staticmethod
    def FORWARD(count: int = 1) -> str:
        """Move the cursor forward a specified amount of lines (Defaults to 1)"""
    @staticmethod
    def BACK(count: int = 1) -> str:
        """Move the cursor back a specified amount of lines (Defaults to 1)"""
    @staticmethod
    def SET_POS(x: int, y: int) -> str:
        """Set the cursor position to coordinates which are 1-based"""

class TextStyle(AnsiSequence, Enum):
    """Create text style ANSI sequences"""
    RESET_ALL: int
    ALT_RESET_ALL: str
    INTENSITY_BOLD: int
    INTENSITY_DIM: int
    INTENSITY_NORMAL: int
    ITALIC_ENABLE: int
    ITALIC_DISABLE: int
    OVERLINE_ENABLE: int
    OVERLINE_DISABLE: int
    STRIKETHROUGH_ENABLE: int
    STRIKETHROUGH_DISABLE: int
    UNDERLINE_ENABLE: int
    UNDERLINE_DISABLE: int

class Fg(FgColor, Enum):
    """
    Create ANSI sequences for the 16 standard terminal foreground text colors.
    A terminal's color settings affect how these colors appear.
    To reset any foreground color, use Fg.RESET.
    """
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    LIGHT_GRAY: int
    DARK_GRAY: int
    LIGHT_RED: int
    LIGHT_GREEN: int
    LIGHT_YELLOW: int
    LIGHT_BLUE: int
    LIGHT_MAGENTA: int
    LIGHT_CYAN: int
    WHITE: int
    RESET: int

class Bg(BgColor, Enum):
    """
    Create ANSI sequences for the 16 standard terminal background text colors.
    A terminal's color settings affect how these colors appear.
    To reset any background color, use Bg.RESET.
    """
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    LIGHT_GRAY: int
    DARK_GRAY: int
    LIGHT_RED: int
    LIGHT_GREEN: int
    LIGHT_YELLOW: int
    LIGHT_BLUE: int
    LIGHT_MAGENTA: int
    LIGHT_CYAN: int
    WHITE: int
    RESET: int

class EightBitFg(FgColor, Enum):
    """
    Create ANSI sequences for 8-bit terminal foreground text colors. Most terminals support 8-bit/256-color mode.
    The first 16 colors correspond to the 16 colors from Fg and behave the same way.
    To reset any foreground color, including 8-bit, use Fg.RESET.
    """
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    LIGHT_GRAY: int
    DARK_GRAY: int
    LIGHT_RED: int
    LIGHT_GREEN: int
    LIGHT_YELLOW: int
    LIGHT_BLUE: int
    LIGHT_MAGENTA: int
    LIGHT_CYAN: int
    WHITE: int
    GRAY_0: int
    NAVY_BLUE: int
    DARK_BLUE: int
    BLUE_3A: int
    BLUE_3B: int
    BLUE_1: int
    DARK_GREEN: int
    DEEP_SKY_BLUE_4A: int
    DEEP_SKY_BLUE_4B: int
    DEEP_SKY_BLUE_4C: int
    DODGER_BLUE_3: int
    DODGER_BLUE_2: int
    GREEN_4: int
    SPRING_GREEN_4: int
    TURQUOISE_4: int
    DEEP_SKY_BLUE_3A: int
    DEEP_SKY_BLUE_3B: int
    DODGER_BLUE_1: int
    GREEN_3A: int
    SPRING_GREEN_3A: int
    DARK_CYAN: int
    LIGHT_SEA_GREEN: int
    DEEP_SKY_BLUE_2: int
    DEEP_SKY_BLUE_1: int
    GREEN_3B: int
    SPRING_GREEN_3B: int
    SPRING_GREEN_2A: int
    CYAN_3: int
    DARK_TURQUOISE: int
    TURQUOISE_2: int
    GREEN_1: int
    SPRING_GREEN_2B: int
    SPRING_GREEN_1: int
    MEDIUM_SPRING_GREEN: int
    CYAN_2: int
    CYAN_1: int
    DARK_RED_1: int
    DEEP_PINK_4A: int
    PURPLE_4A: int
    PURPLE_4B: int
    PURPLE_3: int
    BLUE_VIOLET: int
    ORANGE_4A: int
    GRAY_37: int
    MEDIUM_PURPLE_4: int
    SLATE_BLUE_3A: int
    SLATE_BLUE_3B: int
    ROYAL_BLUE_1: int
    CHARTREUSE_4: int
    DARK_SEA_GREEN_4A: int
    PALE_TURQUOISE_4: int
    STEEL_BLUE: int
    STEEL_BLUE_3: int
    CORNFLOWER_BLUE: int
    CHARTREUSE_3A: int
    DARK_SEA_GREEN_4B: int
    CADET_BLUE_2: int
    CADET_BLUE_1: int
    SKY_BLUE_3: int
    STEEL_BLUE_1A: int
    CHARTREUSE_3B: int
    PALE_GREEN_3A: int
    SEA_GREEN_3: int
    AQUAMARINE_3: int
    MEDIUM_TURQUOISE: int
    STEEL_BLUE_1B: int
    CHARTREUSE_2A: int
    SEA_GREEN_2: int
    SEA_GREEN_1A: int
    SEA_GREEN_1B: int
    AQUAMARINE_1A: int
    DARK_SLATE_GRAY_2: int
    DARK_RED_2: int
    DEEP_PINK_4B: int
    DARK_MAGENTA_1: int
    DARK_MAGENTA_2: int
    DARK_VIOLET_1A: int
    PURPLE_1A: int
    ORANGE_4B: int
    LIGHT_PINK_4: int
    PLUM_4: int
    MEDIUM_PURPLE_3A: int
    MEDIUM_PURPLE_3B: int
    SLATE_BLUE_1: int
    YELLOW_4A: int
    WHEAT_4: int
    GRAY_53: int
    LIGHT_SLATE_GRAY: int
    MEDIUM_PURPLE: int
    LIGHT_SLATE_BLUE: int
    YELLOW_4B: int
    DARK_OLIVE_GREEN_3A: int
    DARK_GREEN_SEA: int
    LIGHT_SKY_BLUE_3A: int
    LIGHT_SKY_BLUE_3B: int
    SKY_BLUE_2: int
    CHARTREUSE_2B: int
    DARK_OLIVE_GREEN_3B: int
    PALE_GREEN_3B: int
    DARK_SEA_GREEN_3A: int
    DARK_SLATE_GRAY_3: int
    SKY_BLUE_1: int
    CHARTREUSE_1: int
    LIGHT_GREEN_2: int
    LIGHT_GREEN_3: int
    PALE_GREEN_1A: int
    AQUAMARINE_1B: int
    DARK_SLATE_GRAY_1: int
    RED_3A: int
    DEEP_PINK_4C: int
    MEDIUM_VIOLET_RED: int
    MAGENTA_3A: int
    DARK_VIOLET_1B: int
    PURPLE_1B: int
    DARK_ORANGE_3A: int
    INDIAN_RED_1A: int
    HOT_PINK_3A: int
    MEDIUM_ORCHID_3: int
    MEDIUM_ORCHID: int
    MEDIUM_PURPLE_2A: int
    DARK_GOLDENROD: int
    LIGHT_SALMON_3A: int
    ROSY_BROWN: int
    GRAY_63: int
    MEDIUM_PURPLE_2B: int
    MEDIUM_PURPLE_1: int
    GOLD_3A: int
    DARK_KHAKI: int
    NAVAJO_WHITE_3: int
    GRAY_69: int
    LIGHT_STEEL_BLUE_3: int
    LIGHT_STEEL_BLUE: int
    YELLOW_3A: int
    DARK_OLIVE_GREEN_3: int
    DARK_SEA_GREEN_3B: int
    DARK_SEA_GREEN_2: int
    LIGHT_CYAN_3: int
    LIGHT_SKY_BLUE_1: int
    GREEN_YELLOW: int
    DARK_OLIVE_GREEN_2: int
    PALE_GREEN_1B: int
    DARK_SEA_GREEN_5B: int
    DARK_SEA_GREEN_5A: int
    PALE_TURQUOISE_1: int
    RED_3B: int
    DEEP_PINK_3A: int
    DEEP_PINK_3B: int
    MAGENTA_3B: int
    MAGENTA_3C: int
    MAGENTA_2A: int
    DARK_ORANGE_3B: int
    INDIAN_RED_1B: int
    HOT_PINK_3B: int
    HOT_PINK_2: int
    ORCHID: int
    MEDIUM_ORCHID_1A: int
    ORANGE_3: int
    LIGHT_SALMON_3B: int
    LIGHT_PINK_3: int
    PINK_3: int
    PLUM_3: int
    VIOLET: int
    GOLD_3B: int
    LIGHT_GOLDENROD_3: int
    TAN: int
    MISTY_ROSE_3: int
    THISTLE_3: int
    PLUM_2: int
    YELLOW_3B: int
    KHAKI_3: int
    LIGHT_GOLDENROD_2A: int
    LIGHT_YELLOW_3: int
    GRAY_84: int
    LIGHT_STEEL_BLUE_1: int
    YELLOW_2: int
    DARK_OLIVE_GREEN_1A: int
    DARK_OLIVE_GREEN_1B: int
    DARK_SEA_GREEN_1: int
    HONEYDEW_2: int
    LIGHT_CYAN_1: int
    RED_1: int
    DEEP_PINK_2: int
    DEEP_PINK_1A: int
    DEEP_PINK_1B: int
    MAGENTA_2B: int
    MAGENTA_1: int
    ORANGE_RED_1: int
    INDIAN_RED_1C: int
    INDIAN_RED_1D: int
    HOT_PINK_1A: int
    HOT_PINK_1B: int
    MEDIUM_ORCHID_1B: int
    DARK_ORANGE: int
    SALMON_1: int
    LIGHT_CORAL: int
    PALE_VIOLET_RED_1: int
    ORCHID_2: int
    ORCHID_1: int
    ORANGE_1: int
    SANDY_BROWN: int
    LIGHT_SALMON_1: int
    LIGHT_PINK_1: int
    PINK_1: int
    PLUM_1: int
    GOLD_1: int
    LIGHT_GOLDENROD_2B: int
    LIGHT_GOLDENROD_2C: int
    NAVAJO_WHITE_1: int
    MISTY_ROSE1: int
    THISTLE_1: int
    YELLOW_1: int
    LIGHT_GOLDENROD_1: int
    KHAKI_1: int
    WHEAT_1: int
    CORNSILK_1: int
    GRAY_100: int
    GRAY_3: int
    GRAY_7: int
    GRAY_11: int
    GRAY_15: int
    GRAY_19: int
    GRAY_23: int
    GRAY_27: int
    GRAY_30: int
    GRAY_35: int
    GRAY_39: int
    GRAY_42: int
    GRAY_46: int
    GRAY_50: int
    GRAY_54: int
    GRAY_58: int
    GRAY_62: int
    GRAY_66: int
    GRAY_70: int
    GRAY_74: int
    GRAY_78: int
    GRAY_82: int
    GRAY_85: int
    GRAY_89: int
    GRAY_93: int

class EightBitBg(BgColor, Enum):
    """
    Create ANSI sequences for 8-bit terminal background text colors. Most terminals support 8-bit/256-color mode.
    The first 16 colors correspond to the 16 colors from Bg and behave the same way.
    To reset any background color, including 8-bit, use Bg.RESET.
    """
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    LIGHT_GRAY: int
    DARK_GRAY: int
    LIGHT_RED: int
    LIGHT_GREEN: int
    LIGHT_YELLOW: int
    LIGHT_BLUE: int
    LIGHT_MAGENTA: int
    LIGHT_CYAN: int
    WHITE: int
    GRAY_0: int
    NAVY_BLUE: int
    DARK_BLUE: int
    BLUE_3A: int
    BLUE_3B: int
    BLUE_1: int
    DARK_GREEN: int
    DEEP_SKY_BLUE_4A: int
    DEEP_SKY_BLUE_4B: int
    DEEP_SKY_BLUE_4C: int
    DODGER_BLUE_3: int
    DODGER_BLUE_2: int
    GREEN_4: int
    SPRING_GREEN_4: int
    TURQUOISE_4: int
    DEEP_SKY_BLUE_3A: int
    DEEP_SKY_BLUE_3B: int
    DODGER_BLUE_1: int
    GREEN_3A: int
    SPRING_GREEN_3A: int
    DARK_CYAN: int
    LIGHT_SEA_GREEN: int
    DEEP_SKY_BLUE_2: int
    DEEP_SKY_BLUE_1: int
    GREEN_3B: int
    SPRING_GREEN_3B: int
    SPRING_GREEN_2A: int
    CYAN_3: int
    DARK_TURQUOISE: int
    TURQUOISE_2: int
    GREEN_1: int
    SPRING_GREEN_2B: int
    SPRING_GREEN_1: int
    MEDIUM_SPRING_GREEN: int
    CYAN_2: int
    CYAN_1: int
    DARK_RED_1: int
    DEEP_PINK_4A: int
    PURPLE_4A: int
    PURPLE_4B: int
    PURPLE_3: int
    BLUE_VIOLET: int
    ORANGE_4A: int
    GRAY_37: int
    MEDIUM_PURPLE_4: int
    SLATE_BLUE_3A: int
    SLATE_BLUE_3B: int
    ROYAL_BLUE_1: int
    CHARTREUSE_4: int
    DARK_SEA_GREEN_4A: int
    PALE_TURQUOISE_4: int
    STEEL_BLUE: int
    STEEL_BLUE_3: int
    CORNFLOWER_BLUE: int
    CHARTREUSE_3A: int
    DARK_SEA_GREEN_4B: int
    CADET_BLUE_2: int
    CADET_BLUE_1: int
    SKY_BLUE_3: int
    STEEL_BLUE_1A: int
    CHARTREUSE_3B: int
    PALE_GREEN_3A: int
    SEA_GREEN_3: int
    AQUAMARINE_3: int
    MEDIUM_TURQUOISE: int
    STEEL_BLUE_1B: int
    CHARTREUSE_2A: int
    SEA_GREEN_2: int
    SEA_GREEN_1A: int
    SEA_GREEN_1B: int
    AQUAMARINE_1A: int
    DARK_SLATE_GRAY_2: int
    DARK_RED_2: int
    DEEP_PINK_4B: int
    DARK_MAGENTA_1: int
    DARK_MAGENTA_2: int
    DARK_VIOLET_1A: int
    PURPLE_1A: int
    ORANGE_4B: int
    LIGHT_PINK_4: int
    PLUM_4: int
    MEDIUM_PURPLE_3A: int
    MEDIUM_PURPLE_3B: int
    SLATE_BLUE_1: int
    YELLOW_4A: int
    WHEAT_4: int
    GRAY_53: int
    LIGHT_SLATE_GRAY: int
    MEDIUM_PURPLE: int
    LIGHT_SLATE_BLUE: int
    YELLOW_4B: int
    DARK_OLIVE_GREEN_3A: int
    DARK_GREEN_SEA: int
    LIGHT_SKY_BLUE_3A: int
    LIGHT_SKY_BLUE_3B: int
    SKY_BLUE_2: int
    CHARTREUSE_2B: int
    DARK_OLIVE_GREEN_3B: int
    PALE_GREEN_3B: int
    DARK_SEA_GREEN_3A: int
    DARK_SLATE_GRAY_3: int
    SKY_BLUE_1: int
    CHARTREUSE_1: int
    LIGHT_GREEN_2: int
    LIGHT_GREEN_3: int
    PALE_GREEN_1A: int
    AQUAMARINE_1B: int
    DARK_SLATE_GRAY_1: int
    RED_3A: int
    DEEP_PINK_4C: int
    MEDIUM_VIOLET_RED: int
    MAGENTA_3A: int
    DARK_VIOLET_1B: int
    PURPLE_1B: int
    DARK_ORANGE_3A: int
    INDIAN_RED_1A: int
    HOT_PINK_3A: int
    MEDIUM_ORCHID_3: int
    MEDIUM_ORCHID: int
    MEDIUM_PURPLE_2A: int
    DARK_GOLDENROD: int
    LIGHT_SALMON_3A: int
    ROSY_BROWN: int
    GRAY_63: int
    MEDIUM_PURPLE_2B: int
    MEDIUM_PURPLE_1: int
    GOLD_3A: int
    DARK_KHAKI: int
    NAVAJO_WHITE_3: int
    GRAY_69: int
    LIGHT_STEEL_BLUE_3: int
    LIGHT_STEEL_BLUE: int
    YELLOW_3A: int
    DARK_OLIVE_GREEN_3: int
    DARK_SEA_GREEN_3B: int
    DARK_SEA_GREEN_2: int
    LIGHT_CYAN_3: int
    LIGHT_SKY_BLUE_1: int
    GREEN_YELLOW: int
    DARK_OLIVE_GREEN_2: int
    PALE_GREEN_1B: int
    DARK_SEA_GREEN_5B: int
    DARK_SEA_GREEN_5A: int
    PALE_TURQUOISE_1: int
    RED_3B: int
    DEEP_PINK_3A: int
    DEEP_PINK_3B: int
    MAGENTA_3B: int
    MAGENTA_3C: int
    MAGENTA_2A: int
    DARK_ORANGE_3B: int
    INDIAN_RED_1B: int
    HOT_PINK_3B: int
    HOT_PINK_2: int
    ORCHID: int
    MEDIUM_ORCHID_1A: int
    ORANGE_3: int
    LIGHT_SALMON_3B: int
    LIGHT_PINK_3: int
    PINK_3: int
    PLUM_3: int
    VIOLET: int
    GOLD_3B: int
    LIGHT_GOLDENROD_3: int
    TAN: int
    MISTY_ROSE_3: int
    THISTLE_3: int
    PLUM_2: int
    YELLOW_3B: int
    KHAKI_3: int
    LIGHT_GOLDENROD_2A: int
    LIGHT_YELLOW_3: int
    GRAY_84: int
    LIGHT_STEEL_BLUE_1: int
    YELLOW_2: int
    DARK_OLIVE_GREEN_1A: int
    DARK_OLIVE_GREEN_1B: int
    DARK_SEA_GREEN_1: int
    HONEYDEW_2: int
    LIGHT_CYAN_1: int
    RED_1: int
    DEEP_PINK_2: int
    DEEP_PINK_1A: int
    DEEP_PINK_1B: int
    MAGENTA_2B: int
    MAGENTA_1: int
    ORANGE_RED_1: int
    INDIAN_RED_1C: int
    INDIAN_RED_1D: int
    HOT_PINK_1A: int
    HOT_PINK_1B: int
    MEDIUM_ORCHID_1B: int
    DARK_ORANGE: int
    SALMON_1: int
    LIGHT_CORAL: int
    PALE_VIOLET_RED_1: int
    ORCHID_2: int
    ORCHID_1: int
    ORANGE_1: int
    SANDY_BROWN: int
    LIGHT_SALMON_1: int
    LIGHT_PINK_1: int
    PINK_1: int
    PLUM_1: int
    GOLD_1: int
    LIGHT_GOLDENROD_2B: int
    LIGHT_GOLDENROD_2C: int
    NAVAJO_WHITE_1: int
    MISTY_ROSE1: int
    THISTLE_1: int
    YELLOW_1: int
    LIGHT_GOLDENROD_1: int
    KHAKI_1: int
    WHEAT_1: int
    CORNSILK_1: int
    GRAY_100: int
    GRAY_3: int
    GRAY_7: int
    GRAY_11: int
    GRAY_15: int
    GRAY_19: int
    GRAY_23: int
    GRAY_27: int
    GRAY_30: int
    GRAY_35: int
    GRAY_39: int
    GRAY_42: int
    GRAY_46: int
    GRAY_50: int
    GRAY_54: int
    GRAY_58: int
    GRAY_62: int
    GRAY_66: int
    GRAY_70: int
    GRAY_74: int
    GRAY_78: int
    GRAY_82: int
    GRAY_85: int
    GRAY_89: int
    GRAY_93: int

class RgbFg(FgColor):
    """
    Create ANSI sequences for 24-bit (RGB) terminal foreground text colors. The terminal must support 24-bit/true-color mode.
    To reset any foreground color, including 24-bit, use Fg.RESET.
    """
    def __init__(self, r: int, g: int, b: int) -> None:
        """
        RgbFg initializer

        :param r: integer from 0-255 for the red component of the color
        :param g: integer from 0-255 for the green component of the color
        :param b: integer from 0-255 for the blue component of the color
        :raises: ValueError if r, g, or b is not in the range 0-255
        """

class RgbBg(BgColor):
    """
    Create ANSI sequences for 24-bit (RGB) terminal background text colors. The terminal must support 24-bit/true-color mode.
    To reset any background color, including 24-bit, use Bg.RESET.
    """
    def __init__(self, r: int, g: int, b: int) -> None:
        """
        RgbBg initializer

        :param r: integer from 0-255 for the red component of the color
        :param g: integer from 0-255 for the green component of the color
        :param b: integer from 0-255 for the blue component of the color
        :raises: ValueError if r, g, or b is not in the range 0-255
        """

def style(value: Any, *, fg: FgColor | None = None, bg: BgColor | None = None, bold: bool | None = None, dim: bool | None = None, italic: bool | None = None, overline: bool | None = None, strikethrough: bool | None = None, underline: bool | None = None) -> str:
    """
    Apply ANSI colors and/or styles to a string and return it.
    The styling is self contained which means that at the end of the string reset code(s) are issued
    to undo whatever styling was done at the beginning.

    :param value: object whose text is to be styled
    :param fg: foreground color provided as any subclass of FgColor (e.g. Fg, EightBitFg, RgbFg)
               Defaults to no color.
    :param bg: foreground color provided as any subclass of BgColor (e.g. Bg, EightBitBg, RgbBg)
               Defaults to no color.
    :param bold: apply the bold style if True. Defaults to False.
    :param dim: apply the dim style if True. Defaults to False.
    :param italic: apply the italic style if True. Defaults to False.
    :param overline: apply the overline style if True. Defaults to False.
    :param strikethrough: apply the strikethrough style if True. Defaults to False.
    :param underline: apply the underline style if True. Defaults to False.
    :raises: TypeError if fg isn't None or a subclass of FgColor
    :raises: TypeError if bg isn't None or a subclass of BgColor
    :return: the stylized string
    """

style_success: Incomplete
style_warning: Incomplete
style_error: Incomplete

def async_alert_str(*, terminal_columns: int, prompt: str, line: str, cursor_offset: int, alert_msg: str) -> str:
    """Calculate the desired string, including ANSI escape codes, for displaying an asynchronous alert message.

    :param terminal_columns: terminal width (number of columns)
    :param prompt: prompt that is displayed on the current line
    :param line: current contents of the Readline line buffer
    :param cursor_offset: the offset of the current cursor position within line
    :param alert_msg: the message to display to the user
    :return: the correct string so that the alert message appears to the user to be printed above the current line.
    """
