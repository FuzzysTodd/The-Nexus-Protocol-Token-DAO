__all__ = ['footnotes']

def footnotes(md) -> None:
    '''A mistune plugin to support footnotes, spec defined at
    https://michelf.ca/projects/php-markdown/extra/#footnotes

    Here is an example:

    .. code-block:: text

        That\'s some text with a footnote.[^1]

        [^1]: And that\'s the footnote.

    It will be converted into HTML:

    .. code-block:: html

        <p>That\'s some text with a footnote.<sup class="footnote-ref" id="fnref-1"><a href="#fn-1">1</a></sup></p>
        <section class="footnotes">
        <ol>
        <li id="fn-1"><p>And that\'s the footnote.<a href="#fnref-1" class="footnote">&#8617;</a></p></li>
        </ol>
        </section>

    :param md: Markdown instance
    '''
