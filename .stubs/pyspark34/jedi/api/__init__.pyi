from _typeshed import Incomplete
from jedi import cache as cache, debug as debug, settings as settings
from jedi.api import classes as classes, helpers as helpers, interpreter as interpreter, refactoring as refactoring
from jedi.api.completion import Completion as Completion, search_in_module as search_in_module
from jedi.api.environment import InterpreterEnvironment as InterpreterEnvironment
from jedi.api.errors import parso_to_jedi_errors as parso_to_jedi_errors
from jedi.api.helpers import validate_line_column as validate_line_column
from jedi.api.keywords import KeywordName as KeywordName
from jedi.api.project import Project as Project, get_default_project as get_default_project
from jedi.api.refactoring.extract import extract_function as extract_function, extract_variable as extract_variable
from jedi.file_io import KnownContentFileIO as KnownContentFileIO
from jedi.inference import InferenceState as InferenceState, imports as imports
from jedi.inference.arguments import try_iter_content as try_iter_content
from jedi.inference.base_value import ValueSet as ValueSet
from jedi.inference.gradual.conversion import convert_names as convert_names, convert_values as convert_values
from jedi.inference.gradual.utils import load_proper_stub_module as load_proper_stub_module
from jedi.inference.helpers import infer_call_of_leaf as infer_call_of_leaf
from jedi.inference.references import find_references as find_references
from jedi.inference.syntax_tree import tree_name_to_values as tree_name_to_values
from jedi.inference.sys_path import transform_path_to_dotted as transform_path_to_dotted
from jedi.inference.utils import to_list as to_list
from jedi.inference.value import ModuleValue as ModuleValue
from jedi.inference.value.iterable import unpack_tuple_to_dict as unpack_tuple_to_dict
from jedi.parser_utils import get_executable_nodes as get_executable_nodes

class Script:
    """
    A Script is the base for completions, goto or whatever you want to do with
    Jedi. The counter part of this class is :class:`Interpreter`, which works
    with actual dictionaries and can work with a REPL. This class
    should be used when a user edits code in an editor.

    You can either use the ``code`` parameter or ``path`` to read a file.
    Usually you're going to want to use both of them (in an editor).

    The Script's ``sys.path`` is very customizable:

    - If `project` is provided with a ``sys_path``, that is going to be used.
    - If `environment` is provided, its ``sys.path`` will be used
      (see :func:`Environment.get_sys_path <jedi.api.environment.Environment.get_sys_path>`);
    - Otherwise ``sys.path`` will match that of the default environment of
      Jedi, which typically matches the sys path that was used at the time
      when Jedi was imported.

    Most methods have a ``line`` and a ``column`` parameter. Lines in Jedi are
    always 1-based and columns are always zero based. To avoid repetition they
    are not always documented. You can omit both line and column. Jedi will
    then just do whatever action you are calling at the end of the file. If you
    provide only the line, just will complete at the end of that line.

    .. warning:: By default :attr:`jedi.settings.fast_parser` is enabled, which means
        that parso reuses modules (i.e. they are not immutable). With this setting
        Jedi is **not thread safe** and it is also not safe to use multiple
        :class:`.Script` instances and its definitions at the same time.

        If you are a normal plugin developer this should not be an issue. It is
        an issue for people that do more complex stuff with Jedi.

        This is purely a performance optimization and works pretty well for all
        typical usages, however consider to turn the setting off if it causes
        you problems. See also
        `this discussion <https://github.com/davidhalter/jedi/issues/1240>`_.

    :param code: The source code of the current file, separated by newlines.
    :type code: str
    :param path: The path of the file in the file system, or ``''`` if
        it hasn't been saved yet.
    :type path: str or pathlib.Path or None
    :param Environment environment: Provide a predefined :ref:`Environment <environments>`
        to work with a specific Python version or virtualenv.
    :param Project project: Provide a :class:`.Project` to make sure finding
        references works well, because the right folder is searched. There are
        also ways to modify the sys path and other things.
    """
    path: Incomplete
    def __init__(self, code: Incomplete | None = None, *, path: Incomplete | None = None, environment: Incomplete | None = None, project: Incomplete | None = None) -> None: ...
    def complete(self, line: Incomplete | None = None, column: Incomplete | None = None, *, fuzzy: bool = False):
        '''
        Completes objects under the cursor.

        Those objects contain information about the completions, more than just
        names.

        :param fuzzy: Default False. Will return fuzzy completions, which means
            that e.g. ``ooa`` will match ``foobar``.
        :return: Completion objects, sorted by name. Normal names appear
            before "private" names that start with ``_`` and those appear
            before magic methods and name mangled names that start with ``__``.
        :rtype: list of :class:`.Completion`
        '''
    def infer(self, line: Incomplete | None = None, column: Incomplete | None = None, *, only_stubs: bool = False, prefer_stubs: bool = False): ...
    def goto(self, line: Incomplete | None = None, column: Incomplete | None = None, *, follow_imports: bool = False, follow_builtin_imports: bool = False, only_stubs: bool = False, prefer_stubs: bool = False): ...
    def search(self, string, *, all_scopes: bool = False):
        """
        Searches a name in the current file. For a description of how the
        search string should look like, please have a look at
        :meth:`.Project.search`.

        :param bool all_scopes: Default False; searches not only for
            definitions on the top level of a module level, but also in
            functions and classes.
        :yields: :class:`.Name`
        """
    def complete_search(self, string, **kwargs):
        """
        Like :meth:`.Script.search`, but completes that string. If you want to
        have all possible definitions in a file you can also provide an empty
        string.

        :param bool all_scopes: Default False; searches not only for
            definitions on the top level of a module level, but also in
            functions and classes.
        :param fuzzy: Default False. Will return fuzzy completions, which means
            that e.g. ``ooa`` will match ``foobar``.
        :yields: :class:`.Completion`
        """
    def help(self, line: Incomplete | None = None, column: Incomplete | None = None):
        """
        Used to display a help window to users.  Uses :meth:`.Script.goto` and
        returns additional definitions for keywords and operators.

        Typically you will want to display :meth:`.BaseName.docstring` to the
        user for all the returned definitions.

        The additional definitions are ``Name(...).type == 'keyword'``.
        These definitions do not have a lot of value apart from their docstring
        attribute, which contains the output of Python's :func:`help` function.

        :rtype: list of :class:`.Name`
        """
    def get_references(self, line: Incomplete | None = None, column: Incomplete | None = None, **kwargs):
        """
        Lists all references of a variable in a project. Since this can be
        quite hard to do for Jedi, if it is too complicated, Jedi will stop
        searching.

        :param include_builtins: Default ``True``. If ``False``, checks if a definition
            is a builtin (e.g. ``sys``) and in that case does not return it.
        :param scope: Default ``'project'``. If ``'file'``, include references in
            the current module only.
        :rtype: list of :class:`.Name`
        """
    def get_signatures(self, line: Incomplete | None = None, column: Incomplete | None = None):
        """
        Return the function object of the call under the cursor.

        E.g. if the cursor is here::

            abs(# <-- cursor is here

        This would return the ``abs`` function. On the other hand::

            abs()# <-- cursor is here

        This would return an empty list..

        :rtype: list of :class:`.Signature`
        """
    def get_context(self, line: Incomplete | None = None, column: Incomplete | None = None):
        """
        Returns the scope context under the cursor. This basically means the
        function, class or module where the cursor is at.

        :rtype: :class:`.Name`
        """
    def get_names(self, **kwargs):
        """
        Returns names defined in the current file.

        :param all_scopes: If True lists the names of all scopes instead of
            only the module namespace.
        :param definitions: If True lists the names that have been defined by a
            class, function or a statement (``a = b`` returns ``a``).
        :param references: If True lists all the names that are not listed by
            ``definitions=True``. E.g. ``a = b`` returns ``b``.
        :rtype: list of :class:`.Name`
        """
    def get_syntax_errors(self):
        """
        Lists all syntax errors in the current file.

        :rtype: list of :class:`.SyntaxError`
        """
    def rename(self, line: Incomplete | None = None, column: Incomplete | None = None, *, new_name):
        """
        Renames all references of the variable under the cursor.

        :param new_name: The variable under the cursor will be renamed to this
            string.
        :raises: :exc:`.RefactoringError`
        :rtype: :class:`.Refactoring`
        """
    def extract_variable(self, line, column, *, new_name, until_line: Incomplete | None = None, until_column: Incomplete | None = None):
        """
        Moves an expression to a new statement.

        For example if you have the cursor on ``foo`` and provide a
        ``new_name`` called ``bar``::

            foo = 3.1
            x = int(foo + 1)

        the code above will become::

            foo = 3.1
            bar = foo + 1
            x = int(bar)

        :param new_name: The expression under the cursor will be renamed to
            this string.
        :param int until_line: The the selection range ends at this line, when
            omitted, Jedi will be clever and try to define the range itself.
        :param int until_column: The the selection range ends at this column, when
            omitted, Jedi will be clever and try to define the range itself.
        :raises: :exc:`.RefactoringError`
        :rtype: :class:`.Refactoring`
        """
    def extract_function(self, line, column, *, new_name, until_line: Incomplete | None = None, until_column: Incomplete | None = None):
        """
        Moves an expression to a new function.

        For example if you have the cursor on ``foo`` and provide a
        ``new_name`` called ``bar``::

            global_var = 3

            def x():
                foo = 3.1
                x = int(foo + 1 + global_var)

        the code above will become::

            global_var = 3

            def bar(foo):
                return int(foo + 1 + global_var)

            def x():
                foo = 3.1
                x = bar(foo)

        :param new_name: The expression under the cursor will be replaced with
            a function with this name.
        :param int until_line: The the selection range ends at this line, when
            omitted, Jedi will be clever and try to define the range itself.
        :param int until_column: The the selection range ends at this column, when
            omitted, Jedi will be clever and try to define the range itself.
        :raises: :exc:`.RefactoringError`
        :rtype: :class:`.Refactoring`
        """
    def inline(self, line: Incomplete | None = None, column: Incomplete | None = None):
        """
        Inlines a variable under the cursor. This is basically the opposite of
        extracting a variable. For example with the cursor on bar::

            foo = 3.1
            bar = foo + 1
            x = int(bar)

        the code above will become::

            foo = 3.1
            x = int(foo + 1)

        :raises: :exc:`.RefactoringError`
        :rtype: :class:`.Refactoring`
        """

class Interpreter(Script):
    '''
    Jedi\'s API for Python REPLs.

    Implements all of the methods that are present in :class:`.Script` as well.

    In addition to completions that normal REPL completion does like
    ``str.upper``, Jedi also supports code completion based on static code
    analysis. For example Jedi will complete ``str().upper``.

    >>> from os.path import join
    >>> namespace = locals()
    >>> script = Interpreter(\'join("").up\', [namespace])
    >>> print(script.complete()[0].name)
    upper

    All keyword arguments are same as the arguments for :class:`.Script`.

    :param str code: Code to parse.
    :type namespaces: typing.List[dict]
    :param namespaces: A list of namespace dictionaries such as the one
        returned by :func:`globals` and :func:`locals`.
    '''
    namespaces: Incomplete
    def __init__(self, code, namespaces, *, project: Incomplete | None = None, **kwds) -> None: ...

def preload_module(*modules) -> None:
    """
    Preloading modules tells Jedi to load a module now, instead of lazy parsing
    of modules. This can be useful for IDEs, to control which modules to load
    on startup.

    :param modules: different module names, list of string.
    """
def set_debug_function(func_cb=..., warnings: bool = True, notices: bool = True, speed: bool = True) -> None:
    """
    Define a callback debug function to get all the debug messages.

    If you don't specify any arguments, debug messages will be printed to stdout.

    :param func_cb: The callback function for debug messages.
    """
