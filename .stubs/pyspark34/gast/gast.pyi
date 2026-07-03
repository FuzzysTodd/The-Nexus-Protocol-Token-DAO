from .ast3 import ast_to_gast as ast_to_gast, gast_to_ast as gast_to_ast
from ast import AST

class TypeIgnore(AST): ...

def parse(*args, **kwargs): ...
def literal_eval(node_or_string): ...
def get_docstring(node, clean: bool = True): ...
def copy_location(new_node, old_node):
    """
    Copy source location (`lineno`, `col_offset`, `end_lineno`, and
    `end_col_offset` attributes) from *old_node* to *new_node* if possible,
    and return *new_node*.
    """
def fix_missing_locations(node):
    """
    When you compile a node tree with compile(), the compiler expects lineno
    and col_offset attributes for every node that supports them.  This is
    rather tedious to fill in for generated nodes, so this helper adds these
    attributes recursively where not already set, by setting them to the values
    of the parent node.  It works recursively starting at *node*.
    """
def increment_lineno(node, n: int = 1):
    '''
    Increment the line number and end line number of each node in the tree
    starting at *node* by *n*. This is useful to "move code" to a different
    location in a file.
    '''
