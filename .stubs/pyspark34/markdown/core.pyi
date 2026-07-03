from _typeshed import Incomplete

__all__ = ['Markdown', 'markdown', 'markdownFromFile']

class Markdown:
    """Convert Markdown to HTML."""
    doc_tag: str
    output_formats: Incomplete
    tab_length: Incomplete
    ESCAPED_CHARS: Incomplete
    block_level_elements: Incomplete
    registeredExtensions: Incomplete
    docType: str
    stripTopLevelTags: bool
    references: Incomplete
    htmlStash: Incomplete
    def __init__(self, **kwargs) -> None:
        """
        Creates a new Markdown instance.

        Keyword arguments:

        * `extensions`: A list of extensions.
            If an item is an instance of a subclass of `markdown.extension.Extension`, the  instance will be used
            as-is. If an item is of type string, first an entry point will be loaded. If that fails, the string is
            assumed to use Python dot notation (`path.to.module:ClassName`) to load a `markdown.Extension` subclass. If
            no class is specified, then a `makeExtension` function is called within the specified module.
        * `extension_configs`: Configuration settings for extensions.
        * `output_format`: Format of output. Supported formats are:
            * `xhtml`: Outputs XHTML style tags. Default.
            * `html`: Outputs HTML style tags.
        * `tab_length`: Length of tabs in the source. Default: 4

        """
    preprocessors: Incomplete
    parser: Incomplete
    inlinePatterns: Incomplete
    treeprocessors: Incomplete
    postprocessors: Incomplete
    def build_parser(self):
        """ Build the parser from the various parts. """
    def registerExtensions(self, extensions, configs):
        """
        Register extensions with this instance of Markdown.

        Keyword arguments:

        * `extensions`: A list of extensions, which can either
           be strings or objects.
        * `configs`: A dictionary mapping extension names to `configs` options.

        """
    def build_extension(self, ext_name, configs):
        """
        Build extension from a string name, then return an instance.

        First attempt to load an entry point. The string name must be registered as an entry point in the
        `markdown.extensions` group which points to a subclass of the `markdown.extensions.Extension` class.
        If multiple distributions have registered the same name, the first one found is returned.

        If no entry point is found, assume dot notation (`path.to.module:ClassName`). Load the specified class and
        return an instance. If no class is specified, import the module and call a `makeExtension` function and return
        the `Extension` instance returned by that function.
        """
    def registerExtension(self, extension):
        """ This gets called by the extension """
    def reset(self):
        """
        Resets all state variables so that we can start with a new text.
        """
    output_format: Incomplete
    serializer: Incomplete
    def set_output_format(self, format):
        """ Set the output format for the class instance. """
    def is_block_level(self, tag):
        """Check if the tag is a block level HTML tag."""
    lines: Incomplete
    def convert(self, source):
        """
        Convert markdown to serialized XHTML or HTML.

        Keyword arguments:

        * `source`: Source text as a Unicode string.

        Markdown processing takes place in five steps:

        1. A bunch of `preprocessors` munge the input text.
        2. `BlockParser()` parses the high-level structural elements of the
           pre-processed text into an `ElementTree`.
        3. A bunch of `treeprocessors` are run against the `ElementTree`. One
           such `treeprocessor` runs `InlinePatterns` against the `ElementTree`,
           detecting inline markup.
        4. Some post-processors are run against the text after the `ElementTree`
           has been serialized into text.
        5. The output is written to a string.

        """
    def convertFile(self, input: Incomplete | None = None, output: Incomplete | None = None, encoding: Incomplete | None = None):
        """Converts a markdown file and returns the HTML as a Unicode string.

        Decodes the file using the provided encoding (defaults to `utf-8`),
        passes the file content to markdown, and outputs the html to either
        the provided stream or the file with provided name, using the same
        encoding as the source file. The `xmlcharrefreplace` error handler is
        used when encoding the output.

        **Note:** This is the only place that decoding and encoding of Unicode
        takes place in Python-Markdown.  (All other code is Unicode-in /
        Unicode-out.)

        Keyword arguments:

        * `input`: File object or path. Reads from `stdin` if `None`.
        * `output`: File object or path. Writes to `stdout` if `None`.
        * `encoding`: Encoding of input and output files. Defaults to `utf-8`.

        """

def markdown(text, **kwargs):
    """Convert a markdown string to HTML and return HTML as a Unicode string.

    This is a shortcut function for `Markdown` class to cover the most
    basic use case.  It initializes an instance of `Markdown`, loads the
    necessary extensions and runs the parser on the given text.

    Keyword arguments:

    * `text`: Markdown formatted text as Unicode or ASCII string.
    * Any arguments accepted by the Markdown class.

    Returns: An HTML document as a string.

    """
def markdownFromFile(**kwargs) -> None:
    """Read markdown code from a file and write it to a file or a stream.

    This is a shortcut function which initializes an instance of `Markdown`,
    and calls the `convertFile` method rather than `convert`.

    Keyword arguments:

    * `input`: a file name or readable object.
    * `output`: a file name or writable object.
    * `encoding`: Encoding of input and output.
    * Any arguments accepted by the `Markdown` class.

    """
