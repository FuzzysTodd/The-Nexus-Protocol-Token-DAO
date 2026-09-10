from _typeshed import Incomplete
from nltk.draw.tree import TreeSegmentWidget as TreeSegmentWidget, tree_to_treesegment as tree_to_treesegment
from nltk.draw.util import CanvasFrame as CanvasFrame, ColorizedList as ColorizedList, ShowText as ShowText, SymbolWidget as SymbolWidget, TextWidget as TextWidget
from nltk.grammar import CFG as CFG, Nonterminal as Nonterminal, nonterminals as nonterminals
from nltk.tree import Tree as Tree

class ProductionList(ColorizedList):
    ARROW: Incomplete

class CFGEditor:
    """
    A dialog window for creating and editing context free grammars.
    ``CFGEditor`` imposes the following restrictions:

    - All nonterminals must be strings consisting of word
      characters.
    - All terminals must be strings consisting of word characters
      and space characters.
    """
    ARROW: Incomplete
    def __init__(self, parent, cfg: Incomplete | None = None, set_cfg_callback: Incomplete | None = None) -> None: ...

class CFGDemo:
    def __init__(self, grammar, text) -> None: ...
    def reset_workspace(self) -> None: ...
    def workspace_markprod(self, production) -> None: ...
    def destroy(self, *args) -> None: ...
    def mainloop(self, *args, **kwargs) -> None: ...

def demo2() -> None: ...
def demo() -> None: ...
def demo3() -> None: ...
