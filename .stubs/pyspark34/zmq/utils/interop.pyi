from typing import Any

def cast_int_addr(n: Any) -> int:
    """Cast an address to a Python int

    This could be a Python integer or a CFFI pointer
    """
