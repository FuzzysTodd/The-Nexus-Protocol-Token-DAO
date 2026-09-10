from .version import SIP_VERSION_STR as SIP_VERSION_STR
from argparse import ArgumentParser as ArgParser

class ArgumentParser(ArgParser):
    """ An argument parser for all sip command line tools. """
    def __init__(self, description, **kwargs) -> None:
        """ Initialise the parser. """
