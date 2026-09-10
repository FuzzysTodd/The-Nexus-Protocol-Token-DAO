import logging

class LoggingHandler(logging.Handler):
    def __init__(self, level=...) -> None: ...
    def emit(self, record) -> None: ...

def install_logger(given_logger, level=..., fmt: str = '%(levelname)s:%(name)s:%(message)s') -> None:
    """ Configures the given logger; format, logging level, style, etc """
