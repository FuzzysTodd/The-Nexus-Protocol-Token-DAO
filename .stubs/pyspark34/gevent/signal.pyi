from _typeshed import Incomplete
from gevent._util import copy_globals as copy_globals

__implements__: Incomplete
__extensions__: Incomplete

def getsignal(signalnum):
    """
    Exactly the same as :func:`signal.getsignal` except where
    :const:`signal.SIGCHLD` is concerned.

    For :const:`signal.SIGCHLD`, this cooperates with :func:`signal`
    to provide consistent answers.
    """
def signal(signalnum, handler):
    """
    Exactly the same as :func:`signal.signal` except where
    :const:`signal.SIGCHLD` is concerned.

    .. note::

       A :const:`signal.SIGCHLD` handler installed with this function
       will only be triggered for children that are forked using
       :func:`gevent.os.fork` (:func:`gevent.os.fork_and_watch`);
       children forked before monkey patching, or otherwise by the raw
       :func:`os.fork`, will not trigger the handler installed by this
       function. (It's unlikely that a SIGCHLD handler installed with
       the builtin :func:`signal.signal` would be triggered either;
       libev typically overwrites such a handler at the C level. At
       the very least, it's full of race conditions.)

    .. note::

        Use of ``SIG_IGN`` and ``SIG_DFL`` may also have race conditions
        with libev child watchers and the :mod:`gevent.subprocess` module.

    .. versionchanged:: 1.2a1
         If ``SIG_IGN`` or ``SIG_DFL`` are used to ignore ``SIGCHLD``, a
         future use of ``gevent.subprocess`` and libev child watchers
         will once again work. However, on Python 2, use of ``os.popen``
         will fail.

    .. versionchanged:: 1.1rc2
         Allow using ``SIG_IGN`` and ``SIG_DFL`` to reset and ignore ``SIGCHLD``.
         However, this allows the possibility of a race condition if ``gevent.subprocess``
         had already been used.
    """

__imports__: Incomplete
