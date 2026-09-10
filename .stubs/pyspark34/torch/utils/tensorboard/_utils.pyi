def figure_to_image(figures, close: bool = True):
    """Render matplotlib figure to numpy format.

    Note that this requires the ``matplotlib`` package.

    Args:
        figures (matplotlib.pyplot.figure or list of figures): figure or a list of figures
        close (bool): Flag to automatically close the figure

    Returns:
        numpy.array: image in [CHW] order
    """
def make_grid(I, ncols: int = 8): ...
def convert_to_HWC(tensor, input_format): ...
