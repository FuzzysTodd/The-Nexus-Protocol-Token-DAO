import argparse
from _typeshed import Incomplete

__all__ = ['magic_arguments', 'argument', 'argument_group', 'kwds', 'parse_argstring']

class MagicHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """A HelpFormatter with a couple of changes to meet our needs.
    """
    def add_usage(self, usage, actions, groups, prefix: str = '::\n\n  %') -> None: ...

class MagicArgumentParser(argparse.ArgumentParser):
    """ An ArgumentParser tweaked for use by IPython magics.
    """
    def __init__(self, prog: Incomplete | None = None, usage: Incomplete | None = None, description: Incomplete | None = None, epilog: Incomplete | None = None, parents: Incomplete | None = None, formatter_class=..., prefix_chars: str = '-', argument_default: Incomplete | None = None, conflict_handler: str = 'error', add_help: bool = False) -> None: ...
    def error(self, message) -> None:
        """ Raise a catchable error instead of exiting.
        """
    def parse_argstring(self, argstring):
        """ Split a string into an argument list and parse that argument list.
        """

def parse_argstring(magic_func, argstring):
    """ Parse the string of arguments for the given magic function.
    """

class ArgDecorator:
    """ Base class for decorators to add ArgumentParser information to a method.
    """
    def __call__(self, func): ...
    def add_to_parser(self, parser, group) -> None:
        """ Add this object's information to the parser, if necessary.
        """

class magic_arguments(ArgDecorator):
    """ Mark the magic as having argparse arguments and possibly adjust the
    name.
    """
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...
    def __call__(self, func): ...

class ArgMethodWrapper(ArgDecorator):
    """
    Base class to define a wrapper for ArgumentParser method.

    Child class must define either `_method_name` or `add_to_parser`.

    """
    args: Incomplete
    kwds: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def add_to_parser(self, parser, group) -> None:
        """ Add this object's information to the parser.
        """

class argument(ArgMethodWrapper):
    """ Store arguments and keywords to pass to add_argument().

    Instances also serve to decorate command methods.
    """
class defaults(ArgMethodWrapper):
    """ Store arguments and keywords to pass to set_defaults().

    Instances also serve to decorate command methods.
    """

class argument_group(ArgMethodWrapper):
    """ Store arguments and keywords to pass to add_argument_group().

    Instances also serve to decorate command methods.
    """
    def add_to_parser(self, parser, group):
        """ Add this object's information to the parser.
        """

class kwds(ArgDecorator):
    """ Provide other keywords to the sub-parser constructor.
    """
    kwds: Incomplete
    def __init__(self, **kwds) -> None: ...
    def __call__(self, func): ...
