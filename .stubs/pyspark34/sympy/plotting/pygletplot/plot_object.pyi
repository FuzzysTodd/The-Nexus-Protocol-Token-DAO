class PlotObject:
    """
    Base class for objects which can be displayed in
    a Plot.
    """
    visible: bool
    def draw(self) -> None:
        """
        OpenGL rendering code for the plot object.
        Override in base class.
        """
