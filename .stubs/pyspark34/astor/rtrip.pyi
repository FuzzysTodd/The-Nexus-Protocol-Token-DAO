from astor.code_gen import to_source as to_source
from astor.file_util import code_to_ast as code_to_ast
from astor.node_util import allow_ast_comparison as allow_ast_comparison, dump_tree as dump_tree, fast_compare as fast_compare, strip_tree as strip_tree

dsttree: str

def out_prep(s, pre_encoded=...): ...
def convert(srctree, dsttree=..., readonly: bool = False, dumpall: bool = False, ignore_exceptions: bool = False, fullcomp: bool = False):
    """Walk the srctree, and convert/copy all python files
    into the dsttree

    """
def usage(msg) -> None: ...
