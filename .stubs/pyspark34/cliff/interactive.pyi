import cmd2
from _typeshed import Incomplete

class InteractiveApp(cmd2.Cmd):
    '''Provides "interactive mode" features.

    Refer to the cmd2_ and cmd_ documentation for details
    about subclassing and configuring this class.

    .. _cmd2: https://cmd2.readthedocs.io/en/latest/
    .. _cmd: http://docs.python.org/library/cmd.html

    :param parent_app: The calling application (expected to be derived
                       from :class:`cliff.main.App`).
    :param command_manager: A :class:`cliff.commandmanager.CommandManager`
                            instance.
    :param stdin: Standard input stream
    :param stdout: Standard output stream
    '''
    use_rawinput: bool
    doc_header: str
    app_cmd_header: str
    parent_app: Incomplete
    prompt: Incomplete
    command_manager: Incomplete
    errexit: Incomplete
    def __init__(self, parent_app, command_manager, stdin, stdout, errexit: bool = False) -> None: ...
    def default(self, line): ...
    def completenames(self, text, line, begidx, endidx):
        """Tab-completion for command prefix without completer delimiter.

        This method returns cmd style and cliff style commands matching
        provided command prefix (text).
        """
    def completedefault(self, text, line, begidx, endidx):
        """Default tab-completion for command prefix with completer delimiter.

        This method filters only cliff style commands matching provided
        command prefix (line) as cmd2 style commands cannot contain spaces.
        This method returns text + missing command part of matching commands.
        This method does not handle options in cmd2/cliff style commands, you
        must define complete_$method to handle them.
        """
    def help_help(self) -> None: ...
    stdout: Incomplete
    def do_help(self, arg): ...
    do_exit: Incomplete
    def get_names(self): ...
    def precmd(self, statement):
        """Hook method executed just before the command is executed by
        :meth:`~cmd2.Cmd.onecmd` and after adding it to history.

        :param statement: subclass of str which also contains the parsed input
        :return: a potentially modified version of the input Statement object
        """
    def cmdloop(self): ...
