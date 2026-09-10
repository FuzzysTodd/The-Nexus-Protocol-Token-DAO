from .depends import Require as Require
from .dist import Distribution as Distribution
from .extension import Extension as Extension
from .warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning
from _typeshed import Incomplete

__all__ = ['setup', 'Distribution', 'Command', 'Extension', 'Require', 'SetuptoolsDeprecationWarning', 'find_packages', 'find_namespace_packages']

find_packages: Incomplete
find_namespace_packages: Incomplete

def setup(**attrs): ...

class Command(_Command):
    '''
    Setuptools internal actions are organized using a *command design pattern*.
    This means that each action (or group of closely related actions) executed during
    the build should be implemented as a ``Command`` subclass.

    These commands are abstractions and do not necessarily correspond to a command that
    can (or should) be executed via a terminal, in a CLI fashion (although historically
    they would).

    When creating a new command from scratch, custom defined classes **SHOULD** inherit
    from ``setuptools.Command`` and implement a few mandatory methods.
    Between these mandatory methods, are listed:

    .. method:: initialize_options(self)

        Set or (reset) all options/attributes/caches used by the command
        to their default values. Note that these values may be overwritten during
        the build.

    .. method:: finalize_options(self)

        Set final values for all options/attributes used by the command.
        Most of the time, each option/attribute/cache should only be set if it does not
        have any value yet (e.g. ``if self.attr is None: self.attr = val``).

    .. method:: run(self)

        Execute the actions intended by the command.
        (Side effects **SHOULD** only take place when ``run`` is executed,
        for example, creating new files or writing to the terminal output).

    A useful analogy for command classes is to think of them as subroutines with local
    variables called "options".  The options are "declared" in ``initialize_options()``
    and "defined" (given their final values, aka "finalized") in ``finalize_options()``,
    both of which must be defined by every command class. The "body" of the subroutine,
    (where it does all the work) is the ``run()`` method.
    Between ``initialize_options()`` and ``finalize_options()``, ``setuptools`` may set
    the values for options/attributes based on user\'s input (or circumstance),
    which means that the implementation should be careful to not overwrite values in
    ``finalize_options`` unless necessary.

    Please note that other commands (or other parts of setuptools) may also overwrite
    the values of the command\'s options/attributes multiple times during the build
    process.
    Therefore it is important to consistently implement ``initialize_options()`` and
    ``finalize_options()``. For example, all derived attributes (or attributes that
    depend on the value of other attributes) **SHOULD** be recomputed in
    ``finalize_options``.

    When overwriting existing commands, custom defined classes **MUST** abide by the
    same APIs implemented by the original class. They also **SHOULD** inherit from the
    original class.
    '''
    command_consumes_arguments: bool
    def __init__(self, dist, **kw) -> None:
        """
        Construct the command for dist, updating
        vars(self) with any keyword parameters.
        """
    def ensure_string_list(self, option) -> None:
        '''Ensure that \'option\' is a list of strings.  If \'option\' is
        currently a string, we split it either on /,\\s*/ or /\\s+/, so
        "foo bar baz", "foo,bar,baz", and "foo,   bar baz" all become
        ["foo", "bar", "baz"].

        ..
           TODO: This method seems to be similar to the one in ``distutils.cmd``
           Probably it is just here for backward compatibility with old Python versions?

        :meta private:
        '''
    def reinitialize_command(self, command, reinit_subcommands: int = 0, **kw): ...

class sic(str):
    """Treat this string as-is (https://en.wikipedia.org/wiki/Sic)"""
