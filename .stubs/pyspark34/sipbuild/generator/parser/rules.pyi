from ..scoped_name import ScopedName as ScopedName
from ..specification import AccessSpecifier as AccessSpecifier, Argument as Argument, ArgumentType as ArgumentType, ArrayArgument as ArrayArgument, ClassKey as ClassKey, Docstring as Docstring, DocstringFormat as DocstringFormat, Extract as Extract, FunctionCall as FunctionCall, IfaceFile as IfaceFile, IfaceFileType as IfaceFileType, KwArgs as KwArgs, License as License, MappedType as MappedType, MappedTypeTemplate as MappedTypeTemplate, Overload as Overload, Property as Property, PyQtMethodSpecifier as PyQtMethodSpecifier, QualifierType as QualifierType, Signature as Signature, Template as Template, ThrowArguments as ThrowArguments, Value as Value, ValueType as ValueType, VirtualErrorHandler as VirtualErrorHandler, WrappedTypedef as WrappedTypedef, WrappedVariable as WrappedVariable
from ..templates import same_template_signature as same_template_signature
from ..utils import cached_name as cached_name, normalised_scoped_name as normalised_scoped_name, search_typedefs as search_typedefs
from .annotations import DottedName as DottedName
from .tokens import tokens as tokens
from _typeshed import Incomplete

parser: Incomplete
start: str

def p_error(t) -> None:
    """ Invoked when a syntax error occurs. """
def p_specification(p) -> None:
    """specification : statement
        | specification statement"""
def p_statement(p) -> None:
    """statement : eof
        | namespace_statement
        | composite_module
        | copying
        | defdocstringfmt
        | defdocstringsig
        | defencoding
        | defmetatype
        | defsupertype
        | exported_header_code
        | exported_type_hint_code
        | extract
        | feature
        | hidden_ns
        | import
        | include
        | init_code
        | license
        | mapped_type
        | mapped_type_template
        | module
        | module_code
        | module_header_code
        | platforms
        | plugin
        | preinit_code
        | postinit_code
        | timeline
        | type_hint_code
        | unit_code
        | unit_postinclude_code
        | virtual_error_handler"""
def p_namespace_statement(p) -> None:
    """namespace_statement : if_start
        | if_end
        | class_decl
        | class_template
        | enum_decl
        | exception
        | function
        | namespace_decl
        | struct_decl
        | typedef_decl
        | union_decl
        | variable
        | type_header_code"""
def p_eof(p) -> None:
    """eof : EOF"""
def p_begin_args(p) -> None:
    """begin_args :"""
def p_end_args(p) -> None:
    """end_args :"""
def p_need_eol(p) -> None:
    """need_eol :"""
def p_autopyname(p) -> None:
    """autopyname : AutoPyName begin_args '(' remove_leading '=' STRING end_args ')'"""
def p_get_buffer_code(p) -> None:
    """get_buffer_code : BIGetBufferCode CODE_BLOCK"""
def p_release_buffer_code(p) -> None:
    """release_buffer_code : BIReleaseBufferCode CODE_BLOCK"""
def p_composite_module(p) -> None:
    """composite_module : CompositeModule dotted_name c_module_body
        | CompositeModule begin_args '(' c_module_args end_args ')' c_module_body"""
def p_c_module_args(p) -> None:
    """c_module_args : c_module_arg
        | c_module_args ',' c_module_arg"""
def p_c_module_arg(p) -> None:
    """c_module_arg : name '=' dotted_name"""
def p_c_module_body(p) -> None:
    """c_module_body : '{' c_module_body_directives '}' ';'
        | empty"""
def p_c_module_body_directives(p) -> None:
    """c_module_body_directives : c_module_body_directive
        | c_module_body_directives c_module_body_directive"""
def p_c_module_body_directive(p) -> None:
    """c_module_body_directive : if_start
        | if_end
        | docstring"""
def p_convert_from_type_code(p) -> None:
    """convert_from_type_code : ConvertFromTypeCode CODE_BLOCK"""
def p_convert_to_subclass_code(p) -> None:
    """convert_to_subclass_code : ConvertToSubClassCode CODE_BLOCK"""
def p_convert_to_type_code(p) -> None:
    """convert_to_type_code : ConvertToTypeCode CODE_BLOCK"""
def p_copying(p) -> None:
    """copying : Copying CODE_BLOCK"""
def p_defdocstringfmt(p) -> None:
    """defdocstringfmt : DefaultDocstringFormat STRING
        | DefaultDocstringFormat begin_args '(' name '=' STRING end_args ')'"""
def p_defdocstringsig(p) -> None:
    """defdocstringsig : DefaultDocstringSignature STRING
        | DefaultDocstringSignature begin_args '(' name '=' STRING end_args ')'"""
def p_defencoding(p) -> None:
    """defencoding : DefaultEncoding STRING
        |  DefaultEncoding begin_args '(' name '=' STRING end_args ')'"""
def p_defmetatype(p) -> None:
    """defmetatype : DefaultMetatype dotted_name
        | DefaultMetatype begin_args '(' name '=' dotted_name end_args ')'"""
def p_defsupertype(p) -> None:
    """defsupertype : DefaultSupertype dotted_name
        | DefaultSupertype begin_args '(' name '=' dotted_name end_args ')'"""
def p_docstring(p) -> None:
    """docstring : Docstring docstring_args CODE_BLOCK"""
def p_docstring_args(p) -> None:
    """docstring_args : empty
    | STRING
    | begin_args '(' docstring_arg_list end_args ')'"""
def p_docstring_arg_list(p) -> None:
    """docstring_arg_list : docstring_arg
        | docstring_arg_list ',' docstring_arg"""
def p_docstring_arg(p) -> None:
    """docstring_arg : format '=' STRING
    | signature '=' STRING"""
def p_exported_header_code(p) -> None:
    """exported_header_code : ExportedHeaderCode CODE_BLOCK"""
def p_exported_type_hint_code(p) -> None:
    """exported_type_hint_code : ExportedTypeHintCode CODE_BLOCK"""
def p_extract(p) -> None:
    """extract : Extract NAME CODE_BLOCK
        | Extract begin_args '(' extract_args end_args ')' CODE_BLOCK"""
def p_extract_args(p) -> None:
    """extract_args : extract_arg
        | extract_args ',' extract_arg"""
def p_extract_arg(p) -> None:
    """extract_arg : id '=' NAME
        | order '=' NUMBER"""
def p_feature(p) -> None:
    """feature : Feature NAME
        | Feature begin_args '(' name '=' NAME end_args ')'"""
def p_finalisation_code(p) -> None:
    """finalisation_code : FinalisationCode CODE_BLOCK"""
def p_gc_clear_code(p) -> None:
    """gc_clear_code : GCClearCode CODE_BLOCK"""
def p_gc_traverse_code(p) -> None:
    """gc_traverse_code : GCTraverseCode CODE_BLOCK"""
def p_hidden_ns(p) -> None:
    """hidden_ns : HideNamespace scoped_name
        | HideNamespace begin_args '(' hidden_ns_args end_args ')'"""
def p_hidden_ns_args(p) -> None:
    """hidden_ns_args : hidden_ns_arg
        | hidden_ns_args ',' hidden_ns_arg"""
def p_hidden_ns_arg(p) -> None:
    """hidden_ns_arg : name '=' scoped_name"""
def p_if_start(p) -> None:
    """if_start : If '(' qualifiers ')'"""
def p_if_end(p) -> None:
    """if_end : End"""
def p_import(p) -> None:
    """import : Import need_eol import_simple EOL
        | Import begin_args '(' import_compound end_args ')'"""
def p_import_simple(p) -> None:
    """import_simple : file_path"""
def p_import_compound(p) -> None:
    """import_compound : import_args"""
def p_import_args(p) -> None:
    """import_args : import_arg
        | import_args ',' import_arg"""
def p_import_arg(p) -> None:
    """import_arg : name '=' file_path"""
def p_include(p) -> None:
    """include : Include need_eol include_simple EOL
        | Include begin_args '(' include_compound end_args ')'"""
def p_include_simple(p) -> None:
    """include_simple : file_path"""
def p_include_compund(p) -> None:
    """include_compound : include_args"""
def p_include_args(p) -> None:
    """include_args : include_arg
        | include_args ',' include_arg"""
def p_include_arg(p) -> None:
    """include_arg : name '=' file_path
        | optional '=' bool_value"""
def p_init_code(p) -> None:
    """init_code : InitialisationCode CODE_BLOCK"""
def p_instance_code(p) -> None:
    """instance_code : InstanceCode CODE_BLOCK"""
def p_license(p) -> None:
    """license : License STRING
        | License begin_args '(' license_args end_args ')'"""
def p_license_args(p) -> None:
    """license_args : license_arg
        | license_args ',' license_arg"""
def p_license_arg(p) -> None:
    """license_arg : licensee '=' STRING
        | signature '=' STRING
        | timestamp '=' STRING
        | type '=' STRING"""
def p_mapped_type(p) -> None:
    """mapped_type : mapped_type_head '{' mapped_type_body '}' ';'"""
def p_mapped_type_template(p) -> None:
    """mapped_type_template : mapped_type_template_head '{' mapped_type_body '}' ';'"""
def p_mapped_type_head(p) -> None:
    """mapped_type_head : MappedType base_type opt_annos"""
def p_mapped_type_template_head(p) -> None:
    """mapped_type_template_head : template_decl MappedType base_type opt_annos"""
def p_mapped_type_body(p) -> None:
    """mapped_type_body : mapped_type_line
        | mapped_type_body mapped_type_line"""
def p_mapped_type_line(p) -> None:
    """mapped_type_line : if_start
        | if_end
        | convert_from_type_code
        | convert_to_type_code
        | enum_decl
        | instance_code
        | mapped_type_function
        | release_code
        | type_code
        | type_header_code"""
def p_mapped_type_function(p) -> None:
    """mapped_type_function : static cpp_type NAME '(' opt_arg_list ')' opt_const opt_exceptions opt_annos opt_signature ';' opt_docstring premethod_code method_code"""
def p_module_header_code(p) -> None:
    """module_header_code : ModuleHeaderCode CODE_BLOCK"""
def p_module(p) -> None:
    """module : Module dotted_name module_body
        | Module begin_args '(' module_args end_args ')' module_body"""
def p_module_args(p) -> None:
    """module_args : module_arg
        | module_args ',' module_arg"""
def p_module_arg(p) -> None:
    """module_arg : all_raise_py_exception '=' bool_value
        | call_super_init '=' bool_value
        | default_VirtualErrorHandler '=' NAME
        | keyword_arguments '=' STRING
        | language '=' STRING
        | name '=' dotted_name
        | py_ssize_t_clean '=' bool_value
        | use_argument_names '=' bool_value
        | use_limited_api '=' bool_value"""
def p_module_body(p) -> None:
    """module_body : '{' module_body_directives '}' ';'
        | empty"""
def p_module_body_directives(p) -> None:
    """module_body_directives : module_body_directive
        | module_body_directives module_body_directive"""
def p_module_body_directive(p) -> None:
    """module_body_directive : if_start
        | if_end
        | autopyname
        | docstring"""
def p_module_code(p) -> None:
    """module_code : ModuleCode CODE_BLOCK"""
def p_pickle_code(p) -> None:
    """pickle_code : PickleCode CODE_BLOCK"""
def p_platforms(p) -> None:
    """platforms : Platforms '{' qualifier_list '}'"""
def p_plugin(p) -> None:
    """plugin : Plugin NAME"""
def p_postinit_code(p) -> None:
    """postinit_code : PostInitialisationCode CODE_BLOCK"""
def p_preinit_code(p) -> None:
    """preinit_code : PreInitialisationCode CODE_BLOCK"""
def p_property(p) -> None:
    """property : Property begin_args '(' property_args end_args ')' opt_property_body"""
def p_property_args(p) -> None:
    """property_args : property_arg
        | property_args ',' property_arg"""
def p_property_arg(p) -> None:
    """property_arg : get '=' NAME
        | name '=' NAME
        | set '=' NAME"""
def p_opt_property_body(p) -> None:
    """opt_property_body : empty
        | '{' property_body '}' ';'"""
def p_property_body(p) -> None:
    """property_body : property_line
        | property_body property_line"""
def p_property_line(p) -> None:
    """property_line : if_start
        | if_end
        | docstring"""
def p_release_code(p) -> None:
    """release_code : ReleaseCode CODE_BLOCK"""
def p_timeline(p) -> None:
    """timeline : Timeline '{' qualifier_list '}'"""
def p_type_code(p) -> None:
    """type_code : TypeCode CODE_BLOCK"""
def p_type_header_code(p) -> None:
    """type_header_code : TypeHeaderCode CODE_BLOCK"""
def p_type_hint_code(p) -> None:
    """type_hint_code : TypeHintCode CODE_BLOCK"""
def p_unit_code(p) -> None:
    """unit_code : UnitCode CODE_BLOCK"""
def p_unit_postinclude_code(p) -> None:
    """unit_postinclude_code : UnitPostIncludeCode CODE_BLOCK"""
def p_virtual_error_handler(p) -> None:
    """virtual_error_handler : VirtualErrorHandler NAME CODE_BLOCK
        | VirtualErrorHandler begin_args '(' veh_args end_args ')' CODE_BLOCK"""
def p_veh_args(p) -> None:
    """veh_args : veh_arg
        | veh_args ',' veh_arg"""
def p_veh_arg(p) -> None:
    """veh_arg : name '=' NAME"""
def p_cpp_type(p) -> None:
    """cpp_type : const base_type derefs opt_ref
        | base_type derefs opt_ref"""
def p_base_type(p) -> None:
    """base_type : pod_type
        | scoped_name
        | scoped_name '<' cpp_types '>'
        | struct scoped_name
        | union scoped_name"""
def p_pod_type(p) -> None:
    """pod_type : unsigned long long
        | signed char
        | long long
        | unsigned char
        | unsigned short
        | unsigned int
        | unsigned long
        | unsigned
        | short
        | int
        | long
        | float
        | double
        | bool
        | char
        | wchar_t
        | void
        | SIP_PYOBJECT
        | SIP_PYTUPLE
        | SIP_PYLIST
        | SIP_PYDICT
        | SIP_PYCALLABLE
        | SIP_PYSLICE
        | SIP_PYTYPE
        | SIP_PYBUFFER
        | SIP_PYENUM
        | SIP_SSIZE_T
        | Py_hash_t
        | Py_ssize_t
        | size_t
        | ELLIPSIS"""
def p_cpp_types(p) -> None:
    """cpp_types : cpp_type
        | cpp_types ',' cpp_type"""
def p_derefs(p) -> None:
    """derefs : empty
        | derefs '*'
        | derefs '*' const"""
def p_opt_ref(p) -> None:
    """opt_ref : '&'
        | empty"""
def p_class_template(p) -> None:
    """class_template : template_decl class_decl"""
def p_class_docstring(p) -> None:
    """class_docstring : docstring"""
def p_class_decl(p) -> None:
    """class_decl : class class_head opt_class_definition ';'"""
def p_class_head(p) -> None:
    """class_head : scoped_name superclasses opt_annos"""
def p_struct_decl(p) -> None:
    """struct_decl : struct struct_head opt_class_definition ';'"""
def p_struct_head(p) -> None:
    """struct_head : scoped_name superclasses opt_annos"""
def p_superclasses(p) -> None:
    """superclasses : ':' superclass_list
        | empty"""
def p_superclass_list(p) -> None:
    """superclass_list : superclass
        | superclass_list ',' superclass"""
def p_superclass(p) -> None:
    """superclass : class_access scoped_name"""
def p_class_access(p) -> None:
    """class_access : empty
        | public
        | protected
        | private"""
def p_opt_class_definition(p) -> None:
    """opt_class_definition : '{' opt_class_body '}'
        | empty"""
def p_opt_class_body(p) -> None:
    """opt_class_body : class_body
        | empty"""
def p_class_body(p) -> None:
    """class_body : class_line
        | class_body class_line"""
def p_class_line(p) -> None:
    """class_line : if_start
        | if_end
        | class_decl
        | class_docstring
        | class_template
        | ctor
        | dtor
        | enum_decl
        | exception
        | typedef_decl
        | method_variable
        | namespace_decl
        | struct_decl
        | union_decl
        | public_specifier
        | protected_specifier
        | private_specifier
        | signals_specifier
        | convert_from_type_code
        | convert_to_subclass_code
        | convert_to_type_code
        | finalisation_code
        | gc_clear_code
        | gc_traverse_code
        | get_buffer_code
        | instance_code
        | pickle_code
        | property
        | release_buffer_code
        | type_code
        | type_header_code
        | type_hint_code
        | BIGetReadBufferCode CODE_BLOCK
        | BIGetWriteBufferCode CODE_BLOCK
        | BIGetSegCountCode CODE_BLOCK
        | BIGetCharBufferCode CODE_BLOCK"""
def p_ctor(p) -> None:
    """ctor : explicit ctor_decl
        | ctor_decl"""
def p_ctor_decl(p) -> None:
    """ctor_decl : NAME '(' opt_arg_list ')' opt_exceptions opt_annos opt_ctor_signature ';' opt_docstring premethod_code method_code"""
def p_opt_ctor_signature(p) -> None:
    """opt_ctor_signature : '[' '(' opt_arg_list ')' ']'
        | empty"""
def p_dtor(p) -> None:
    """dtor : opt_virtual '~' NAME '(' ')' opt_exceptions opt_abstract opt_annos ';' premethod_code method_code virtual_catcher_code"""
def p_method_variable(p) -> None:
    """method_variable : Q_SIGNAL simple_method_variable
        | Q_SLOT simple_method_variable
        | simple_method_variable"""
def p_simple_method_variable(p) -> None:
    """simple_method_variable : virtual function
        | static plain_method_variable
        | plain_method_variable"""
def p_plain_method_variable(p) -> None:
    """plain_method_variable : function
        | variable"""
def p_public_specifier(p) -> None:
    """public_specifier : public opt_slots ':'"""
def p_protected_specifier(p) -> None:
    """protected_specifier : protected opt_slots ':'"""
def p_private_specifier(p) -> None:
    """private_specifier : private opt_slots ':'"""
def p_signals_specifier(p) -> None:
    """signals_specifier : signals ':'
        | Q_SIGNALS ':'"""
def p_opt_slots(p) -> None:
    """opt_slots : slots
        | Q_SLOTS
        | empty"""
def p_enum_decl(p) -> None:
    """enum_decl : enum opt_enum_key opt_name opt_annos '{' opt_enum_body '}' ';'"""
def p_opt_enum_key(p) -> None:
    """opt_enum_key : class
        | struct
        | union
        | empty"""
def p_opt_enum_body(p) -> None:
    """opt_enum_body : enum_body
        | empty"""
def p_enum_body(p) -> None:
    """enum_body : enum_line
        | enum_body enum_line"""
def p_enum_line(p) -> None:
    """enum_line : if_start
        | if_end
        | NAME opt_enum_assign opt_annos opt_comma"""
def p_opt_enum_assign(p) -> None:
    """opt_enum_assign : '=' value
        | empty"""
def p_opt_comma(p) -> None:
    """opt_comma : empty
        | ','"""
def p_exception(p) -> None:
    """exception : Exception scoped_name opt_base_exception opt_annos '{' exception_body '}' ';'"""
def p_opt_base_exception(p) -> None:
    """opt_base_exception : '(' scoped_name ')'
        | empty"""
def p_exception_body(p) -> None:
    """exception_body : exception_line
        | exception_body exception_line"""
def p_exception_line(p) -> None:
    """exception_line : if_start
        | if_end
        | RaiseCode CODE_BLOCK
        | TypeHeaderCode CODE_BLOCK"""
def p_function(p) -> None:
    """function : function_decl
        | assignment_operator_decl
        | operator_decl
        | operator_cast_decl"""
def p_function_decl(p) -> None:
    """function_decl : cpp_type NAME '(' opt_arg_list ')' opt_const opt_final opt_exceptions opt_abstract opt_annos opt_signature ';' opt_docstring premethod_code method_code virtual_catcher_code virtual_call_code"""
def p_assignment_operator_decl(p) -> None:
    """assignment_operator_decl : cpp_type operator '=' '(' cpp_type ')' ';'"""
def p_operator_decl(p) -> None:
    """operator_decl : cpp_type operator operator_name '(' opt_arg_list ')' opt_const opt_final opt_exceptions opt_abstract opt_annos opt_signature ';' premethod_code method_code virtual_catcher_code virtual_call_code"""
def p_operator_cast_decl(p) -> None:
    """operator_cast_decl : operator cpp_type '(' opt_arg_list ')' opt_const opt_final opt_exceptions opt_abstract opt_annos opt_signature ';' premethod_code method_code virtual_catcher_code virtual_call_code"""
def p_opt_arg_list(p) -> None:
    """opt_arg_list : arg_list
        | empty"""
def p_arg_list(p) -> None:
    """arg_list : arg_value
        | arg_list ',' arg_value"""
def p_arg_value(p) -> None:
    """arg_value : arg_type opt_assign"""
def p_arg_type(p) -> None:
    """arg_type : cpp_type opt_name opt_annos"""
def p_opt_assign(p) -> None:
    """opt_assign : '=' expr
        | empty"""
def p_expr(p) -> None:
    """expr : value
        | expr binop value"""
def p_value(p) -> None:
    """value : opt_cast opt_unop simple_value"""
def p_simple_value(p) -> None:
    """simple_value : empty_value
        | function_call_value
        | null_value
        | number_value
        | quoted_char_value
        | real_value
        | scoped_name_value
        | string_value"""
def p_empty_value(p) -> None:
    """empty_value : '{' '}'"""
def p_function_call_value(p) -> None:
    """function_call_value : base_type '(' opt_expr_list ')'"""
def p_null_value(p) -> None:
    """null_value : NULL"""
def p_number_value(p) -> None:
    """number_value : NUMBER
        | bool_value"""
def p_quoted_char_value(p) -> None:
    """quoted_char_value : QUOTED_CHAR"""
def p_real_value(p) -> None:
    """real_value : REAL"""
def p_scoped_name_value(p) -> None:
    """scoped_name_value : scoped_name"""
def p_string_value(p) -> None:
    """string_value : STRING"""
def p_opt_expr_list(p) -> None:
    """opt_expr_list : expr_list
        | empty"""
def p_expr_list(p) -> None:
    """expr_list : expr
        | expr_list ',' expr"""
def p_opt_cast(p) -> None:
    """opt_cast : '(' scoped_name ')'
        | empty"""
def p_binop(p) -> None:
    """binop : '-'
        | '+'
        | '*'
        | '/'
        | '&'
        | '|'"""
def p_opt_unop(p) -> None:
    """opt_unop : empty
        | '!'
        | '~'
        | '-'
        | '+'
        | '*'
        | '&'"""
def p_opt_exceptions(p) -> None:
    """opt_exceptions : empty
        | noexcept
        | throw '(' opt_exception_list ')'"""
def p_opt_exception_list(p) -> None:
    """opt_exception_list : exception_list
        | empty"""
def p_exception_list(p) -> None:
    """exception_list : scoped_name
        | exception_list ',' scoped_name"""
def p_opt_abstract(p) -> None:
    """opt_abstract : '=' NUMBER
        | empty"""
def p_opt_signature(p) -> None:
    """opt_signature : '[' cpp_type '(' opt_arg_list ')' ']'
        | empty"""
def p_operator_name(p) -> None:
    """operator_name : '+'
        | '-'
        | '*'
        | '/'
        | '%'
        | '&'
        | '|'
        | '^'
        | '<' '<'
        | '>' '>'
        | '+' '='
        | '-' '='
        | '*' '='
        | '/' '='
        | '%' '='
        | '&' '='
        | '|' '='
        | '^' '='
        | '<' '<' '='
        | '>' '>' '='
        | '~'
        | '(' ')'
        | '[' ']'
        | '<'
        | '<' '='
        | '=' '='
        | '!' '='
        | '>'
        | '>' '='"""
def p_method_code(p) -> None:
    """method_code : MethodCode CODE_BLOCK
        | empty"""
def p_premethod_code(p) -> None:
    """premethod_code : PreMethodCode CODE_BLOCK
        | empty"""
def p_virtual_call_code(p) -> None:
    """virtual_call_code : VirtualCallCode CODE_BLOCK
        | empty"""
def p_virtual_catcher_code(p) -> None:
    """virtual_catcher_code : VirtualCatcherCode CODE_BLOCK
        | empty"""
def p_namespace_decl(p) -> None:
    """namespace_decl : namespace namespace_head opt_namespace_body ';'"""
def p_namespace_head(p) -> None:
    """namespace_head : scoped_name opt_annos"""
def p_opt_namespace_body(p) -> None:
    """opt_namespace_body : '{' namespace_body '}'
        | empty"""
def p_namespace_body(p) -> None:
    """namespace_body : namespace_statement
        | namespace_body namespace_statement"""
def p_typedef_decl(p) -> None:
    """typedef_decl : typedef cpp_type NAME opt_annos ';' opt_docstring
        | typedef cpp_type '(' '*' NAME ')' '(' cpp_types ')' opt_annos ';' opt_docstring"""
def p_union_decl(p) -> None:
    """union_decl : union union_head opt_class_definition ';'"""
def p_union_head(p) -> None:
    """union_head : scoped_name opt_annos"""
def p_variable(p) -> None:
    """variable : cpp_type NAME opt_annos variable_body ';'"""
def p_variable_body(p) -> None:
    """variable_body : '{' variable_body_directives '}'
        | empty"""
def p_variable_body_directives(p) -> None:
    """variable_body_directives : variable_body_directive
        | variable_body_directives variable_body_directive"""
def p_variable_body_directive(p) -> None:
    """variable_body_directive : if_start
        | if_end
        | AccessCode CODE_BLOCK
        | GetCode CODE_BLOCK
        | SetCode CODE_BLOCK"""
def p_opt_annos(p) -> None:
    """opt_annos : '/' annotations '/'
        | empty"""
def p_annotations(p) -> None:
    """annotations : annotation
        | annotations ',' annotation"""
def p_annotation(p) -> None:
    """annotation : NAME
        | NAME '=' annotation_value"""
def p_annotation_value(p) -> None:
    """annotation_value : dotted_name
        | STRING
        | NUMBER"""

precedence: Incomplete

def p_scoped_name(p) -> None:
    """scoped_name : SCOPE relative_scoped_name
        | relative_scoped_name"""
def p_relative_scoped_name(p) -> None:
    """relative_scoped_name : NAME
        | relative_scoped_name SCOPE NAME"""
def p_template_decl(p) -> None:
    """template_decl : template '<' cpp_types '>'"""
def p_bool_value(p) -> None:
    """bool_value : true
        | True
        | false
        | False"""
def p_dotted_name(p) -> None:
    """dotted_name : NAME
        | DOTTED_NAME"""
def p_file_path(p) -> None:
    """file_path : NAME
        | DOTTED_NAME
        | FILE_PATH"""
def p_empty(p) -> None:
    """empty :"""
def p_opt_const(p) -> None:
    """opt_const : const
        | empty"""
def p_opt_docstring(p) -> None:
    """opt_docstring : docstring
        | empty"""
def p_opt_final(p) -> None:
    """opt_final : final
        | empty"""
def p_opt_name(p) -> None:
    """opt_name : NAME
        | empty"""
def p_opt_virtual(p) -> None:
    """opt_virtual : virtual
        | empty"""
def p_ored_qualifiers(p) -> None:
    """ored_qualifiers : NAME
        | '!' NAME
        | ored_qualifiers LOGICAL_OR NAME
        | ored_qualifiers LOGICAL_OR '!' NAME"""
def p_qualifier_list(p) -> None:
    """qualifier_list : NAME
        | qualifier_list NAME"""
def p_qualifiers(p) -> None:
    """qualifiers : ored_qualifiers
        | opt_name '-' opt_name"""
