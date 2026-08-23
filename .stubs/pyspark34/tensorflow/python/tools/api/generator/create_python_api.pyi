from _typeshed import Incomplete
from tensorflow.python.tools.api.generator import doc_srcs as doc_srcs
from tensorflow.python.util import tf_decorator as tf_decorator, tf_export as tf_export

API_ATTRS: Incomplete
API_ATTRS_V1: Incomplete

class SymbolExposedTwiceError(Exception):
    """Raised when different symbols are exported with the same name."""

def get_canonical_import(import_set):
    """Obtain one single import from a set of possible sources of a symbol.

  One symbol might come from multiple places as it is being imported and
  reexported. To simplify API changes, we always use the same import for the
  same module, and give preference based on higher priority and alphabetical
  ordering.

  Args:
    import_set: (set) Imports providing the same symbol. This is a set of tuples
      in the form (import, priority). We want to pick an import with highest
      priority.

  Returns:
    A module name to import
  """

class _ModuleInitCodeBuilder:
    """Builds a map from module name to imports included in that module."""
    def __init__(self, output_package, api_version, lazy_loading=..., use_relative_imports: bool = False) -> None: ...
    def add_import(self, symbol, source_module_name, source_name, dest_module_name, dest_name) -> None:
        """Adds this import to module_imports.

    Args:
      symbol: TensorFlow Python symbol.
      source_module_name: (string) Module to import from.
      source_name: (string) Name of the symbol to import.
      dest_module_name: (string) Module name to add import to.
      dest_name: (string) Import the symbol using this name.

    Raises:
      SymbolExposedTwiceError: Raised when an import with the same
        dest_name has already been added to dest_module_name.
    """
    def build(self):
        """Get a map from destination module to __init__.py code for that module.

    Returns:
      A dictionary where
        key: (string) destination module (for e.g. tf or tf.consts).
        value: (string) text that should be in __init__.py files for
          corresponding modules.
    """
    def format_import(self, source_module_name, source_name, dest_name):
        """Formats import statement.

    Args:
      source_module_name: (string) Source module to import from.
      source_name: (string) Source symbol name to import.
      dest_name: (string) Destination alias name.

    Returns:
      An import statement string.
    """
    def get_destination_modules(self): ...
    def copy_imports(self, from_dest_module, to_dest_module) -> None: ...

def add_nested_compat_imports(module_builder, compat_api_versions, output_package) -> None:
    """Adds compat.vN.compat.vK modules to module builder.

  To avoid circular imports, we want to add __init__.py files under
  compat.vN.compat.vK and under compat.vN.compat.vK.compat. For all other
  imports, we point to corresponding modules under compat.vK.

  Args:
    module_builder: `_ModuleInitCodeBuilder` instance.
    compat_api_versions: Supported compatibility versions.
    output_package: Base output python package where generated API will be
      added.
  """
def add_imports_for_symbol(module_code_builder, symbol, source_module_name, source_name, api_name, api_version, output_module_prefix: str = '') -> None:
    """Add imports for the given symbol to `module_code_builder`.

  Args:
    module_code_builder: `_ModuleInitCodeBuilder` instance.
    symbol: A symbol.
    source_module_name: Module that we can import the symbol from.
    source_name: Name we can import the symbol with.
    api_name: API name. Currently, must be either `tensorflow` or `estimator`.
    api_version: API version.
    output_module_prefix: Prefix to prepend to destination module.
  """
def get_api_init_text(packages, packages_to_ignore, output_package, api_name, api_version, compat_api_versions: Incomplete | None = None, lazy_loading=..., use_relative_imports: bool = False):
    """Get a map from destination module to __init__.py code for that module.

  Args:
    packages: Base python packages containing python with target tf_export
      decorators.
    packages_to_ignore: python packages to be ignored when checking for
      tf_export decorators.
    output_package: Base output python package where generated API will be
      added.
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).
    api_version: API version you want to generate (1 or 2).
    compat_api_versions: Additional API versions to generate under compat/
      directory.
    lazy_loading: Boolean flag. If True, a lazy loading `__init__.py` file is
      produced and if `False`, static imports are used.
    use_relative_imports: True if we should use relative imports when importing
      submodules.

  Returns:
    A dictionary where
      key: (string) destination module (for e.g. tf or tf.consts).
      value: (string) text that should be in __init__.py files for
        corresponding modules.
  """
def get_module(dir_path, relative_to_dir):
    """Get module that corresponds to path relative to relative_to_dir.

  Args:
    dir_path: Path to directory.
    relative_to_dir: Get module relative to this directory.

  Returns:
    Name of module that corresponds to the given directory.
  """
def get_module_docstring(module_name, package, api_name):
    """Get docstring for the given module.

  This method looks for docstring in the following order:
  1. Checks if module has a docstring specified in doc_srcs.
  2. Checks if module has a docstring source module specified
     in doc_srcs. If it does, gets docstring from that module.
  3. Checks if module with module_name exists under base package.
     If it does, gets docstring from that module.
  4. Returns a default docstring.

  Args:
    module_name: module name relative to tensorflow (excluding 'tensorflow.'
      prefix) to get a docstring for.
    package: Base python package containing python with target tf_export
      decorators.
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).

  Returns:
    One-line docstring to describe the module.
  """
def create_primary_api_files(output_files, packages, packages_to_ignore, root_init_template, output_dir, output_package, api_name, api_version, compat_api_versions, compat_init_templates, lazy_loading=..., use_relative_imports: bool = False) -> None:
    '''Creates __init__.py files for the Python API.

  Args:
    output_files: List of __init__.py file paths to create.
    packages: Base python packages containing python with target tf_export
      decorators.
    packages_to_ignore: python packages to be ignored when checking for
      tf_export decorators.
    root_init_template: Template for top-level __init__.py file. "# API IMPORTS
      PLACEHOLDER" comment in the template file will be replaced with imports.
    output_dir: output API root directory.
    output_package: Base output package where generated API will be added.
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).
    api_version: API version to generate (`v1` or `v2`).
    compat_api_versions: Additional API versions to generate in compat/
      subdirectory.
    compat_init_templates: List of templates for top level compat init files in
      the same order as compat_api_versions.
    lazy_loading: Boolean flag. If True, a lazy loading `__init__.py` file is
      produced and if `False`, static imports are used.
    use_relative_imports: True if we should use relative imports when import
      submodules.

  Raises:
    ValueError: if output_files list is missing a required file.
  '''
def create_proxy_api_files(output_files, proxy_module_root, output_dir) -> None:
    """Creates __init__.py files in proxy format for the Python API.

  Args:
    output_files: List of __init__.py file paths to create.
    proxy_module_root: Module root for proxy-import format. If specified, proxy
      files with content like `from proxy_module_root.proxy_module import *`
      will be created to enable import resolution under TensorFlow.
    output_dir: output API root directory.
  """
def main() -> None: ...
