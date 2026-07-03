import argparse as orig_argparse
from autopage import argparse

class _ArgumentContainerMixIn:
    def add_argument_group(self, *args, **kwargs): ...
    def add_mutually_exclusive_group(self, **kwargs): ...

class ArgumentParser(_ArgumentContainerMixIn, argparse.ArgumentParser): ...
class _ArgumentGroup(_ArgumentContainerMixIn, orig_argparse._ArgumentGroup): ...
class _MutuallyExclusiveGroup(_ArgumentContainerMixIn, orig_argparse._MutuallyExclusiveGroup): ...
class SmartHelpFormatter(argparse.HelpFormatter):
    """Smart help formatter to output raw help message if help contain 
.

    Some command help messages maybe have multiple line content, the built-in
    argparse.HelpFormatter wrap and split the content according to width, and
    ignore 
 in the raw help message, it merge multiple line content in one
    line to output, that looks messy. SmartHelpFormatter keep the raw help
    message format if it contain 
, and wrap long line like HelpFormatter
    behavior.
    """
