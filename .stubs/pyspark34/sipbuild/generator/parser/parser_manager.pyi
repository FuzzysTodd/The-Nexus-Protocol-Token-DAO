from . import rules as rules, tokens as tokens
from ...bindings_configuration import get_bindings_configuration as get_bindings_configuration
from ...exceptions import UserException as UserException
from ..error_log import ErrorLog as ErrorLog
from ..instantiations import instantiate_class as instantiate_class
from ..python_slots import invalid_global_slot as invalid_global_slot, slot_name_detail_map as slot_name_detail_map
from ..scoped_name import ScopedName as ScopedName
from ..specification import AccessSpecifier as AccessSpecifier, Argument as Argument, ArgumentType as ArgumentType, ArrayArgument as ArrayArgument, CachedName as CachedName, ClassKey as ClassKey, CodeBlock as CodeBlock, Constructor as Constructor, DocstringFormat as DocstringFormat, DocstringSignature as DocstringSignature, EnumBaseType as EnumBaseType, GILAction as GILAction, IfaceFile as IfaceFile, IfaceFileType as IfaceFileType, KwArgs as KwArgs, MappedType as MappedType, Member as Member, Module as Module, Overload as Overload, PyQtMethodSpecifier as PyQtMethodSpecifier, PySlot as PySlot, Qualifier as Qualifier, QualifierType as QualifierType, Signature as Signature, SourceLocation as SourceLocation, Specification as Specification, Transfer as Transfer, TypeHints as TypeHints, WrappedClass as WrappedClass, WrappedEnum as WrappedEnum, WrappedEnumMember as WrappedEnumMember, WrappedException as WrappedException
from ..templates import encoded_template_name as encoded_template_name, same_template_signature as same_template_signature
from ..utils import argument_as_str as argument_as_str, cached_name as cached_name, find_iface_file as find_iface_file, normalised_scoped_name as normalised_scoped_name, same_base_type as same_base_type
from .annotations import InvalidAnnotation as InvalidAnnotation, validate_annotation_value as validate_annotation_value
from _typeshed import Incomplete

class ParserManager:
    """ This object manages the actual lexer and parser objects providing them
    with state and utility functions.
    """
    class_templates: Incomplete
    tags: Incomplete
    spec: Incomplete
    modules: Incomplete
    c_bindings: Incomplete
    code_block: Incomplete
    module_state: Incomplete
    paren_depth: int
    parsing_template: bool
    parsing_virtual: bool
    raw_sip_file: Incomplete
    skip_stack: Incomplete
    def __init__(self, hex_version, encoding, abi_version, tags, disabled_features, protected_is_public, include_dirs, sip_module, is_strict) -> None:
        """ Initialise the manager. """
    def complete_class(self, p, symbol, annotations, has_body):
        """ Complete the definition of the class that is the current scope, pop
        it and return it.
        """
    def define_class(self, p, symbol, class_key, scoped_name, annotations, superclasses: Incomplete | None = None) -> None:
        """ Create a new class and make it the current scope. """
    def disambiguate_token(self, value, keywords):
        """ Disambiguate a token by inspecting its value. """
    def find_class(self, p, symbol, iface_file_type, fq_cpp_name, tmpl_arg: bool = False):
        """ Return a WrappedClass object for a C++ name creating it if
        necessary.
        """
    def find_exception(self, p, symbol, fq_cpp_name, raise_code: Incomplete | None = None):
        """ Find an exception, optionally creating a new one. """
    def new_class(self, p, symbol, iface_file_type, fq_cpp_name, virtual_error_handler: Incomplete | None = None, type_hints: Incomplete | None = None):
        """ Create a new, unannotated class and add it to the current scope.
        """
    def add_ctor(self, p, symbol, arg_list, annotations, *, exceptions, cpp_signature, docstring, premethod_code, method_code) -> None:
        """ Create a Constructor and add it to the current scope. """
    def add_dtor(self, p, symbol, name, annotations, *, exceptions, abstract, premethod_code, method_code, virtual_catcher_code) -> None:
        """ Add a dtor to the current scope. """
    def add_enum(self, p, symbol, cpp_name, is_scoped, annotations, members) -> None:
        """ Create a new enum and add it to the current scope. """
    def add_function(self, p, symbol, cpp_name, result, arg_list, annotations, *, const: bool = False, final: bool = False, exceptions: Incomplete | None = None, abstract: bool = False, cpp_signature: Incomplete | None = None, docstring: Incomplete | None = None, premethod_code: Incomplete | None = None, method_code: Incomplete | None = None, virtual_catcher_code: Incomplete | None = None, virtual_call_code: Incomplete | None = None):
        """ Create and return an Overload and add it to the current scope. """
    def add_mapped_type(self, p, symbol, cpp_type, annotations) -> None:
        """ Create a new mapped type and add it to the current scope. """
    def add_qualifier(self, p, symbol, name, type, order: int = 0, timeline: int = 0) -> None:
        """ Create a Qualifier and add it to the current module. """
    def add_typedef(self, p, symbol, typedef) -> None:
        """ Add a typedef to the current scope. """
    def annotate_mapped_type(self, p, symbol, mapped_type, annotations) -> None:
        """ Apply annotations to a mapped type. """
    def apply_common_argument_annotations(self, p, symbol, arg, annotations) -> None:
        """ Apply the annotations common to callable arguments and return type.
        """
    def apply_type_annotations(self, p, symbol, type, annotations) -> None:
        """ Apply the annotations for an argument type. """
    def check_annotations(self, p, symbol, context, annotations) -> None:
        """ Check that all the annotations provided as a dict of name/values
        are valid in a given context.
        """
    def check_attributes(self, p, symbol, py_name, is_function: bool = False, ignore: Incomplete | None = None) -> None:
        """ Check that a Python name will not clash with another object in the
        same Python scope.
        """
    def cpp_only(self, p, symbol, feature) -> None:
        """ Check that a C++ feature isn't being used in a C module. """
    def convert_docstring_format(self, p, symbol):
        """ Convert a string to the corresponding DocstringFormat member. """
    def convert_docstring_signature(self, p, symbol):
        """ Convert a string to the corresponding DocstringSignature member.
        """
    def convert_encoding(self, p, symbol, value: Incomplete | None = None):
        """ Convert a string to the corresponding ArgumentType member. """
    def convert_kw_args(self, p, symbol, value: Incomplete | None = None):
        """ Convert a string to the corresponding KwArgs member. """
    def ensure_import(self) -> None:
        """ We allow %Modules that are part of a %CompositeModule to be either
        %Imported or %Included.  In the case of the latter we need to adjust
        things so that it appears like the former.
        """
    def evaluate_feature_or_platform(self, p, symbol, name: Incomplete | None = None, inverted: bool = False):
        """ Evaluate a feature or platform qualifier. """
    def evaluate_timeline(self, p, symbol_lower, symbol_upper):
        """ Evaluate a timeline qualifier. """
    def find_qualifier(self, p, symbol, name, required: bool = True):
        """ Return a Qualifier or None if one doesn't exist. """
    def get_py_name(self, cpp_name, annotations):
        """ Return a valid Python name given a C/C++ name. """
    def get_transfer(self, p, symbol, annotations):
        """ Return the a Transfer value from a dict of annotations. """
    def get_type_hints(self, p, symbol, annotations):
        """ Return a TypeHints object constructed from a dict of annotations or
        None if none were specified.
        """
    @property
    def in_main_module(self):
        """ Set if the current module is the main one, ie. the one for which
        code will be generated for.
        """
    def instantiate_class_template(self, p, symbol, fq_cpp_name, template, py_name, no_type_name, docstring):
        """ Try and instantiate a class template and return True if one was
        found.
        """
    def lexer_error(self, t, text) -> None:
        """ Record an error caused by a token. """
    def parse(self, sip_file):
        """ Parse a .sip file and return a 3-tuple of a Specification object, a
        list of Module objects and a list of the .sip files that specify the
        module to be generated.  A UserException is raised if there was an
        error.
        """
    def parser_error(self, p, symbol, text) -> None:
        """ Record an error caused by a symbol in a production. """
    def pop_file(self) -> None:
        """ Restore the current .sip file from the stack and make it current.
        An IndexError is raised if the stack is empty.
        """
    def pop_module_state(self) -> None:
        """ Restore the current module state. """
    def pop_scope(self) -> None:
        """ Pop the current scope. """
    def push_file(self, p, symbol, sip_file: Incomplete | None = None, new_module: bool = False, optional: bool = False) -> None:
        """ Push the current .sip file onto the stack and make the new one
        current.  The new .sip file may be part of a new module (ie. %Import
        rather than %Include).
        """
    def push_scope(self, scope, access_specifier: Incomplete | None = None) -> None:
        """ Push a new scope. """
    def set_lexer_state(self, state: str = 'INITIAL') -> None:
        """ Set the lexer state. """
    @property
    def scope(self):
        """ The current scope if any. """
    @property
    def scope_access_specifier(self):
        """ The current access specifier. """
    @scope_access_specifier.setter
    def scope_access_specifier(self, access_specifier) -> None:
        """ Set the current access specifier. """
    @property
    def scope_pyqt_method_specifier(self):
        """ The current method specifier. """
    @scope_pyqt_method_specifier.setter
    def scope_pyqt_method_specifier(self, pyqt_method_specifier) -> None:
        """ Set the current method specifier. """
    @property
    def skipping(self):
        """ True if symbols are currently being skipped. """
    def validate_annotation(self, p, symbol, value):
        """ Validate an annotation and its value and return a valid version of
        the value.
        """
    def validate_function(self, p, symbol, overload) -> None:
        """ Validate a completed function. """
    def validate_mapped_type(self, p, symbol, mapped_type) -> None:
        """ Validate a completed mapped type. """
    def validate_variable(self, p, symbol, variable) -> None:
        """ Validate a completed variable. """
    def find_iface_file(self, p, symbol, fq_cpp_name, iface_file_type, cpp_type: Incomplete | None = None):
        """ Return an interface file for a fully qualified C/C++ name and type
        creating it if necessary.
        """
    def get_source_location(self, p, symbol):
        """ Return a SourceLocation object for a symbol. """

class ModuleState:
    """ Encapsulate the parser-related state for a module. """
    module: Incomplete
    sip_file: Incomplete
    all_raise_py_exception: bool
    auto_py_name_rules: Incomplete
    call_super_init: Incomplete
    default_encoding: Incomplete
    kw_args: Incomplete
    nr_timelines: int
    def __init__(self, module, sip_file) -> None:
        """ Initialise the state. """

class ScopeState:
    """ Encapsulate the parser-related state for a scope. """
    scope: Incomplete
    access_specifier: Incomplete
    pyqt_method_specifier: Incomplete
    def __init__(self, scope, access_specifier) -> None:
        """ Initialise the state. """

class UnexpectedEOF(Exception):
    """ This is raised by p_error() when an unexpected EOF is seen. """
