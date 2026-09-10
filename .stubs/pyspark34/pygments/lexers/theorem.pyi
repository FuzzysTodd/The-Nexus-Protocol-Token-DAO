from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['CoqLexer', 'IsabelleLexer', 'LeanLexer']

class CoqLexer(RegexLexer):
    """
    For the Coq theorem prover.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: int
    keywords1: Incomplete
    keywords2: Incomplete
    keywords3: Incomplete
    keywords4: Incomplete
    keywords5: Incomplete
    keywords6: Incomplete
    keyopts: Incomplete
    operators: str
    prefix_syms: str
    infix_syms: str
    tokens: Incomplete
    def analyse_text(text): ...

class IsabelleLexer(RegexLexer):
    """
    For the Isabelle proof assistant.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keyword_minor: Incomplete
    keyword_diag: Incomplete
    keyword_thy: Incomplete
    keyword_section: Incomplete
    keyword_subsection: Incomplete
    keyword_theory_decl: Incomplete
    keyword_theory_script: Incomplete
    keyword_theory_goal: Incomplete
    keyword_qed: Incomplete
    keyword_abandon_proof: Incomplete
    keyword_proof_goal: Incomplete
    keyword_proof_block: Incomplete
    keyword_proof_chain: Incomplete
    keyword_proof_decl: Incomplete
    keyword_proof_asm: Incomplete
    keyword_proof_asm_goal: Incomplete
    keyword_proof_script: Incomplete
    operators: Incomplete
    proof_operators: Incomplete
    tokens: Incomplete

class LeanLexer(RegexLexer):
    """
    For the Lean theorem prover.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
