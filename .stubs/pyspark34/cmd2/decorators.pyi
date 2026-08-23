import argparse
from . import constants as constants
from .argparse_custom import Cmd2AttributeWrapper as Cmd2AttributeWrapper
from .command_definition import CommandFunc as CommandFunc, CommandSet as CommandSet
from .exceptions import Cmd2ArgparseError as Cmd2ArgparseError
from .parsing import Statement as Statement
from .utils import strip_doc_annotations as strip_doc_annotations
from _typeshed import Incomplete
from typing import Callable, List

def with_category(category: str) -> Callable[[CommandFunc], CommandFunc]:
    """A decorator to apply a category to a ``do_*`` command method.

    :param category: the name of the category in which this command should
                     be grouped when displaying the list of commands.

    :Example:

    >>> class MyApp(cmd2.Cmd):
    >>>   @cmd2.with_category('Text Functions')
    >>>   def do_echo(self, args)
    >>>     self.poutput(args)

    For an alternative approach to categorizing commands using a function, see
    :func:`~cmd2.utils.categorize`
    """

RawCommandFuncOptionalBoolReturn: Incomplete
ArgListCommandFuncOptionalBoolReturn: Incomplete
ArgListCommandFuncBoolReturn: Incomplete
ArgListCommandFuncNoneReturn: Incomplete
ArgListCommandFunc = ArgListCommandFuncOptionalBoolReturn | ArgListCommandFuncBoolReturn | ArgListCommandFuncNoneReturn

def with_argument_list(func_arg: ArgListCommandFunc | None = None, *, preserve_quotes: bool = False) -> RawCommandFuncOptionalBoolReturn | Callable[[ArgListCommandFunc], RawCommandFuncOptionalBoolReturn]:
    """
    A decorator to alter the arguments passed to a ``do_*`` method. Default
    passes a string of whatever the user typed. With this decorator, the
    decorated method will receive a list of arguments parsed from user input.

    :param func_arg: Single-element positional argument list containing ``do_*`` method
                 this decorator is wrapping
    :param preserve_quotes: if ``True``, then argument quotes will not be stripped
    :return: function that gets passed a list of argument strings

    :Example:

    >>> class MyApp(cmd2.Cmd):
    >>>     @cmd2.with_argument_list
    >>>     def do_echo(self, arglist):
    >>>         self.poutput(' '.join(arglist)
    """

ArgparseCommandFuncOptionalBoolReturn: Incomplete
ArgparseCommandFuncBoolReturn: Incomplete
ArgparseCommandFuncNoneReturn: Incomplete
ArgparseCommandFunc = ArgparseCommandFuncOptionalBoolReturn | ArgparseCommandFuncBoolReturn | ArgparseCommandFuncNoneReturn

def with_argparser(parser: argparse.ArgumentParser, *, ns_provider: Callable[..., argparse.Namespace] | None = None, preserve_quotes: bool = False, with_unknown_args: bool = False) -> Callable[[ArgparseCommandFunc], RawCommandFuncOptionalBoolReturn]:
    '''A decorator to alter a cmd2 method to populate its ``args`` argument by parsing arguments
    with the given instance of argparse.ArgumentParser.

    :param parser: unique instance of ArgumentParser
    :param ns_provider: An optional function that accepts a cmd2.Cmd or cmd2.CommandSet object as an argument and returns an
                        argparse.Namespace. This is useful if the Namespace needs to be prepopulated with state data that
                        affects parsing.
    :param preserve_quotes: if ``True``, then arguments passed to argparse maintain their quotes
    :param with_unknown_args: if true, then capture unknown args
    :return: function that gets passed argparse-parsed args in a ``Namespace``
             A :class:`cmd2.argparse_custom.Cmd2AttributeWrapper` called ``cmd2_statement`` is included
             in the ``Namespace`` to provide access to the :class:`cmd2.Statement` object that was created when
             parsing the command line. This can be useful if the command function needs to know the command line.

    :Example:

    >>> parser = cmd2.Cmd2ArgumentParser()
    >>> parser.add_argument(\'-p\', \'--piglatin\', action=\'store_true\', help=\'atinLay\')
    >>> parser.add_argument(\'-s\', \'--shout\', action=\'store_true\', help=\'N00B EMULATION MODE\')
    >>> parser.add_argument(\'-r\', \'--repeat\', type=int, help=\'output [n] times\')
    >>> parser.add_argument(\'words\', nargs=\'+\', help=\'words to print\')
    >>>
    >>> class MyApp(cmd2.Cmd):
    >>>     @cmd2.with_argparser(parser, preserve_quotes=True)
    >>>     def do_argprint(self, args):
    >>>         "Print the options and argument list this options command was called with."
    >>>         self.poutput(f\'args: {args!r}\')

    :Example with unknown args:

    >>> parser = cmd2.Cmd2ArgumentParser()
    >>> parser.add_argument(\'-p\', \'--piglatin\', action=\'store_true\', help=\'atinLay\')
    >>> parser.add_argument(\'-s\', \'--shout\', action=\'store_true\', help=\'N00B EMULATION MODE\')
    >>> parser.add_argument(\'-r\', \'--repeat\', type=int, help=\'output [n] times\')
    >>>
    >>> class MyApp(cmd2.Cmd):
    >>>     @cmd2.with_argparser(parser, with_unknown_args=True)
    >>>     def do_argprint(self, args, unknown):
    >>>         "Print the options and argument list this options command was called with."
    >>>         self.poutput(f\'args: {args!r}\')
    >>>         self.poutput(f\'unknowns: {unknown}\')

    '''
def as_subcommand_to(command: str, subcommand: str, parser: argparse.ArgumentParser, *, help: str | None = None, aliases: List[str] | None = None) -> Callable[[ArgparseCommandFunc], ArgparseCommandFunc]:
    """
    Tag this method as a subcommand to an existing argparse decorated command.

    :param command: Command Name. Space-delimited subcommands may optionally be specified
    :param subcommand: Subcommand name
    :param parser: argparse Parser for this subcommand
    :param help: Help message for this subcommand which displays in the list of subcommands of the command we are adding to.
                 This is passed as the help argument to ArgumentParser.add_subparser().
    :param aliases: Alternative names for this subcommand. This is passed as the alias argument to
                    ArgumentParser.add_subparser().
    :return: Wrapper function that can receive an argparse.Namespace
    """
