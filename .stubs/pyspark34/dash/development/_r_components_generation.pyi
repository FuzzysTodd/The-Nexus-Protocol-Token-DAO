from ._all_keywords import r_keywords as r_keywords
from ._py_components_generation import reorder_props as reorder_props
from _typeshed import Incomplete

r_component_string: str
frame_open_template: str
frame_element_template: str
frame_body_template: str
frame_close_template: str
help_string: str
description_template: str
rbuild_ignore_string: str
pkghelp_stub: str
wildcard_helper: str
wildcard_template: str
wildcard_help_template: str

def generate_class_string(name, props, project_shortname, prefix): ...
def generate_js_metadata(pkg_data, project_shortname):
    """Dynamically generate R function to supply JavaScript and CSS dependency
    information required by the dash package for R.

    Parameters
    ----------
    project_shortname = component library name, in snake case

    Returns
    -------
    function_string = complete R function code to provide component features
    """
def get_async_type(dep): ...
def wrap(tag, code): ...
def write_help_file(name, props, description, prefix, rpkg_data) -> None:
    """Write R documentation file (.Rd) given component name and properties.

    Parameters
    ----------
    name = the name of the Dash component for which a help file is generated
    props = the properties of the component
    description = the component's description, inserted into help file header
    prefix = the DashR library prefix (optional, can be a blank string)
    rpkg_data = package metadata (optional)

    Returns
    -------
    writes an R help file to the man directory for the generated R package
    """
def write_class_file(name, props, description, project_shortname, prefix: Incomplete | None = None, rpkg_data: Incomplete | None = None) -> None: ...
def write_js_metadata(pkg_data, project_shortname, has_wildcards) -> None:
    """Write an internal (not exported) R function to return all JS
    dependencies as required by dash.

    Parameters
    ----------
    project_shortname = hyphenated string, e.g. dash-html-components

    Returns
    -------
    """
def generate_rpkg(pkg_data, rpkg_data, project_shortname, export_string, package_depends, package_imports, package_suggests, has_wildcards) -> None:
    """Generate documents for R package creation.

    Parameters
    ----------
    pkg_data
    rpkg_data
    project_shortname
    export_string
    package_depends
    package_imports
    package_suggests
    has_wildcards

    Returns
    -------
    """
def snake_case_to_camel_case(namestring): ...
def format_fn_name(prefix, name): ...
def generate_exports(project_shortname, components, metadata, pkg_data, rpkg_data, prefix, package_depends, package_imports, package_suggests, **kwargs) -> None: ...
def make_namespace_exports(components, prefix): ...
def get_r_prop_types(type_object):
    """Mapping from the PropTypes js type object to the R type."""
def get_r_type(type_object, is_flow_type: bool = False, indent_num: int = 0):
    """
    Convert JS types to R types for the component definition
    Parameters
    ----------
    type_object: dict
        react-docgen-generated prop type dictionary
    is_flow_type: bool
    indent_num: int
        Number of indents to use for the docstring for the prop
    Returns
    -------
    str
        Python type string
    """
def print_r_type(typedata): ...
def create_prop_docstring_r(prop_name, type_object, required, description, indent_num, is_flow_type: bool = False):
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
def get_wildcards_r(prop_keys): ...
