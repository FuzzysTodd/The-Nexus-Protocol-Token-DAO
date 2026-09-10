import abc
from _typeshed import Incomplete

class Command(metaclass=abc.ABCMeta):
    """Base class for command plugins.

    When the command is instantiated, it loads extensions from a
    namespace based on the parent application namespace and the
    command name::

        app.namespace + '.' + cmd_name.replace(' ', '_')

    :param app: Application instance invoking the command.
    :paramtype app: cliff.app.App

    """
    deprecated: bool
    conflict_handler: str
    app: Incomplete
    app_args: Incomplete
    cmd_name: Incomplete
    def __init__(self, app, app_args, cmd_name: Incomplete | None = None) -> None: ...
    def get_description(self):
        """Return the command description.

        The default is to use the first line of the class' docstring
        as the description. Set the ``_description`` class attribute
        to a one-line description of a command to use a different
        value. This is useful for enabling translations, for example,
        with ``_description`` set to a string wrapped with a gettext
        translation marker.

        """
    def get_epilog(self):
        """Return the command epilog."""
    def get_parser(self, prog_name):
        """Return an :class:`argparse.ArgumentParser`.
        """
    @abc.abstractmethod
    def take_action(self, parsed_args):
        """Override to do something useful.

        The returned value will be returned by the program.
        """
    def run(self, parsed_args):
        """Invoked by the application when the command is run.

        Developers implementing commands should override
        :meth:`take_action`.

        Developers creating new command base classes (such as
        :class:`Lister` and :class:`ShowOne`) should override this
        method to wrap :meth:`take_action`.

        Return the value returned by :meth:`take_action` or 0.
        """
