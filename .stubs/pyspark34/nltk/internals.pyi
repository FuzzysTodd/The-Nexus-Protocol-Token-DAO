from _typeshed import Incomplete
from collections.abc import Generator

def config_java(bin: Incomplete | None = None, options: Incomplete | None = None, verbose: bool = False) -> None:
    """
    Configure nltk's java interface, by letting nltk know where it can
    find the Java binary, and what extra options (if any) should be
    passed to Java when it is run.

    :param bin: The full path to the Java binary.  If not specified,
        then nltk will search the system for a Java binary; and if
        one is not found, it will raise a ``LookupError`` exception.
    :type bin: str
    :param options: A list of options that should be passed to the
        Java binary when it is called.  A common value is
        ``'-Xmx512m'``, which tells Java binary to increase
        the maximum heap size to 512 megabytes.  If no options are
        specified, then do not modify the options list.
    :type options: list(str)
    """
def java(cmd, classpath: Incomplete | None = None, stdin: Incomplete | None = None, stdout: Incomplete | None = None, stderr: Incomplete | None = None, blocking: bool = True):
    """
    Execute the given java command, by opening a subprocess that calls
    Java.  If java has not yet been configured, it will be configured
    by calling ``config_java()`` with no arguments.

    :param cmd: The java command that should be called, formatted as
        a list of strings.  Typically, the first string will be the name
        of the java class; and the remaining strings will be arguments
        for that java class.
    :type cmd: list(str)

    :param classpath: A ``':'`` separated list of directories, JAR
        archives, and ZIP archives to search for class files.
    :type classpath: str

    :param stdin: Specify the executed program's
        standard input file handles, respectively.  Valid values are ``subprocess.PIPE``,
        an existing file descriptor (a positive integer), an existing
        file object, 'pipe', 'stdout', 'devnull' and None.  ``subprocess.PIPE`` indicates that a
        new pipe to the child should be created.  With None, no
        redirection will occur; the child's file handles will be
        inherited from the parent.  Additionally, stderr can be
        ``subprocess.STDOUT``, which indicates that the stderr data
        from the applications should be captured into the same file
        handle as for stdout.

    :param stdout: Specify the executed program's standard output file
        handle. See ``stdin`` for valid values.

    :param stderr: Specify the executed program's standard error file
        handle. See ``stdin`` for valid values.


    :param blocking: If ``false``, then return immediately after
        spawning the subprocess.  In this case, the return value is
        the ``Popen`` object, and not a ``(stdout, stderr)`` tuple.

    :return: If ``blocking=True``, then return a tuple ``(stdout,
        stderr)``, containing the stdout and stderr outputs generated
        by the java command if the ``stdout`` and ``stderr`` parameters
        were set to ``subprocess.PIPE``; or None otherwise.  If
        ``blocking=False``, then return a ``subprocess.Popen`` object.

    :raise OSError: If the java command returns a nonzero return code.
    """

class ReadError(ValueError):
    """
    Exception raised by read_* functions when they fail.
    :param position: The index in the input string where an error occurred.
    :param expected: What was expected when an error occurred.
    """
    expected: Incomplete
    position: Incomplete
    def __init__(self, expected, position) -> None: ...

def read_str(s, start_position):
    '''
    If a Python string literal begins at the specified position in the
    given string, then return a tuple ``(val, end_position)``
    containing the value of the string literal and the position where
    it ends.  Otherwise, raise a ``ReadError``.

    :param s: A string that will be checked to see if within which a
        Python string literal exists.
    :type s: str

    :param start_position: The specified beginning position of the string ``s``
        to begin regex matching.
    :type start_position: int

    :return: A tuple containing the matched string literal evaluated as a
        string and the end position of the string literal.
    :rtype: tuple(str, int)

    :raise ReadError: If the ``_STRING_START_RE`` regex doesn\'t return a
        match in ``s`` at ``start_position``, i.e., open quote. If the
        ``_STRING_END_RE`` regex doesn\'t return a match in ``s`` at the
        end of the first match, i.e., close quote.
    :raise ValueError: If an invalid string (i.e., contains an invalid
        escape sequence) is passed into the ``eval``.

    :Example:

    >>> from nltk.internals import read_str
    >>> read_str(\'"Hello", World!\', 0)
    (\'Hello\', 7)

    '''
def read_int(s, start_position):
    """
    If an integer begins at the specified position in the given
    string, then return a tuple ``(val, end_position)`` containing the
    value of the integer and the position where it ends.  Otherwise,
    raise a ``ReadError``.

    :param s: A string that will be checked to see if within which a
        Python integer exists.
    :type s: str

    :param start_position: The specified beginning position of the string ``s``
        to begin regex matching.
    :type start_position: int

    :return: A tuple containing the matched integer casted to an int,
        and the end position of the int in ``s``.
    :rtype: tuple(int, int)

    :raise ReadError: If the ``_READ_INT_RE`` regex doesn't return a
        match in ``s`` at ``start_position``.

    :Example:

    >>> from nltk.internals import read_int
    >>> read_int('42 is the answer', 0)
    (42, 2)

    """
def read_number(s, start_position):
    """
    If an integer or float begins at the specified position in the
    given string, then return a tuple ``(val, end_position)``
    containing the value of the number and the position where it ends.
    Otherwise, raise a ``ReadError``.

    :param s: A string that will be checked to see if within which a
        Python number exists.
    :type s: str

    :param start_position: The specified beginning position of the string ``s``
        to begin regex matching.
    :type start_position: int

    :return: A tuple containing the matched number casted to a ``float``,
        and the end position of the number in ``s``.
    :rtype: tuple(float, int)

    :raise ReadError: If the ``_READ_NUMBER_VALUE`` regex doesn't return a
        match in ``s`` at ``start_position``.

    :Example:

    >>> from nltk.internals import read_number
    >>> read_number('Pi is 3.14159', 6)
    (3.14159, 13)

    """
def overridden(method):
    """
    :return: True if ``method`` overrides some method with the same
        name in a base class.  This is typically used when defining
        abstract base classes or interfaces, to allow subclasses to define
        either of two related methods:

        >>> class EaterI:
        ...     '''Subclass must define eat() or batch_eat().'''
        ...     def eat(self, food):
        ...         if overridden(self.batch_eat):
        ...             return self.batch_eat([food])[0]
        ...         else:
        ...             raise NotImplementedError()
        ...     def batch_eat(self, foods):
        ...         return [self.eat(food) for food in foods]

    :type method: instance method
    """
def deprecated(message):
    """
    A decorator used to mark functions as deprecated.  This will cause
    a warning to be printed the when the function is used.  Usage:

        >>> from nltk.internals import deprecated
        >>> @deprecated('Use foo() instead')
        ... def bar(x):
        ...     print(x/10)

    """

class Deprecated:
    '''
    A base class used to mark deprecated classes.  A typical usage is to
    alert users that the name of a class has changed:

        >>> from nltk.internals import Deprecated
        >>> class NewClassName:
        ...     pass # All logic goes here.
        ...
        >>> class OldClassName(Deprecated, NewClassName):
        ...     "Use NewClassName instead."

    The docstring of the deprecated class will be used in the
    deprecation warning message.
    '''
    def __new__(cls, *args, **kwargs): ...

class Counter:
    """
    A counter that auto-increments each time its value is read.
    """
    def __init__(self, initial_value: int = 0) -> None: ...
    def get(self): ...

def find_file_iter(filename, env_vars=(), searchpath=(), file_names: Incomplete | None = None, url: Incomplete | None = None, verbose: bool = False, finding_dir: bool = False) -> Generator[Incomplete, None, None]:
    """
    Search for a file to be used by nltk.

    :param filename: The name or path of the file.
    :param env_vars: A list of environment variable names to check.
    :param file_names: A list of alternative file names to check.
    :param searchpath: List of directories to search.
    :param url: URL presented to user for download help.
    :param verbose: Whether or not to print path when a file is found.
    """
def find_file(filename, env_vars=(), searchpath=(), file_names: Incomplete | None = None, url: Incomplete | None = None, verbose: bool = False): ...
def find_dir(filename, env_vars=(), searchpath=(), file_names: Incomplete | None = None, url: Incomplete | None = None, verbose: bool = False): ...
def find_binary_iter(name, path_to_bin: Incomplete | None = None, env_vars=(), searchpath=(), binary_names: Incomplete | None = None, url: Incomplete | None = None, verbose: bool = False) -> Generator[Incomplete, Incomplete, None]:
    """
    Search for a file to be used by nltk.

    :param name: The name or path of the file.
    :param path_to_bin: The user-supplied binary location (deprecated)
    :param env_vars: A list of environment variable names to check.
    :param file_names: A list of alternative file names to check.
    :param searchpath: List of directories to search.
    :param url: URL presented to user for download help.
    :param verbose: Whether or not to print path when a file is found.
    """
def find_binary(name, path_to_bin: Incomplete | None = None, env_vars=(), searchpath=(), binary_names: Incomplete | None = None, url: Incomplete | None = None, verbose: bool = False): ...
def find_jar_iter(name_pattern, path_to_jar: Incomplete | None = None, env_vars=(), searchpath=(), url: Incomplete | None = None, verbose: bool = False, is_regex: bool = False) -> Generator[Incomplete, None, None]:
    """
    Search for a jar that is used by nltk.

    :param name_pattern: The name of the jar file
    :param path_to_jar: The user-supplied jar location, or None.
    :param env_vars: A list of environment variable names to check
                     in addition to the CLASSPATH variable which is
                     checked by default.
    :param searchpath: List of directories to search.
    :param is_regex: Whether name is a regular expression.
    """
def find_jar(name_pattern, path_to_jar: Incomplete | None = None, env_vars=(), searchpath=(), url: Incomplete | None = None, verbose: bool = False, is_regex: bool = False): ...
def find_jars_within_path(path_to_jars): ...
def import_from_stdlib(module):
    """
    When python is run from within the nltk/ directory tree, the
    current directory is included at the beginning of the search path.
    Unfortunately, that means that modules within nltk can sometimes
    shadow standard library modules.  As an example, the stdlib
    'inspect' module will attempt to import the stdlib 'tokenize'
    module, but will instead end up importing NLTK's 'tokenize' module
    instead (causing the import to fail).
    """

class ElementWrapper:
    """
    A wrapper around ElementTree Element objects whose main purpose is
    to provide nicer __repr__ and __str__ methods.  In addition, any
    of the wrapped Element's methods that return other Element objects
    are overridden to wrap those values before returning them.

    This makes Elements more convenient to work with in
    interactive sessions and doctests, at the expense of some
    efficiency.
    """
    def __new__(cls, etree):
        """
        Create and return a wrapper around a given Element object.
        If ``etree`` is an ``ElementWrapper``, then ``etree`` is
        returned as-is.
        """
    def __init__(self, etree) -> None:
        '''
        Initialize a new Element wrapper for ``etree``.

        If ``etree`` is a string, then it will be converted to an
        Element object using ``ElementTree.fromstring()`` first:

            >>> ElementWrapper("<test></test>")
            <Element "<?xml version=\'1.0\' encoding=\'utf8\'?>\\n<test />">

        '''
    def unwrap(self):
        """
        Return the Element object wrapped by this wrapper.
        """
    def __getattr__(self, attrib): ...
    def __setattr__(self, attr, value): ...
    def __delattr__(self, attr): ...
    def __setitem__(self, index, element) -> None: ...
    def __delitem__(self, index) -> None: ...
    def __setslice__(self, start, stop, elements) -> None: ...
    def __delslice__(self, start, stop) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __getslice__(self, start, stop): ...
    def getchildren(self): ...
    def getiterator(self, tag: Incomplete | None = None): ...
    def makeelement(self, tag, attrib): ...
    def find(self, path): ...
    def findall(self, path): ...

def slice_bounds(sequence, slice_obj, allow_step: bool = False):
    """
    Given a slice, return the corresponding (start, stop) bounds,
    taking into account None indices and negative indices.  The
    following guarantees are made for the returned start and stop values:

      - 0 <= start <= len(sequence)
      - 0 <= stop <= len(sequence)
      - start <= stop

    :raise ValueError: If ``slice_obj.step`` is not None.
    :param allow_step: If true, then the slice object may have a
        non-None step.  If it does, then return a tuple
        (start, stop, step).
    """
def is_writable(path): ...
def raise_unorderable_types(ordering, a, b) -> None: ...
