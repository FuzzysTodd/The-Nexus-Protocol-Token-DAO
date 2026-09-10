from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['Modula2Lexer']

class Modula2Lexer(RegexLexer):
    '''
    For Modula-2 source code.

    The Modula-2 lexer supports several dialects.  By default, it operates in
    fallback mode, recognising the *combined* literals, punctuation symbols
    and operators of all supported dialects, and the *combined* reserved words
    and builtins of PIM Modula-2, ISO Modula-2 and Modula-2 R10, while not
    differentiating between library defined identifiers.

    To select a specific dialect, a dialect option may be passed
    or a dialect tag may be embedded into a source file.

    Dialect Options:

    `m2pim`
        Select PIM Modula-2 dialect.
    `m2iso`
        Select ISO Modula-2 dialect.
    `m2r10`
        Select Modula-2 R10 dialect.
    `objm2`
        Select Objective Modula-2 dialect.

    The PIM and ISO dialect options may be qualified with a language extension.

    Language Extensions:

    `+aglet`
        Select Aglet Modula-2 extensions, available with m2iso.
    `+gm2`
        Select GNU Modula-2 extensions, available with m2pim.
    `+p1`
        Select p1 Modula-2 extensions, available with m2iso.
    `+xds`
        Select XDS Modula-2 extensions, available with m2iso.


    Passing a Dialect Option via Unix Commandline Interface

    Dialect options may be passed to the lexer using the `dialect` key.
    Only one such option should be passed. If multiple dialect options are
    passed, the first valid option is used, any subsequent options are ignored.

    Examples:

    `$ pygmentize -O full,dialect=m2iso -f html -o /path/to/output /path/to/input`
        Use ISO dialect to render input to HTML output
    `$ pygmentize -O full,dialect=m2iso+p1 -f rtf -o /path/to/output /path/to/input`
        Use ISO dialect with p1 extensions to render input to RTF output


    Embedding a Dialect Option within a source file

    A dialect option may be embedded in a source file in form of a dialect
    tag, a specially formatted comment that specifies a dialect option.

    Dialect Tag EBNF::

       dialectTag :
           OpeningCommentDelim Prefix dialectOption ClosingCommentDelim ;

       dialectOption :
           \'m2pim\' | \'m2iso\' | \'m2r10\' | \'objm2\' |
           \'m2iso+aglet\' | \'m2pim+gm2\' | \'m2iso+p1\' | \'m2iso+xds\' ;

       Prefix : \'!\' ;

       OpeningCommentDelim : \'(*\' ;

       ClosingCommentDelim : \'*)\' ;

    No whitespace is permitted between the tokens of a dialect tag.

    In the event that a source file contains multiple dialect tags, the first
    tag that contains a valid dialect option will be used and any subsequent
    dialect tags will be ignored.  Ideally, a dialect tag should be placed
    at the beginning of a source file.

    An embedded dialect tag overrides a dialect option set via command line.

    Examples:

    ``(*!m2r10*) DEFINITION MODULE Foobar; ...``
        Use Modula2 R10 dialect to render this source file.
    ``(*!m2pim+gm2*) DEFINITION MODULE Bazbam; ...``
        Use PIM dialect with GNU extensions to render this source file.


    Algol Publication Mode:

    In Algol publication mode, source text is rendered for publication of
    algorithms in scientific papers and academic texts, following the format
    of the Revised Algol-60 Language Report.  It is activated by passing
    one of two corresponding styles as an option:

    `algol`
        render reserved words lowercase underline boldface
        and builtins lowercase boldface italic
    `algol_nu`
        render reserved words lowercase boldface (no underlining)
        and builtins lowercase boldface italic

    The lexer automatically performs the required lowercase conversion when
    this mode is activated.

    Example:

    ``$ pygmentize -O full,style=algol -f latex -o /path/to/output /path/to/input``
        Render input file in Algol publication mode to LaTeX output.


    Rendering Mode of First Class ADT Identifiers:

    The rendering of standard library first class ADT identifiers is controlled
    by option flag "treat_stdlib_adts_as_builtins".

    When this option is turned on, standard library ADT identifiers are rendered
    as builtins.  When it is turned off, they are rendered as ordinary library
    identifiers.

    `treat_stdlib_adts_as_builtins` (default: On)

    The option is useful for dialects that support ADTs as first class objects
    and provide ADTs in the standard library that would otherwise be built-in.

    At present, only Modula-2 R10 supports library ADTs as first class objects
    and therefore, no ADT identifiers are defined for any other dialects.

    Example:

    ``$ pygmentize -O full,dialect=m2r10,treat_stdlib_adts_as_builtins=Off ...``
        Render standard library ADTs as ordinary library types.

    .. versionadded:: 1.3

    .. versionchanged:: 2.1
       Added multi-dialect support.
    '''
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    common_reserved_words: Incomplete
    common_builtins: Incomplete
    common_pseudo_builtins: Incomplete
    pim_lexemes_to_reject: Incomplete
    pim_additional_reserved_words: Incomplete
    pim_additional_builtins: Incomplete
    pim_additional_pseudo_builtins: Incomplete
    iso_lexemes_to_reject: Incomplete
    iso_additional_reserved_words: Incomplete
    iso_additional_builtins: Incomplete
    iso_additional_pseudo_builtins: Incomplete
    m2r10_lexemes_to_reject: Incomplete
    m2r10_additional_reserved_words: Incomplete
    m2r10_additional_builtins: Incomplete
    m2r10_additional_pseudo_builtins: Incomplete
    objm2_lexemes_to_reject: Incomplete
    objm2_additional_reserved_words: Incomplete
    objm2_additional_builtins: Incomplete
    objm2_additional_pseudo_builtins: Incomplete
    aglet_additional_reserved_words: Incomplete
    aglet_additional_builtins: Incomplete
    aglet_additional_pseudo_builtins: Incomplete
    gm2_additional_reserved_words: Incomplete
    gm2_additional_builtins: Incomplete
    gm2_additional_pseudo_builtins: Incomplete
    p1_additional_reserved_words: Incomplete
    p1_additional_builtins: Incomplete
    p1_additional_pseudo_builtins: Incomplete
    xds_additional_reserved_words: Incomplete
    xds_additional_builtins: Incomplete
    xds_additional_pseudo_builtins: Incomplete
    pim_stdlib_module_identifiers: Incomplete
    pim_stdlib_type_identifiers: Incomplete
    pim_stdlib_proc_identifiers: Incomplete
    pim_stdlib_var_identifiers: Incomplete
    pim_stdlib_const_identifiers: Incomplete
    iso_stdlib_module_identifiers: Incomplete
    iso_stdlib_type_identifiers: Incomplete
    iso_stdlib_proc_identifiers: Incomplete
    iso_stdlib_var_identifiers: Incomplete
    iso_stdlib_const_identifiers: Incomplete
    m2r10_stdlib_adt_identifiers: Incomplete
    m2r10_stdlib_blueprint_identifiers: Incomplete
    m2r10_stdlib_module_identifiers: Incomplete
    m2r10_stdlib_type_identifiers: Incomplete
    m2r10_stdlib_proc_identifiers: Incomplete
    m2r10_stdlib_var_identifiers: Incomplete
    m2r10_stdlib_const_identifiers: Incomplete
    dialects: Incomplete
    lexemes_to_reject_db: Incomplete
    reserved_words_db: Incomplete
    builtins_db: Incomplete
    pseudo_builtins_db: Incomplete
    stdlib_adts_db: Incomplete
    stdlib_modules_db: Incomplete
    stdlib_types_db: Incomplete
    stdlib_procedures_db: Incomplete
    stdlib_variables_db: Incomplete
    stdlib_constants_db: Incomplete
    dialect_set_by_tag: bool
    algol_publication_mode: bool
    treat_stdlib_adts_as_builtins: Incomplete
    def __init__(self, **options) -> None: ...
    dialect: Incomplete
    lexemes_to_reject: Incomplete
    reserved_words: Incomplete
    builtins: Incomplete
    pseudo_builtins: Incomplete
    adts: Incomplete
    modules: Incomplete
    types: Incomplete
    procedures: Incomplete
    variables: Incomplete
    constants: Incomplete
    def set_dialect(self, dialect_id) -> None: ...
    def get_dialect_from_dialect_tag(self, dialect_tag): ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text):
        """It's Pascal-like, but does not use FUNCTION -- uses PROCEDURE
        instead."""
