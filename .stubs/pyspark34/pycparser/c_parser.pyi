from . import c_ast as c_ast
from .ast_transforms import fix_atomic_specifiers as fix_atomic_specifiers, fix_switch_cases as fix_switch_cases
from .c_lexer import CLexer as CLexer
from .ply import yacc as yacc
from .plyparser import PLYParser as PLYParser, ParseError as ParseError, parameterized as parameterized, template as template
from _typeshed import Incomplete

class CParser(PLYParser):
    clex: Incomplete
    tokens: Incomplete
    cparser: Incomplete
    def __init__(self, lex_optimize: bool = True, lexer=..., lextab: str = 'pycparser.lextab', yacc_optimize: bool = True, yacctab: str = 'pycparser.yacctab', yacc_debug: bool = False, taboutputdir: str = '') -> None:
        """ Create a new CParser.

            Some arguments for controlling the debug/optimization
            level of the parser are provided. The defaults are
            tuned for release/performance mode.
            The simple rules for using them are:
            *) When tweaking CParser/CLexer, set these to False
            *) When releasing a stable parser, set to True

            lex_optimize:
                Set to False when you're modifying the lexer.
                Otherwise, changes in the lexer won't be used, if
                some lextab.py file exists.
                When releasing with a stable lexer, set to True
                to save the re-generation of the lexer table on
                each run.

            lexer:
                Set this parameter to define the lexer to use if
                you're not using the default CLexer.

            lextab:
                Points to the lex table that's used for optimized
                mode. Only if you're modifying the lexer and want
                some tests to avoid re-generating the table, make
                this point to a local lex table file (that's been
                earlier generated with lex_optimize=True)

            yacc_optimize:
                Set to False when you're modifying the parser.
                Otherwise, changes in the parser won't be used, if
                some parsetab.py file exists.
                When releasing with a stable parser, set to True
                to save the re-generation of the parser table on
                each run.

            yacctab:
                Points to the yacc table that's used for optimized
                mode. Only if you're modifying the parser, make
                this point to a local yacc table file

            yacc_debug:
                Generate a parser.out file that explains how yacc
                built the parsing table from the grammar.

            taboutputdir:
                Set this parameter to control the location of generated
                lextab and yacctab files.
        """
    def parse(self, text, filename: str = '', debug: bool = False):
        """ Parses C code and returns an AST.

            text:
                A string containing the C source code

            filename:
                Name of the file being parsed (for meaningful
                error messages)

            debug:
                Debug flag to YACC
        """
    precedence: Incomplete
    def p_translation_unit_or_empty(self, p) -> None:
        """ translation_unit_or_empty   : translation_unit
                                        | empty
        """
    def p_translation_unit_1(self, p) -> None:
        """ translation_unit    : external_declaration
        """
    def p_translation_unit_2(self, p) -> None:
        """ translation_unit    : translation_unit external_declaration
        """
    def p_external_declaration_1(self, p) -> None:
        """ external_declaration    : function_definition
        """
    def p_external_declaration_2(self, p) -> None:
        """ external_declaration    : declaration
        """
    def p_external_declaration_3(self, p) -> None:
        """ external_declaration    : pp_directive
                                    | pppragma_directive
        """
    def p_external_declaration_4(self, p) -> None:
        """ external_declaration    : SEMI
        """
    def p_external_declaration_5(self, p) -> None:
        """ external_declaration    : static_assert
        """
    def p_static_assert_declaration(self, p) -> None:
        """ static_assert           : _STATIC_ASSERT LPAREN constant_expression COMMA unified_string_literal RPAREN
                                    | _STATIC_ASSERT LPAREN constant_expression RPAREN
        """
    def p_pp_directive(self, p) -> None:
        """ pp_directive  : PPHASH
        """
    def p_pppragma_directive(self, p) -> None:
        """ pppragma_directive      : PPPRAGMA
                                    | PPPRAGMA PPPRAGMASTR
        """
    def p_function_definition_1(self, p) -> None:
        """ function_definition : id_declarator declaration_list_opt compound_statement
        """
    def p_function_definition_2(self, p) -> None:
        """ function_definition : declaration_specifiers id_declarator declaration_list_opt compound_statement
        """
    def p_statement(self, p) -> None:
        """ statement   : labeled_statement
                        | expression_statement
                        | compound_statement
                        | selection_statement
                        | iteration_statement
                        | jump_statement
                        | pppragma_directive
                        | static_assert
        """
    def p_pragmacomp_or_statement(self, p) -> None:
        """ pragmacomp_or_statement     : pppragma_directive statement
                                        | statement
        """
    def p_decl_body(self, p) -> None:
        """ decl_body : declaration_specifiers init_declarator_list_opt
                      | declaration_specifiers_no_type id_init_declarator_list_opt
        """
    def p_declaration(self, p) -> None:
        """ declaration : decl_body SEMI
        """
    def p_declaration_list(self, p) -> None:
        """ declaration_list    : declaration
                                | declaration_list declaration
        """
    def p_declaration_specifiers_no_type_1(self, p) -> None:
        """ declaration_specifiers_no_type  : type_qualifier declaration_specifiers_no_type_opt
        """
    def p_declaration_specifiers_no_type_2(self, p) -> None:
        """ declaration_specifiers_no_type  : storage_class_specifier declaration_specifiers_no_type_opt
        """
    def p_declaration_specifiers_no_type_3(self, p) -> None:
        """ declaration_specifiers_no_type  : function_specifier declaration_specifiers_no_type_opt
        """
    def p_declaration_specifiers_no_type_4(self, p) -> None:
        """ declaration_specifiers_no_type  : atomic_specifier declaration_specifiers_no_type_opt
        """
    def p_declaration_specifiers_no_type_5(self, p) -> None:
        """ declaration_specifiers_no_type  : alignment_specifier declaration_specifiers_no_type_opt
        """
    def p_declaration_specifiers_1(self, p) -> None:
        """ declaration_specifiers  : declaration_specifiers type_qualifier
        """
    def p_declaration_specifiers_2(self, p) -> None:
        """ declaration_specifiers  : declaration_specifiers storage_class_specifier
        """
    def p_declaration_specifiers_3(self, p) -> None:
        """ declaration_specifiers  : declaration_specifiers function_specifier
        """
    def p_declaration_specifiers_4(self, p) -> None:
        """ declaration_specifiers  : declaration_specifiers type_specifier_no_typeid
        """
    def p_declaration_specifiers_5(self, p) -> None:
        """ declaration_specifiers  : type_specifier
        """
    def p_declaration_specifiers_6(self, p) -> None:
        """ declaration_specifiers  : declaration_specifiers_no_type type_specifier
        """
    def p_declaration_specifiers_7(self, p) -> None:
        """ declaration_specifiers  : declaration_specifiers alignment_specifier
        """
    def p_storage_class_specifier(self, p) -> None:
        """ storage_class_specifier : AUTO
                                    | REGISTER
                                    | STATIC
                                    | EXTERN
                                    | TYPEDEF
                                    | _THREAD_LOCAL
        """
    def p_function_specifier(self, p) -> None:
        """ function_specifier  : INLINE
                                | _NORETURN
        """
    def p_type_specifier_no_typeid(self, p) -> None:
        """ type_specifier_no_typeid  : VOID
                                      | _BOOL
                                      | CHAR
                                      | SHORT
                                      | INT
                                      | LONG
                                      | FLOAT
                                      | DOUBLE
                                      | _COMPLEX
                                      | SIGNED
                                      | UNSIGNED
                                      | __INT128
        """
    def p_type_specifier(self, p) -> None:
        """ type_specifier  : typedef_name
                            | enum_specifier
                            | struct_or_union_specifier
                            | type_specifier_no_typeid
                            | atomic_specifier
        """
    def p_atomic_specifier(self, p) -> None:
        """ atomic_specifier  : _ATOMIC LPAREN type_name RPAREN
        """
    def p_type_qualifier(self, p) -> None:
        """ type_qualifier  : CONST
                            | RESTRICT
                            | VOLATILE
                            | _ATOMIC
        """
    def p_init_declarator_list(self, p) -> None:
        """ init_declarator_list    : init_declarator
                                    | init_declarator_list COMMA init_declarator
        """
    def p_init_declarator(self, p) -> None:
        """ init_declarator : declarator
                            | declarator EQUALS initializer
        """
    def p_id_init_declarator_list(self, p) -> None:
        """ id_init_declarator_list    : id_init_declarator
                                       | id_init_declarator_list COMMA init_declarator
        """
    def p_id_init_declarator(self, p) -> None:
        """ id_init_declarator : id_declarator
                               | id_declarator EQUALS initializer
        """
    def p_specifier_qualifier_list_1(self, p) -> None:
        """ specifier_qualifier_list    : specifier_qualifier_list type_specifier_no_typeid
        """
    def p_specifier_qualifier_list_2(self, p) -> None:
        """ specifier_qualifier_list    : specifier_qualifier_list type_qualifier
        """
    def p_specifier_qualifier_list_3(self, p) -> None:
        """ specifier_qualifier_list  : type_specifier
        """
    def p_specifier_qualifier_list_4(self, p) -> None:
        """ specifier_qualifier_list  : type_qualifier_list type_specifier
        """
    def p_specifier_qualifier_list_5(self, p) -> None:
        """ specifier_qualifier_list  : alignment_specifier
        """
    def p_specifier_qualifier_list_6(self, p) -> None:
        """ specifier_qualifier_list  : specifier_qualifier_list alignment_specifier
        """
    def p_struct_or_union_specifier_1(self, p) -> None:
        """ struct_or_union_specifier   : struct_or_union ID
                                        | struct_or_union TYPEID
        """
    def p_struct_or_union_specifier_2(self, p) -> None:
        """ struct_or_union_specifier : struct_or_union brace_open struct_declaration_list brace_close
                                      | struct_or_union brace_open brace_close
        """
    def p_struct_or_union_specifier_3(self, p) -> None:
        """ struct_or_union_specifier   : struct_or_union ID brace_open struct_declaration_list brace_close
                                        | struct_or_union ID brace_open brace_close
                                        | struct_or_union TYPEID brace_open struct_declaration_list brace_close
                                        | struct_or_union TYPEID brace_open brace_close
        """
    def p_struct_or_union(self, p) -> None:
        """ struct_or_union : STRUCT
                            | UNION
        """
    def p_struct_declaration_list(self, p) -> None:
        """ struct_declaration_list     : struct_declaration
                                        | struct_declaration_list struct_declaration
        """
    def p_struct_declaration_1(self, p) -> None:
        """ struct_declaration : specifier_qualifier_list struct_declarator_list_opt SEMI
        """
    def p_struct_declaration_2(self, p) -> None:
        """ struct_declaration : SEMI
        """
    def p_struct_declaration_3(self, p) -> None:
        """ struct_declaration : pppragma_directive
        """
    def p_struct_declarator_list(self, p) -> None:
        """ struct_declarator_list  : struct_declarator
                                    | struct_declarator_list COMMA struct_declarator
        """
    def p_struct_declarator_1(self, p) -> None:
        """ struct_declarator : declarator
        """
    def p_struct_declarator_2(self, p) -> None:
        """ struct_declarator   : declarator COLON constant_expression
                                | COLON constant_expression
        """
    def p_enum_specifier_1(self, p) -> None:
        """ enum_specifier  : ENUM ID
                            | ENUM TYPEID
        """
    def p_enum_specifier_2(self, p) -> None:
        """ enum_specifier  : ENUM brace_open enumerator_list brace_close
        """
    def p_enum_specifier_3(self, p) -> None:
        """ enum_specifier  : ENUM ID brace_open enumerator_list brace_close
                            | ENUM TYPEID brace_open enumerator_list brace_close
        """
    def p_enumerator_list(self, p) -> None:
        """ enumerator_list : enumerator
                            | enumerator_list COMMA
                            | enumerator_list COMMA enumerator
        """
    def p_alignment_specifier(self, p) -> None:
        """ alignment_specifier  : _ALIGNAS LPAREN type_name RPAREN
                                 | _ALIGNAS LPAREN constant_expression RPAREN
        """
    def p_enumerator(self, p) -> None:
        """ enumerator  : ID
                        | ID EQUALS constant_expression
        """
    def p_declarator(self, p) -> None:
        """ declarator  : id_declarator
                        | typeid_declarator
        """
    def p_xxx_declarator_1(self, p) -> None:
        """ xxx_declarator  : direct_xxx_declarator
        """
    def p_xxx_declarator_2(self, p) -> None:
        """ xxx_declarator  : pointer direct_xxx_declarator
        """
    def p_direct_xxx_declarator_1(self, p) -> None:
        """ direct_xxx_declarator   : yyy
        """
    def p_direct_xxx_declarator_2(self, p) -> None:
        """ direct_xxx_declarator   : LPAREN xxx_declarator RPAREN
        """
    def p_direct_xxx_declarator_3(self, p) -> None:
        """ direct_xxx_declarator   : direct_xxx_declarator LBRACKET type_qualifier_list_opt assignment_expression_opt RBRACKET
        """
    def p_direct_xxx_declarator_4(self, p) -> None:
        """ direct_xxx_declarator   : direct_xxx_declarator LBRACKET STATIC type_qualifier_list_opt assignment_expression RBRACKET
                                    | direct_xxx_declarator LBRACKET type_qualifier_list STATIC assignment_expression RBRACKET
        """
    def p_direct_xxx_declarator_5(self, p) -> None:
        """ direct_xxx_declarator   : direct_xxx_declarator LBRACKET type_qualifier_list_opt TIMES RBRACKET
        """
    def p_direct_xxx_declarator_6(self, p) -> None:
        """ direct_xxx_declarator   : direct_xxx_declarator LPAREN parameter_type_list RPAREN
                                    | direct_xxx_declarator LPAREN identifier_list_opt RPAREN
        """
    def p_pointer(self, p) -> None:
        """ pointer : TIMES type_qualifier_list_opt
                    | TIMES type_qualifier_list_opt pointer
        """
    def p_type_qualifier_list(self, p) -> None:
        """ type_qualifier_list : type_qualifier
                                | type_qualifier_list type_qualifier
        """
    def p_parameter_type_list(self, p) -> None:
        """ parameter_type_list : parameter_list
                                | parameter_list COMMA ELLIPSIS
        """
    def p_parameter_list(self, p) -> None:
        """ parameter_list  : parameter_declaration
                            | parameter_list COMMA parameter_declaration
        """
    def p_parameter_declaration_1(self, p) -> None:
        """ parameter_declaration   : declaration_specifiers id_declarator
                                    | declaration_specifiers typeid_noparen_declarator
        """
    def p_parameter_declaration_2(self, p) -> None:
        """ parameter_declaration   : declaration_specifiers abstract_declarator_opt
        """
    def p_identifier_list(self, p) -> None:
        """ identifier_list : identifier
                            | identifier_list COMMA identifier
        """
    def p_initializer_1(self, p) -> None:
        """ initializer : assignment_expression
        """
    def p_initializer_2(self, p) -> None:
        """ initializer : brace_open initializer_list_opt brace_close
                        | brace_open initializer_list COMMA brace_close
        """
    def p_initializer_list(self, p) -> None:
        """ initializer_list    : designation_opt initializer
                                | initializer_list COMMA designation_opt initializer
        """
    def p_designation(self, p) -> None:
        """ designation : designator_list EQUALS
        """
    def p_designator_list(self, p) -> None:
        """ designator_list : designator
                            | designator_list designator
        """
    def p_designator(self, p) -> None:
        """ designator  : LBRACKET constant_expression RBRACKET
                        | PERIOD identifier
        """
    def p_type_name(self, p) -> None:
        """ type_name   : specifier_qualifier_list abstract_declarator_opt
        """
    def p_abstract_declarator_1(self, p) -> None:
        """ abstract_declarator     : pointer
        """
    def p_abstract_declarator_2(self, p) -> None:
        """ abstract_declarator     : pointer direct_abstract_declarator
        """
    def p_abstract_declarator_3(self, p) -> None:
        """ abstract_declarator     : direct_abstract_declarator
        """
    def p_direct_abstract_declarator_1(self, p) -> None:
        """ direct_abstract_declarator  : LPAREN abstract_declarator RPAREN """
    def p_direct_abstract_declarator_2(self, p) -> None:
        """ direct_abstract_declarator  : direct_abstract_declarator LBRACKET assignment_expression_opt RBRACKET
        """
    def p_direct_abstract_declarator_3(self, p) -> None:
        """ direct_abstract_declarator  : LBRACKET type_qualifier_list_opt assignment_expression_opt RBRACKET
        """
    def p_direct_abstract_declarator_4(self, p) -> None:
        """ direct_abstract_declarator  : direct_abstract_declarator LBRACKET TIMES RBRACKET
        """
    def p_direct_abstract_declarator_5(self, p) -> None:
        """ direct_abstract_declarator  : LBRACKET TIMES RBRACKET
        """
    def p_direct_abstract_declarator_6(self, p) -> None:
        """ direct_abstract_declarator  : direct_abstract_declarator LPAREN parameter_type_list_opt RPAREN
        """
    def p_direct_abstract_declarator_7(self, p) -> None:
        """ direct_abstract_declarator  : LPAREN parameter_type_list_opt RPAREN
        """
    def p_block_item(self, p) -> None:
        """ block_item  : declaration
                        | statement
        """
    def p_block_item_list(self, p) -> None:
        """ block_item_list : block_item
                            | block_item_list block_item
        """
    def p_compound_statement_1(self, p) -> None:
        """ compound_statement : brace_open block_item_list_opt brace_close """
    def p_labeled_statement_1(self, p) -> None:
        """ labeled_statement : ID COLON pragmacomp_or_statement """
    def p_labeled_statement_2(self, p) -> None:
        """ labeled_statement : CASE constant_expression COLON pragmacomp_or_statement """
    def p_labeled_statement_3(self, p) -> None:
        """ labeled_statement : DEFAULT COLON pragmacomp_or_statement """
    def p_selection_statement_1(self, p) -> None:
        """ selection_statement : IF LPAREN expression RPAREN pragmacomp_or_statement """
    def p_selection_statement_2(self, p) -> None:
        """ selection_statement : IF LPAREN expression RPAREN statement ELSE pragmacomp_or_statement """
    def p_selection_statement_3(self, p) -> None:
        """ selection_statement : SWITCH LPAREN expression RPAREN pragmacomp_or_statement """
    def p_iteration_statement_1(self, p) -> None:
        """ iteration_statement : WHILE LPAREN expression RPAREN pragmacomp_or_statement """
    def p_iteration_statement_2(self, p) -> None:
        """ iteration_statement : DO pragmacomp_or_statement WHILE LPAREN expression RPAREN SEMI """
    def p_iteration_statement_3(self, p) -> None:
        """ iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN pragmacomp_or_statement """
    def p_iteration_statement_4(self, p) -> None:
        """ iteration_statement : FOR LPAREN declaration expression_opt SEMI expression_opt RPAREN pragmacomp_or_statement """
    def p_jump_statement_1(self, p) -> None:
        """ jump_statement  : GOTO ID SEMI """
    def p_jump_statement_2(self, p) -> None:
        """ jump_statement  : BREAK SEMI """
    def p_jump_statement_3(self, p) -> None:
        """ jump_statement  : CONTINUE SEMI """
    def p_jump_statement_4(self, p) -> None:
        """ jump_statement  : RETURN expression SEMI
                            | RETURN SEMI
        """
    def p_expression_statement(self, p) -> None:
        """ expression_statement : expression_opt SEMI """
    def p_expression(self, p) -> None:
        """ expression  : assignment_expression
                        | expression COMMA assignment_expression
        """
    def p_parenthesized_compound_expression(self, p) -> None:
        """ assignment_expression : LPAREN compound_statement RPAREN """
    def p_typedef_name(self, p) -> None:
        """ typedef_name : TYPEID """
    def p_assignment_expression(self, p) -> None:
        """ assignment_expression   : conditional_expression
                                    | unary_expression assignment_operator assignment_expression
        """
    def p_assignment_operator(self, p) -> None:
        """ assignment_operator : EQUALS
                                | XOREQUAL
                                | TIMESEQUAL
                                | DIVEQUAL
                                | MODEQUAL
                                | PLUSEQUAL
                                | MINUSEQUAL
                                | LSHIFTEQUAL
                                | RSHIFTEQUAL
                                | ANDEQUAL
                                | OREQUAL
        """
    def p_constant_expression(self, p) -> None:
        """ constant_expression : conditional_expression """
    def p_conditional_expression(self, p) -> None:
        """ conditional_expression  : binary_expression
                                    | binary_expression CONDOP expression COLON conditional_expression
        """
    def p_binary_expression(self, p) -> None:
        """ binary_expression   : cast_expression
                                | binary_expression TIMES binary_expression
                                | binary_expression DIVIDE binary_expression
                                | binary_expression MOD binary_expression
                                | binary_expression PLUS binary_expression
                                | binary_expression MINUS binary_expression
                                | binary_expression RSHIFT binary_expression
                                | binary_expression LSHIFT binary_expression
                                | binary_expression LT binary_expression
                                | binary_expression LE binary_expression
                                | binary_expression GE binary_expression
                                | binary_expression GT binary_expression
                                | binary_expression EQ binary_expression
                                | binary_expression NE binary_expression
                                | binary_expression AND binary_expression
                                | binary_expression OR binary_expression
                                | binary_expression XOR binary_expression
                                | binary_expression LAND binary_expression
                                | binary_expression LOR binary_expression
        """
    def p_cast_expression_1(self, p) -> None:
        """ cast_expression : unary_expression """
    def p_cast_expression_2(self, p) -> None:
        """ cast_expression : LPAREN type_name RPAREN cast_expression """
    def p_unary_expression_1(self, p) -> None:
        """ unary_expression    : postfix_expression """
    def p_unary_expression_2(self, p) -> None:
        """ unary_expression    : PLUSPLUS unary_expression
                                | MINUSMINUS unary_expression
                                | unary_operator cast_expression
        """
    def p_unary_expression_3(self, p) -> None:
        """ unary_expression    : SIZEOF unary_expression
                                | SIZEOF LPAREN type_name RPAREN
                                | _ALIGNOF LPAREN type_name RPAREN
        """
    def p_unary_operator(self, p) -> None:
        """ unary_operator  : AND
                            | TIMES
                            | PLUS
                            | MINUS
                            | NOT
                            | LNOT
        """
    def p_postfix_expression_1(self, p) -> None:
        """ postfix_expression  : primary_expression """
    def p_postfix_expression_2(self, p) -> None:
        """ postfix_expression  : postfix_expression LBRACKET expression RBRACKET """
    def p_postfix_expression_3(self, p) -> None:
        """ postfix_expression  : postfix_expression LPAREN argument_expression_list RPAREN
                                | postfix_expression LPAREN RPAREN
        """
    def p_postfix_expression_4(self, p) -> None:
        """ postfix_expression  : postfix_expression PERIOD ID
                                | postfix_expression PERIOD TYPEID
                                | postfix_expression ARROW ID
                                | postfix_expression ARROW TYPEID
        """
    def p_postfix_expression_5(self, p) -> None:
        """ postfix_expression  : postfix_expression PLUSPLUS
                                | postfix_expression MINUSMINUS
        """
    def p_postfix_expression_6(self, p) -> None:
        """ postfix_expression  : LPAREN type_name RPAREN brace_open initializer_list brace_close
                                | LPAREN type_name RPAREN brace_open initializer_list COMMA brace_close
        """
    def p_primary_expression_1(self, p) -> None:
        """ primary_expression  : identifier """
    def p_primary_expression_2(self, p) -> None:
        """ primary_expression  : constant """
    def p_primary_expression_3(self, p) -> None:
        """ primary_expression  : unified_string_literal
                                | unified_wstring_literal
        """
    def p_primary_expression_4(self, p) -> None:
        """ primary_expression  : LPAREN expression RPAREN """
    def p_primary_expression_5(self, p) -> None:
        """ primary_expression  : OFFSETOF LPAREN type_name COMMA offsetof_member_designator RPAREN
        """
    def p_offsetof_member_designator(self, p) -> None:
        """ offsetof_member_designator : identifier
                                         | offsetof_member_designator PERIOD identifier
                                         | offsetof_member_designator LBRACKET expression RBRACKET
        """
    def p_argument_expression_list(self, p) -> None:
        """ argument_expression_list    : assignment_expression
                                        | argument_expression_list COMMA assignment_expression
        """
    def p_identifier(self, p) -> None:
        """ identifier  : ID """
    def p_constant_1(self, p) -> None:
        """ constant    : INT_CONST_DEC
                        | INT_CONST_OCT
                        | INT_CONST_HEX
                        | INT_CONST_BIN
                        | INT_CONST_CHAR
        """
    def p_constant_2(self, p) -> None:
        """ constant    : FLOAT_CONST
                        | HEX_FLOAT_CONST
        """
    def p_constant_3(self, p) -> None:
        """ constant    : CHAR_CONST
                        | WCHAR_CONST
                        | U8CHAR_CONST
                        | U16CHAR_CONST
                        | U32CHAR_CONST
        """
    def p_unified_string_literal(self, p) -> None:
        """ unified_string_literal  : STRING_LITERAL
                                    | unified_string_literal STRING_LITERAL
        """
    def p_unified_wstring_literal(self, p) -> None:
        """ unified_wstring_literal : WSTRING_LITERAL
                                    | U8STRING_LITERAL
                                    | U16STRING_LITERAL
                                    | U32STRING_LITERAL
                                    | unified_wstring_literal WSTRING_LITERAL
                                    | unified_wstring_literal U8STRING_LITERAL
                                    | unified_wstring_literal U16STRING_LITERAL
                                    | unified_wstring_literal U32STRING_LITERAL
        """
    def p_brace_open(self, p) -> None:
        """ brace_open  :   LBRACE
        """
    def p_brace_close(self, p) -> None:
        """ brace_close :   RBRACE
        """
    def p_empty(self, p) -> None:
        """empty : """
    def p_error(self, p) -> None: ...
