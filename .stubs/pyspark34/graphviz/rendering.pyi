import os
from . import backend, saving

__all__ = ['Render']

class Render(saving.Save, backend.Render, backend.View):
    """Write source lines to file and render with Graphviz."""
    def render(self, filename: os.PathLike | str | None = None, directory: os.PathLike | str | None = None, view: bool = False, cleanup: bool = False, format: str | None = None, renderer: str | None = None, formatter: str | None = None, neato_no_op: bool | int | None = None, quiet: bool = False, quiet_view: bool = False, *, outfile: os.PathLike | str | None = None, engine: str | None = None, raise_if_result_exists: bool = False, overwrite_source: bool = False) -> str:
        """Save the source to file and render with the Graphviz engine.

        Args:
            filename: Filename for saving the source
                (defaults to ``name`` + ``'.gv'``).s
            directory: (Sub)directory for source saving and rendering.
            view (bool): Open the rendered result
                with the default application.
            cleanup (bool): Delete the source file
                after successful rendering.
            format: The output format used for rendering
                (``'pdf'``, ``'png'``, etc.).
            renderer: The output renderer used for rendering
                (``'cairo'``, ``'gd'``, ...).
            formatter: The output formatter used for rendering
                (``'cairo'``, ``'gd'``, ...).
            neato_no_op: Neato layout engine no-op flag.
            quiet (bool): Suppress ``stderr`` output
                from the layout subprocess.
            quiet_view (bool): Suppress ``stderr`` output
                from the viewer process
                (implies ``view=True``, ineffective on Windows platform).
            outfile: Path for the rendered output file.
            engine: Layout engine for rendering
                (``'dot'``, ``'neato'``, ...).
            raise_if_result_exits: Raise :exc:`graphviz.FileExistsError`
                if the result file exists.
            overwrite_source: Allow ``dot`` to write to the file it reads from.
                Incompatible with ``raise_if_result_exists``.

        Returns:
            The (possibly relative) path of the rendered file.

        Raises:
            ValueError: If ``engine``, ``format``, ``renderer``, or ``formatter``
                are unknown.
            graphviz.RequiredArgumentError: If ``formatter`` is given
                but ``renderer`` is None.
            ValueError: If ``outfile`` is the same file as the source file
                unless ``overwite_source=True``.
            graphviz.ExecutableNotFound: If the Graphviz ``dot`` executable
                is not found.
            graphviz.CalledProcessError: If the returncode (exit status)
                of the rendering ``dot`` subprocess is non-zero.
            RuntimeError: If viewer opening is requested but not supported.

        Example:
            >>> doctest_mark_exe()
            >>> import graphviz
            >>> dot = graphviz.Graph(name='spam', directory='doctest-output')
            >>> dot.render(format='png').replace('\\\\', '/')
            'doctest-output/spam.gv.png'
            >>> dot.render(outfile='spam.svg').replace('\\\\', '/')
            'doctest-output/spam.svg'

        Note:
            The layout command is started from the directory of ``filepath``,
            so that references to external files
            (e.g. ``[image=images/camelot.png]``)
            can be given as paths relative to the DOT source file.
        """
    def view(self, filename: os.PathLike | str | None = None, directory: os.PathLike | str | None = None, cleanup: bool = False, quiet: bool = False, quiet_view: bool = False) -> str:
        """Save the source to file, open the rendered result in a viewer.

        Convenience short-cut for running ``.render(view=True)``.

        Args:
            filename: Filename for saving the source
                (defaults to ``name`` + ``'.gv'``).
            directory: (Sub)directory for source saving and rendering.
            cleanup (bool): Delete the source file after successful rendering.
            quiet (bool): Suppress ``stderr`` output from the layout subprocess.
            quiet_view (bool): Suppress ``stderr`` output
                from the viewer process (ineffective on Windows).

        Returns:
            The (possibly relative) path of the rendered file.

        Raises:
            graphviz.ExecutableNotFound: If the Graphviz executable
                is not found.
            graphviz.CalledProcessError: If the exit status is non-zero.
            RuntimeError: If opening the viewer is not supported.

        Short-cut method for calling :meth:`.render` with ``view=True``.

        Note:
            There is no option to wait for the application to close,
            and no way to retrieve the application's exit status.
        """
