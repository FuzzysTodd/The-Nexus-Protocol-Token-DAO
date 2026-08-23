__version__: str

def get_include():
    """
    Returns a list of header include paths (for lxml itself, libxml2
    and libxslt) needed to compile C code against lxml if it was built
    with statically linked libraries.
    """
