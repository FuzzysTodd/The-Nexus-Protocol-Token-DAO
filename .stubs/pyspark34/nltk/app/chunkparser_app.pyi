from _typeshed import Incomplete

__all__ = ['app']

class RegexpChunkApp:
    """
    A graphical tool for exploring the regular expression based chunk
    parser ``nltk.chunk.RegexpChunkParser``.

    See ``HELP`` for instructional text.
    """
    TAGSET: Incomplete
    HELP: Incomplete
    HELP_AUTOTAG: Incomplete
    def normalize_grammar(self, grammar): ...
    tagset: Incomplete
    chunker: Incomplete
    grammar: Incomplete
    normalized_grammar: Incomplete
    grammar_changed: int
    devset: Incomplete
    devset_name: Incomplete
    devset_index: int
    def __init__(self, devset_name: str = 'conll2000', devset: Incomplete | None = None, grammar: str = '', chunk_label: str = 'NP', tagset: Incomplete | None = None) -> None:
        """
        :param devset_name: The name of the development set; used for
            display & for save files.  If either the name 'treebank'
            or the name 'conll2000' is used, and devset is None, then
            devset will be set automatically.
        :param devset: A list of chunked sentences
        :param grammar: The initial grammar to display.
        :param tagset: Dictionary from tags to string descriptions, used
            for the help page.  Defaults to ``self.TAGSET``.
        """
    def toggle_show_trace(self, *e): ...
    charnum: Incomplete
    linenum: Incomplete
    def show_trace(self, *e) -> None: ...
    def show_help(self, tab): ...
    top: Incomplete
    def destroy(self, *e) -> None: ...
    def show_devset(self, index: Incomplete | None = None) -> None: ...
    def update(self, *event) -> None: ...
    def reset(self) -> None: ...
    SAVE_GRAMMAR_TEMPLATE: str
    def save_grammar(self, filename: Incomplete | None = None) -> None: ...
    def load_grammar(self, filename: Incomplete | None = None) -> None: ...
    def save_history(self, filename: Incomplete | None = None) -> None: ...
    def about(self, *e) -> None: ...
    def set_devset_size(self, size: Incomplete | None = None) -> None: ...
    def resize(self, size: Incomplete | None = None) -> None: ...
    def mainloop(self, *args, **kwargs) -> None:
        """
        Enter the Tkinter mainloop.  This function must be called if
        this demo is created from a non-interactive program (e.g.
        from a secript); otherwise, the demo will close as soon as
        the script completes.
        """

def app() -> None: ...
