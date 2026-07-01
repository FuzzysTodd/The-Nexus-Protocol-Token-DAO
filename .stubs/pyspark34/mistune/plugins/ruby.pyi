from ..helpers import parse_link as parse_link, parse_link_label as parse_link_label
from ..util import unikey as unikey

RUBY_PATTERN: str

def parse_ruby(inline, m, state): ...
def render_ruby(renderer, text, rt): ...
def ruby(md) -> None:
    '''A mistune plugin to support ``<ruby>`` tag. The syntax is defined
    at https://lepture.com/en/2022/markdown-ruby-markup:

    .. code-block:: text

        [漢字(ㄏㄢˋㄗˋ)]
        [漢(ㄏㄢˋ)字(ㄗˋ)]

        [漢字(ㄏㄢˋㄗˋ)][link]
        [漢字(ㄏㄢˋㄗˋ)](/url "title")

        [link]: /url "title"

    :param md: Markdown instance
    '''
