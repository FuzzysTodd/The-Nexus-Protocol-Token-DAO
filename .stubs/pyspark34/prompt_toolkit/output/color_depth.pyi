from enum import Enum

__all__ = ['ColorDepth']

class ColorDepth(str, Enum):
    """
    Possible color depth values for the output.
    """
    value: str
    DEPTH_1_BIT: str
    DEPTH_4_BIT: str
    DEPTH_8_BIT: str
    DEPTH_24_BIT: str
    MONOCHROME = DEPTH_1_BIT
    ANSI_COLORS_ONLY = DEPTH_4_BIT
    DEFAULT = DEPTH_8_BIT
    TRUE_COLOR = DEPTH_24_BIT
    @classmethod
    def from_env(cls) -> ColorDepth | None:
        """
        Return the color depth if the $PROMPT_TOOLKIT_COLOR_DEPTH environment
        variable has been set.

        This is a way to enforce a certain color depth in all prompt_toolkit
        applications.
        """
    @classmethod
    def default(cls) -> ColorDepth:
        """
        Return the default color depth for the default output.
        """
