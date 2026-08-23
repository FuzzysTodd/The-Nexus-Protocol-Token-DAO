from _typeshed import Incomplete

LOG: Incomplete

class EntryPointWrapper:
    """Wrap up a command class already imported to make it look like a plugin.
    """
    name: Incomplete
    command_class: Incomplete
    def __init__(self, name, command_class) -> None: ...
    def load(self, require: bool = False): ...

class CommandManager:
    """Discovers commands and handles lookup based on argv data.

    :param namespace: String containing the entrypoint namespace for the
        plugins to be loaded. For example, ``'cliff.formatter.list'``.
    :param convert_underscores: Whether cliff should convert underscores to
        spaces in entry_point commands.
    """
    commands: Incomplete
    namespace: Incomplete
    convert_underscores: Incomplete
    group_list: Incomplete
    def __init__(self, namespace, convert_underscores: bool = True) -> None: ...
    def load_commands(self, namespace) -> None:
        """Load all the commands from an entrypoint"""
    def __iter__(self): ...
    def add_command(self, name, command_class) -> None: ...
    def add_legacy_command(self, old_name, new_name) -> None:
        """Map an old command name to the new name.

        :param old_name: The old command name.
        :type old_name: str
        :param new_name: The new command name.
        :type new_name: str
        """
    def find_command(self, argv):
        """Given an argument list, find a command and
        return the processor and any remaining arguments.
        """
    def add_command_group(self, group: Incomplete | None = None) -> None:
        """Adds another group of command entrypoints"""
    def get_command_groups(self):
        """Returns a list of the loaded command groups"""
    def get_command_names(self, group: Incomplete | None = None):
        """Returns a list of commands loaded for the specified group"""
