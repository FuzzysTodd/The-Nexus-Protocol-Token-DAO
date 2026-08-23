from pasta.augment import import_utils as import_utils
from pasta.base import ast_utils as ast_utils, scope as scope

def rename_external(t, old_name, new_name):
    """Rename an imported name in a module.

  This will rewrite all import statements in `tree` that reference the old
  module as well as any names in `tree` which reference the imported name. This
  may introduce new import statements, but only if necessary.

  For example, to move and rename the module `foo.bar.utils` to `foo.bar_utils`:
  > rename_external(tree, 'foo.bar.utils', 'foo.bar_utils')

  - import foo.bar.utils
  + import foo.bar_utils

  - from foo.bar import utils
  + from foo import bar_utils

  - from foo.bar import logic, utils
  + from foo.bar import logic
  + from foo import bar_utils

  Arguments:
    t: (ast.Module) Module syntax tree to perform the rename in. This will be
      updated as a result of this function call with all affected nodes changed
      and potentially new Import/ImportFrom nodes added.
    old_name: (string) Fully-qualified path of the name to replace.
    new_name: (string) Fully-qualified path of the name to update to.

  Returns:
    True if any changes were made, False otherwise.
  """
