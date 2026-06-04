from _typeshed import Incomplete

__version__: str

def default_filter(name, obj):
    """Attribute filter.

    It filters out module attributes, and also methods starting with an
    underscore ``_``.

    This is used as the default filter for the :func:`create_patches` function
    and the :func:`patches` decorator.

    Parameters
    ----------
    name : str
        Attribute name.
    obj : object
        Attribute value.

    Returns
    -------
    bool
        Whether the attribute should be returned.
    """

class DecoratorData:
    """Decorator data.

    Attributes
    ----------
    patches : list of gorilla.Patch
        Patches created through the decorators.
    override : dict
        Any overriding value defined by the :func:`destination`, :func:`name`,
        and :func:`settings` decorators.
    filter : bool or None
        Value defined by the :func:`filter` decorator, if any, or ``None``
        otherwise.
    """
    patches: Incomplete
    override: Incomplete
    filter: Incomplete
    def __init__(self) -> None:
        """Constructor."""

class Settings:
    """Define the patching behaviour.

    Attributes
    ----------
    allow_hit : bool
        A hit occurs when an attribute at the destination already exists with
        the name given by the patch. If ``False``, the patch process won't
        allow setting a new value for the attribute by raising an exception.
        Defaults to ``False``.
    store_hit : bool
        If ``True`` and :attr:`allow_hit` is also set to ``True``, then any
        attribute at the destination that is hit is stored under a different
        name before being overwritten by the patch. Defaults to ``True``.
    """
    allow_hit: bool
    store_hit: bool
    def __init__(self, **kwargs) -> None:
        """Constructor.

        Parameters
        ----------
        kwargs
            Keyword arguments, see the attributes.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Patch:
    """Describe all the information required to apply a patch.

    Attributes
    ----------
    destination : obj
        Patch destination.
    name : str
        Name of the attribute at the destination.
    obj : obj
        Attribute value.
    settings : gorilla.Settings or None
        Settings. If ``None``, the default settings are used.

    Warning
    -------
    It is highly recommended to use the output of the function
    :func:`get_attribute` for setting the attribute :attr:`obj`. This will
    ensure that the descriptor protocol is bypassed instead of possibly
    retrieving attributes invalid for patching, such as bound methods.
    """
    destination: Incomplete
    name: Incomplete
    obj: Incomplete
    settings: Incomplete
    is_inplace_patch: Incomplete
    def __init__(self, destination, name, obj, settings: Incomplete | None = None) -> None:
        """Constructor.

        Parameters
        ----------
        destination : object
            See the :attr:`~Patch.destination` attribute.
        name : str
            See the :attr:`~Patch.name` attribute.
        obj : object
            See the :attr:`~Patch.obj` attribute.
        settings : gorilla.Settings
            See the :attr:`~Patch.settings` attribute.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

def apply(patch) -> None:
    """Apply a patch.

    The patch's :attr:`~Patch.obj` attribute is injected into the patch's
    :attr:`~Patch.destination` under the patch's :attr:`~Patch.name`.

    This is a wrapper around calling
    ``setattr(patch.destination, patch.name, patch.obj)``.

    Parameters
    ----------
    patch : gorilla.Patch
        Patch.

    Raises
    ------
    RuntimeError
        Overwriting an existing attribute is not allowed when the setting
        :attr:`Settings.allow_hit` is set to ``True``.

    Note
    ----
    If both the attributes :attr:`Settings.allow_hit` and
    :attr:`Settings.store_hit` are ``True`` but that the target attribute seems
    to have already been stored, then it won't be stored again to avoid losing
    the original attribute that was stored the first time around.
    """
def revert(patch) -> None:
    """Revert a patch.
    Parameters
    ----------
    patch : gorilla.Patch
        Patch.
    Note
    ----
    This is only possible if the attribute :attr:`Settings.store_hit` was set
    to ``True`` when applying the patch and overriding an existing attribute.

    Notice:
    This method is taken from
    https://github.com/christophercrouzet/gorilla/blob/v0.4.0/gorilla.py#L318-L351
    with modifictions for autologging disablement purposes.
    """
def patch(destination, name: Incomplete | None = None, settings: Incomplete | None = None):
    """Decorator to create a patch.

    The object being decorated becomes the :attr:`~Patch.obj` attribute of the
    patch.

    Parameters
    ----------
    destination : object
        Patch destination.
    name : str
        Name of the attribute at the destination.
    settings : gorilla.Settings
        Settings.

    Returns
    -------
    object
        The decorated object.

    See Also
    --------
    :class:`Patch`.
    """
def destination(value):
    """Modifier decorator to update a patch's destination.

    This only modifies the behaviour of the :func:`create_patches` function
    and the :func:`patches` decorator, given that their parameter
    ``use_decorators`` is set to ``True``.

    Parameters
    ----------
    value : object
        Patch destination.

    Returns
    -------
    object
        The decorated object.
    """
def name(value):
    """Modifier decorator to update a patch's name.

    This only modifies the behaviour of the :func:`create_patches` function
    and the :func:`patches` decorator, given that their parameter
    ``use_decorators`` is set to ``True``.

    Parameters
    ----------
    value : object
        Patch name.

    Returns
    -------
    object
        The decorated object.
    """
def settings(**kwargs):
    """Modifier decorator to update a patch's settings.

    This only modifies the behaviour of the :func:`create_patches` function
    and the :func:`patches` decorator, given that their parameter
    ``use_decorators`` is set to ``True``.

    Parameters
    ----------
    kwargs
        Settings to update. See :class:`Settings` for the list.

    Returns
    -------
    object
        The decorated object.
    """
def filter(value):
    """Modifier decorator to force the inclusion or exclusion of an attribute.

    This only modifies the behaviour of the :func:`create_patches` function
    and the :func:`patches` decorator, given that their parameter
    ``use_decorators`` is set to ``True``.

    Parameters
    ----------
    value : bool
        ``True`` to force inclusion, ``False`` to force exclusion, and ``None``
        to inherit from the behaviour defined by :func:`create_patches` or
        :func:`patches`.

    Returns
    -------
    object
        The decorated object.
    """
def find_patches(modules, recursive: bool = True):
    """Find all the patches created through decorators.

    Parameters
    ----------
    modules : list of module
        Modules and/or packages to search the patches in.
    recursive : bool
        ``True`` to search recursively in subpackages.

    Returns
    -------
    list of gorilla.Patch
        Patches found.

    Raises
    ------
    TypeError
        The input is not a valid package or module.

    See Also
    --------
    :func:`patch`, :func:`patches`.
    """
def get_original_attribute(obj, name, bypass_descriptor_protocol: bool = False):
    """Retrieve an overridden attribute that has been stored.

    Parameters
    ----------
    obj : object
        Object to search the attribute in.
    name : str
        Name of the attribute.
    bypass_descriptor_protocol: boolean
        bypassing descriptor protocol if true. When storing original method during patching or
        restoring original method during reverting patch, we need set bypass_descriptor_protocol
        to be True to ensure get the raw attribute object.

    Returns
    -------
    object
        The attribute found.

    Raises
    ------
    AttributeError
        The attribute couldn't be found.

    Note
    ----
    if setting store_hit=False, then after patch applied, this methods may return patched
    attribute instead of original attribute in specific cases.

    See Also
    --------
    :attr:`Settings.allow_hit`.
    """
def get_decorator_data(obj, set_default: bool = False):
    """Retrieve any decorator data from an object.

    Parameters
    ----------
    obj : object
        Object.
    set_default : bool
        If no data is found, a default one is set on the object and returned,
        otherwise ``None`` is returned.

    Returns
    -------
    gorilla.DecoratorData
        The decorator data or ``None``.
    """
