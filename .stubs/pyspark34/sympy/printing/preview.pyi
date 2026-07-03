from .latex import latex as latex
from _typeshed import Incomplete
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.misc import debug as debug

__doctest_requires__: Incomplete

def system_default_viewer(fname, fmt) -> None:
    """ Open fname with the default system viewer.

    In practice, it is impossible for python to know when the system viewer is
    done. For this reason, we ensure the passed file will not be deleted under
    it, and this function does not attempt to block.
    """
def pyglet_viewer(fname, fmt) -> None: ...
def preview(expr, output: str = 'png', viewer: Incomplete | None = None, euler: bool = True, packages=(), filename: Incomplete | None = None, outputbuffer: Incomplete | None = None, preamble: Incomplete | None = None, dvioptions: Incomplete | None = None, outputTexFile: Incomplete | None = None, extra_preamble: Incomplete | None = None, fontsize: Incomplete | None = None, **latex_settings) -> None:
    '''
    View expression or LaTeX markup in PNG, DVI, PostScript or PDF form.

    If the expr argument is an expression, it will be exported to LaTeX and
    then compiled using the available TeX distribution.  The first argument,
    \'expr\', may also be a LaTeX string.  The function will then run the
    appropriate viewer for the given output format or use the user defined
    one. By default png output is generated.

    By default pretty Euler fonts are used for typesetting (they were used to
    typeset the well known "Concrete Mathematics" book). For that to work, you
    need the \'eulervm.sty\' LaTeX style (in Debian/Ubuntu, install the
    texlive-fonts-extra package). If you prefer default AMS fonts or your
    system lacks \'eulervm\' LaTeX package then unset the \'euler\' keyword
    argument.

    To use viewer auto-detection, lets say for \'png\' output, issue

    >>> from sympy import symbols, preview, Symbol
    >>> x, y = symbols("x,y")

    >>> preview(x + y, output=\'png\')

    This will choose \'pyglet\' by default. To select a different one, do

    >>> preview(x + y, output=\'png\', viewer=\'gimp\')

    The \'png\' format is considered special. For all other formats the rules
    are slightly different. As an example we will take \'dvi\' output format. If
    you would run

    >>> preview(x + y, output=\'dvi\')

    then \'view\' will look for available \'dvi\' viewers on your system
    (predefined in the function, so it will try evince, first, then kdvi and
    xdvi). If nothing is found, it will fall back to using a system file
    association (via ``open`` and ``xdg-open``). To always use your system file
    association without searching for the above readers, use

    >>> from sympy.printing.preview import system_default_viewer
    >>> preview(x + y, output=\'dvi\', viewer=system_default_viewer)

    If this still does not find the viewer you want, it can be set explicitly.

    >>> preview(x + y, output=\'dvi\', viewer=\'superior-dvi-viewer\')

    This will skip auto-detection and will run user specified
    \'superior-dvi-viewer\'. If ``view`` fails to find it on your system it will
    gracefully raise an exception.

    You may also enter ``\'file\'`` for the viewer argument. Doing so will cause
    this function to return a file object in read-only mode, if ``filename``
    is unset. However, if it was set, then \'preview\' writes the generated
    file to this filename instead.

    There is also support for writing to a ``io.BytesIO`` like object, which
    needs to be passed to the ``outputbuffer`` argument.

    >>> from io import BytesIO
    >>> obj = BytesIO()
    >>> preview(x + y, output=\'png\', viewer=\'BytesIO\',
    ...         outputbuffer=obj)

    The LaTeX preamble can be customized by setting the \'preamble\' keyword
    argument. This can be used, e.g., to set a different font size, use a
    custom documentclass or import certain set of LaTeX packages.

    >>> preamble = "\\\\documentclass[10pt]{article}\\n" \\\n    ...            "\\\\usepackage{amsmath,amsfonts}\\\\begin{document}"
    >>> preview(x + y, output=\'png\', preamble=preamble)

    It is also possible to use the standard preamble and provide additional
    information to the preamble using the ``extra_preamble`` keyword argument.

    >>> from sympy import sin
    >>> extra_preamble = "\\\\renewcommand{\\\\sin}{\\\\cos}"
    >>> preview(sin(x), output=\'png\', extra_preamble=extra_preamble)

    If the value of \'output\' is different from \'dvi\' then command line
    options can be set (\'dvioptions\' argument) for the execution of the
    \'dvi\'+output conversion tool. These options have to be in the form of a
    list of strings (see ``subprocess.Popen``).

    Additional keyword args will be passed to the :func:`~sympy.printing.latex.latex` call,
    e.g., the ``symbol_names`` flag.

    >>> phidd = Symbol(\'phidd\')
    >>> preview(phidd, symbol_names={phidd: r\'\\ddot{\\varphi}\'})

    For post-processing the generated TeX File can be written to a file by
    passing the desired filename to the \'outputTexFile\' keyword
    argument. To write the TeX code to a file named
    ``"sample.tex"`` and run the default png viewer to display the resulting
    bitmap, do

    >>> preview(x + y, outputTexFile="sample.tex")


    '''
