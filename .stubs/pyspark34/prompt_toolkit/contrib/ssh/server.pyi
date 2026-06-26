import asyncssh
from _typeshed import Incomplete
from typing import Any, Awaitable, Callable

__all__ = ['PromptToolkitSSHSession', 'PromptToolkitSSHServer']

class PromptToolkitSSHSession(asyncssh.SSHServerSession):
    interact: Incomplete
    enable_cpr: Incomplete
    interact_task: Incomplete
    app_session: Incomplete
    stdout: Incomplete
    def __init__(self, interact: Callable[[PromptToolkitSSHSession], Awaitable[None]], *, enable_cpr: bool) -> None: ...
    def connection_made(self, chan: Any) -> None: ...
    def shell_requested(self) -> bool: ...
    def session_started(self) -> None: ...
    def terminal_size_changed(self, width: int, height: int, pixwidth: object, pixheight: object) -> None: ...
    def data_received(self, data: str, datatype: object) -> None: ...

class PromptToolkitSSHServer(asyncssh.SSHServer):
    '''
    Run a prompt_toolkit application over an asyncssh server.

    This takes one argument, an `interact` function, which is called for each
    connection. This should be an asynchronous function that runs the
    prompt_toolkit applications. This function runs in an `AppSession`, which
    means that we can have multiple UI interactions concurrently.

    Example usage:

    .. code:: python

        async def interact(ssh_session: PromptToolkitSSHSession) -> None:
            await yes_no_dialog("my title", "my text").run_async()

            prompt_session = PromptSession()
            text = await prompt_session.prompt_async("Type something: ")
            print_formatted_text(\'You said: \', text)

        server = PromptToolkitSSHServer(interact=interact)
        loop = get_running_loop()
        loop.run_until_complete(
            asyncssh.create_server(
                lambda: MySSHServer(interact),
                "",
                port,
                server_host_keys=["/etc/ssh/..."],
            )
        )
        loop.run_forever()

    :param enable_cpr: When `True`, the default, try to detect whether the SSH
        client runs in a terminal that responds to "cursor position requests".
        That way, we can properly determine how much space there is available
        for the UI (especially for drop down menus) to render.
    '''
    interact: Incomplete
    enable_cpr: Incomplete
    def __init__(self, interact: Callable[[PromptToolkitSSHSession], Awaitable[None]], *, enable_cpr: bool = True) -> None: ...
    def begin_auth(self, username: str) -> bool: ...
    def session_requested(self) -> PromptToolkitSSHSession: ...
