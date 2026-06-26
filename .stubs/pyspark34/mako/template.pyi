from _typeshed import Incomplete
from mako import cache as cache, codegen as codegen, compat as compat, exceptions as exceptions, runtime as runtime, util as util
from mako.lexer import Lexer as Lexer

class Template:
    '''Represents a compiled template.

    :class:`.Template` includes a reference to the original
    template source (via the :attr:`.source` attribute)
    as well as the source code of the
    generated Python module (i.e. the :attr:`.code` attribute),
    as well as a reference to an actual Python module.

    :class:`.Template` is constructed using either a literal string
    representing the template text, or a filename representing a filesystem
    path to a source file.

    :param text: textual template source.  This argument is mutually
     exclusive versus the ``filename`` parameter.

    :param filename: filename of the source template.  This argument is
     mutually exclusive versus the ``text`` parameter.

    :param buffer_filters: string list of filters to be applied
     to the output of ``%def``\\ s which are buffered, cached, or otherwise
     filtered, after all filters
     defined with the ``%def`` itself have been applied. Allows the
     creation of default expression filters that let the output
     of return-valued ``%def``\\ s "opt out" of that filtering via
     passing special attributes or objects.

    :param cache_args: Dictionary of cache configuration arguments that
     will be passed to the :class:`.CacheImpl`.   See :ref:`caching_toplevel`.

    :param cache_dir:

     .. deprecated:: 0.6
        Use the ``\'dir\'`` argument in the ``cache_args`` dictionary.
        See :ref:`caching_toplevel`.

    :param cache_enabled: Boolean flag which enables caching of this
     template.  See :ref:`caching_toplevel`.

    :param cache_impl: String name of a :class:`.CacheImpl` caching
     implementation to use.   Defaults to ``\'beaker\'``.

    :param cache_type:

     .. deprecated:: 0.6
        Use the ``\'type\'`` argument in the ``cache_args`` dictionary.
        See :ref:`caching_toplevel`.

    :param cache_url:

     .. deprecated:: 0.6
        Use the ``\'url\'`` argument in the ``cache_args`` dictionary.
        See :ref:`caching_toplevel`.

    :param default_filters: List of string filter names that will
     be applied to all expressions.  See :ref:`filtering_default_filters`.

    :param enable_loop: When ``True``, enable the ``loop`` context variable.
     This can be set to ``False`` to support templates that may
     be making usage of the name "``loop``".   Individual templates can
     re-enable the "loop" context by placing the directive
     ``enable_loop="True"`` inside the ``<%page>`` tag -- see
     :ref:`migrating_loop`.

    :param encoding_errors: Error parameter passed to ``encode()`` when
     string encoding is performed. See :ref:`usage_unicode`.

    :param error_handler: Python callable which is called whenever
     compile or runtime exceptions occur. The callable is passed
     the current context as well as the exception. If the
     callable returns ``True``, the exception is considered to
     be handled, else it is re-raised after the function
     completes. Is used to provide custom error-rendering
     functions.

     .. seealso::

        :paramref:`.Template.include_error_handler` - include-specific
        error handler function

    :param format_exceptions: if ``True``, exceptions which occur during
     the render phase of this template will be caught and
     formatted into an HTML error page, which then becomes the
     rendered result of the :meth:`.render` call. Otherwise,
     runtime exceptions are propagated outwards.

    :param imports: String list of Python statements, typically individual
     "import" lines, which will be placed into the module level
     preamble of all generated Python modules. See the example
     in :ref:`filtering_default_filters`.

    :param future_imports: String list of names to import from `__future__`.
     These will be concatenated into a comma-separated string and inserted
     into the beginning of the template, e.g. ``futures_imports=[\'FOO\',
     \'BAR\']`` results in ``from __future__ import FOO, BAR``.  If you\'re
     interested in using features like the new division operator, you must
     use future_imports to convey that to the renderer, as otherwise the
     import will not appear as the first executed statement in the generated
     code and will therefore not have the desired effect.

    :param include_error_handler: An error handler that runs when this template
     is included within another one via the ``<%include>`` tag, and raises an
     error.  Compare to the :paramref:`.Template.error_handler` option.

     .. versionadded:: 1.0.6

     .. seealso::

        :paramref:`.Template.error_handler` - top-level error handler function

    :param input_encoding: Encoding of the template\'s source code.  Can
     be used in lieu of the coding comment. See
     :ref:`usage_unicode` as well as :ref:`unicode_toplevel` for
     details on source encoding.

    :param lookup: a :class:`.TemplateLookup` instance that will be used
     for all file lookups via the ``<%namespace>``,
     ``<%include>``, and ``<%inherit>`` tags. See
     :ref:`usage_templatelookup`.

    :param module_directory: Filesystem location where generated
     Python module files will be placed.

    :param module_filename: Overrides the filename of the generated
     Python module file. For advanced usage only.

    :param module_writer: A callable which overrides how the Python
     module is written entirely.  The callable is passed the
     encoded source content of the module and the destination
     path to be written to.   The default behavior of module writing
     uses a tempfile in conjunction with a file move in order
     to make the operation atomic.   So a user-defined module
     writing function that mimics the default behavior would be:

     .. sourcecode:: python

         import tempfile
         import os
         import shutil

         def module_writer(source, outputpath):
             (dest, name) = \\\\\n                 tempfile.mkstemp(
                     dir=os.path.dirname(outputpath)
                 )

             os.write(dest, source)
             os.close(dest)
             shutil.move(name, outputpath)

         from mako.template import Template
         mytemplate = Template(
                         filename="index.html",
                         module_directory="/path/to/modules",
                         module_writer=module_writer
                     )

     The function is provided for unusual configurations where
     certain platform-specific permissions or other special
     steps are needed.

    :param output_encoding: The encoding to use when :meth:`.render`
     is called.
     See :ref:`usage_unicode` as well as :ref:`unicode_toplevel`.

    :param preprocessor: Python callable which will be passed
     the full template source before it is parsed. The return
     result of the callable will be used as the template source
     code.

    :param lexer_cls: A :class:`.Lexer` class used to parse
     the template.   The :class:`.Lexer` class is used by
     default.

     .. versionadded:: 0.7.4

    :param strict_undefined: Replaces the automatic usage of
     ``UNDEFINED`` for any undeclared variables not located in
     the :class:`.Context` with an immediate raise of
     ``NameError``. The advantage is immediate reporting of
     missing variables which include the name.

     .. versionadded:: 0.3.6

    :param uri: string URI or other identifier for this template.
     If not provided, the ``uri`` is generated from the filesystem
     path, or from the in-memory identity of a non-file-based
     template. The primary usage of the ``uri`` is to provide a key
     within :class:`.TemplateLookup`, as well as to generate the
     file path of the generated Python module file, if
     ``module_directory`` is specified.

    '''
    lexer_cls = Lexer
    module_id: Incomplete
    uri: Incomplete
    input_encoding: Incomplete
    output_encoding: Incomplete
    encoding_errors: Incomplete
    enable_loop: Incomplete
    strict_undefined: Incomplete
    module_writer: Incomplete
    default_filters: Incomplete
    buffer_filters: Incomplete
    imports: Incomplete
    future_imports: Incomplete
    preprocessor: Incomplete
    module: Incomplete
    filename: Incomplete
    callable_: Incomplete
    format_exceptions: Incomplete
    error_handler: Incomplete
    include_error_handler: Incomplete
    lookup: Incomplete
    module_directory: Incomplete
    def __init__(self, text: Incomplete | None = None, filename: Incomplete | None = None, uri: Incomplete | None = None, format_exceptions: bool = False, error_handler: Incomplete | None = None, lookup: Incomplete | None = None, output_encoding: Incomplete | None = None, encoding_errors: str = 'strict', module_directory: Incomplete | None = None, cache_args: Incomplete | None = None, cache_impl: str = 'beaker', cache_enabled: bool = True, cache_type: Incomplete | None = None, cache_dir: Incomplete | None = None, cache_url: Incomplete | None = None, module_filename: Incomplete | None = None, input_encoding: Incomplete | None = None, module_writer: Incomplete | None = None, default_filters: Incomplete | None = None, buffer_filters=(), strict_undefined: bool = False, imports: Incomplete | None = None, future_imports: Incomplete | None = None, enable_loop: bool = True, preprocessor: Incomplete | None = None, lexer_cls: Incomplete | None = None, include_error_handler: Incomplete | None = None) -> None: ...
    def reserved_names(self): ...
    @property
    def source(self):
        """Return the template source code for this :class:`.Template`."""
    @property
    def code(self):
        """Return the module source code for this :class:`.Template`."""
    def cache(self): ...
    @property
    def cache_dir(self): ...
    @property
    def cache_url(self): ...
    @property
    def cache_type(self): ...
    def render(self, *args, **data):
        """Render the output of this template as a string.

        If the template specifies an output encoding, the string
        will be encoded accordingly, else the output is raw (raw
        output uses `StringIO` and can't handle multibyte
        characters). A :class:`.Context` object is created corresponding
        to the given data. Arguments that are explicitly declared
        by this template's internal rendering method are also
        pulled from the given ``*args``, ``**data`` members.

        """
    def render_unicode(self, *args, **data):
        """Render the output of this template as a unicode object."""
    def render_context(self, context, *args, **kwargs) -> None:
        """Render this :class:`.Template` with the given context.

        The data is written to the context's buffer.

        """
    def has_def(self, name): ...
    def get_def(self, name):
        """Return a def of this template as a :class:`.DefTemplate`."""
    def list_defs(self):
        """return a list of defs in the template.

        .. versionadded:: 1.0.4

        """
    @property
    def last_modified(self): ...

class ModuleTemplate(Template):
    '''A Template which is constructed given an existing Python module.

    e.g.::

         t = Template("this is a template")
         f = file("mymodule.py", "w")
         f.write(t.code)
         f.close()

         import mymodule

         t = ModuleTemplate(mymodule)
         print(t.render())

    '''
    module_id: Incomplete
    uri: Incomplete
    input_encoding: Incomplete
    output_encoding: Incomplete
    encoding_errors: Incomplete
    enable_loop: Incomplete
    module: Incomplete
    filename: Incomplete
    callable_: Incomplete
    format_exceptions: Incomplete
    error_handler: Incomplete
    include_error_handler: Incomplete
    lookup: Incomplete
    def __init__(self, module, module_filename: Incomplete | None = None, template: Incomplete | None = None, template_filename: Incomplete | None = None, module_source: Incomplete | None = None, template_source: Incomplete | None = None, output_encoding: Incomplete | None = None, encoding_errors: str = 'strict', format_exceptions: bool = False, error_handler: Incomplete | None = None, lookup: Incomplete | None = None, cache_args: Incomplete | None = None, cache_impl: str = 'beaker', cache_enabled: bool = True, cache_type: Incomplete | None = None, cache_dir: Incomplete | None = None, cache_url: Incomplete | None = None, include_error_handler: Incomplete | None = None) -> None: ...

class DefTemplate(Template):
    """A :class:`.Template` which represents a callable def in a parent
    template."""
    parent: Incomplete
    callable_: Incomplete
    output_encoding: Incomplete
    module: Incomplete
    encoding_errors: Incomplete
    format_exceptions: Incomplete
    error_handler: Incomplete
    include_error_handler: Incomplete
    enable_loop: Incomplete
    lookup: Incomplete
    def __init__(self, parent, callable_) -> None: ...
    def get_def(self, name): ...

class ModuleInfo:
    """Stores information about a module currently loaded into
    memory, provides reverse lookups of template source, module
    source code based on a module's identifier.

    """
    module: Incomplete
    module_filename: Incomplete
    template_filename: Incomplete
    module_source: Incomplete
    template_source: Incomplete
    template_uri: Incomplete
    def __init__(self, module, module_filename, template, template_filename, module_source, template_source, template_uri) -> None: ...
    @classmethod
    def get_module_source_metadata(cls, module_source, full_line_map: bool = False): ...
    @property
    def code(self): ...
    @property
    def source(self): ...
