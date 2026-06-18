from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Pattern(_BaseTraceHierarchyType):
    @property
    def bgcolor(self):
        '''
        When there is no colorscale sets the color of background
        pattern fill. Defaults to a `marker.color` background when
        `fillmode` is "overlay". Otherwise, defaults to a transparent
        background.

        The \'bgcolor\' property is a color and may be specified as:
          - A hex string (e.g. \'#ff0000\')
          - An rgb/rgba string (e.g. \'rgb(255,0,0)\')
          - An hsl/hsla string (e.g. \'hsl(0,100%,50%)\')
          - An hsv/hsva string (e.g. \'hsv(0,100%,100%)\')
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        '''
    @bgcolor.setter
    def bgcolor(self, val) -> None: ...
    @property
    def bgcolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `bgcolor`.

        The 'bgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
    @bgcolorsrc.setter
    def bgcolorsrc(self, val) -> None: ...
    @property
    def fgcolor(self):
        '''
        When there is no colorscale sets the color of foreground
        pattern fill. Defaults to a `marker.color` background when
        `fillmode` is "replace". Otherwise, defaults to dark grey or
        white to increase contrast with the `bgcolor`.

        The \'fgcolor\' property is a color and may be specified as:
          - A hex string (e.g. \'#ff0000\')
          - An rgb/rgba string (e.g. \'rgb(255,0,0)\')
          - An hsl/hsla string (e.g. \'hsl(0,100%,50%)\')
          - An hsv/hsva string (e.g. \'hsv(0,100%,100%)\')
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        '''
    @fgcolor.setter
    def fgcolor(self, val) -> None: ...
    @property
    def fgcolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `fgcolor`.

        The 'fgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
    @fgcolorsrc.setter
    def fgcolorsrc(self, val) -> None: ...
    @property
    def fgopacity(self):
        '''
        Sets the opacity of the foreground pattern fill. Defaults to a
        0.5 when `fillmode` is "overlay". Otherwise, defaults to 1.

        The \'fgopacity\' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        '''
    @fgopacity.setter
    def fgopacity(self, val) -> None: ...
    @property
    def fillmode(self):
        """
        Determines whether `marker.color` should be used as a default
        to `bgcolor` or a `fgcolor`.

        The 'fillmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['replace', 'overlay']

        Returns
        -------
        Any
        """
    @fillmode.setter
    def fillmode(self, val) -> None: ...
    @property
    def shape(self):
        """
        Sets the shape of the pattern fill. By default, no pattern is
        used for filling the area.

        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['', '/', '\\', 'x', '-', '|', '+', '.']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
    @shape.setter
    def shape(self, val) -> None: ...
    @property
    def shapesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `shape`.

        The 'shapesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
    @shapesrc.setter
    def shapesrc(self, val) -> None: ...
    @property
    def size(self):
        """
        Sets the size of unit squares of the pattern fill in pixels,
        which corresponds to the interval of repetition of the pattern.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
    @size.setter
    def size(self, val) -> None: ...
    @property
    def sizesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `size`.

        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
    @sizesrc.setter
    def sizesrc(self, val) -> None: ...
    @property
    def solidity(self):
        """
        Sets the solidity of the pattern fill. Solidity is roughly the
        fraction of the area filled by the pattern. Solidity of 0 shows
        only the background color without pattern and solidty of 1
        shows only the foreground color without pattern.

        The 'solidity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
    @solidity.setter
    def solidity(self, val) -> None: ...
    @property
    def soliditysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `solidity`.

        The 'soliditysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
    @soliditysrc.setter
    def soliditysrc(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, bgcolor: Incomplete | None = None, bgcolorsrc: Incomplete | None = None, fgcolor: Incomplete | None = None, fgcolorsrc: Incomplete | None = None, fgopacity: Incomplete | None = None, fillmode: Incomplete | None = None, shape: Incomplete | None = None, shapesrc: Incomplete | None = None, size: Incomplete | None = None, sizesrc: Incomplete | None = None, solidity: Incomplete | None = None, soliditysrc: Incomplete | None = None, **kwargs) -> None:
        '''
        Construct a new Pattern object

        Sets the pattern within the marker.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.pie.marker.Pattern`
        bgcolor
            When there is no colorscale sets the color of
            background pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "overlay". Otherwise,
            defaults to a transparent background.
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `bgcolor`.
        fgcolor
            When there is no colorscale sets the color of
            foreground pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "replace". Otherwise,
            defaults to dark grey or white to increase contrast
            with the `bgcolor`.
        fgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `fgcolor`.
        fgopacity
            Sets the opacity of the foreground pattern fill.
            Defaults to a 0.5 when `fillmode` is "overlay".
            Otherwise, defaults to 1.
        fillmode
            Determines whether `marker.color` should be used as a
            default to `bgcolor` or a `fgcolor`.
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        shapesrc
            Sets the source reference on Chart Studio Cloud for
            `shape`.
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.
        soliditysrc
            Sets the source reference on Chart Studio Cloud for
            `solidity`.

        Returns
        -------
        Pattern
        '''
