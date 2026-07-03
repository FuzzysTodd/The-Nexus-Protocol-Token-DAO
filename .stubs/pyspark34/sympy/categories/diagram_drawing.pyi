from _typeshed import Incomplete
from sympy.categories import CompositeMorphism as CompositeMorphism, Diagram as Diagram, IdentityMorphism as IdentityMorphism, NamedMorphism as NamedMorphism
from sympy.core import Dict as Dict, Symbol as Symbol, default_sort_key as default_sort_key
from sympy.printing.latex import latex as latex
from sympy.sets import FiniteSet as FiniteSet
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.iterables import iterable as iterable

__doctest_requires__: Incomplete

class _GrowableGrid:
    """
    Holds a growable grid of objects.

    Explanation
    ===========

    It is possible to append or prepend a row or a column to the grid
    using the corresponding methods.  Prepending rows or columns has
    the effect of changing the coordinates of the already existing
    elements.

    This class currently represents a naive implementation of the
    functionality with little attempt at optimisation.
    """
    def __init__(self, width, height) -> None: ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    def __getitem__(self, i_j):
        """
        Returns the element located at in the i-th line and j-th
        column.
        """
    def __setitem__(self, i_j, newvalue) -> None:
        """
        Sets the element located at in the i-th line and j-th
        column.
        """
    def append_row(self) -> None:
        """
        Appends an empty row to the grid.
        """
    def append_column(self) -> None:
        """
        Appends an empty column to the grid.
        """
    def prepend_row(self) -> None:
        """
        Prepends the grid with an empty row.
        """
    def prepend_column(self) -> None:
        """
        Prepends the grid with an empty column.
        """

class DiagramGrid:
    '''
    Constructs and holds the fitting of the diagram into a grid.

    Explanation
    ===========

    The mission of this class is to analyse the structure of the
    supplied diagram and to place its objects on a grid such that,
    when the objects and the morphisms are actually drawn, the diagram
    would be "readable", in the sense that there will not be many
    intersections of moprhisms.  This class does not perform any
    actual drawing.  It does strive nevertheless to offer sufficient
    metadata to draw a diagram.

    Consider the following simple diagram.

    >>> from sympy.categories import Object, NamedMorphism
    >>> from sympy.categories import Diagram, DiagramGrid
    >>> from sympy import pprint
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> diagram = Diagram([f, g])

    The simplest way to have a diagram laid out is the following:

    >>> grid = DiagramGrid(diagram)
    >>> (grid.width, grid.height)
    (2, 2)
    >>> pprint(grid)
    A  B
    <BLANKLINE>
       C

    Sometimes one sees the diagram as consisting of logical groups.
    One can advise ``DiagramGrid`` as to such groups by employing the
    ``groups`` keyword argument.

    Consider the following diagram:

    >>> D = Object("D")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> h = NamedMorphism(D, A, "h")
    >>> k = NamedMorphism(D, B, "k")
    >>> diagram = Diagram([f, g, h, k])

    Lay it out with generic layout:

    >>> grid = DiagramGrid(diagram)
    >>> pprint(grid)
    A  B  D
    <BLANKLINE>
       C

    Now, we can group the objects `A` and `D` to have them near one
    another:

    >>> grid = DiagramGrid(diagram, groups=[[A, D], B, C])
    >>> pprint(grid)
    B     C
    <BLANKLINE>
    A  D

    Note how the positioning of the other objects changes.

    Further indications can be supplied to the constructor of
    :class:`DiagramGrid` using keyword arguments.  The currently
    supported hints are explained in the following paragraphs.

    :class:`DiagramGrid` does not automatically guess which layout
    would suit the supplied diagram better.  Consider, for example,
    the following linear diagram:

    >>> E = Object("E")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> h = NamedMorphism(C, D, "h")
    >>> i = NamedMorphism(D, E, "i")
    >>> diagram = Diagram([f, g, h, i])

    When laid out with the generic layout, it does not get to look
    linear:

    >>> grid = DiagramGrid(diagram)
    >>> pprint(grid)
    A  B
    <BLANKLINE>
       C  D
    <BLANKLINE>
          E

    To get it laid out in a line, use ``layout="sequential"``:

    >>> grid = DiagramGrid(diagram, layout="sequential")
    >>> pprint(grid)
    A  B  C  D  E

    One may sometimes need to transpose the resulting layout.  While
    this can always be done by hand, :class:`DiagramGrid` provides a
    hint for that purpose:

    >>> grid = DiagramGrid(diagram, layout="sequential", transpose=True)
    >>> pprint(grid)
    A
    <BLANKLINE>
    B
    <BLANKLINE>
    C
    <BLANKLINE>
    D
    <BLANKLINE>
    E

    Separate hints can also be provided for each group.  For an
    example, refer to ``tests/test_drawing.py``, and see the different
    ways in which the five lemma [FiveLemma] can be laid out.

    See Also
    ========

    Diagram

    References
    ==========

    .. [FiveLemma] https://en.wikipedia.org/wiki/Five_lemma
    '''
    def __init__(self, diagram, groups: Incomplete | None = None, **hints) -> None: ...
    @property
    def width(self):
        '''
        Returns the number of columns in this diagram layout.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> from sympy.categories import Diagram, DiagramGrid
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> diagram = Diagram([f, g])
        >>> grid = DiagramGrid(diagram)
        >>> grid.width
        2

        '''
    @property
    def height(self):
        '''
        Returns the number of rows in this diagram layout.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> from sympy.categories import Diagram, DiagramGrid
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> diagram = Diagram([f, g])
        >>> grid = DiagramGrid(diagram)
        >>> grid.height
        2

        '''
    def __getitem__(self, i_j):
        '''
        Returns the object placed in the row ``i`` and column ``j``.
        The indices are 0-based.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> from sympy.categories import Diagram, DiagramGrid
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> diagram = Diagram([f, g])
        >>> grid = DiagramGrid(diagram)
        >>> (grid[0, 0], grid[0, 1])
        (Object("A"), Object("B"))
        >>> (grid[1, 0], grid[1, 1])
        (None, Object("C"))

        '''
    @property
    def morphisms(self):
        '''
        Returns those morphisms (and their properties) which are
        sufficiently meaningful to be drawn.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> from sympy.categories import Diagram, DiagramGrid
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> diagram = Diagram([f, g])
        >>> grid = DiagramGrid(diagram)
        >>> grid.morphisms
        {NamedMorphism(Object("A"), Object("B"), "f"): EmptySet,
        NamedMorphism(Object("B"), Object("C"), "g"): EmptySet}

        '''

class ArrowStringDescription:
    '''
    Stores the information necessary for producing an Xy-pic
    description of an arrow.

    The principal goal of this class is to abstract away the string
    representation of an arrow and to also provide the functionality
    to produce the actual Xy-pic string.

    ``unit`` sets the unit which will be used to specify the amount of
    curving and other distances.  ``horizontal_direction`` should be a
    string of ``"r"`` or ``"l"`` specifying the horizontal offset of the
    target cell of the arrow relatively to the current one.
    ``vertical_direction`` should  specify the vertical offset using a
    series of either ``"d"`` or ``"u"``.  ``label_position`` should be
    either ``"^"``, ``"_"``,  or ``"|"`` to specify that the label should
    be positioned above the arrow, below the arrow or just over the arrow,
    in a break.  Note that the notions "above" and "below" are relative
    to arrow direction.  ``label`` stores the morphism label.

    This works as follows (disregard the yet unexplained arguments):

    >>> from sympy.categories.diagram_drawing import ArrowStringDescription
    >>> astr = ArrowStringDescription(
    ... unit="mm", curving=None, curving_amount=None,
    ... looping_start=None, looping_end=None, horizontal_direction="d",
    ... vertical_direction="r", label_position="_", label="f")
    >>> print(str(astr))
    \\ar[dr]_{f}

    ``curving`` should be one of ``"^"``, ``"_"`` to specify in which
    direction the arrow is going to curve. ``curving_amount`` is a number
    describing how many ``unit``\'s the morphism is going to curve:

    >>> astr = ArrowStringDescription(
    ... unit="mm", curving="^", curving_amount=12,
    ... looping_start=None, looping_end=None, horizontal_direction="d",
    ... vertical_direction="r", label_position="_", label="f")
    >>> print(str(astr))
    \\ar@/^12mm/[dr]_{f}

    ``looping_start`` and ``looping_end`` are currently only used for
    loop morphisms, those which have the same domain and codomain.
    These two attributes should store a valid Xy-pic direction and
    specify, correspondingly, the direction the arrow gets out into
    and the direction the arrow gets back from:

    >>> astr = ArrowStringDescription(
    ... unit="mm", curving=None, curving_amount=None,
    ... looping_start="u", looping_end="l", horizontal_direction="",
    ... vertical_direction="", label_position="_", label="f")
    >>> print(str(astr))
    \\ar@(u,l)[]_{f}

    ``label_displacement`` controls how far the arrow label is from
    the ends of the arrow.  For example, to position the arrow label
    near the arrow head, use ">":

    >>> astr = ArrowStringDescription(
    ... unit="mm", curving="^", curving_amount=12,
    ... looping_start=None, looping_end=None, horizontal_direction="d",
    ... vertical_direction="r", label_position="_", label="f")
    >>> astr.label_displacement = ">"
    >>> print(str(astr))
    \\ar@/^12mm/[dr]_>{f}

    Finally, ``arrow_style`` is used to specify the arrow style.  To
    get a dashed arrow, for example, use "{-->}" as arrow style:

    >>> astr = ArrowStringDescription(
    ... unit="mm", curving="^", curving_amount=12,
    ... looping_start=None, looping_end=None, horizontal_direction="d",
    ... vertical_direction="r", label_position="_", label="f")
    >>> astr.arrow_style = "{-->}"
    >>> print(str(astr))
    \\ar@/^12mm/@{-->}[dr]_{f}

    Notes
    =====

    Instances of :class:`ArrowStringDescription` will be constructed
    by :class:`XypicDiagramDrawer` and provided for further use in
    formatters.  The user is not expected to construct instances of
    :class:`ArrowStringDescription` themselves.

    To be able to properly utilise this class, the reader is encouraged
    to checkout the Xy-pic user guide, available at [Xypic].

    See Also
    ========

    XypicDiagramDrawer

    References
    ==========

    .. [Xypic] https://xy-pic.sourceforge.net/
    '''
    unit: Incomplete
    curving: Incomplete
    curving_amount: Incomplete
    looping_start: Incomplete
    looping_end: Incomplete
    horizontal_direction: Incomplete
    vertical_direction: Incomplete
    label_position: Incomplete
    label: Incomplete
    label_displacement: str
    arrow_style: str
    forced_label_position: bool
    def __init__(self, unit, curving, curving_amount, looping_start, looping_end, horizontal_direction, vertical_direction, label_position, label) -> None: ...

class XypicDiagramDrawer:
    '''
    Given a :class:`~.Diagram` and the corresponding
    :class:`DiagramGrid`, produces the Xy-pic representation of the
    diagram.

    The most important method in this class is ``draw``.  Consider the
    following triangle diagram:

    >>> from sympy.categories import Object, NamedMorphism, Diagram
    >>> from sympy.categories import DiagramGrid, XypicDiagramDrawer
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> diagram = Diagram([f, g], {g * f: "unique"})

    To draw this diagram, its objects need to be laid out with a
    :class:`DiagramGrid`::

    >>> grid = DiagramGrid(diagram)

    Finally, the drawing:

    >>> drawer = XypicDiagramDrawer()
    >>> print(drawer.draw(diagram, grid))
    \\xymatrix{
    A \\ar[d]_{g\\circ f} \\ar[r]^{f} & B \\ar[ld]^{g} \\\\\n    C &
    }

    For further details see the docstring of this method.

    To control the appearance of the arrows, formatters are used.  The
    dictionary ``arrow_formatters`` maps morphisms to formatter
    functions.  A formatter is accepts an
    :class:`ArrowStringDescription` and is allowed to modify any of
    the arrow properties exposed thereby.  For example, to have all
    morphisms with the property ``unique`` appear as dashed arrows,
    and to have their names prepended with `\\exists !`, the following
    should be done:

    >>> def formatter(astr):
    ...   astr.label = r"\\exists !" + astr.label
    ...   astr.arrow_style = "{-->}"
    >>> drawer.arrow_formatters["unique"] = formatter
    >>> print(drawer.draw(diagram, grid))
    \\xymatrix{
    A \\ar@{-->}[d]_{\\exists !g\\circ f} \\ar[r]^{f} & B \\ar[ld]^{g} \\\\\n    C &
    }

    To modify the appearance of all arrows in the diagram, set
    ``default_arrow_formatter``.  For example, to place all morphism
    labels a little bit farther from the arrow head so that they look
    more centred, do as follows:

    >>> def default_formatter(astr):
    ...   astr.label_displacement = "(0.45)"
    >>> drawer.default_arrow_formatter = default_formatter
    >>> print(drawer.draw(diagram, grid))
    \\xymatrix{
    A \\ar@{-->}[d]_(0.45){\\exists !g\\circ f} \\ar[r]^(0.45){f} & B \\ar[ld]^(0.45){g} \\\\\n    C &
    }

    In some diagrams some morphisms are drawn as curved arrows.
    Consider the following diagram:

    >>> D = Object("D")
    >>> E = Object("E")
    >>> h = NamedMorphism(D, A, "h")
    >>> k = NamedMorphism(D, B, "k")
    >>> diagram = Diagram([f, g, h, k])
    >>> grid = DiagramGrid(diagram)
    >>> drawer = XypicDiagramDrawer()
    >>> print(drawer.draw(diagram, grid))
    \\xymatrix{
    A \\ar[r]_{f} & B \\ar[d]^{g} & D \\ar[l]^{k} \\ar@/_3mm/[ll]_{h} \\\\\n    & C &
    }

    To control how far the morphisms are curved by default, one can
    use the ``unit`` and ``default_curving_amount`` attributes:

    >>> drawer.unit = "cm"
    >>> drawer.default_curving_amount = 1
    >>> print(drawer.draw(diagram, grid))
    \\xymatrix{
    A \\ar[r]_{f} & B \\ar[d]^{g} & D \\ar[l]^{k} \\ar@/_1cm/[ll]_{h} \\\\\n    & C &
    }

    In some diagrams, there are multiple curved morphisms between the
    same two objects.  To control by how much the curving changes
    between two such successive morphisms, use
    ``default_curving_step``:

    >>> drawer.default_curving_step = 1
    >>> h1 = NamedMorphism(A, D, "h1")
    >>> diagram = Diagram([f, g, h, k, h1])
    >>> grid = DiagramGrid(diagram)
    >>> print(drawer.draw(diagram, grid))
    \\xymatrix{
    A \\ar[r]_{f} \\ar@/^1cm/[rr]^{h_{1}} & B \\ar[d]^{g} & D \\ar[l]^{k} \\ar@/_2cm/[ll]_{h} \\\\\n    & C &
    }

    The default value of ``default_curving_step`` is 4 units.

    See Also
    ========

    draw, ArrowStringDescription
    '''
    unit: str
    default_curving_amount: int
    default_curving_step: int
    arrow_formatters: Incomplete
    default_arrow_formatter: Incomplete
    def __init__(self) -> None: ...
    def draw(self, diagram, grid, masked: Incomplete | None = None, diagram_format: str = ''):
        '''
        Returns the Xy-pic representation of ``diagram`` laid out in
        ``grid``.

        Consider the following simple triangle diagram.

        >>> from sympy.categories import Object, NamedMorphism, Diagram
        >>> from sympy.categories import DiagramGrid, XypicDiagramDrawer
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> diagram = Diagram([f, g], {g * f: "unique"})

        To draw this diagram, its objects need to be laid out with a
        :class:`DiagramGrid`::

        >>> grid = DiagramGrid(diagram)

        Finally, the drawing:

        >>> drawer = XypicDiagramDrawer()
        >>> print(drawer.draw(diagram, grid))
        \\xymatrix{
        A \\ar[d]_{g\\circ f} \\ar[r]^{f} & B \\ar[ld]^{g} \\\\\n        C &
        }

        The argument ``masked`` can be used to skip morphisms in the
        presentation of the diagram:

        >>> print(drawer.draw(diagram, grid, masked=[g * f]))
        \\xymatrix{
        A \\ar[r]^{f} & B \\ar[ld]^{g} \\\\\n        C &
        }

        Finally, the ``diagram_format`` argument can be used to
        specify the format string of the diagram.  For example, to
        increase the spacing by 1 cm, proceeding as follows:

        >>> print(drawer.draw(diagram, grid, diagram_format="@+1cm"))
        \\xymatrix@+1cm{
        A \\ar[d]_{g\\circ f} \\ar[r]^{f} & B \\ar[ld]^{g} \\\\\n        C &
        }

        '''

def xypic_draw_diagram(diagram, masked: Incomplete | None = None, diagram_format: str = '', groups: Incomplete | None = None, **hints):
    '''
    Provides a shortcut combining :class:`DiagramGrid` and
    :class:`XypicDiagramDrawer`.  Returns an Xy-pic presentation of
    ``diagram``.  The argument ``masked`` is a list of morphisms which
    will be not be drawn.  The argument ``diagram_format`` is the
    format string inserted after "\\xymatrix".  ``groups`` should be a
    set of logical groups.  The ``hints`` will be passed directly to
    the constructor of :class:`DiagramGrid`.

    For more information about the arguments, see the docstrings of
    :class:`DiagramGrid` and ``XypicDiagramDrawer.draw``.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism, Diagram
    >>> from sympy.categories import xypic_draw_diagram
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> diagram = Diagram([f, g], {g * f: "unique"})
    >>> print(xypic_draw_diagram(diagram))
    \\xymatrix{
    A \\ar[d]_{g\\circ f} \\ar[r]^{f} & B \\ar[ld]^{g} \\\\\n    C &
    }

    See Also
    ========

    XypicDiagramDrawer, DiagramGrid
    '''
def preview_diagram(diagram, masked: Incomplete | None = None, diagram_format: str = '', groups: Incomplete | None = None, output: str = 'png', viewer: Incomplete | None = None, euler: bool = True, **hints) -> None:
    '''
    Combines the functionality of ``xypic_draw_diagram`` and
    ``sympy.printing.preview``.  The arguments ``masked``,
    ``diagram_format``, ``groups``, and ``hints`` are passed to
    ``xypic_draw_diagram``, while ``output``, ``viewer, and ``euler``
    are passed to ``preview``.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism, Diagram
    >>> from sympy.categories import preview_diagram
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> d = Diagram([f, g], {g * f: "unique"})
    >>> preview_diagram(d)

    See Also
    ========

    XypicDiagramDrawer
    '''
