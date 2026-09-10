from _typeshed import Incomplete
from matplotlib.colors import Colormap as Colormap
from pandas import IndexSlice as IndexSlice, RangeIndex as RangeIndex
from pandas._config import get_option as get_option
from pandas._typing import Axis as Axis, AxisInt as AxisInt, FilePath as FilePath, IndexLabel as IndexLabel, Level as Level, QuantileInterpolation as QuantileInterpolation, Scalar as Scalar, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.frame import DataFrame as DataFrame, Series as Series
from pandas.core.generic import NDFrame as NDFrame
from pandas.io.formats.format import save_to_buffer as save_to_buffer
from pandas.io.formats.style_render import CSSProperties as CSSProperties, CSSStyles as CSSStyles, ExtFormatter as ExtFormatter, StylerRenderer as StylerRenderer, Subset as Subset, Tooltips as Tooltips, format_table_styles as format_table_styles, maybe_convert_css_to_tuples as maybe_convert_css_to_tuples, non_reducing_slice as non_reducing_slice, refactor_levels as refactor_levels
from pandas.util._decorators import Substitution as Substitution, doc as doc
from typing import Any, Callable, Hashable, Sequence, overload

jinja2: Incomplete
has_mpl: bool
subset_args: str
properties_args: str
coloring_args: str
buffering_args: str
encoding_args: str

class Styler(StylerRenderer):
    '''
    Helps style a DataFrame or Series according to the data with HTML and CSS.

    Parameters
    ----------
    data : Series or DataFrame
        Data to be styled - either a Series or DataFrame.
    precision : int, optional
        Precision to round floats to. If not given defaults to
        ``pandas.options.styler.format.precision``.

        .. versionchanged:: 1.4.0
    table_styles : list-like, default None
        List of {selector: (attr, value)} dicts; see Notes.
    uuid : str, default None
        A unique identifier to avoid CSS collisions; generated automatically.
    caption : str, tuple, default None
        String caption to attach to the table. Tuple only used for LaTeX dual captions.
    table_attributes : str, default None
        Items that show up in the opening ``<table>`` tag
        in addition to automatic (by default) id.
    cell_ids : bool, default True
        If True, each cell will have an ``id`` attribute in their HTML tag.
        The ``id`` takes the form ``T_<uuid>_row<num_row>_col<num_col>``
        where ``<uuid>`` is the unique identifier, ``<num_row>`` is the row
        number and ``<num_col>`` is the column number.
    na_rep : str, optional
        Representation for missing values.
        If ``na_rep`` is None, no special formatting is applied, and falls back to
        ``pandas.options.styler.format.na_rep``.

    uuid_len : int, default 5
        If ``uuid`` is not specified, the length of the ``uuid`` to randomly generate
        expressed in hex characters, in range [0, 32].

        .. versionadded:: 1.2.0

    decimal : str, optional
        Character used as decimal separator for floats, complex and integers. If not
        given uses ``pandas.options.styler.format.decimal``.

        .. versionadded:: 1.3.0

    thousands : str, optional, default None
        Character used as thousands separator for floats, complex and integers. If not
        given uses ``pandas.options.styler.format.thousands``.

        .. versionadded:: 1.3.0

    escape : str, optional
        Use \'html\' to replace the characters ``&``, ``<``, ``>``, ``\'``, and ``"``
        in cell display string with HTML-safe sequences.
        Use \'latex\' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
        ``{``, ``}``, ``~``, ``^``, and ``\\`` in the cell display string with
        LaTeX-safe sequences. If not given uses ``pandas.options.styler.format.escape``.

        .. versionadded:: 1.3.0
    formatter : str, callable, dict, optional
        Object to define how values are displayed. See ``Styler.format``. If not given
        uses ``pandas.options.styler.format.formatter``.

        .. versionadded:: 1.4.0

    Attributes
    ----------
    env : Jinja2 jinja2.Environment
    template_html : Jinja2 Template
    template_html_table : Jinja2 Template
    template_html_style : Jinja2 Template
    template_latex : Jinja2 Template
    loader : Jinja2 Loader

    See Also
    --------
    DataFrame.style : Return a Styler object containing methods for building
        a styled HTML representation for the DataFrame.

    Notes
    -----
    Most styling will be done by passing style functions into
    ``Styler.apply`` or ``Styler.applymap``. Style functions should
    return values with strings containing CSS ``\'attr: value\'`` that will
    be applied to the indicated cells.

    If using in the Jupyter notebook, Styler has defined a ``_repr_html_``
    to automatically render itself. Otherwise call Styler.to_html to get
    the generated HTML.

    CSS classes are attached to the generated HTML

    * Index and Column names include ``index_name`` and ``level<k>``
      where `k` is its level in a MultiIndex
    * Index label cells include

      * ``row_heading``
      * ``row<n>`` where `n` is the numeric position of the row
      * ``level<k>`` where `k` is the level in a MultiIndex

    * Column label cells include
      * ``col_heading``
      * ``col<n>`` where `n` is the numeric position of the column
      * ``level<k>`` where `k` is the level in a MultiIndex

    * Blank cells include ``blank``
    * Data cells include ``data``
    * Trimmed cells include ``col_trim`` or ``row_trim``.

    Any, or all, or these classes can be renamed by using the ``css_class_names``
    argument in ``Styler.set_table_classes``, giving a value such as
    *{"row": "MY_ROW_CLASS", "col_trim": "", "row_trim": ""}*.
    '''
    def __init__(self, data: DataFrame | Series, precision: int | None = None, table_styles: CSSStyles | None = None, uuid: str | None = None, caption: str | tuple | list | None = None, table_attributes: str | None = None, cell_ids: bool = True, na_rep: str | None = None, uuid_len: int = 5, decimal: str | None = None, thousands: str | None = None, escape: str | None = None, formatter: ExtFormatter | None = None) -> None: ...
    def concat(self, other: Styler) -> Styler:
        '''
        Append another Styler to combine the output into a single table.

        .. versionadded:: 1.5.0

        Parameters
        ----------
        other : Styler
            The other Styler object which has already been styled and formatted. The
            data for this Styler must have the same columns as the original, and the
            number of index levels must also be the same to render correctly.

        Returns
        -------
        Styler

        Notes
        -----
        The purpose of this method is to extend existing styled dataframes with other
        metrics that may be useful but may not conform to the original\'s structure.
        For example adding a sub total row, or displaying metrics such as means,
        variance or counts.

        Styles that are applied using the ``apply``, ``applymap``, ``apply_index``
        and ``applymap_index``, and formatting applied with ``format`` and
        ``format_index`` will be preserved.

        .. warning::
            Only the output methods ``to_html``, ``to_string`` and ``to_latex``
            currently work with concatenated Stylers.

            Other output methods, including ``to_excel``, **do not** work with
            concatenated Stylers.

        The following should be noted:

          - ``table_styles``, ``table_attributes``, ``caption`` and ``uuid`` are all
            inherited from the original Styler and not ``other``.
          - hidden columns and hidden index levels will be inherited from the
            original Styler
          - ``css`` will be inherited from the original Styler, and the value of
            keys ``data``, ``row_heading`` and ``row`` will be prepended with
            ``foot0_``. If more concats are chained, their styles will be prepended
            with ``foot1_``, \'\'foot_2\'\', etc., and if a concatenated style have
            another concatanated style, the second style will be prepended with
            ``foot{parent}_foot{child}_``.

        A common use case is to concatenate user defined functions with
        ``DataFrame.agg`` or with described statistics via ``DataFrame.describe``.
        See examples.

        Examples
        --------
        A common use case is adding totals rows, or otherwise, via methods calculated
        in ``DataFrame.agg``.

        >>> df = DataFrame([[4, 6], [1, 9], [3, 4], [5, 5], [9,6]],
        ...                columns=["Mike", "Jim"],
        ...                index=["Mon", "Tue", "Wed", "Thurs", "Fri"])
        >>> styler = df.style.concat(df.agg(["sum"]).style)  # doctest: +SKIP

        .. figure:: ../../_static/style/footer_simple.png

        Since the concatenated object is a Styler the existing functionality can be
        used to conditionally format it as well as the original.

        >>> descriptors = df.agg(["sum", "mean", lambda s: s.dtype])
        >>> descriptors.index = ["Total", "Average", "dtype"]
        >>> other = (descriptors.style
        ...          .highlight_max(axis=1, subset=(["Total", "Average"], slice(None)))
        ...          .format(subset=("Average", slice(None)), precision=2, decimal=",")
        ...          .applymap(lambda v: "font-weight: bold;"))
        >>> styler = (df.style
        ...             .highlight_max(color="salmon")
        ...             .set_table_styles([{"selector": ".foot_row0",
        ...                                 "props": "border-top: 1px solid black;"}]))
        >>> styler.concat(other)  # doctest: +SKIP

        .. figure:: ../../_static/style/footer_extended.png

        When ``other`` has fewer index levels than the original Styler it is possible
        to extend the index in ``other``, with placeholder levels.

        >>> df = DataFrame([[1], [2]], index=pd.MultiIndex.from_product([[0], [1, 2]]))
        >>> descriptors = df.agg(["sum"])
        >>> descriptors.index = pd.MultiIndex.from_product([[""], descriptors.index])
        >>> df.style.concat(descriptors.style)  # doctest: +SKIP
        '''
    tooltips: Incomplete
    def set_tooltips(self, ttips: DataFrame, props: CSSProperties | None = None, css_class: str | None = None) -> Styler:
        '''
        Set the DataFrame of strings on ``Styler`` generating ``:hover`` tooltips.

        These string based tooltips are only applicable to ``<td>`` HTML elements,
        and cannot be used for column or index headers.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        ttips : DataFrame
            DataFrame containing strings that will be translated to tooltips, mapped
            by identical column and index values that must exist on the underlying
            Styler data. None, NaN values, and empty strings will be ignored and
            not affect the rendered HTML.
        props : list-like or str, optional
            List of (attr, value) tuples or a valid CSS string. If ``None`` adopts
            the internal default values described in notes.
        css_class : str, optional
            Name of the tooltip class used in CSS, should conform to HTML standards.
            Only useful if integrating tooltips with external CSS. If ``None`` uses the
            internal default value \'pd-t\'.

        Returns
        -------
        Styler

        Notes
        -----
        Tooltips are created by adding `<span class="pd-t"></span>` to each data cell
        and then manipulating the table level CSS to attach pseudo hover and pseudo
        after selectors to produce the required the results.

        The default properties for the tooltip CSS class are:

        - visibility: hidden
        - position: absolute
        - z-index: 1
        - background-color: black
        - color: white
        - transform: translate(-20px, -20px)

        The property \'visibility: hidden;\' is a key prerequisite to the hover
        functionality, and should always be included in any manual properties
        specification, using the ``props`` argument.

        Tooltips are not designed to be efficient, and can add large amounts of
        additional HTML for larger tables, since they also require that ``cell_ids``
        is forced to `True`.

        Examples
        --------
        Basic application

        >>> df = pd.DataFrame(data=[[0, 1], [2, 3]])
        >>> ttips = pd.DataFrame(
        ...    data=[["Min", ""], [np.nan, "Max"]], columns=df.columns, index=df.index
        ... )
        >>> s = df.style.set_tooltips(ttips).to_html()

        Optionally controlling the tooltip visual display

        >>> df.style.set_tooltips(ttips, css_class=\'tt-add\', props=[
        ...     (\'visibility\', \'hidden\'),
        ...     (\'position\', \'absolute\'),
        ...     (\'z-index\', 1)])  # doctest: +SKIP
        >>> df.style.set_tooltips(ttips, css_class=\'tt-add\',
        ...     props=\'visibility:hidden; position:absolute; z-index:1;\')
        ... # doctest: +SKIP
        '''
    def to_excel(self, excel_writer, sheet_name: str = 'Sheet1', na_rep: str = '', float_format: str | None = None, columns: Sequence[Hashable] | None = None, header: Sequence[Hashable] | bool = True, index: bool = True, index_label: IndexLabel | None = None, startrow: int = 0, startcol: int = 0, engine: str | None = None, merge_cells: bool = True, encoding: str | None = None, inf_rep: str = 'inf', verbose: bool = True, freeze_panes: tuple[int, int] | None = None, storage_options: StorageOptions = None) -> None: ...
    @overload
    def to_latex(self, buf: FilePath | WriteBuffer[str], *, column_format: str | None = ..., position: str | None = ..., position_float: str | None = ..., hrules: bool | None = ..., clines: str | None = ..., label: str | None = ..., caption: str | tuple | None = ..., sparse_index: bool | None = ..., sparse_columns: bool | None = ..., multirow_align: str | None = ..., multicol_align: str | None = ..., siunitx: bool = ..., environment: str | None = ..., encoding: str | None = ..., convert_css: bool = ...) -> None: ...
    @overload
    def to_latex(self, buf: None = ..., *, column_format: str | None = ..., position: str | None = ..., position_float: str | None = ..., hrules: bool | None = ..., clines: str | None = ..., label: str | None = ..., caption: str | tuple | None = ..., sparse_index: bool | None = ..., sparse_columns: bool | None = ..., multirow_align: str | None = ..., multicol_align: str | None = ..., siunitx: bool = ..., environment: str | None = ..., encoding: str | None = ..., convert_css: bool = ...) -> str: ...
    @overload
    def to_html(self, buf: FilePath | WriteBuffer[str], *, table_uuid: str | None = ..., table_attributes: str | None = ..., sparse_index: bool | None = ..., sparse_columns: bool | None = ..., bold_headers: bool = ..., caption: str | None = ..., max_rows: int | None = ..., max_columns: int | None = ..., encoding: str | None = ..., doctype_html: bool = ..., exclude_styles: bool = ..., **kwargs) -> None: ...
    @overload
    def to_html(self, buf: None = ..., *, table_uuid: str | None = ..., table_attributes: str | None = ..., sparse_index: bool | None = ..., sparse_columns: bool | None = ..., bold_headers: bool = ..., caption: str | None = ..., max_rows: int | None = ..., max_columns: int | None = ..., encoding: str | None = ..., doctype_html: bool = ..., exclude_styles: bool = ..., **kwargs) -> str: ...
    @overload
    def to_string(self, buf: FilePath | WriteBuffer[str], *, encoding=..., sparse_index: bool | None = ..., sparse_columns: bool | None = ..., max_rows: int | None = ..., max_columns: int | None = ..., delimiter: str = ...) -> None: ...
    @overload
    def to_string(self, buf: None = ..., *, encoding=..., sparse_index: bool | None = ..., sparse_columns: bool | None = ..., max_rows: int | None = ..., max_columns: int | None = ..., delimiter: str = ...) -> str: ...
    def set_td_classes(self, classes: DataFrame) -> Styler:
        '''
        Set the ``class`` attribute of ``<td>`` HTML elements.

        Parameters
        ----------
        classes : DataFrame
            DataFrame containing strings that will be translated to CSS classes,
            mapped by identical column and index key values that must exist on the
            underlying Styler data. None, NaN values, and empty strings will
            be ignored and not affect the rendered HTML.

        Returns
        -------
        Styler

        See Also
        --------
        Styler.set_table_styles: Set the table styles included within the ``<style>``
            HTML element.
        Styler.set_table_attributes: Set the table attributes added to the ``<table>``
            HTML element.

        Notes
        -----
        Can be used in combination with ``Styler.set_table_styles`` to define an
        internal CSS solution without reference to external CSS files.

        Examples
        --------
        >>> df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=["A", "B", "C"])
        >>> classes = pd.DataFrame([
        ...     ["min-val red", "", "blue"],
        ...     ["red", None, "blue max-val"]
        ... ], index=df.index, columns=df.columns)
        >>> df.style.set_td_classes(classes)  # doctest: +SKIP

        Using `MultiIndex` columns and a `classes` `DataFrame` as a subset of the
        underlying,

        >>> df = pd.DataFrame([[1,2],[3,4]], index=["a", "b"],
        ...     columns=[["level0", "level0"], ["level1a", "level1b"]])
        >>> classes = pd.DataFrame(["min-val"], index=["a"],
        ...     columns=[["level0"],["level1a"]])
        >>> df.style.set_td_classes(classes)  # doctest: +SKIP

        Form of the output with new additional css classes,

        >>> df = pd.DataFrame([[1]])
        >>> css = pd.DataFrame([["other-class"]])
        >>> s = Styler(df, uuid="_", cell_ids=False).set_td_classes(css)
        >>> s.hide(axis=0).to_html()  # doctest: +SKIP
        \'<style type="text/css"></style>\'
        \'<table id="T__">\'
        \'  <thead>\'
        \'    <tr><th class="col_heading level0 col0" >0</th></tr>\'
        \'  </thead>\'
        \'  <tbody>\'
        \'    <tr><td class="data row0 col0 other-class" >1</td></tr>\'
        \'  </tbody>\'
        \'</table>\'
        '''
    def __copy__(self) -> Styler: ...
    def __deepcopy__(self, memo) -> Styler: ...
    def clear(self) -> None:
        """
        Reset the ``Styler``, removing any previously applied styles.

        Returns None.
        """
    def apply(self, func: Callable, axis: Axis | None = 0, subset: Subset | None = None, **kwargs) -> Styler:
        '''
        Apply a CSS-styling function column-wise, row-wise, or table-wise.

        Updates the HTML representation with the result.

        Parameters
        ----------
        func : function
            ``func`` should take a Series if ``axis`` in [0,1] and return a list-like
            object of same length, or a Series, not necessarily of same length, with
            valid index labels considering ``subset``.
            ``func`` should take a DataFrame if ``axis`` is ``None`` and return either
            an ndarray with the same shape or a DataFrame, not necessarily of the same
            shape, with valid index and columns labels considering ``subset``.

            .. versionchanged:: 1.3.0

            .. versionchanged:: 1.4.0

        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            Apply to each column (``axis=0`` or ``\'index\'``), to each row
            (``axis=1`` or ``\'columns\'``), or to the entire DataFrame at once
            with ``axis=None``.
        %(subset)s
        **kwargs : dict
            Pass along to ``func``.

        Returns
        -------
        Styler

        See Also
        --------
        Styler.applymap_index: Apply a CSS-styling function to headers elementwise.
        Styler.apply_index: Apply a CSS-styling function to headers level-wise.
        Styler.applymap: Apply a CSS-styling function elementwise.

        Notes
        -----
        The elements of the output of ``func`` should be CSS styles as strings, in the
        format \'attribute: value; attribute2: value2; ...\' or,
        if nothing is to be applied to that element, an empty string or ``None``.

        This is similar to ``DataFrame.apply``, except that ``axis=None``
        applies the function to the entire DataFrame at once,
        rather than column-wise or row-wise.

        Examples
        --------
        >>> def highlight_max(x, color):
        ...     return np.where(x == np.nanmax(x.to_numpy()), f"color: {color};", None)
        >>> df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
        >>> df.style.apply(highlight_max, color=\'red\')  # doctest: +SKIP
        >>> df.style.apply(highlight_max, color=\'blue\', axis=1)  # doctest: +SKIP
        >>> df.style.apply(highlight_max, color=\'green\', axis=None)  # doctest: +SKIP

        Using ``subset`` to restrict application to a single column or multiple columns

        >>> df.style.apply(highlight_max, color=\'red\', subset="A")
        ...  # doctest: +SKIP
        >>> df.style.apply(highlight_max, color=\'red\', subset=["A", "B"])
        ...  # doctest: +SKIP

        Using a 2d input to ``subset`` to select rows in addition to columns

        >>> df.style.apply(highlight_max, color=\'red\', subset=([0,1,2], slice(None)))
        ...  # doctest: +SKIP
        >>> df.style.apply(highlight_max, color=\'red\', subset=(slice(0,5,2), "A"))
        ...  # doctest: +SKIP

        Using a function which returns a Series / DataFrame of unequal length but
        containing valid index labels

        >>> df = pd.DataFrame([[1, 2], [3, 4], [4, 6]], index=["A1", "A2", "Total"])
        >>> total_style = pd.Series("font-weight: bold;", index=["Total"])
        >>> df.style.apply(lambda s: total_style)  # doctest: +SKIP

        See `Table Visualization <../../user_guide/style.ipynb>`_ user guide for
        more details.
        '''
    def apply_index(self, func: Callable, axis: AxisInt | str = 0, level: Level | list[Level] | None = None, **kwargs) -> Styler:
        '''
        Apply a CSS-styling function to the index or column headers, {wise}.

        Updates the HTML representation with the result.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        func : function
            ``func`` should {func}.
        axis : {{0, 1, "index", "columns"}}
            The headers over which to apply the function.
        level : int, str, list, optional
            If index is MultiIndex the level(s) over which to apply the function.
        **kwargs : dict
            Pass along to ``func``.

        Returns
        -------
        Styler

        See Also
        --------
        Styler.{alt}_index: Apply a CSS-styling function to headers {altwise}.
        Styler.apply: Apply a CSS-styling function column-wise, row-wise, or table-wise.
        Styler.applymap: Apply a CSS-styling function elementwise.

        Notes
        -----
        Each input to ``func`` will be {input_note}. The output of ``func`` should be
        {output_note}, in the format \'attribute: value; attribute2: value2; ...\'
        or, if nothing is to be applied to that element, an empty string or ``None``.

        Examples
        --------
        Basic usage to conditionally highlight values in the index.

        >>> df = pd.DataFrame([[1,2], [3,4]], index=["A", "B"])
        >>> def color_b(s):
        ...     return {ret}
        >>> df.style.{this}_index(color_b)  # doctest: +SKIP

        .. figure:: ../../_static/style/appmaphead1.png

        Selectively applying to specific levels of MultiIndex columns.

        >>> midx = pd.MultiIndex.from_product([[\'ix\', \'jy\'], [0, 1], [\'x3\', \'z4\']])
        >>> df = pd.DataFrame([np.arange(8)], columns=midx)
        >>> def highlight_x({var}):
        ...     return {ret2}
        >>> df.style.{this}_index(highlight_x, axis="columns", level=[0, 2])
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/appmaphead2.png
        '''
    def applymap_index(self, func: Callable, axis: AxisInt | str = 0, level: Level | list[Level] | None = None, **kwargs) -> Styler: ...
    def applymap(self, func: Callable, subset: Subset | None = None, **kwargs) -> Styler:
        '''
        Apply a CSS-styling function elementwise.

        Updates the HTML representation with the result.

        Parameters
        ----------
        func : function
            ``func`` should take a scalar and return a string.
        %(subset)s
        **kwargs : dict
            Pass along to ``func``.

        Returns
        -------
        Styler

        See Also
        --------
        Styler.applymap_index: Apply a CSS-styling function to headers elementwise.
        Styler.apply_index: Apply a CSS-styling function to headers level-wise.
        Styler.apply: Apply a CSS-styling function column-wise, row-wise, or table-wise.

        Notes
        -----
        The elements of the output of ``func`` should be CSS styles as strings, in the
        format \'attribute: value; attribute2: value2; ...\' or,
        if nothing is to be applied to that element, an empty string or ``None``.

        Examples
        --------
        >>> def color_negative(v, color):
        ...     return f"color: {color};" if v < 0 else None
        >>> df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
        >>> df.style.applymap(color_negative, color=\'red\')  # doctest: +SKIP

        Using ``subset`` to restrict application to a single column or multiple columns

        >>> df.style.applymap(color_negative, color=\'red\', subset="A")
        ...  # doctest: +SKIP
        >>> df.style.applymap(color_negative, color=\'red\', subset=["A", "B"])
        ...  # doctest: +SKIP

        Using a 2d input to ``subset`` to select rows in addition to columns

        >>> df.style.applymap(color_negative, color=\'red\',
        ...  subset=([0,1,2], slice(None)))  # doctest: +SKIP
        >>> df.style.applymap(color_negative, color=\'red\', subset=(slice(0,5,2), "A"))
        ...  # doctest: +SKIP

        See `Table Visualization <../../user_guide/style.ipynb>`_ user guide for
        more details.
        '''
    table_attributes: Incomplete
    def set_table_attributes(self, attributes: str) -> Styler:
        '''
        Set the table attributes added to the ``<table>`` HTML element.

        These are items in addition to automatic (by default) ``id`` attribute.

        Parameters
        ----------
        attributes : str

        Returns
        -------
        Styler

        See Also
        --------
        Styler.set_table_styles: Set the table styles included within the ``<style>``
            HTML element.
        Styler.set_td_classes: Set the DataFrame of strings added to the ``class``
            attribute of ``<td>`` HTML elements.

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4))
        >>> df.style.set_table_attributes(\'class="pure-table"\')  # doctest: +SKIP
        # ... <table class="pure-table"> ...
        '''
    def export(self) -> dict[str, Any]:
        """
        Export the styles applied to the current Styler.

        Can be applied to a second Styler with ``Styler.use``.

        Returns
        -------
        dict

        See Also
        --------
        Styler.use: Set the styles on the current Styler.
        Styler.copy: Create a copy of the current Styler.

        Notes
        -----
        This method is designed to copy non-data dependent attributes of
        one Styler to another. It differs from ``Styler.copy`` where data and
        data dependent attributes are also copied.

        The following items are exported since they are not generally data dependent:

          - Styling functions added by the ``apply`` and ``applymap``
          - Whether axes and names are hidden from the display, if unambiguous.
          - Table attributes
          - Table styles

        The following attributes are considered data dependent and therefore not
        exported:

          - Caption
          - UUID
          - Tooltips
          - Any hidden rows or columns identified by Index labels
          - Any formatting applied using ``Styler.format``
          - Any CSS classes added using ``Styler.set_td_classes``

        Examples
        --------

        >>> styler = DataFrame([[1, 2], [3, 4]]).style
        >>> styler2 = DataFrame([[9, 9, 9]]).style
        >>> styler.hide(axis=0).highlight_max(axis=1)  # doctest: +SKIP
        >>> export = styler.export()
        >>> styler2.use(export)  # doctest: +SKIP
        """
    hide_index_names: Incomplete
    hide_column_names: Incomplete
    css: Incomplete
    def use(self, styles: dict[str, Any]) -> Styler:
        '''
        Set the styles on the current Styler.

        Possibly uses styles from ``Styler.export``.

        Parameters
        ----------
        styles : dict(str, Any)
            List of attributes to add to Styler. Dict keys should contain only:
              - "apply": list of styler functions, typically added with ``apply`` or
                ``applymap``.
              - "table_attributes": HTML attributes, typically added with
                ``set_table_attributes``.
              - "table_styles": CSS selectors and properties, typically added with
                ``set_table_styles``.
              - "hide_index":  whether the index is hidden, typically added with
                ``hide_index``, or a boolean list for hidden levels.
              - "hide_columns": whether column headers are hidden, typically added with
                ``hide_columns``, or a boolean list for hidden levels.
              - "hide_index_names": whether index names are hidden.
              - "hide_column_names": whether column header names are hidden.
              - "css": the css class names used.

        Returns
        -------
        Styler

        See Also
        --------
        Styler.export : Export the non data dependent attributes to the current Styler.

        Examples
        --------

        >>> styler = DataFrame([[1, 2], [3, 4]]).style
        >>> styler2 = DataFrame([[9, 9, 9]]).style
        >>> styler.hide(axis=0).highlight_max(axis=1)  # doctest: +SKIP
        >>> export = styler.export()
        >>> styler2.use(export)  # doctest: +SKIP
        '''
    uuid: Incomplete
    def set_uuid(self, uuid: str) -> Styler:
        """
        Set the uuid applied to ``id`` attributes of HTML elements.

        Parameters
        ----------
        uuid : str

        Returns
        -------
        Styler

        Notes
        -----
        Almost all HTML elements within the table, and including the ``<table>`` element
        are assigned ``id`` attributes. The format is ``T_uuid_<extra>`` where
        ``<extra>`` is typically a more specific identifier, such as ``row1_col2``.
        """
    caption: Incomplete
    def set_caption(self, caption: str | tuple | list) -> Styler:
        """
        Set the text added to a ``<caption>`` HTML element.

        Parameters
        ----------
        caption : str, tuple, list
            For HTML output either the string input is used or the first element of the
            tuple. For LaTeX the string input provides a caption and the additional
            tuple input allows for full captions and short captions, in that order.

        Returns
        -------
        Styler
        """
    def set_sticky(self, axis: Axis = 0, pixel_size: int | None = None, levels: Level | list[Level] | None = None) -> Styler:
        '''
        Add CSS to permanently display the index or column headers in a scrolling frame.

        Parameters
        ----------
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            Whether to make the index or column headers sticky.
        pixel_size : int, optional
            Required to configure the width of index cells or the height of column
            header cells when sticking a MultiIndex (or with a named Index).
            Defaults to 75 and 25 respectively.
        levels : int, str, list, optional
            If ``axis`` is a MultiIndex the specific levels to stick. If ``None`` will
            stick all levels.

        Returns
        -------
        Styler

        Notes
        -----
        This method uses the CSS \'position: sticky;\' property to display. It is
        designed to work with visible axes, therefore both:

          - `styler.set_sticky(axis="index").hide(axis="index")`
          - `styler.set_sticky(axis="columns").hide(axis="columns")`

        may produce strange behaviour due to CSS controls with missing elements.
        '''
    table_styles: Incomplete
    def set_table_styles(self, table_styles: dict[Any, CSSStyles] | CSSStyles | None = None, axis: AxisInt = 0, overwrite: bool = True, css_class_names: dict[str, str] | None = None) -> Styler:
        '''
        Set the table styles included within the ``<style>`` HTML element.

        This function can be used to style the entire table, columns, rows or
        specific HTML selectors.

        Parameters
        ----------
        table_styles : list or dict
            If supplying a list, each individual table_style should be a
            dictionary with ``selector`` and ``props`` keys. ``selector``
            should be a CSS selector that the style will be applied to
            (automatically prefixed by the table\'s UUID) and ``props``
            should be a list of tuples with ``(attribute, value)``.
            If supplying a dict, the dict keys should correspond to
            column names or index values, depending upon the specified
            `axis` argument. These will be mapped to row or col CSS
            selectors. MultiIndex values as dict keys should be
            in their respective tuple form. The dict values should be
            a list as specified in the form with CSS selectors and
            props that will be applied to the specified row or column.

            .. versionchanged:: 1.2.0

        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            Apply to each column (``axis=0`` or ``\'index\'``), to each row
            (``axis=1`` or ``\'columns\'``). Only used if `table_styles` is
            dict.

            .. versionadded:: 1.2.0

        overwrite : bool, default True
            Styles are replaced if `True`, or extended if `False`. CSS
            rules are preserved so most recent styles set will dominate
            if selectors intersect.

            .. versionadded:: 1.2.0

        css_class_names : dict, optional
            A dict of strings used to replace the default CSS classes described below.

            .. versionadded:: 1.4.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.set_td_classes: Set the DataFrame of strings added to the ``class``
            attribute of ``<td>`` HTML elements.
        Styler.set_table_attributes: Set the table attributes added to the ``<table>``
            HTML element.

        Notes
        -----
        The default CSS classes dict, whose values can be replaced is as follows:

        .. code-block:: python

            css_class_names = {"row_heading": "row_heading",
                               "col_heading": "col_heading",
                               "index_name": "index_name",
                               "col": "col",
                               "row": "row",
                               "col_trim": "col_trim",
                               "row_trim": "row_trim",
                               "level": "level",
                               "data": "data",
                               "blank": "blank",
                               "foot": "foot"}

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4),
        ...                   columns=[\'A\', \'B\', \'C\', \'D\'])
        >>> df.style.set_table_styles(
        ...     [{\'selector\': \'tr:hover\',
        ...       \'props\': [(\'background-color\', \'yellow\')]}]
        ... )  # doctest: +SKIP

        Or with CSS strings

        >>> df.style.set_table_styles(
        ...     [{\'selector\': \'tr:hover\',
        ...       \'props\': \'background-color: yellow; font-size: 1em;\'}]
        ... )  # doctest: +SKIP

        Adding column styling by name

        >>> df.style.set_table_styles({
        ...     \'A\': [{\'selector\': \'\',
        ...            \'props\': [(\'color\', \'red\')]}],
        ...     \'B\': [{\'selector\': \'td\',
        ...            \'props\': \'color: blue;\'}]
        ... }, overwrite=False)  # doctest: +SKIP

        Adding row styling

        >>> df.style.set_table_styles({
        ...     0: [{\'selector\': \'td:hover\',
        ...          \'props\': [(\'font-size\', \'25px\')]}]
        ... }, axis=1, overwrite=False)  # doctest: +SKIP

        See `Table Visualization <../../user_guide/style.ipynb>`_ user guide for
        more details.
        '''
    def hide(self, subset: Subset | None = None, axis: Axis = 0, level: Level | list[Level] | None = None, names: bool = False) -> Styler:
        '''
        Hide the entire index / column headers, or specific rows / columns from display.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        subset : label, array-like, IndexSlice, optional
            A valid 1d input or single key along the axis within
            `DataFrame.loc[<subset>, :]` or `DataFrame.loc[:, <subset>]` depending
            upon ``axis``, to limit ``data`` to select hidden rows / columns.
        axis : {"index", 0, "columns", 1}
            Apply to the index or columns.
        level : int, str, list
            The level(s) to hide in a MultiIndex if hiding the entire index / column
            headers. Cannot be used simultaneously with ``subset``.
        names : bool
            Whether to hide the level name(s) of the index / columns headers in the case
            it (or at least one the levels) remains visible.

        Returns
        -------
        Styler

        Notes
        -----
        .. warning::
           This method only works with the output methods ``to_html``, ``to_string``
           and ``to_latex``.

           Other output methods, including ``to_excel``, ignore this hiding method
           and will display all data.

        This method has multiple functionality depending upon the combination
        of the ``subset``, ``level`` and ``names`` arguments (see examples). The
        ``axis`` argument is used only to control whether the method is applied to row
        or column headers:

        .. list-table:: Argument combinations
           :widths: 10 20 10 60
           :header-rows: 1

           * - ``subset``
             - ``level``
             - ``names``
             - Effect
           * - None
             - None
             - False
             - The axis-Index is hidden entirely.
           * - None
             - None
             - True
             - Only the axis-Index names are hidden.
           * - None
             - Int, Str, List
             - False
             - Specified axis-MultiIndex levels are hidden entirely.
           * - None
             - Int, Str, List
             - True
             - Specified axis-MultiIndex levels are hidden entirely and the names of
               remaining axis-MultiIndex levels.
           * - Subset
             - None
             - False
             - The specified data rows/columns are hidden, but the axis-Index itself,
               and names, remain unchanged.
           * - Subset
             - None
             - True
             - The specified data rows/columns and axis-Index names are hidden, but
               the axis-Index itself remains unchanged.
           * - Subset
             - Int, Str, List
             - Boolean
             - ValueError: cannot supply ``subset`` and ``level`` simultaneously.

        Note this method only hides the identifed elements so can be chained to hide
        multiple elements in sequence.

        Examples
        --------
        Simple application hiding specific rows:

        >>> df = pd.DataFrame([[1,2], [3,4], [5,6]], index=["a", "b", "c"])
        >>> df.style.hide(["a", "b"])  # doctest: +SKIP
             0    1
        c    5    6

        Hide the index and retain the data values:

        >>> midx = pd.MultiIndex.from_product([["x", "y"], ["a", "b", "c"]])
        >>> df = pd.DataFrame(np.random.randn(6,6), index=midx, columns=midx)
        >>> df.style.format("{:.1f}").hide()  # doctest: +SKIP
                         x                    y
           a      b      c      a      b      c
         0.1    0.0    0.4    1.3    0.6   -1.4
         0.7    1.0    1.3    1.5   -0.0   -0.2
         1.4   -0.8    1.6   -0.2   -0.4   -0.3
         0.4    1.0   -0.2   -0.8   -1.2    1.1
        -0.6    1.2    1.8    1.9    0.3    0.3
         0.8    0.5   -0.3    1.2    2.2   -0.8

        Hide specific rows in a MultiIndex but retain the index:

        >>> df.style.format("{:.1f}").hide(subset=(slice(None), ["a", "c"]))
        ...   # doctest: +SKIP
                                 x                    y
                   a      b      c      a      b      c
        x   b    0.7    1.0    1.3    1.5   -0.0   -0.2
        y   b   -0.6    1.2    1.8    1.9    0.3    0.3

        Hide specific rows and the index through chaining:

        >>> df.style.format("{:.1f}").hide(subset=(slice(None), ["a", "c"])).hide()
        ...   # doctest: +SKIP
                         x                    y
           a      b      c      a      b      c
         0.7    1.0    1.3    1.5   -0.0   -0.2
        -0.6    1.2    1.8    1.9    0.3    0.3

        Hide a specific level:

        >>> df.style.format("{:,.1f}").hide(level=1)  # doctest: +SKIP
                             x                    y
               a      b      c      a      b      c
        x    0.1    0.0    0.4    1.3    0.6   -1.4
             0.7    1.0    1.3    1.5   -0.0   -0.2
             1.4   -0.8    1.6   -0.2   -0.4   -0.3
        y    0.4    1.0   -0.2   -0.8   -1.2    1.1
            -0.6    1.2    1.8    1.9    0.3    0.3
             0.8    0.5   -0.3    1.2    2.2   -0.8

        Hiding just the index level names:

        >>> df.index.names = ["lev0", "lev1"]
        >>> df.style.format("{:,.1f}").hide(names=True)  # doctest: +SKIP
                                 x                    y
                   a      b      c      a      b      c
        x   a    0.1    0.0    0.4    1.3    0.6   -1.4
            b    0.7    1.0    1.3    1.5   -0.0   -0.2
            c    1.4   -0.8    1.6   -0.2   -0.4   -0.3
        y   a    0.4    1.0   -0.2   -0.8   -1.2    1.1
            b   -0.6    1.2    1.8    1.9    0.3    0.3
            c    0.8    0.5   -0.3    1.2    2.2   -0.8

        Examples all produce equivalently transposed effects with ``axis="columns"``.
        '''
    def background_gradient(self, cmap: str | Colormap = 'PuBu', low: float = 0, high: float = 0, axis: Axis | None = 0, subset: Subset | None = None, text_color_threshold: float = 0.408, vmin: float | None = None, vmax: float | None = None, gmap: Sequence | None = None) -> Styler:
        '''
        Color the {name} in a gradient style.

        The {name} color is determined according
        to the data in each column, row or frame, or by a given
        gradient map. Requires matplotlib.

        Parameters
        ----------
        cmap : str or colormap
            Matplotlib colormap.
        low : float
            Compress the color range at the low end. This is a multiple of the data
            range to extend below the minimum; good values usually in [0, 1],
            defaults to 0.
        high : float
            Compress the color range at the high end. This is a multiple of the data
            range to extend above the maximum; good values usually in [0, 1],
            defaults to 0.
        axis : {{0, 1, "index", "columns", None}}, default 0
            Apply to each column (``axis=0`` or ``\'index\'``), to each row
            (``axis=1`` or ``\'columns\'``), or to the entire DataFrame at once
            with ``axis=None``.
        %(subset)s
        {text_threshold}
        vmin : float, optional
            Minimum data value that corresponds to colormap minimum value.
            If not specified the minimum value of the data (or gmap) will be used.
        vmax : float, optional
            Maximum data value that corresponds to colormap maximum value.
            If not specified the maximum value of the data (or gmap) will be used.
        gmap : array-like, optional
            Gradient map for determining the {name} colors. If not supplied
            will use the underlying data from rows, columns or frame. If given as an
            ndarray or list-like must be an identical shape to the underlying data
            considering ``axis`` and ``subset``. If given as DataFrame or Series must
            have same index and column labels considering ``axis`` and ``subset``.
            If supplied, ``vmin`` and ``vmax`` should be given relative to this
            gradient map.

            .. versionadded:: 1.3.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.{alt}_gradient: Color the {alt} in a gradient style.

        Notes
        -----
        When using ``low`` and ``high`` the range
        of the gradient, given by the data if ``gmap`` is not given or by ``gmap``,
        is extended at the low end effectively by
        `map.min - low * map.range` and at the high end by
        `map.max + high * map.range` before the colors are normalized and determined.

        If combining with ``vmin`` and ``vmax`` the `map.min`, `map.max` and
        `map.range` are replaced by values according to the values derived from
        ``vmin`` and ``vmax``.

        This method will preselect numeric columns and ignore non-numeric columns
        unless a ``gmap`` is supplied in which case no preselection occurs.

        Examples
        --------
        >>> df = pd.DataFrame(columns=["City", "Temp (c)", "Rain (mm)", "Wind (m/s)"],
        ...                   data=[["Stockholm", 21.6, 5.0, 3.2],
        ...                         ["Oslo", 22.4, 13.3, 3.1],
        ...                         ["Copenhagen", 24.5, 0.0, 6.7]])

        Shading the values column-wise, with ``axis=0``, preselecting numeric columns

        >>> df.style.{name}_gradient(axis=0)  # doctest: +SKIP

        .. figure:: ../../_static/style/{image_prefix}_ax0.png

        Shading all values collectively using ``axis=None``

        >>> df.style.{name}_gradient(axis=None)  # doctest: +SKIP

        .. figure:: ../../_static/style/{image_prefix}_axNone.png

        Compress the color map from the both ``low`` and ``high`` ends

        >>> df.style.{name}_gradient(axis=None, low=0.75, high=1.0)  # doctest: +SKIP

        .. figure:: ../../_static/style/{image_prefix}_axNone_lowhigh.png

        Manually setting ``vmin`` and ``vmax`` gradient thresholds

        >>> df.style.{name}_gradient(axis=None, vmin=6.7, vmax=21.6)  # doctest: +SKIP

        .. figure:: ../../_static/style/{image_prefix}_axNone_vminvmax.png

        Setting a ``gmap`` and applying to all columns with another ``cmap``

        >>> df.style.{name}_gradient(axis=0, gmap=df[\'Temp (c)\'], cmap=\'YlOrRd\')
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/{image_prefix}_gmap.png

        Setting the gradient map for a dataframe (i.e. ``axis=None``), we need to
        explicitly state ``subset`` to match the ``gmap`` shape

        >>> gmap = np.array([[1,2,3], [2,3,4], [3,4,5]])
        >>> df.style.{name}_gradient(axis=None, gmap=gmap,
        ...     cmap=\'YlOrRd\', subset=[\'Temp (c)\', \'Rain (mm)\', \'Wind (m/s)\']
        ... )  # doctest: +SKIP

        .. figure:: ../../_static/style/{image_prefix}_axNone_gmap.png
        '''
    def text_gradient(self, cmap: str | Colormap = 'PuBu', low: float = 0, high: float = 0, axis: Axis | None = 0, subset: Subset | None = None, vmin: float | None = None, vmax: float | None = None, gmap: Sequence | None = None) -> Styler: ...
    def set_properties(self, subset: Subset | None = None, **kwargs) -> Styler:
        '''
        Set defined CSS-properties to each ``<td>`` HTML element for the given subset.

        Parameters
        ----------
        %(subset)s
        **kwargs : dict
            A dictionary of property, value pairs to be set for each cell.

        Returns
        -------
        Styler

        Notes
        -----
        This is a convenience methods which wraps the :meth:`Styler.applymap` calling a
        function returning the CSS-properties independently of the data.

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4))
        >>> df.style.set_properties(color="white", align="right")  # doctest: +SKIP
        >>> df.style.set_properties(**{\'background-color\': \'yellow\'})  # doctest: +SKIP

        See `Table Visualization <../../user_guide/style.ipynb>`_ user guide for
        more details.
        '''
    def bar(self, subset: Subset | None = None, axis: Axis | None = 0, *, color: str | list | tuple | None = None, cmap: Any | None = None, width: float = 100, height: float = 100, align: str | float | Callable = 'mid', vmin: float | None = None, vmax: float | None = None, props: str = 'width: 10em;') -> Styler:
        '''
        Draw bar chart in the cell backgrounds.

        .. versionchanged:: 1.4.0

        Parameters
        ----------
        %(subset)s
        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            Apply to each column (``axis=0`` or ``\'index\'``), to each row
            (``axis=1`` or ``\'columns\'``), or to the entire DataFrame at once
            with ``axis=None``.
        color : str or 2-tuple/list
            If a str is passed, the color is the same for both
            negative and positive numbers. If 2-tuple/list is used, the
            first element is the color_negative and the second is the
            color_positive (eg: [\'#d65f5f\', \'#5fba7d\']).
        cmap : str, matplotlib.cm.ColorMap
            A string name of a matplotlib Colormap, or a Colormap object. Cannot be
            used together with ``color``.

            .. versionadded:: 1.4.0
        width : float, default 100
            The percentage of the cell, measured from the left, in which to draw the
            bars, in [0, 100].
        height : float, default 100
            The percentage height of the bar in the cell, centrally aligned, in [0,100].

            .. versionadded:: 1.4.0
        align : str, int, float, callable, default \'mid\'
            How to align the bars within the cells relative to a width adjusted center.
            If string must be one of:

            - \'left\' : bars are drawn rightwards from the minimum data value.
            - \'right\' : bars are drawn leftwards from the maximum data value.
            - \'zero\' : a value of zero is located at the center of the cell.
            - \'mid\' : a value of (max-min)/2 is located at the center of the cell,
              or if all values are negative (positive) the zero is
              aligned at the right (left) of the cell.
            - \'mean\' : the mean value of the data is located at the center of the cell.

            If a float or integer is given this will indicate the center of the cell.

            If a callable should take a 1d or 2d array and return a scalar.

            .. versionchanged:: 1.4.0

        vmin : float, optional
            Minimum bar value, defining the left hand limit
            of the bar drawing range, lower values are clipped to `vmin`.
            When None (default): the minimum value of the data will be used.
        vmax : float, optional
            Maximum bar value, defining the right hand limit
            of the bar drawing range, higher values are clipped to `vmax`.
            When None (default): the maximum value of the data will be used.
        props : str, optional
            The base CSS of the cell that is extended to add the bar chart. Defaults to
            `"width: 10em;"`.

            .. versionadded:: 1.4.0

        Returns
        -------
        Styler

        Notes
        -----
        This section of the user guide:
        `Table Visualization <../../user_guide/style.ipynb>`_ gives
        a number of examples for different settings and color coordination.
        '''
    def highlight_null(self, color: str = 'red', subset: Subset | None = None, props: str | None = None) -> Styler:
        """
        Highlight missing values with a style.

        Parameters
        ----------
        %(color)s

            .. versionadded:: 1.5.0

        %(subset)s

            .. versionadded:: 1.1.0

        %(props)s

            .. versionadded:: 1.3.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.highlight_max: Highlight the maximum with a style.
        Styler.highlight_min: Highlight the minimum with a style.
        Styler.highlight_between: Highlight a defined range with a style.
        Styler.highlight_quantile: Highlight values defined by a quantile with a style.
        """
    def highlight_max(self, subset: Subset | None = None, color: str = 'yellow', axis: Axis | None = 0, props: str | None = None) -> Styler:
        """
        Highlight the maximum with a style.

        Parameters
        ----------
        %(subset)s
        %(color)s
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            Apply to each column (``axis=0`` or ``'index'``), to each row
            (``axis=1`` or ``'columns'``), or to the entire DataFrame at once
            with ``axis=None``.
        %(props)s

            .. versionadded:: 1.3.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.highlight_null: Highlight missing values with a style.
        Styler.highlight_min: Highlight the minimum with a style.
        Styler.highlight_between: Highlight a defined range with a style.
        Styler.highlight_quantile: Highlight values defined by a quantile with a style.
        """
    def highlight_min(self, subset: Subset | None = None, color: str = 'yellow', axis: Axis | None = 0, props: str | None = None) -> Styler:
        """
        Highlight the minimum with a style.

        Parameters
        ----------
        %(subset)s
        %(color)s
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            Apply to each column (``axis=0`` or ``'index'``), to each row
            (``axis=1`` or ``'columns'``), or to the entire DataFrame at once
            with ``axis=None``.
        %(props)s

            .. versionadded:: 1.3.0

        Returns
        -------
        Styler

        See Also
        --------
        Styler.highlight_null: Highlight missing values with a style.
        Styler.highlight_max: Highlight the maximum with a style.
        Styler.highlight_between: Highlight a defined range with a style.
        Styler.highlight_quantile: Highlight values defined by a quantile with a style.
        """
    def highlight_between(self, subset: Subset | None = None, color: str = 'yellow', axis: Axis | None = 0, left: Scalar | Sequence | None = None, right: Scalar | Sequence | None = None, inclusive: str = 'both', props: str | None = None) -> Styler:
        '''
        Highlight a defined range with a style.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        %(subset)s
        %(color)s
        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            If ``left`` or ``right`` given as sequence, axis along which to apply those
            boundaries. See examples.
        left : scalar or datetime-like, or sequence or array-like, default None
            Left bound for defining the range.
        right : scalar or datetime-like, or sequence or array-like, default None
            Right bound for defining the range.
        inclusive : {\'both\', \'neither\', \'left\', \'right\'}
            Identify whether bounds are closed or open.
        %(props)s

        Returns
        -------
        Styler

        See Also
        --------
        Styler.highlight_null: Highlight missing values with a style.
        Styler.highlight_max: Highlight the maximum with a style.
        Styler.highlight_min: Highlight the minimum with a style.
        Styler.highlight_quantile: Highlight values defined by a quantile with a style.

        Notes
        -----
        If ``left`` is ``None`` only the right bound is applied.
        If ``right`` is ``None`` only the left bound is applied. If both are ``None``
        all values are highlighted.

        ``axis`` is only needed if ``left`` or ``right`` are provided as a sequence or
        an array-like object for aligning the shapes. If ``left`` and ``right`` are
        both scalars then all ``axis`` inputs will give the same result.

        This function only works with compatible ``dtypes``. For example a datetime-like
        region can only use equivalent datetime-like ``left`` and ``right`` arguments.
        Use ``subset`` to control regions which have multiple ``dtypes``.

        Examples
        --------
        Basic usage

        >>> df = pd.DataFrame({
        ...     \'One\': [1.2, 1.6, 1.5],
        ...     \'Two\': [2.9, 2.1, 2.5],
        ...     \'Three\': [3.1, 3.2, 3.8],
        ... })
        >>> df.style.highlight_between(left=2.1, right=2.9)  # doctest: +SKIP

        .. figure:: ../../_static/style/hbetw_basic.png

        Using a range input sequence along an ``axis``, in this case setting a ``left``
        and ``right`` for each column individually

        >>> df.style.highlight_between(left=[1.4, 2.4, 3.4], right=[1.6, 2.6, 3.6],
        ...     axis=1, color="#fffd75")  # doctest: +SKIP

        .. figure:: ../../_static/style/hbetw_seq.png

        Using ``axis=None`` and providing the ``left`` argument as an array that
        matches the input DataFrame, with a constant ``right``

        >>> df.style.highlight_between(left=[[2,2,3],[2,2,3],[3,3,3]], right=3.5,
        ...     axis=None, color="#fffd75")  # doctest: +SKIP

        .. figure:: ../../_static/style/hbetw_axNone.png

        Using ``props`` instead of default background coloring

        >>> df.style.highlight_between(left=1.5, right=3.5,
        ...     props=\'font-weight:bold;color:#e83e8c\')  # doctest: +SKIP

        .. figure:: ../../_static/style/hbetw_props.png
        '''
    def highlight_quantile(self, subset: Subset | None = None, color: str = 'yellow', axis: Axis | None = 0, q_left: float = 0.0, q_right: float = 1.0, interpolation: QuantileInterpolation = 'linear', inclusive: str = 'both', props: str | None = None) -> Styler:
        '''
        Highlight values defined by a quantile with a style.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        %(subset)s
        %(color)s
        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            Axis along which to determine and highlight quantiles. If ``None`` quantiles
            are measured over the entire DataFrame. See examples.
        q_left : float, default 0
            Left bound, in [0, q_right), for the target quantile range.
        q_right : float, default 1
            Right bound, in (q_left, 1], for the target quantile range.
        interpolation : {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}
            Argument passed to ``Series.quantile`` or ``DataFrame.quantile`` for
            quantile estimation.
        inclusive : {\'both\', \'neither\', \'left\', \'right\'}
            Identify whether quantile bounds are closed or open.
        %(props)s

        Returns
        -------
        Styler

        See Also
        --------
        Styler.highlight_null: Highlight missing values with a style.
        Styler.highlight_max: Highlight the maximum with a style.
        Styler.highlight_min: Highlight the minimum with a style.
        Styler.highlight_between: Highlight a defined range with a style.

        Notes
        -----
        This function does not work with ``str`` dtypes.

        Examples
        --------
        Using ``axis=None`` and apply a quantile to all collective data

        >>> df = pd.DataFrame(np.arange(10).reshape(2,5) + 1)
        >>> df.style.highlight_quantile(axis=None, q_left=0.8, color="#fffd75")
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/hq_axNone.png

        Or highlight quantiles row-wise or column-wise, in this case by row-wise

        >>> df.style.highlight_quantile(axis=1, q_left=0.8, color="#fffd75")
        ...  # doctest: +SKIP

        .. figure:: ../../_static/style/hq_ax1.png

        Use ``props`` instead of default background coloring

        >>> df.style.highlight_quantile(axis=None, q_left=0.2, q_right=0.8,
        ...     props=\'font-weight:bold;color:#e83e8c\')  # doctest: +SKIP

        .. figure:: ../../_static/style/hq_props.png
        '''
    @classmethod
    def from_custom_template(cls, searchpath, html_table: str | None = None, html_style: str | None = None):
        """
        Factory function for creating a subclass of ``Styler``.

        Uses custom templates and Jinja environment.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        searchpath : str or list
            Path or paths of directories containing the templates.
        html_table : str
            Name of your custom template to replace the html_table template.

            .. versionadded:: 1.3.0

        html_style : str
            Name of your custom template to replace the html_style template.

            .. versionadded:: 1.3.0

        Returns
        -------
        MyStyler : subclass of Styler
            Has the correct ``env``,``template_html``, ``template_html_table`` and
            ``template_html_style`` class attributes set.
        """
    def pipe(self, func: Callable, *args, **kwargs):
        '''
        Apply ``func(self, *args, **kwargs)``, and return the result.

        Parameters
        ----------
        func : function
            Function to apply to the Styler.  Alternatively, a
            ``(callable, keyword)`` tuple where ``keyword`` is a string
            indicating the keyword of ``callable`` that expects the Styler.
        *args : optional
            Arguments passed to `func`.
        **kwargs : optional
            A dictionary of keyword arguments passed into ``func``.

        Returns
        -------
        object :
            The value returned by ``func``.

        See Also
        --------
        DataFrame.pipe : Analogous method for DataFrame.
        Styler.apply : Apply a CSS-styling function column-wise, row-wise, or
            table-wise.

        Notes
        -----
        Like :meth:`DataFrame.pipe`, this method can simplify the
        application of several user-defined functions to a styler.  Instead
        of writing:

        .. code-block:: python

            f(g(df.style.format(precision=3), arg1=a), arg2=b, arg3=c)

        users can write:

        .. code-block:: python

            (df.style.format(precision=3)
               .pipe(g, arg1=a)
               .pipe(f, arg2=b, arg3=c))

        In particular, this allows users to define functions that take a
        styler object, along with other parameters, and return the styler after
        making styling changes (such as calling :meth:`Styler.apply` or
        :meth:`Styler.set_properties`).

        Examples
        --------

        **Common Use**

        A common usage pattern is to pre-define styling operations which
        can be easily applied to a generic styler in a single ``pipe`` call.

        >>> def some_highlights(styler, min_color="red", max_color="blue"):
        ...      styler.highlight_min(color=min_color, axis=None)
        ...      styler.highlight_max(color=max_color, axis=None)
        ...      styler.highlight_null()
        ...      return styler
        >>> df = pd.DataFrame([[1, 2, 3, pd.NA], [pd.NA, 4, 5, 6]], dtype="Int64")
        >>> df.style.pipe(some_highlights, min_color="green")  # doctest: +SKIP

        .. figure:: ../../_static/style/df_pipe_hl.png

        Since the method returns a ``Styler`` object it can be chained with other
        methods as if applying the underlying highlighters directly.

        >>> (df.style.format("{:.1f}")
        ...         .pipe(some_highlights, min_color="green")
        ...         .highlight_between(left=2, right=5))  # doctest: +SKIP

        .. figure:: ../../_static/style/df_pipe_hl2.png

        **Advanced Use**

        Sometimes it may be necessary to pre-define styling functions, but in the case
        where those functions rely on the styler, data or context. Since
        ``Styler.use`` and ``Styler.export`` are designed to be non-data dependent,
        they cannot be used for this purpose. Additionally the ``Styler.apply``
        and ``Styler.format`` type methods are not context aware, so a solution
        is to use ``pipe`` to dynamically wrap this functionality.

        Suppose we want to code a generic styling function that highlights the final
        level of a MultiIndex. The number of levels in the Index is dynamic so we
        need the ``Styler`` context to define the level.

        >>> def highlight_last_level(styler):
        ...     return styler.apply_index(
        ...         lambda v: "background-color: pink; color: yellow", axis="columns",
        ...         level=styler.columns.nlevels-1
        ...     )  # doctest: +SKIP
        >>> df.columns = pd.MultiIndex.from_product([["A", "B"], ["X", "Y"]])
        >>> df.style.pipe(highlight_last_level)  # doctest: +SKIP

        .. figure:: ../../_static/style/df_pipe_applymap.png

        Additionally suppose we want to highlight a column header if there is any
        missing data in that column.
        In this case we need the data object itself to determine the effect on the
        column headers.

        >>> def highlight_header_missing(styler, level):
        ...     def dynamic_highlight(s):
        ...         return np.where(
        ...             styler.data.isna().any(), "background-color: red;", ""
        ...         )
        ...     return styler.apply_index(dynamic_highlight, axis=1, level=level)
        >>> df.style.pipe(highlight_header_missing, level=1)  # doctest: +SKIP

        .. figure:: ../../_static/style/df_pipe_applydata.png
        '''
