from ._all_keywords import julia_keywords as julia_keywords
from ._py_components_generation import reorder_props as reorder_props
from _typeshed import Incomplete

jl_dash_base_uuid: str
jl_dash_uuid: str
jl_component_string: str
jl_children_signatures: str
jl_children_definitions: str
jl_package_file_string: str
jl_projecttoml_string: str
jl_base_version: Incomplete
jl_component_include_string: str
jl_resource_tuple_string: str
core_packages: Incomplete

def jl_package_name(namestring): ...
def stringify_wildcards(wclist, no_symbol: bool = False): ...
def get_wildcards_jl(props): ...
def get_jl_prop_types(type_object):
    """Mapping from the PropTypes js type object to the Julia type."""
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
    '''
def get_jl_type(type_object):
    """
    Convert JS types to Julia types for the component definition
    Parameters
    ----------
    type_object: dict
        react-docgen-generated prop type dictionary
    Returns
    -------
    str
        Julia type string
    """
def print_jl_type(typedata): ...
def create_docstring_jl(component_name, props, description):
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
def create_prop_docstring_jl(prop_name, type_object, required, description, indent_num):
    """
    Create the Dash component prop docstring
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
def format_fn_name(prefix, name): ...
def generate_metadata_strings(resources, metatype): ...
def is_core_package(project_shortname): ...
def base_package_name(project_shortname): ...
def base_package_uid(project_shortname): ...
def generate_package_file(project_shortname, components, pkg_data, prefix) -> None: ...
def generate_toml_file(project_shortname, pkg_data) -> None: ...
def generate_class_string(name, props, description, project_shortname, prefix): ...
def generate_struct_file(name, props, description, project_shortname, prefix) -> None: ...
def generate_module(project_shortname, components, metadata, pkg_data, prefix, **kwargs) -> None: ...
