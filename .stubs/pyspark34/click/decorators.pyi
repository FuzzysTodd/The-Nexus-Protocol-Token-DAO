import typing as t
import typing_extensions as te
from .core import Argument as Argument, Command as Command, Context as Context, Group as Group, Option as Option, Parameter as Parameter
from .globals import get_current_context as get_current_context
from .utils import echo as echo

P = te.ParamSpec('P')
R = t.TypeVar('R')
T = t.TypeVar('T')
FC = t.TypeVar('FC', bound=_AnyCallable | Command)

def pass_context(f: t.Callable[te.Concatenate[Context, P], R]) -> t.Callable[P, R]:
    """Marks a callback as wanting to receive the current context
    object as first argument.
    """
def pass_obj(f: t.Callable[te.Concatenate[t.Any, P], R]) -> t.Callable[P, R]:
    """Similar to :func:`pass_context`, but only pass the object on the
    context onwards (:attr:`Context.obj`).  This is useful if that object
    represents the state of a nested system.
    """
def make_pass_decorator(object_type: t.Type[T], ensure: bool = False) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], 't.Callable[P, R]']:
    """Given an object type this creates a decorator that will work
    similar to :func:`pass_obj` but instead of passing the object of the
    current context, it will find the innermost context of type
    :func:`object_type`.

    This generates a decorator that works roughly like this::

        from functools import update_wrapper

        def decorator(f):
            @pass_context
            def new_func(ctx, *args, **kwargs):
                obj = ctx.find_object(object_type)
                return ctx.invoke(f, obj, *args, **kwargs)
            return update_wrapper(new_func, f)
        return decorator

    :param object_type: the type of the object to pass.
    :param ensure: if set to `True`, a new object will be created and
                   remembered on the context if it's not there yet.
    """
def pass_meta_key(key: str, *, doc_description: str | None = None) -> t.Callable[[t.Callable[te.Concatenate[t.Any, P], R]], t.Callable[P, R]]:
    '''Create a decorator that passes a key from
    :attr:`click.Context.meta` as the first argument to the decorated
    function.

    :param key: Key in ``Context.meta`` to pass.
    :param doc_description: Description of the object being passed,
        inserted into the decorator\'s docstring. Defaults to "the \'key\'
        key from Context.meta".

    .. versionadded:: 8.0
    '''
CmdType = t.TypeVar('CmdType', bound=Command)

@t.overload
def command(name: _AnyCallable) -> Command: ...
@t.overload
def command(name: str | None, cls: t.Type[CmdType], **attrs: t.Any) -> t.Callable[[_AnyCallable], CmdType]: ...
@t.overload
def command(name: None = None, *, cls: t.Type[CmdType], **attrs: t.Any) -> t.Callable[[_AnyCallable], CmdType]: ...
@t.overload
def command(name: str | None = ..., cls: None = None, **attrs: t.Any) -> t.Callable[[_AnyCallable], Command]: ...
GrpType = t.TypeVar('GrpType', bound=Group)

@t.overload
def group(name: _AnyCallable) -> Group: ...
@t.overload
def group(name: str | None, cls: t.Type[GrpType], **attrs: t.Any) -> t.Callable[[_AnyCallable], GrpType]: ...
@t.overload
def group(name: None = None, *, cls: t.Type[GrpType], **attrs: t.Any) -> t.Callable[[_AnyCallable], GrpType]: ...
@t.overload
def group(name: str | None = ..., cls: None = None, **attrs: t.Any) -> t.Callable[[_AnyCallable], Group]: ...
def argument(*param_decls: str, cls: t.Type[Argument] | None = None, **attrs: t.Any) -> t.Callable[[FC], FC]:
    """Attaches an argument to the command.  All positional arguments are
    passed as parameter declarations to :class:`Argument`; all keyword
    arguments are forwarded unchanged (except ``cls``).
    This is equivalent to creating an :class:`Argument` instance manually
    and attaching it to the :attr:`Command.params` list.

    For the default argument class, refer to :class:`Argument` and
    :class:`Parameter` for descriptions of parameters.

    :param cls: the argument class to instantiate.  This defaults to
                :class:`Argument`.
    :param param_decls: Passed as positional arguments to the constructor of
        ``cls``.
    :param attrs: Passed as keyword arguments to the constructor of ``cls``.
    """
def option(*param_decls: str, cls: t.Type[Option] | None = None, **attrs: t.Any) -> t.Callable[[FC], FC]:
    """Attaches an option to the command.  All positional arguments are
    passed as parameter declarations to :class:`Option`; all keyword
    arguments are forwarded unchanged (except ``cls``).
    This is equivalent to creating an :class:`Option` instance manually
    and attaching it to the :attr:`Command.params` list.

    For the default option class, refer to :class:`Option` and
    :class:`Parameter` for descriptions of parameters.

    :param cls: the option class to instantiate.  This defaults to
                :class:`Option`.
    :param param_decls: Passed as positional arguments to the constructor of
        ``cls``.
    :param attrs: Passed as keyword arguments to the constructor of ``cls``.
    """
def confirmation_option(*param_decls: str, **kwargs: t.Any) -> t.Callable[[FC], FC]:
    '''Add a ``--yes`` option which shows a prompt before continuing if
    not passed. If the prompt is declined, the program will exit.

    :param param_decls: One or more option names. Defaults to the single
        value ``"--yes"``.
    :param kwargs: Extra arguments are passed to :func:`option`.
    '''
def password_option(*param_decls: str, **kwargs: t.Any) -> t.Callable[[FC], FC]:
    '''Add a ``--password`` option which prompts for a password, hiding
    input and asking to enter the value again for confirmation.

    :param param_decls: One or more option names. Defaults to the single
        value ``"--password"``.
    :param kwargs: Extra arguments are passed to :func:`option`.
    '''
def version_option(version: str | None = None, *param_decls: str, package_name: str | None = None, prog_name: str | None = None, message: str | None = None, **kwargs: t.Any) -> t.Callable[[FC], FC]:
    '''Add a ``--version`` option which immediately prints the version
    number and exits the program.

    If ``version`` is not provided, Click will try to detect it using
    :func:`importlib.metadata.version` to get the version for the
    ``package_name``. On Python < 3.8, the ``importlib_metadata``
    backport must be installed.

    If ``package_name`` is not provided, Click will try to detect it by
    inspecting the stack frames. This will be used to detect the
    version, so it must match the name of the installed package.

    :param version: The version number to show. If not provided, Click
        will try to detect it.
    :param param_decls: One or more option names. Defaults to the single
        value ``"--version"``.
    :param package_name: The package name to detect the version from. If
        not provided, Click will try to detect it.
    :param prog_name: The name of the CLI to show in the message. If not
        provided, it will be detected from the command.
    :param message: The message to show. The values ``%(prog)s``,
        ``%(package)s``, and ``%(version)s`` are available. Defaults to
        ``"%(prog)s, version %(version)s"``.
    :param kwargs: Extra arguments are passed to :func:`option`.
    :raise RuntimeError: ``version`` could not be detected.

    .. versionchanged:: 8.0
        Add the ``package_name`` parameter, and the ``%(package)s``
        value for messages.

    .. versionchanged:: 8.0
        Use :mod:`importlib.metadata` instead of ``pkg_resources``. The
        version is detected based on the package name, not the entry
        point name. The Python package name must match the installed
        package name, or be passed with ``package_name=``.
    '''
def help_option(*param_decls: str, **kwargs: t.Any) -> t.Callable[[FC], FC]:
    '''Add a ``--help`` option which immediately prints the help page
    and exits the program.

    This is usually unnecessary, as the ``--help`` option is added to
    each command automatically unless ``add_help_option=False`` is
    passed.

    :param param_decls: One or more option names. Defaults to the single
        value ``"--help"``.
    :param kwargs: Extra arguments are passed to :func:`option`.
    '''
