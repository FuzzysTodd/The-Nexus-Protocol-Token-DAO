from argparse import *
import argparse
import autopage
from typing import Any, ContextManager, Sequence, Text, TextIO

def help_pager(out_stream: TextIO | None = None) -> autopage.AutoPager:
    """Return an AutoPager suitable for help output."""
def use_color_for_parser(parser: argparse.ArgumentParser, color: bool) -> None:
    """Configure a parser whether to output in color from HelpFormatters."""

class ColorHelpFormatter(_HelpFormatter):
    class _Section(_HelpFormatter._Section):
        @property
        def heading(self) -> Text | None: ...
        @heading.setter
        def heading(self, heading: Text | None) -> None: ...

class ColorRawDescriptionHelpFormatter(ColorHelpFormatter, argparse.RawDescriptionHelpFormatter):
    """Help message formatter which retains any formatting in descriptions."""
class ColorRawTextHelpFormatter(ColorHelpFormatter, argparse.RawTextHelpFormatter):
    """Help message formatter which retains formatting of all help text."""
class ColorArgDefaultsHelpFormatter(ColorHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    """Help message formatter which adds default values to argument help."""
class ColorMetavarTypeHelpFormatter(ColorHelpFormatter, argparse.MetavarTypeHelpFormatter):
    """Help message formatter which uses the argument 'type' as the default
    metavar value (instead of the argument 'dest')"""

class _HelpAction(argparse._HelpAction):
    def __init__(self, option_strings: Sequence[Text], dest: Text = ..., default: Text = ..., help: Text | None = None) -> None: ...
    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: Text | Sequence[Any] | None, option_string: Text | None = None) -> None: ...

class _ActionsContainer(argparse._ActionsContainer):
    def __init__(self, *args, **kwargs) -> None: ...

class AutoPageArgumentParser(argparse.ArgumentParser, _ActionsContainer): ...
ArgumentParser = AutoPageArgumentParser
HelpFormatter = ColorHelpFormatter
RawDescriptionHelpFormatter = ColorRawDescriptionHelpFormatter
RawTextHelpFormatter = ColorRawTextHelpFormatter
ArgumentDefaultsHelpFormatter = ColorArgDefaultsHelpFormatter
MetavarTypeHelpFormatter = ColorMetavarTypeHelpFormatter

def monkey_patch() -> ContextManager:
    """
    Monkey-patch the system argparse module to automatically page help output.

    The result of calling this function can optionally be used as a context
    manager to restore the status quo when it exits.
    """
