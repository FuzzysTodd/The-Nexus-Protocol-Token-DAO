from ._py_components_generation import generate_class as generate_class, generate_class_file as generate_class_file, generate_classes_files as generate_classes_files, generate_imports as generate_imports
from .base_component import ComponentRegistry as ComponentRegistry

def load_components(metadata_path, namespace: str = 'default_namespace'):
    """Load React component metadata into a format Dash can parse.

    Usage: load_components('../../component-suites/lib/metadata.json')

    Keyword arguments:
    metadata_path -- a path to a JSON file created by
    [`react-docgen`](https://github.com/reactjs/react-docgen).

    Returns:
    components -- a list of component objects with keys
    `type`, `valid_kwargs`, and `setup`.
    """
def generate_classes(namespace, metadata_path: str = 'lib/metadata.json') -> None:
    """Load React component metadata into a format Dash can parse, then create
    Python class files.

    Usage: generate_classes()

    Keyword arguments:
    namespace -- name of the generated Python package (also output dir)

    metadata_path -- a path to a JSON file created by
    [`react-docgen`](https://github.com/reactjs/react-docgen).

    Returns:
    """
