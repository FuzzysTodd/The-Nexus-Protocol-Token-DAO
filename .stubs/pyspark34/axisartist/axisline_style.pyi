from _typeshed import Incomplete
from matplotlib.patches import FancyArrowPatch, _Style

class _FancyAxislineStyle:
    class SimpleArrow(FancyArrowPatch):
        """The artist class that will be returned for SimpleArrow style."""
        def __init__(self, axis_artist, line_path, transform, line_mutation_scale) -> None: ...
        def set_line_mutation_scale(self, scale) -> None: ...
        def set_path(self, path) -> None: ...
        def draw(self, renderer) -> None:
            """
            Draw the axis line.
             1) Transform the path to the display coordinate.
             2) Extend the path to make a room for arrow.
             3) Update the path of the FancyArrowPatch.
             4) Draw.
            """
        def get_window_extent(self, renderer: Incomplete | None = None): ...
    class FilledArrow(SimpleArrow):
        """The artist class that will be returned for FilledArrow style."""
        def __init__(self, axis_artist, line_path, transform, line_mutation_scale, facecolor) -> None: ...

class AxislineStyle(_Style):
    """
    A container class which defines style classes for AxisArtists.

    An instance of any axisline style class is a callable object,
    whose call signature is ::

       __call__(self, axis_artist, path, transform)

    When called, this should return an `.Artist` with the following methods::

      def set_path(self, path):
          # set the path for axisline.

      def set_line_mutation_scale(self, scale):
          # set the scale

      def draw(self, renderer):
          # draw
    """
    class _Base:
        def __init__(self) -> None:
            """
            initialization.
            """
        def __call__(self, axis_artist, transform):
            """
            Given the AxisArtist instance, and transform for the path (set_path
            method), return the Matplotlib artist for drawing the axis line.
            """
    class SimpleArrow(_Base):
        """
        A simple arrow.
        """
        ArrowAxisClass: Incomplete
        size: Incomplete
        def __init__(self, size: int = 1) -> None:
            """
            Parameters
            ----------
            size : float
                Size of the arrow as a fraction of the ticklabel size.
            """
        def new_line(self, axis_artist, transform): ...
    class FilledArrow(SimpleArrow):
        """
        An arrow with a filled head.
        """
        ArrowAxisClass: Incomplete
        size: Incomplete
        def __init__(self, size: int = 1, facecolor: Incomplete | None = None) -> None:
            """
            Parameters
            ----------
            size : float
                Size of the arrow as a fraction of the ticklabel size.
            facecolor : color, default: :rc:`axes.edgecolor`
                Fill color.

                .. versionadded:: 3.7
            """
        def new_line(self, axis_artist, transform): ...
