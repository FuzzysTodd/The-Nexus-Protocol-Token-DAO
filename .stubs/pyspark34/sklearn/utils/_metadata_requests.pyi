from .. import get_config as get_config
from ..exceptions import UnsetMetadataPassedError as UnsetMetadataPassedError
from ._bunch import Bunch as Bunch
from _typeshed import Incomplete
from typing import NamedTuple

METHODS: Incomplete
UNUSED: str
WARN: str
UNCHANGED: str
VALID_REQUEST_VALUES: Incomplete

def request_is_alias(item):
    """Check if an item is a valid alias.

    Values in ``VALID_REQUEST_VALUES`` are not considered aliases in this
    context. Only a string which is a valid identifier is.

    Parameters
    ----------
    item : object
        The given item to be checked if it can be an alias.

    Returns
    -------
    result : bool
        Whether the given item is a valid alias.
    """
def request_is_valid(item):
    """Check if an item is a valid request value (and not an alias).

    Parameters
    ----------
    item : object
        The given item to be checked.

    Returns
    -------
    result : bool
        Whether the given item is valid.
    """

class MethodMetadataRequest:
    """A prescription of how metadata is to be passed to a single method.

    Refer to :class:`MetadataRequest` for how this class is used.

    .. versionadded:: 1.3

    Parameters
    ----------
    owner : str
        A display name for the object owning these requests.

    method : str
        The name of the method to which these requests belong.
    """
    owner: Incomplete
    method: Incomplete
    def __init__(self, owner, method) -> None: ...
    @property
    def requests(self):
        """Dictionary of the form: ``{key: alias}``."""
    def add_request(self, *, param, alias):
        """Add request info for a metadata.

        Parameters
        ----------
        param : str
            The property for which a request is set.

        alias : str, or {True, False, None}
            Specifies which metadata should be routed to `param`

            - str: the name (or alias) of metadata given to a meta-estimator that
              should be routed to this parameter.

            - True: requested

            - False: not requested

            - None: error if passed
        """

class MetadataRequest:
    """Contains the metadata request info of a consumer.

    Instances of :class:`MethodMetadataRequest` are used in this class for each
    available method under `metadatarequest.{method}`.

    Consumer-only classes such as simple estimators return a serialized
    version of this class as the output of `get_metadata_routing()`.

    .. versionadded:: 1.3

    Parameters
    ----------
    owner : str
        The name of the object to which these requests belong.
    """
    def __init__(self, owner) -> None: ...

class RouterMappingPair(NamedTuple):
    mapping: Incomplete
    router: Incomplete

class MethodPair(NamedTuple):
    callee: Incomplete
    caller: Incomplete

class MethodMapping:
    """Stores the mapping between callee and caller methods for a router.

    This class is primarily used in a ``get_metadata_routing()`` of a router
    object when defining the mapping between a sub-object (a sub-estimator or a
    scorer) to the router's methods. It stores a collection of ``Route``
    namedtuples.

    Iterating through an instance of this class will yield named
    ``MethodPair(callee, caller)`` tuples.

    .. versionadded:: 1.3
    """
    def __init__(self) -> None: ...
    def __iter__(self): ...
    def add(self, *, callee, caller):
        """Add a method mapping.

        Parameters
        ----------
        callee : str
            Child object's method name. This method is called in ``caller``.

        caller : str
            Parent estimator's method name in which the ``callee`` is called.

        Returns
        -------
        self : MethodMapping
            Returns self.
        """
    @classmethod
    def from_str(cls, route):
        '''Construct an instance from a string.

        Parameters
        ----------
        route : str
            A string representing the mapping, it can be:

              - `"one-to-one"`: a one to one mapping for all methods.
              - `"method"`: the name of a single method, such as ``fit``,
                ``transform``, ``score``, etc.

        Returns
        -------
        obj : MethodMapping
            A :class:`~utils.metadata_requests.MethodMapping` instance
            constructed from the given string.
        '''

class MetadataRouter:
    '''Stores and handles metadata routing for a router object.

    This class is used by router objects to store and handle metadata routing.
    Routing information is stored as a dictionary of the form ``{"object_name":
    RouteMappingPair(method_mapping, routing_info)}``, where ``method_mapping``
    is an instance of :class:`~utils.metadata_requests.MethodMapping` and
    ``routing_info`` is either a
    :class:`~utils.metadata_requests.MetadataRequest` or a
    :class:`~utils.metadata_requests.MetadataRouter` instance.

    .. versionadded:: 1.3

    Parameters
    ----------
    owner : str
        The name of the object to which these requests belong.
    '''
    owner: Incomplete
    def __init__(self, owner) -> None: ...
    def add_self_request(self, obj):
        """Add `self` (as a consumer) to the routing.

        This method is used if the router is also a consumer, and hence the
        router itself needs to be included in the routing. The passed object
        can be an estimator or a
        :class:``~utils.metadata_requests.MetadataRequest``.

        A router should add itself using this method instead of `add` since it
        should be treated differently than the other objects to which metadata
        is routed by the router.

        Parameters
        ----------
        obj : object
            This is typically the router instance, i.e. `self` in a
            ``get_metadata_routing()`` implementation. It can also be a
            ``MetadataRequest`` instance.

        Returns
        -------
        self : MetadataRouter
            Returns `self`.
        """
    def add(self, *, method_mapping, **objs):
        """Add named objects with their corresponding method mapping.

        Parameters
        ----------
        method_mapping : MethodMapping or str
            The mapping between the child and the parent's methods. If str, the
            output of :func:`~utils.metadata_requests.MethodMapping.from_str`
            is used.

        **objs : dict
            A dictionary of objects from which metadata is extracted by calling
            :func:`~utils.metadata_requests.get_routing_for_object` on them.

        Returns
        -------
        self : MetadataRouter
            Returns `self`.
        """
    def route_params(self, *, caller, params):
        '''Return the input parameters requested by child objects.

        The output of this method is a bunch, which includes the inputs for all
        methods of each child object that are used in the router\'s `caller`
        method.

        If the router is also a consumer, it also checks for warnings of
        `self`\'s/consumer\'s requested metadata.

        Parameters
        ----------
        caller : str
            The name of the method for which the parameters are requested and
            routed. If called inside the :term:`fit` method of a router, it
            would be `"fit"`.

        params : dict
            A dictionary of provided metadata.

        Returns
        -------
        params : Bunch
            A :class:`~utils.Bunch` of the form
            ``{"object_name": {"method_name": {prop: value}}}`` which can be
            used to pass the required metadata to corresponding methods or
            corresponding child objects.
        '''
    def validate_metadata(self, *, method, params) -> None:
        '''Validate given metadata for a method.

        This raises a ``ValueError`` if some of the passed metadata are not
        understood by child objects.

        Parameters
        ----------
        method : str
            The name of the method for which the parameters are requested and
            routed. If called inside the :term:`fit` method of a router, it
            would be `"fit"`.

        params : dict
            A dictionary of provided metadata.
        '''
    def __iter__(self): ...

def get_routing_for_object(obj: Incomplete | None = None):
    """Get a ``Metadata{Router, Request}`` instance from the given object.

    This function returns a
    :class:`~utils.metadata_request.MetadataRouter` or a
    :class:`~utils.metadata_request.MetadataRequest` from the given input.

    This function always returns a copy or an instance constructed from the
    input, such that changing the output of this function will not change the
    original object.

    .. versionadded:: 1.3

    Parameters
    ----------
    obj : object
        - If the object is already a
            :class:`~utils.metadata_requests.MetadataRequest` or a
            :class:`~utils.metadata_requests.MetadataRouter`, return a copy
            of that.
        - If the object provides a `get_metadata_routing` method, return a copy
            of the output of that method.
        - Returns an empty :class:`~utils.metadata_requests.MetadataRequest`
            otherwise.

    Returns
    -------
    obj : MetadataRequest or MetadataRouting
        A ``MetadataRequest`` or a ``MetadataRouting`` taken or created from
        the given object.
    """

REQUESTER_DOC: str
REQUESTER_DOC_PARAM: str
REQUESTER_DOC_RETURN: str

class RequestMethod:
    '''
    A descriptor for request methods.

    .. versionadded:: 1.3

    Parameters
    ----------
    name : str
        The name of the method for which the request function should be
        created, e.g. ``"fit"`` would create a ``set_fit_request`` function.

    keys : list of str
        A list of strings which are accepted parameters by the created
        function, e.g. ``["sample_weight"]`` if the corresponding method
        accepts it as a metadata.

    validate_keys : bool, default=True
        Whether to check if the requested parameters fit the actual parameters
        of the method.

    Notes
    -----
    This class is a descriptor [1]_ and uses PEP-362 to set the signature of
    the returned function [2]_.

    References
    ----------
    .. [1] https://docs.python.org/3/howto/descriptor.html

    .. [2] https://www.python.org/dev/peps/pep-0362/
    '''
    name: Incomplete
    keys: Incomplete
    validate_keys: Incomplete
    def __init__(self, name, keys, validate_keys: bool = True) -> None: ...
    def __get__(self, instance, owner): ...

class _MetadataRequester:
    """Mixin class for adding metadata request functionality.

    ``BaseEstimator`` inherits from this Mixin.

    .. versionadded:: 1.3
    """
    def __init_subclass__(cls, **kwargs) -> None:
        """Set the ``set_{method}_request`` methods.

        This uses PEP-487 [1]_ to set the ``set_{method}_request`` methods. It
        looks for the information available in the set default values which are
        set using ``__metadata_request__*`` class attributes, or inferred
        from method signatures.

        The ``__metadata_request__*`` class attributes are used when a method
        does not explicitly accept a metadata through its arguments or if the
        developer would like to specify a request value for those metadata
        which are different from the default ``None``.

        References
        ----------
        .. [1] https://www.python.org/dev/peps/pep-0487
        """
    def get_metadata_routing(self):
        """Get metadata routing of this object.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        Returns
        -------
        routing : MetadataRequest
            A :class:`~utils.metadata_routing.MetadataRequest` encapsulating
            routing information.
        """

def process_routing(obj, method, other_params, **kwargs):
    '''Validate and route input parameters.

    This function is used inside a router\'s method, e.g. :term:`fit`,
    to validate the metadata and handle the routing.

    Assuming this signature: ``fit(self, X, y, sample_weight=None, **fit_params)``,
    a call to this function would be:
    ``process_routing(self, fit_params, sample_weight=sample_weight)``.

    .. versionadded:: 1.3

    Parameters
    ----------
    obj : object
        An object implementing ``get_metadata_routing``. Typically a
        meta-estimator.

    method : str
        The name of the router\'s method in which this function is called.

    other_params : dict
        A dictionary of extra parameters passed to the router\'s method,
        e.g. ``**fit_params`` passed to a meta-estimator\'s :term:`fit`.

    **kwargs : dict
        Parameters explicitly accepted and included in the router\'s method
        signature.

    Returns
    -------
    routed_params : Bunch
        A :class:`~utils.Bunch` of the form ``{"object_name": {"method_name":
        {prop: value}}}`` which can be used to pass the required metadata to
        corresponding methods or corresponding child objects. The object names
        are those defined in `obj.get_metadata_routing()`.
    '''
