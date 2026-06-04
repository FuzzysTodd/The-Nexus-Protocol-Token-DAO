import abc
import typing
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['safe_patch', 'is_testing', 'exception_safe_function_for_class', 'picklable_exception_safe_function', 'ExceptionSafeClass', 'ExceptionSafeAbstractClass', 'PatchFunction', 'with_managed_run', 'update_wrapper_extended']

def exception_safe_function_for_class(function):
    """
    Wraps the specified function with broad exception handling to guard
    against unexpected errors during autologging.
    Note this function creates an unpicklable function as `safe_function` is locally defined,
    but a class instance containing methods decorated by this function should be pickalable,
    because pickle only saves instance attributes, not methods.
    See https://docs.python.org/3/library/pickle.html#pickling-class-instances for more details.
    """
def picklable_exception_safe_function(function):
    """
    Wraps the specified function with broad exception handling to guard
    against unexpected errors during autologging while preserving picklability.
    """

ExceptionSafeClass: Incomplete
ExceptionSafeAbstractClass: Incomplete

class PatchFunction(metaclass=abc.ABCMeta):
    '''
    Base class representing a function patch implementation with a callback for error handling.
    `PatchFunction` should be subclassed and used in conjunction with `safe_patch` to
    safely modify the implementation of a function. Subclasses of `PatchFunction` should
    use `_patch_implementation` to define modified ("patched") function implementations and
    `_on_exception` to define cleanup logic when `_patch_implementation` terminates due
    to an unhandled exception.
    '''
    @classmethod
    def call(cls, original, *args, **kwargs): ...
    def __call__(self, original, *args, **kwargs): ...

def with_managed_run(autologging_integration, patch_function, tags: Incomplete | None = None):
    """
    Given a `patch_function`, returns an `augmented_patch_function` that wraps the execution of
    `patch_function` with an active MLflow run. The following properties apply:

        - An MLflow run is only created if there is no active run present when the
          patch function is executed

        - If an active run is created by the `augmented_patch_function`, it is terminated
          with the `FINISHED` state at the end of function execution

        - If an active run is created by the `augmented_patch_function`, it is terminated
          with the `FAILED` if an unhandled exception is thrown during function execution

    Note that, if nested runs or non-fluent runs are created by `patch_function`, `patch_function`
    is responsible for terminating them by the time it terminates
    (or in the event of an exception).

    :param autologging_integration: The autologging integration associated
                                    with the `patch_function`.
    :param patch_function: A `PatchFunction` class definition or a function object
                           compatible with `safe_patch`.
    :param tags: A dictionary of string tags to set on each managed run created during the
                 execution of `patch_function`.
    """
def is_testing():
    '''
    Indicates whether or not autologging functionality is running in test mode (as determined
    by the `MLFLOW_AUTOLOGGING_TESTING` environment variable). Test mode performs additional
    validation during autologging, including:

        - Checks for the exception safety of arguments passed to model training functions
          (i.e. all additional arguments should be "exception safe" functions or classes)
        - Disables exception handling for patched function logic, ensuring that patch code
          executes without errors during testing
    '''
def safe_patch(autologging_integration, destination, function_name, patch_function, manage_run: bool = False, extra_tags: Incomplete | None = None):
    """
    Patches the specified `function_name` on the specified `destination` class for autologging
    purposes, preceding its implementation with an error-safe copy of the specified patch
    `patch_function` with the following error handling behavior:
        - Exceptions thrown from the underlying / original function
          (`<destination>.<function_name>`) are propagated to the caller.
        - Exceptions thrown from other parts of the patched implementation (`patch_function`)
          are caught and logged as warnings.
    :param autologging_integration: The name of the autologging integration associated with the
                                    patch.
    :param destination: The Python class on which the patch is being defined.
    :param function_name: The name of the function to patch on the specified `destination` class.
    :param patch_function: The patched function code to apply. This is either a `PatchFunction`
                           class definition or a function object. If it is a function object, the
                           first argument should be reserved for an `original` method argument
                           representing the underlying / original function. Subsequent arguments
                           should be identical to those of the original function being patched.
    :param manage_run: If `True`, applies the `with_managed_run` wrapper to the specified
                       `patch_function`, which automatically creates & terminates an MLflow
                       active run during patch code execution if necessary. If `False`,
                       does not apply the `with_managed_run` wrapper to the specified
                       `patch_function`.
    :param extra_tags: A dictionary of extra tags to set on each managed run created by autologging.
    """

class AutologgingSession:
    integration: Incomplete
    id: Incomplete
    state: str
    def __init__(self, integration, id_) -> None: ...

class _AutologgingSessionManager:
    @classmethod
    def start_session(cls, integration) -> Generator[Incomplete, None, None]: ...
    @classmethod
    def active_session(cls): ...

def update_wrapper_extended(wrapper, wrapped):
    """
    Update a `wrapper` function to look like the `wrapped` function. This is an extension of
    `functools.update_wrapper` that applies the docstring *and* signature of `wrapped` to
    `wrapper`, producing a new function.

    :return: A new function with the same implementation as `wrapper` and the same docstring
             & signature as `wrapped`.
    """

class ValidationExemptArgument(typing.NamedTuple):
    """
    A NamedTuple representing the properties of an argument that is exempt from validation

    autologging_integration: The name of the autologging integration.
    function_name: The name of the function that is being validated.
    type_function: A Callable that accepts an object and returns True if the given object matches
                   the argument type. Returns False otherwise.
    positional_argument_index: The index of the argument in the function signature.
    keyword_argument_name: The name of the argument in the function signature.
    """
    autologging_integration: str
    function_name: str
    type_function: typing.Callable
    positional_argument_index: int = ...
    keyword_argument_name: str = ...
    def matches(self, autologging_integration, function_name, value, argument_index: Incomplete | None = None, argument_name: Incomplete | None = None):
        """
        This method checks if the properties provided through the function arguments matches the
        properties defined in the NamedTuple.

        :param autologging_integration: The name of an autologging integration.
        :param function_name: The name of the function that is being matched.
        :param value: The value of the argument.
        :param argument_index: The index of the argument, if it is passed as a positional
                                          argument. Otherwise it is None.
        :param argument_name: The name of the argument, if it is passed as a keyword
                                      argument. Otherwise it is None.
        :return: Returns True if the given function properties matches the exempt argument's
                 properties. Returns False otherwise.
        """
