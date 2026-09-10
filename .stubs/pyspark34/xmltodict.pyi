from _typeshed import Incomplete

__version__: str

class ParsingInterrupted(Exception): ...

class _DictSAXHandler:
    path: Incomplete
    stack: Incomplete
    data: Incomplete
    item: Incomplete
    item_depth: Incomplete
    xml_attribs: Incomplete
    item_callback: Incomplete
    attr_prefix: Incomplete
    cdata_key: Incomplete
    force_cdata: Incomplete
    cdata_separator: Incomplete
    postprocessor: Incomplete
    dict_constructor: Incomplete
    strip_whitespace: Incomplete
    namespace_separator: Incomplete
    namespaces: Incomplete
    namespace_declarations: Incomplete
    force_list: Incomplete
    comment_key: Incomplete
    def __init__(self, item_depth: int = 0, item_callback=..., xml_attribs: bool = True, attr_prefix: str = '@', cdata_key: str = '#text', force_cdata: bool = False, cdata_separator: str = '', postprocessor: Incomplete | None = None, dict_constructor=..., strip_whitespace: bool = True, namespace_separator: str = ':', namespaces: Incomplete | None = None, force_list: Incomplete | None = None, comment_key: str = '#comment') -> None: ...
    def startNamespaceDecl(self, prefix, uri) -> None: ...
    def startElement(self, full_name, attrs) -> None: ...
    def endElement(self, full_name) -> None: ...
    def characters(self, data) -> None: ...
    def comments(self, data) -> None: ...
    def push_data(self, item, key, data): ...

def parse(xml_input, encoding: Incomplete | None = None, expat=..., process_namespaces: bool = False, namespace_separator: str = ':', disable_entities: bool = True, process_comments: bool = False, **kwargs):
    '''Parse the given XML input and convert it into a dictionary.

    `xml_input` can either be a `string`, a file-like object, or a generator of strings.

    If `xml_attribs` is `True`, element attributes are put in the dictionary
    among regular child elements, using `@` as a prefix to avoid collisions. If
    set to `False`, they are just ignored.

    Simple example::

        >>> import xmltodict
        >>> doc = xmltodict.parse("""
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>
        ... """)
        >>> doc[\'a\'][\'@prop\']
        u\'x\'
        >>> doc[\'a\'][\'b\']
        [u\'1\', u\'2\']

    If `item_depth` is `0`, the function returns a dictionary for the root
    element (default behavior). Otherwise, it calls `item_callback` every time
    an item at the specified depth is found and returns `None` in the end
    (streaming mode).

    The callback function receives two parameters: the `path` from the document
    root to the item (name-attribs pairs), and the `item` (dict). If the
    callback\'s return value is false-ish, parsing will be stopped with the
    :class:`ParsingInterrupted` exception.

    Streaming example::

        >>> def handle(path, item):
        ...     print(\'path:%s item:%s\' % (path, item))
        ...     return True
        ...
        >>> xmltodict.parse("""
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>""", item_depth=2, item_callback=handle)
        path:[(u\'a\', {u\'prop\': u\'x\'}), (u\'b\', None)] item:1
        path:[(u\'a\', {u\'prop\': u\'x\'}), (u\'b\', None)] item:2

    The optional argument `postprocessor` is a function that takes `path`,
    `key` and `value` as positional arguments and returns a new `(key, value)`
    pair where both `key` and `value` may have changed. Usage example::

        >>> def postprocessor(path, key, value):
        ...     try:
        ...         return key + \':int\', int(value)
        ...     except (ValueError, TypeError):
        ...         return key, value
        >>> xmltodict.parse(\'<a><b>1</b><b>2</b><b>x</b></a>\',
        ...                 postprocessor=postprocessor)
        {\'a\': {\'b:int\': [1, 2], \'b\': \'x\'}}

    You can pass an alternate version of `expat` (such as `defusedexpat`) by
    using the `expat` parameter. E.g:

        >>> import defusedexpat
        >>> xmltodict.parse(\'<a>hello</a>\', expat=defusedexpat.pyexpat)
        {\'a\': \'hello\'}

    You can use the force_list argument to force lists to be created even
    when there is only a single child of a given level of hierarchy. The
    force_list argument is a tuple of keys. If the key for a given level
    of hierarchy is in the force_list argument, that level of hierarchy
    will have a list as a child (even if there is only one sub-element).
    The index_keys operation takes precedence over this. This is applied
    after any user-supplied postprocessor has already run.

        For example, given this input:
        <servers>
          <server>
            <name>host1</name>
            <os>Linux</os>
            <interfaces>
              <interface>
                <name>em0</name>
                <ip_address>10.0.0.1</ip_address>
              </interface>
            </interfaces>
          </server>
        </servers>

        If called with force_list=(\'interface\',), it will produce
        this dictionary:
        {\'servers\':
          {\'server\':
            {\'name\': \'host1\',
             \'os\': \'Linux\'},
             \'interfaces\':
              {\'interface\':
                [ {\'name\': \'em0\', \'ip_address\': \'10.0.0.1\' } ] } } }

        `force_list` can also be a callable that receives `path`, `key` and
        `value`. This is helpful in cases where the logic that decides whether
        a list should be forced is more complex.


        If `process_comment` is `True` then comment will be added with comment_key
        (default=`\'#comment\'`) to then tag which contains comment

            For example, given this input:
            <a>
              <b>
                <!-- b comment -->
                <c>
                    <!-- c comment -->
                    1
                </c>
                <d>2</d>
              </b>
            </a>

            If called with process_comment=True, it will produce
            this dictionary:
            \'a\': {
                \'b\': {
                    \'#comment\': \'b comment\',
                    \'c\': {

                        \'#comment\': \'c comment\',
                        \'#text\': \'1\',
                    },
                    \'d\': \'2\',
                },
            }
    '''
def unparse(input_dict, output: Incomplete | None = None, encoding: str = 'utf-8', full_document: bool = True, short_empty_elements: bool = False, **kwargs):
    """Emit an XML document for the given `input_dict` (reverse of `parse`).

    The resulting XML document is returned as a string, but if `output` (a
    file-like object) is specified, it is written there instead.

    Dictionary keys prefixed with `attr_prefix` (default=`'@'`) are interpreted
    as XML node attributes, whereas keys equal to `cdata_key`
    (default=`'#text'`) are treated as character data.

    The `pretty` parameter (default=`False`) enables pretty-printing. In this
    mode, lines are terminated with `'
'` and indented with `'\t'`, but this
    can be customized with the `newl` and `indent` parameters.

    """
