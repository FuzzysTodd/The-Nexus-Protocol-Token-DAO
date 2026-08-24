from _typeshed import Incomplete
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Lonaxis(_BaseLayoutHierarchyType):
    @property
    def dtick(self):
        """
        Sets the graticule's longitude/latitude tick step.

        The 'dtick' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @dtick.setter
    def dtick(self, val) -> None: ...
    @property
    def gridcolor(self):
        """
        Sets the graticule's stroke color.

        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
    @gridcolor.setter
    def gridcolor(self, val) -> None: ...
    @property
    def griddash(self):
        '''
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The \'griddash\' property is an enumeration that may be specified as:
          - One of the following dash styles:
                [\'solid\', \'dot\', \'dash\', \'longdash\', \'dashdot\', \'longdashdot\']
          - A string containing a dash length list in pixels or percentages
                (e.g. \'5px 10px 2px 2px\', \'5, 10, 2, 2\', \'10% 20% 40%\', etc.)

        Returns
        -------
        str
        '''
    @griddash.setter
    def griddash(self, val) -> None: ...
    @property
    def gridwidth(self):
        """
        Sets the graticule's stroke width (in px).

        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
    @gridwidth.setter
    def gridwidth(self, val) -> None: ...
    @property
    def range(self):
        """
            Sets the range of this axis (in degrees), sets the map's
            clipped coordinates.

            The 'range' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'range[0]' property is a number and may be specified as:
              - An int or float
        (1) The 'range[1]' property is a number and may be specified as:
              - An int or float

            Returns
            -------
            list
        """
    @range.setter
    def range(self, val) -> None: ...
    @property
    def showgrid(self):
        """
        Sets whether or not graticule are shown on the map.

        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
    @showgrid.setter
    def showgrid(self, val) -> None: ...
    @property
    def tick0(self):
        """
        Sets the graticule's starting tick longitude/latitude.

        The 'tick0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
    @tick0.setter
    def tick0(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, dtick: Incomplete | None = None, gridcolor: Incomplete | None = None, griddash: Incomplete | None = None, gridwidth: Incomplete | None = None, range: Incomplete | None = None, showgrid: Incomplete | None = None, tick0: Incomplete | None = None, **kwargs) -> None:
        '''
        Construct a new Lonaxis object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.geo.Lonaxis`
        dtick
            Sets the graticule\'s longitude/latitude tick step.
        gridcolor
            Sets the graticule\'s stroke color.
        griddash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        gridwidth
            Sets the graticule\'s stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map\'s clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule\'s starting tick longitude/latitude.

        Returns
        -------
        Lonaxis
        '''
