from _typeshed import Incomplete
from pasta.augment import errors as errors
from pasta.base import ast_utils as ast_utils, scope as scope

def add_import(tree, name_to_import, asname: Incomplete | None = None, from_import: bool = True, merge_from_imports: bool = True):
    '''Adds an import to the module.
  
  This function will try to ensure not to create duplicate imports. If name_to_import is
  already imported, it will return the existing import. This is true even if asname is set
  (asname will be ignored, and the existing name will be returned).
  
  If the import would create a name that already exists in the scope given by tree, this
  function will "import as", and append "_x" to the asname where x is the smallest positive
  integer generating a unique name.

  Arguments:
    tree: (ast.Module) Module AST to modify.
    name_to_import: (string) The absolute name to import.
    asname: (string) The alias for the import ("import name_to_import as asname")
    from_import: (boolean) If True, import the name using an ImportFrom node.
    merge_from_imports: (boolean) If True, merge a newly inserted ImportFrom
      node into an existing ImportFrom node, if applicable.

  Returns:
    The name (as a string) that can be used to reference the imported name. This
      can be the fully-qualified name, the basename, or an alias name.
  '''
def split_import(sc, node, alias_to_remove):
    """Split an import node by moving the given imported alias into a new import.

  Arguments:
    sc: (scope.Scope) Scope computed on whole tree of the code being modified.
    node: (ast.Import|ast.ImportFrom) An import node to split.
    alias_to_remove: (ast.alias) The import alias node to remove. This must be a
      child of the given `node` argument.

  Raises:
    errors.InvalidAstError: if `node` is not appropriately contained in the tree
      represented by the scope `sc`.
  """
def get_unused_import_aliases(tree, sc: Incomplete | None = None):
    """Get the import aliases that aren't used.

  Arguments:
    tree: (ast.AST) An ast to find imports in.
    sc: A scope.Scope representing tree (generated from scratch if not
    provided).

  Returns:
    A list of ast.alias representing imported aliases that aren't referenced in
    the given tree.
  """
def remove_import_alias_node(sc, node) -> None:
    """Remove an alias and if applicable remove their entire import.

  Arguments:
    sc: (scope.Scope) Scope computed on whole tree of the code being modified.
    node: (ast.Import|ast.ImportFrom|ast.alias) The node to remove.
  """
def remove_duplicates(tree, sc: Incomplete | None = None):
    """Remove duplicate imports, where it is safe to do so.

  This does NOT remove imports that create new aliases

  Arguments:
    tree: (ast.AST) An ast to modify imports in.
    sc: A scope.Scope representing tree (generated from scratch if not
    provided).

  Returns:
    Whether any changes were made.
  """
