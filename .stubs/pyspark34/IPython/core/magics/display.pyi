from IPython.core import magic_arguments as magic_arguments
from IPython.core.magic import Magics as Magics, cell_magic as cell_magic, magics_class as magics_class
from IPython.display import HTML as HTML, Javascript as Javascript, Latex as Latex, Markdown as Markdown, SVG as SVG, display as display

class DisplayMagics(Magics):
    """Magics for displaying various output types with literals

    Defines javascript/latex/svg/html cell magics for writing
    blocks in those languages, to be rendered in the frontend.
    """
    def js(self, line, cell) -> None:
        """Run the cell block of Javascript code

        Alias of `%%javascript`

        Starting with IPython 8.0 %%javascript is pending deprecation to be replaced
        by a more flexible system

        Please See https://github.com/ipython/ipython/issues/13376
        """
    def javascript(self, line, cell) -> None:
        """Run the cell block of Javascript code

        Starting with IPython 8.0 %%javascript is pending deprecation to be replaced
        by a more flexible system

        Please See https://github.com/ipython/ipython/issues/13376
        """
    def latex(self, line, cell) -> None:
        """Render the cell as a block of LaTeX

        The subset of LaTeX which is supported depends on the implementation in
        the client.  In the Jupyter Notebook, this magic only renders the subset
        of LaTeX defined by MathJax
        [here](https://docs.mathjax.org/en/v2.5-latest/tex.html)."""
    def svg(self, line, cell) -> None:
        """Render the cell as an SVG literal"""
    def html(self, line, cell) -> None:
        """Render the cell as a block of HTML"""
    def markdown(self, line, cell) -> None:
        """Render the cell as Markdown text block"""
