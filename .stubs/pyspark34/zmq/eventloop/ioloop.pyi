from tornado.ioloop import *
from tornado.ioloop import IOLoop

ZMQIOLoop = IOLoop

def install() -> None:
    """DEPRECATED

    pyzmq 17 no longer needs any special integration for tornado.
    """
