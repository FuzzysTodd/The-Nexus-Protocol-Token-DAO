from .exceptions import UserFileException as UserFileException, UserParseException as UserParseException
from .module import resolve_abi_version as resolve_abi_version
from .toml import toml_load as toml_load

def get_bindings_configuration(abi_major, sip_file, sip_include_dirs):
    """ Get the configuration of a set of bindings. """
