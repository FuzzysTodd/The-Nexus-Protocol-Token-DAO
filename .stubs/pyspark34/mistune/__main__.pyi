from . import create_markdown as create_markdown
from .renderers.markdown import MarkdownRenderer as MarkdownRenderer
from .renderers.rst import RSTRenderer as RSTRenderer

CMD_HELP: str

def cli(): ...
def read_stdin(): ...
