from .util import PtyProcessError as PtyProcessError, which as which
from _typeshed import Incomplete

use_native_pty_fork: bool
PY3: Incomplete

class PtyProcess:
    """This class represents a process running in a pseudoterminal.
    
    The main constructor is the :meth:`spawn` classmethod.
    """
    string_type = bytes
    linesep: Incomplete
    crlf: Incomplete
    @staticmethod
    def write_to_stdout(b): ...
    encoding: Incomplete
    argv: Incomplete
    env: Incomplete
    launch_dir: Incomplete
    pid: Incomplete
    fd: Incomplete
    fileobj: Incomplete
    terminated: bool
    closed: bool
    exitstatus: Incomplete
    signalstatus: Incomplete
    status: Incomplete
    flag_eof: bool
    delayafterclose: float
    delayafterterminate: float
    def __init__(self, pid, fd) -> None: ...
    @classmethod
    def spawn(cls, argv, cwd: Incomplete | None = None, env: Incomplete | None = None, echo: bool = True, preexec_fn: Incomplete | None = None, dimensions=(24, 80), pass_fds=()):
        """Start the given command in a child process in a pseudo terminal.

        This does all the fork/exec type of stuff for a pty, and returns an
        instance of PtyProcess.

        If preexec_fn is supplied, it will be called with no arguments in the
        child process before exec-ing the specified command.
        It may, for instance, set signal handlers to SIG_DFL or SIG_IGN.

        Dimensions of the psuedoterminal used for the subprocess can be
        specified as a tuple (rows, cols), or the default (24, 80) will be used.

        By default, all file descriptors except 0, 1 and 2 are closed. This
        behavior can be overridden with pass_fds, a list of file descriptors to
        keep open between the parent and the child.
        """
    def __del__(self) -> None:
        """This makes sure that no system resources are left open. Python only
        garbage collects Python objects. OS file descriptors are not Python
        objects, so they must be handled explicitly. If the child file
        descriptor was opened outside of this class (passed to the constructor)
        then this does not close it. """
    def fileno(self):
        """This returns the file descriptor of the pty for the child.
        """
    def close(self, force: bool = True) -> None:
        """This closes the connection with the child application. Note that
        calling close() more than once is valid. This emulates standard Python
        behavior with files. Set force to True if you want to make sure that
        the child is terminated (SIGKILL is sent if the child ignores SIGHUP
        and SIGINT). """
    def flush(self) -> None:
        """This does nothing. It is here to support the interface for a
        File-like object. """
    def isatty(self):
        """This returns True if the file descriptor is open and connected to a
        tty(-like) device, else False.

        On SVR4-style platforms implementing streams, such as SunOS and HP-UX,
        the child pty may not appear as a terminal device.  This means
        methods such as setecho(), setwinsize(), getwinsize() may raise an
        IOError. """
    def waitnoecho(self, timeout: Incomplete | None = None):
        '''This waits until the terminal ECHO flag is set False. This returns
        True if the echo mode is off. This returns False if the ECHO flag was
        not set False before the timeout. This can be used to detect when the
        child is waiting for a password. Usually a child application will turn
        off echo mode when it is waiting for the user to enter a password. For
        example, instead of expecting the "password:" prompt you can wait for
        the child to set ECHO off::

            p = pexpect.spawn(\'ssh user@example.com\')
            p.waitnoecho()
            p.sendline(mypassword)

        If timeout==None then this method to block until ECHO flag is False.
        '''
    echo: Incomplete
    def getecho(self):
        """This returns the terminal echo mode. This returns True if echo is
        on or False if echo is off. Child applications that are expecting you
        to enter a password often set ECHO False. See waitnoecho().

        Not supported on platforms where ``isatty()`` returns False.  """
    def setecho(self, state) -> None:
        """This sets the terminal echo mode on or off. Note that anything the
        child sent before the echo will be lost, so you should be sure that
        your input buffer is empty before you call setecho(). For example, the
        following will work as expected::

            p = pexpect.spawn('cat') # Echo is on by default.
            p.sendline('1234') # We expect see this twice from the child...
            p.expect(['1234']) # ... once from the tty echo...
            p.expect(['1234']) # ... and again from cat itself.
            p.setecho(False) # Turn off tty echo
            p.sendline('abcd') # We will set this only once (echoed by cat).
            p.sendline('wxyz') # We will set this only once (echoed by cat)
            p.expect(['abcd'])
            p.expect(['wxyz'])

        The following WILL NOT WORK because the lines sent before the setecho
        will be lost::

            p = pexpect.spawn('cat')
            p.sendline('1234')
            p.setecho(False) # Turn off tty echo
            p.sendline('abcd') # We will set this only once (echoed by cat).
            p.sendline('wxyz') # We will set this only once (echoed by cat)
            p.expect(['1234'])
            p.expect(['1234'])
            p.expect(['abcd'])
            p.expect(['wxyz'])


        Not supported on platforms where ``isatty()`` returns False.
        """
    def read(self, size: int = 1024):
        """Read and return at most ``size`` bytes from the pty.

        Can block if there is nothing to read. Raises :exc:`EOFError` if the
        terminal was closed.
        
        Unlike Pexpect's ``read_nonblocking`` method, this doesn't try to deal
        with the vagaries of EOF on platforms that do strange things, like IRIX
        or older Solaris systems. It handles the errno=EIO pattern used on
        Linux, and the empty-string return used on BSD platforms and (seemingly)
        on recent Solaris.
        """
    def readline(self):
        """Read one line from the pseudoterminal, and return it as unicode.

        Can block if there is nothing to read. Raises :exc:`EOFError` if the
        terminal was closed.
        """
    def write(self, s, flush: bool = True):
        """Write bytes to the pseudoterminal.
        
        Returns the number of bytes written.
        """
    def sendcontrol(self, char):
        """Helper method that wraps send() with mnemonic access for sending control
        character to the child (such as Ctrl-C or Ctrl-D).  For example, to send
        Ctrl-G (ASCII 7, bell, '\x07')::

            child.sendcontrol('g')

        See also, sendintr() and sendeof().
        """
    def sendeof(self):
        """This sends an EOF to the child. This sends a character which causes
        the pending parent output buffer to be sent to the waiting child
        program without waiting for end-of-line. If it is the first character
        of the line, the read() in the user program returns 0, which signifies
        end-of-file. This means to work as expected a sendeof() has to be
        called at the beginning of a line. This method does not send a newline.
        It is the responsibility of the caller to ensure the eof is sent at the
        beginning of a line. """
    def sendintr(self):
        """This sends a SIGINT to the child. It does not require
        the SIGINT to be the first character on a line. """
    def eof(self):
        """This returns True if the EOF exception was ever raised.
        """
    def terminate(self, force: bool = False):
        '''This forces a child process to terminate. It starts nicely with
        SIGHUP and SIGINT. If "force" is True then moves onto SIGKILL. This
        returns True if the child was terminated. This returns False if the
        child could not be terminated. '''
    def wait(self):
        """This waits until the child exits. This is a blocking call. This will
        not read any data from the child, so this will block forever if the
        child has unread output and has terminated. In other words, the child
        may have printed output then called exit(), but, the child is
        technically still alive until its output is read by the parent. """
    def isalive(self):
        """This tests if the child process is running or not. This is
        non-blocking. If the child was terminated then this will read the
        exitstatus or signalstatus of the child. This returns True if the child
        process appears to be running or False if not. It can take literally
        SECONDS for Solaris to return the right status. """
    def kill(self, sig) -> None:
        """Send the given signal to the child application.

        In keeping with UNIX tradition it has a misleading name. It does not
        necessarily kill the child unless you send the right signal. See the
        :mod:`signal` module for constants representing signal numbers.
        """
    def getwinsize(self):
        """Return the window size of the pseudoterminal as a tuple (rows, cols).
        """
    def setwinsize(self, rows, cols):
        """Set the terminal window size of the child tty.

        This will cause a SIGWINCH signal to be sent to the child. This does not
        change the physical window size. It changes the size reported to
        TTY-aware applications like vi or curses -- applications that respond to
        the SIGWINCH signal.
        """

class PtyProcessUnicode(PtyProcess):
    """Unicode wrapper around a process running in a pseudoterminal.

    This class exposes a similar interface to :class:`PtyProcess`, but its read
    methods return unicode, and its :meth:`write` accepts unicode.
    """
    string_type = str
    encoding: Incomplete
    codec_errors: Incomplete
    decoder: Incomplete
    def __init__(self, pid, fd, encoding: str = 'utf-8', codec_errors: str = 'strict') -> None: ...
    def read(self, size: int = 1024):
        """Read at most ``size`` bytes from the pty, return them as unicode.

        Can block if there is nothing to read. Raises :exc:`EOFError` if the
        terminal was closed.

        The size argument still refers to bytes, not unicode code points.
        """
    def readline(self):
        """Read one line from the pseudoterminal, and return it as unicode.

        Can block if there is nothing to read. Raises :exc:`EOFError` if the
        terminal was closed.
        """
    def write(self, s):
        """Write the unicode string ``s`` to the pseudoterminal.

        Returns the number of bytes written.
        """
