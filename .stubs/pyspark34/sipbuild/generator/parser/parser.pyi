from .parser_manager import ParserManager as ParserManager

def parse(sip_file, hex_version, encoding, abi_version, tags, disabled_features, protected_is_public, include_dirs, sip_module, is_strict: bool = True):
    """ Parse a .sip file and return a 3-tuple of a Specification object, a
    list of Module objects and a list of the .sip files that specify the module
    to be generated.  A UserException is raised if there was an error.
    """
