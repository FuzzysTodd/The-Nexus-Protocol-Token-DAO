from _typeshed import Incomplete

class InputDeviceState:
    def __init__(self, ctrl: Incomplete | None = None, alt: Incomplete | None = None, shift: Incomplete | None = None, meta: Incomplete | None = None, button: Incomplete | None = None, buttons: Incomplete | None = None, **_) -> None: ...
    @property
    def alt(self):
        """
        Whether alt key pressed

        Returns
        -------
        bool
        """
    @property
    def ctrl(self):
        """
        Whether ctrl key pressed

        Returns
        -------
        bool
        """
    @property
    def shift(self):
        """
        Whether shift key pressed

        Returns
        -------
        bool
        """
    @property
    def meta(self):
        """
        Whether meta key pressed

        Returns
        -------
        bool
        """
    @property
    def button(self):
        """
        Integer code for the button that was pressed on the mouse to trigger
        the event

        - 0: Main button pressed, usually the left button or the
             un-initialized state
        - 1: Auxiliary button pressed, usually the wheel button or the middle
             button (if present)
        - 2: Secondary button pressed, usually the right button
        - 3: Fourth button, typically the Browser Back button
        - 4: Fifth button, typically the Browser Forward button

        Returns
        -------
        int
        """
    @property
    def buttons(self):
        '''
        Integer code for which combination of buttons are pressed on the
        mouse when the event is triggered.

        -  0: No button or un-initialized
        -  1: Primary button (usually left)
        -  2: Secondary button (usually right)
        -  4: Auxilary button (usually middle or mouse wheel button)
        -  8: 4th button (typically the "Browser Back" button)
        - 16: 5th button (typically the "Browser Forward" button)

        Combinations of buttons are represented as the decimal form of the
        bitmask of the values above.

        For example, pressing both the primary (1) and auxilary (4) buttons
        will result in a code of 5

        Returns
        -------
        int
        '''

class Points:
    def __init__(self, point_inds=[], xs=[], ys=[], trace_name: Incomplete | None = None, trace_index: Incomplete | None = None) -> None: ...
    @property
    def point_inds(self):
        """
        List of selected indexes into the trace's points

        Returns
        -------
        list[int]
        """
    @property
    def xs(self):
        """
        List of x-coordinates of selected points

        Returns
        -------
        list[float]
        """
    @property
    def ys(self):
        """
        List of y-coordinates of selected points

        Returns
        -------
        list[float]
        """
    @property
    def trace_name(self):
        """
        Name of the trace

        Returns
        -------
        str
        """
    @property
    def trace_index(self):
        """
        Index of the trace in the figure

        Returns
        -------
        int
        """

class BoxSelector:
    def __init__(self, xrange: Incomplete | None = None, yrange: Incomplete | None = None, **_) -> None: ...
    @property
    def type(self):
        """
        The selector's type

        Returns
        -------
        str
        """
    @property
    def xrange(self):
        """
        x-axis range extents of the box selection

        Returns
        -------
        (float, float)
        """
    @property
    def yrange(self):
        """
        y-axis range extents of the box selection

        Returns
        -------
        (float, float)
        """

class LassoSelector:
    def __init__(self, xs: Incomplete | None = None, ys: Incomplete | None = None, **_) -> None: ...
    @property
    def type(self):
        """
        The selector's type

        Returns
        -------
        str
        """
    @property
    def xs(self):
        """
        list of x-axis coordinates of each point in the lasso selection
        boundary

        Returns
        -------
        list[float]
        """
    @property
    def ys(self):
        """
        list of y-axis coordinates of each point in the lasso selection
        boundary

        Returns
        -------
        list[float]
        """
