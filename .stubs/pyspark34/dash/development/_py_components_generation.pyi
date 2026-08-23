from ._all_keywords import python_keywords as python_keywords
from ._collect_nodes import collect_nodes as collect_nodes, filter_base_nodes as filter_base_nodes
from .base_component import Component as Component
from _typeshed import Incomplete
from dash.exceptions import NonExistentEventException as NonExistentEventException

def generate_class_string(typename, props, description, namespace, prop_reorder_exceptions: Incomplete | None = None, max_props: Incomplete | None = None):
    """Dynamically generate class strings to have nicely formatted docstrings,
    keyword arguments, and repr.
    Inspired by http://jameso.be/2013/08/06/namedtuple.html
    Parameters
    ----------
    typename
    props
    description
    namespace
    prop_reorder_exceptions
    Returns
    -------
    string
    """
def generate_class_file(typename, props, description, namespace, prop_reorder_exceptions: Incomplete | None = None, max_props: Incomplete | None = None) -> None:
    """Generate a Python class file (.py) given a class string.
    Parameters
    ----------
    typename
    props
    description
    namespace
    prop_reorder_exceptions
    Returns
    -------
    """
def generate_imports(project_shortname, components) -> None: ...
def generate_classes_files(project_shortname, metadata, *component_generators): ...
def generate_class(typename, props, description, namespace, prop_reorder_exceptions: Incomplete | None = None):
    """Generate a Python class object given a class string.
    Parameters
    ----------
    typename
    props
    description
    namespace
    Returns
    -------
    """
def required_props(props):
    """Pull names of required props from the props object.
    Parameters
    ----------
    props: dict
    Returns
    -------
    list
        List of prop names (str) that are required for the Component
    """
def create_docstring(component_name, props, description, prop_reorder_exceptions: Incomplete | None = None):
    """Create the Dash component docstring.
    Parameters
    ----------
    component_name: str
        Component name
    props: dict
        Dictionary with {propName: propMetadata} structure
    description: str
        Component description
    Returns
    -------
    str
        Dash component docstring
    """
def prohibit_events(props) -> None:
    """Events have been removed. Raise an error if we see dashEvents or
    fireEvents.
    Parameters
    ----------
    props: dict
        Dictionary with {propName: propMetadata} structure
    Raises
    -------
    ?
    """
def parse_wildcards(props):
    """Pull out the wildcard attributes from the Component props.
    Parameters
    ----------
    props: dict
        Dictionary with {propName: propMetadata} structure
    Returns
    -------
    list
        List of Dash valid wildcard prefixes
    """
def reorder_props(props):
    '''If "children" is in props, then move it to the front to respect dash
    convention, then \'id\', then the remaining props sorted by prop name
    Parameters
    ----------
    props: dict
        Dictionary with {propName: propMetadata} structure
    Returns
    -------
    dict
        Dictionary with {propName: propMetadata} structure
    '''
def filter_props(props):
    '''Filter props from the Component arguments to exclude:
        - Those without a "type" or a "flowType" field
        - Those with arg.type.name in {\'func\', \'symbol\', \'instanceOf\'}
    Parameters
    ----------
    props: dict
        Dictionary with {propName: propMetadata} structure
    Returns
    -------
    dict
        Filtered dictionary with {propName: propMetadata} structure
    Examples
    --------
    ```python
    prop_args = {
        \'prop1\': {
            \'type\': {\'name\': \'bool\'},
            \'required\': False,
            \'description\': \'A description\',
            \'flowType\': {},
            \'defaultValue\': {\'value\': \'false\', \'computed\': False},
        },
        \'prop2\': {\'description\': \'A prop without a type\'},
        \'prop3\': {
            \'type\': {\'name\': \'func\'},
            \'description\': \'A function prop\',
        },
    }
    # filtered_prop_args is now
    # {
    #    \'prop1\': {
    #        \'type\': {\'name\': \'bool\'},
    #        \'required\': False,
    #        \'description\': \'A description\',
    #        \'flowType\': {},
    #        \'defaultValue\': {\'value\': \'false\', \'computed\': False},
    #    },
    # }
    filtered_prop_args = filter_props(prop_args)
    ```
    '''
def fix_keywords(txt):
    """
    replaces javascript keywords true, false, null with Python keywords
    """
def create_prop_docstring(prop_name, type_object, required, description, default, indent_num, is_flow_type: bool = False):
    """Create the Dash component prop docstring.
    Parameters
    ----------
    prop_name: str
        Name of the Dash component prop
    type_object: dict
        react-docgen-generated prop type dictionary
    required: bool
        Component is required?
    description: str
        Dash component description
    default: dict
        Either None if a default value is not defined, or
        dict containing the key 'value' that defines a
        default value for the prop
    indent_num: int
        Number of indents to use for the context block
        (creates 2 spaces for every indent)
    is_flow_type: bool
        Does the prop use Flow types? Otherwise, uses PropTypes
    Returns
    -------
    str
        Dash component prop docstring
    """
def map_js_to_py_types_prop_types(type_object, indent_num):
    """Mapping from the PropTypes js type object to the Python type."""
def map_js_to_py_types_flow_types(type_object):
    """Mapping from the Flow js types to the Python type."""
def js_to_py_type(type_object, is_flow_type: bool = False, indent_num: int = 0):
    """Convert JS types to Python types for the component definition.
    Parameters
    ----------
    type_object: dict
        react-docgen-generated prop type dictionary
    is_flow_type: bool
        Does the prop use Flow types? Otherwise, uses PropTypes
    indent_num: int
        Number of indents to use for the docstring for the prop
    Returns
    -------
    str
        Python type string
    """
