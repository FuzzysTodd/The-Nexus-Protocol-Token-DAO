from _typeshed import Incomplete

def setup(parser):
    """Add common sampling options to CLI parser.

    Parameters
    ----------
    parser : argparse object

    Returns
    -------
    Updated argparse object
    """
def create(cli_parser: Incomplete | None = None):
    """Create CLI parser object.

    Parameters
    ----------
    cli_parser : function [optional]
        Function to add method specific arguments to parser

    Returns
    -------
    argparse object
    """
def run_cli(cli_parser, run_sample, known_args: Incomplete | None = None) -> None:
    """Run sampling with CLI arguments.

    Parameters
    ----------
    cli_parser : function
        Function to add method specific arguments to parser
    run_sample: function
        Method specific function that runs the sampling
    known_args: list [optional]
        Additional arguments to parse

    Returns
    -------
    argparse object
    """
