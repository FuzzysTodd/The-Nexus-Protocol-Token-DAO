from .util import striptags as striptags
from _typeshed import Incomplete

def add_toc_hook(md, min_level: int = 1, max_level: int = 3, heading_id: Incomplete | None = None):
    """Add a hook to save toc items into ``state.env``. This is
    usually helpful for doc generator::

        import mistune
        from mistune.toc import add_toc_hook, render_toc_ul

        md = mistune.create_markdown(...)
        add_toc_hook(md, level, heading_id)

        html, state = md.parse(text)
        toc_items = state.env['toc_items']
        toc_html = render_toc_ul(toc_items)

    :param md: Markdown instance
    :param min_level: min heading level
    :param max_level: max heading level
    :param heading_id: a function to generate heading_id
    """
def normalize_toc_item(md, token): ...
def render_toc_ul(toc):
    '''Render a <ul> table of content HTML. The param "toc" should
    be formatted into this structure::

        [
          (level, id, text),
        ]

    For example::

        [
          (1, \'toc-intro\', \'Introduction\'),
          (2, \'toc-install\', \'Install\'),
          (2, \'toc-upgrade\', \'Upgrade\'),
          (1, \'toc-license\', \'License\'),
        ]
    '''
