from pip._vendor.packaging.tags import PythonVersion as PythonVersion, Tag as Tag, compatible_tags as compatible_tags, cpython_tags as cpython_tags, generic_tags as generic_tags, interpreter_name as interpreter_name, interpreter_version as interpreter_version, mac_platforms as mac_platforms
from typing import List, Tuple

def version_info_to_nodot(version_info: Tuple[int, ...]) -> str: ...
def get_supported(version: str | None = None, platforms: List[str] | None = None, impl: str | None = None, abis: List[str] | None = None) -> List[Tag]:
    '''Return a list of supported tags for each version specified in
    `versions`.

    :param version: a string version, of the form "33" or "32",
        or None. The version will be assumed to support our ABI.
    :param platform: specify a list of platforms you want valid
        tags for, or None. If None, use the local system platform.
    :param impl: specify the exact implementation you want valid
        tags for, or None. If None, use the local interpreter impl.
    :param abis: specify a list of abis you want valid
        tags for, or None. If None, use the local interpreter abi.
    '''
