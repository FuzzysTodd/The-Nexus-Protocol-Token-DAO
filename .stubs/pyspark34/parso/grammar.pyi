import os
from _typeshed import Incomplete
from parso._compatibility import is_pypy as is_pypy
from parso.cache import load_module as load_module, parser_cache as parser_cache, try_to_save_module as try_to_save_module
from parso.file_io import FileIO as FileIO, KnownContentFileIO as KnownContentFileIO
from parso.normalizer import NormalizerConfig as NormalizerConfig, RefactoringNormalizer as RefactoringNormalizer
from parso.parser import BaseParser as BaseParser
from parso.pgen2 import generate_grammar as generate_grammar
from parso.python import pep8 as pep8
from parso.python.diff import DiffParser as DiffParser
from parso.python.errors import ErrorFinderConfig as ErrorFinderConfig
from parso.python.token import PythonTokenTypes as PythonTokenTypes
from parso.python.tokenize import tokenize as tokenize, tokenize_lines as tokenize_lines
from parso.utils import PythonVersionInfo as PythonVersionInfo, parse_version_string as parse_version_string, python_bytes_to_unicode as python_bytes_to_unicode, split_lines as split_lines
from typing import Generic

class Grammar(Generic[_NodeT]):
    """
    :py:func:`parso.load_grammar` returns instances of this class.

    Creating custom none-python grammars by calling this is not supported, yet.

    :param text: A BNF representation of your grammar.
    """
    def __init__(self, text: str, *, tokenizer, parser=..., diff_parser: Incomplete | None = None) -> None: ...
    def parse(self, code: str | bytes = None, *, error_recovery: bool = True, path: os.PathLike | str = None, start_symbol: str = None, cache: bool = False, diff_cache: bool = False, cache_path: os.PathLike | str = None, file_io: FileIO = None) -> _NodeT:
        """
        If you want to parse a Python file you want to start here, most likely.

        If you need finer grained control over the parsed instance, there will be
        other ways to access it.

        :param str code: A unicode or bytes string. When it's not possible to
            decode bytes to a string, returns a
            :py:class:`UnicodeDecodeError`.
        :param bool error_recovery: If enabled, any code will be returned. If
            it is invalid, it will be returned as an error node. If disabled,
            you will get a ParseError when encountering syntax errors in your
            code.
        :param str start_symbol: The grammar rule (nonterminal) that you want
            to parse. Only allowed to be used when error_recovery is False.
        :param str path: The path to the file you want to open. Only needed for caching.
        :param bool cache: Keeps a copy of the parser tree in RAM and on disk
            if a path is given. Returns the cached trees if the corresponding
            files on disk have not changed. Note that this stores pickle files
            on your file system (e.g. for Linux in ``~/.cache/parso/``).
        :param bool diff_cache: Diffs the cached python module against the new
            code and tries to parse only the parts that have changed. Returns
            the same (changed) module that is found in cache. Using this option
            requires you to not do anything anymore with the cached modules
            under that path, because the contents of it might change. This
            option is still somewhat experimental. If you want stability,
            please don't use it.
        :param bool cache_path: If given saves the parso cache in this
            directory. If not given, defaults to the default cache places on
            each platform.

        :return: A subclass of :py:class:`parso.tree.NodeOrLeaf`. Typically a
            :py:class:`parso.python.tree.Module`.
        """
    def iter_errors(self, node):
        """
        Given a :py:class:`parso.tree.NodeOrLeaf` returns a generator of
        :py:class:`parso.normalizer.Issue` objects. For Python this is
        a list of syntax/indentation errors.
        """
    def refactor(self, base_node, node_to_str_map): ...

class PythonGrammar(Grammar):
    version_info: Incomplete
    def __init__(self, version_info: PythonVersionInfo, bnf_text: str) -> None: ...

def load_grammar(*, version: str = None, path: str = None):
    """
    Loads a :py:class:`parso.Grammar`. The default version is the current Python
    version.

    :param str version: A python version string, e.g. ``version='3.8'``.
    :param str path: A path to a grammar file
    """
