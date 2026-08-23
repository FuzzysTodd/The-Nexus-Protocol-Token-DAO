from ..exceptions import UserException as UserException

def get_module_source_dir(abi_major_version):
    """ Return the name of the directory containing the latest source of the
    sip module that implements the given ABI version.
    """
def get_sip_module_version(abi_major_version):
    """ Return the version number of the latest implementation of the sip
    module with the given ABI as a string.
    """
def resolve_abi_version(abi_version, module: bool = True):
    """ Return a valid ABI version or the latest if none was given. """
