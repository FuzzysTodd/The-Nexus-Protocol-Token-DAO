from ..version import SIP_VERSION as SIP_VERSION, SIP_VERSION_STR as SIP_VERSION_STR
from .abi_version import get_module_source_dir as get_module_source_dir, get_sip_module_version as get_sip_module_version, resolve_abi_version as resolve_abi_version

def module(sip_module, abi_version, project, sdist, setup_cfg, sip_h, sip_rst, target_dir) -> None:
    """ Create the various elements of a sip module. """
def copy_sip_h(abi_major_version, target_dir, sip_module: str = '', version_info: bool = True) -> None:
    """ Copy the sip.h file. """
def copy_sip_pyi(abi_major_version, target_dir) -> None:
    """ Copy the sip.pyi file. """
def copy_nonshared_sources(abi_major_version, target_dir):
    """ Copy the module sources as a non-shared module. """
