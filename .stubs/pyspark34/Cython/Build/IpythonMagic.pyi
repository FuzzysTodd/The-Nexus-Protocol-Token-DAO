from ..Compiler.Errors import CompileError as CompileError
from ..Utils import captured_fd as captured_fd, print_captured as print_captured
from .Dependencies import cythonize as cythonize
from .Inline import cython_inline as cython_inline, load_dynamic as load_dynamic
from IPython.core.magic import Magics
from _typeshed import Incomplete

IO_ENCODING: Incomplete
IS_PY2: Incomplete
PGO_CONFIG: Incomplete

def encode_fs(name): ...

class CythonMagics(Magics):
    def __init__(self, shell) -> None: ...
    def cython_inline(self, line, cell):
        """Compile and run a Cython code cell using Cython.inline.

        This magic simply passes the body of the cell to Cython.inline
        and returns the result. If the variables `a` and `b` are defined
        in the user's namespace, here is a simple example that returns
        their sum::

            %%cython_inline
            return a+b

        For most purposes, we recommend the usage of the `%%cython` magic.
        """
    def cython_pyximport(self, line, cell) -> None:
        """Compile and import a Cython code cell using pyximport.

        The contents of the cell are written to a `.pyx` file in the current
        working directory, which is then imported using `pyximport`. This
        magic requires a module name to be passed::

            %%cython_pyximport modulename
            def f(x):
                return 2.0*x

        The compiled module is then imported and all of its symbols are
        injected into the user's namespace. For most purposes, we recommend
        the usage of the `%%cython` magic.
        """
    def cython(self, line, cell):
        '''Compile and import everything from a Cython code cell.

        The contents of the cell are written to a `.pyx` file in the
        directory `IPYTHONDIR/cython` using a filename with the hash of the
        code. This file is then cythonized and compiled. The resulting module
        is imported and all of its symbols are injected into the user\'s
        namespace. The usage is similar to that of `%%cython_pyximport` but
        you don\'t have to pass a module name::

            %%cython
            def f(x):
                return 2.0*x

        To compile OpenMP codes, pass the required  `--compile-args`
        and `--link-args`.  For example with gcc::

            %%cython --compile-args=-fopenmp --link-args=-fopenmp
            ...

        To enable profile guided optimisation, pass the ``--pgo`` option.
        Note that the cell itself needs to take care of establishing a suitable
        profile when executed. This can be done by implementing the functions to
        optimise, and then calling them directly in the same cell on some realistic
        training data like this::

            %%cython --pgo
            def critical_function(data):
                for item in data:
                    ...

            # execute function several times to build profile
            from somewhere import some_typical_data
            for _ in range(100):
                critical_function(some_typical_data)

        In Python 3.5 and later, you can distinguish between the profile and
        non-profile runs as follows::

            if "_pgo_" in __name__:
                ...  # execute critical code here
        '''
    @property
    def so_ext(self):
        """The extension suffix for compiled modules."""
    @staticmethod
    def clean_annotated_html(html):
        """Clean up the annotated HTML source.

        Strips the link to the generated C or C++ file, which we do not
        present to the user.
        """

__doc__: Incomplete
