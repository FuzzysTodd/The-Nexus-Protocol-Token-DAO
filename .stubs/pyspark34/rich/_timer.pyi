from typing import Generator

def timer(subject: str = 'time') -> Generator[None, None, None]:
    """print the elapsed time. (only used in debugging)"""
