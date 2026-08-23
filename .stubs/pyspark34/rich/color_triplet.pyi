from typing import NamedTuple, Tuple

class ColorTriplet(NamedTuple):
    """The red, green, and blue components of a color."""
    red: int
    green: int
    blue: int
    @property
    def hex(self) -> str:
        """get the color triplet in CSS style."""
    @property
    def rgb(self) -> str:
        '''The color in RGB format.

        Returns:
            str: An rgb color, e.g. ``"rgb(100,23,255)"``.
        '''
    @property
    def normalized(self) -> Tuple[float, float, float]:
        """Convert components into floats between 0 and 1.

        Returns:
            Tuple[float, float, float]: A tuple of three normalized colour components.
        """
