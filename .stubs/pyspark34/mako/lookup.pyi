from _typeshed import Incomplete
from mako import exceptions as exceptions, util as util
from mako.template import Template as Template

class TemplateCollection:
    """Represent a collection of :class:`.Template` objects,
    identifiable via URI.

    A :class:`.TemplateCollection` is linked to the usage of
    all template tags that address other templates, such
    as ``<%include>``, ``<%namespace>``, and ``<%inherit>``.
    The ``file`` attribute of each of those tags refers
    to a string URI that is passed to that :class:`.Template`
    object's :class:`.TemplateCollection` for resolution.

    :class:`.TemplateCollection` is an abstract class,
    with the usual default implementation being :class:`.TemplateLookup`.

    """
    def has_template(self, uri):
        """Return ``True`` if this :class:`.TemplateLookup` is
        capable of returning a :class:`.Template` object for the
        given ``uri``.

        :param uri: String URI of the template to be resolved.

        """
    def get_template(self, uri, relativeto: Incomplete | None = None) -> None:
        """Return a :class:`.Template` object corresponding to the given
        ``uri``.

        The default implementation raises
        :class:`.NotImplementedError`. Implementations should
        raise :class:`.TemplateLookupException` if the given ``uri``
        cannot be resolved.

        :param uri: String URI of the template to be resolved.
        :param relativeto: if present, the given ``uri`` is assumed to
         be relative to this URI.

        """
    def filename_to_uri(self, uri, filename):
        """Convert the given ``filename`` to a URI relative to
        this :class:`.TemplateCollection`."""
    def adjust_uri(self, uri, filename):
        """Adjust the given ``uri`` based on the calling ``filename``.

        When this method is called from the runtime, the
        ``filename`` parameter is taken directly to the ``filename``
        attribute of the calling template. Therefore a custom
        :class:`.TemplateCollection` subclass can place any string
        identifier desired in the ``filename`` parameter of the
        :class:`.Template` objects it constructs and have them come back
        here.

        """

class TemplateLookup(TemplateCollection):
    '''Represent a collection of templates that locates template source files
    from the local filesystem.

    The primary argument is the ``directories`` argument, the list of
    directories to search:

    .. sourcecode:: python

        lookup = TemplateLookup(["/path/to/templates"])
        some_template = lookup.get_template("/index.html")

    The :class:`.TemplateLookup` can also be given :class:`.Template` objects
    programatically using :meth:`.put_string` or :meth:`.put_template`:

    .. sourcecode:: python

        lookup = TemplateLookup()
        lookup.put_string("base.html", \'\'\'
            <html><body>${self.next()}</body></html>
        \'\'\')
        lookup.put_string("hello.html", \'\'\'
            <%include file=\'base.html\'/>

            Hello, world !
        \'\'\')


    :param directories: A list of directory names which will be
     searched for a particular template URI. The URI is appended
     to each directory and the filesystem checked.

    :param collection_size: Approximate size of the collection used
     to store templates. If left at its default of ``-1``, the size
     is unbounded, and a plain Python dictionary is used to
     relate URI strings to :class:`.Template` instances.
     Otherwise, a least-recently-used cache object is used which
     will maintain the size of the collection approximately to
     the number given.

    :param filesystem_checks: When at its default value of ``True``,
     each call to :meth:`.TemplateLookup.get_template()` will
     compare the filesystem last modified time to the time in
     which an existing :class:`.Template` object was created.
     This allows the :class:`.TemplateLookup` to regenerate a
     new :class:`.Template` whenever the original source has
     been updated. Set this to ``False`` for a very minor
     performance increase.

    :param modulename_callable: A callable which, when present,
     is passed the path of the source file as well as the
     requested URI, and then returns the full path of the
     generated Python module file. This is used to inject
     alternate schemes for Python module location. If left at
     its default of ``None``, the built in system of generation
     based on ``module_directory`` plus ``uri`` is used.

    All other keyword parameters available for
    :class:`.Template` are mirrored here. When new
    :class:`.Template` objects are created, the keywords
    established with this :class:`.TemplateLookup` are passed on
    to each new :class:`.Template`.

    '''
    directories: Incomplete
    module_directory: Incomplete
    modulename_callable: Incomplete
    filesystem_checks: Incomplete
    collection_size: Incomplete
    template_args: Incomplete
    def __init__(self, directories: Incomplete | None = None, module_directory: Incomplete | None = None, filesystem_checks: bool = True, collection_size: int = -1, format_exceptions: bool = False, error_handler: Incomplete | None = None, output_encoding: Incomplete | None = None, encoding_errors: str = 'strict', cache_args: Incomplete | None = None, cache_impl: str = 'beaker', cache_enabled: bool = True, cache_type: Incomplete | None = None, cache_dir: Incomplete | None = None, cache_url: Incomplete | None = None, modulename_callable: Incomplete | None = None, module_writer: Incomplete | None = None, default_filters: Incomplete | None = None, buffer_filters=(), strict_undefined: bool = False, imports: Incomplete | None = None, future_imports: Incomplete | None = None, enable_loop: bool = True, input_encoding: Incomplete | None = None, preprocessor: Incomplete | None = None, lexer_cls: Incomplete | None = None, include_error_handler: Incomplete | None = None) -> None: ...
    def get_template(self, uri):
        """Return a :class:`.Template` object corresponding to the given
        ``uri``.

        .. note:: The ``relativeto`` argument is not supported here at
           the moment.

        """
    def adjust_uri(self, uri, relativeto):
        """Adjust the given ``uri`` based on the given relative URI."""
    def filename_to_uri(self, filename):
        """Convert the given ``filename`` to a URI relative to
        this :class:`.TemplateCollection`."""
    def put_string(self, uri, text) -> None:
        """Place a new :class:`.Template` object into this
        :class:`.TemplateLookup`, based on the given string of
        ``text``.

        """
    def put_template(self, uri, template) -> None:
        """Place a new :class:`.Template` object into this
        :class:`.TemplateLookup`, based on the given
        :class:`.Template` object.

        """
