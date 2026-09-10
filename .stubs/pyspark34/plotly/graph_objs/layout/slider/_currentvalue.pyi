from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Currentvalue(_BaseLayoutHierarchyType):
    @property
    def font(self):
        '''
        Sets the font of the current value label text.

        The \'font\' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.currentvalue.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

            Supported dict properties:

                color

                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren\'t available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.slider.currentvalue.Font
        '''
    @font.setter
    def font(self, val) -> None: ...
    @property
    def offset(self):
        """
        The amount of space, in pixels, between the current value label
        and the slider.

        The 'offset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @offset.setter
    def offset(self, val) -> None: ...
    @property
    def prefix(self):
        """
        When currentvalue.visible is true, this sets the prefix of the
        label.

        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
    @prefix.setter
    def prefix(self, val) -> None: ...
    @property
    def suffix(self):
        """
        When currentvalue.visible is true, this sets the suffix of the
        label.

        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
    @suffix.setter
    def suffix(self, val) -> None: ...
    @property
    def visible(self):
        """
        Shows the currently-selected value above the slider.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
    @visible.setter
    def visible(self, val) -> None: ...
    @property
    def xanchor(self):
        """
        The alignment of the value readout relative to the length of
        the slider.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
    @xanchor.setter
    def xanchor(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, font: Incomplete | None = None, offset: Incomplete | None = None, prefix: Incomplete | None = None, suffix: Incomplete | None = None, visible: Incomplete | None = None, xanchor: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Currentvalue object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.slider.Currentvalue`
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.

        Returns
        -------
        Currentvalue
        """
