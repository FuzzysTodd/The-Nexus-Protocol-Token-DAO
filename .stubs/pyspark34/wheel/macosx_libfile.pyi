from _typeshed import Incomplete

FAT_MAGIC: int
FAT_CIGAM: int
FAT_MAGIC_64: int
FAT_CIGAM_64: int
MH_MAGIC: int
MH_CIGAM: int
MH_MAGIC_64: int
MH_CIGAM_64: int
LC_VERSION_MIN_MACOSX: int
LC_BUILD_VERSION: int
CPU_TYPE_ARM64: int
mach_header_fields: Incomplete
mach_header_fields_64: Incomplete
fat_header_fields: Incomplete
fat_arch_fields: Incomplete
fat_arch_64_fields: Incomplete
segment_base_fields: Incomplete
segment_command_fields: Incomplete
segment_command_fields_64: Incomplete
version_min_command_fields: Incomplete
build_version_command_fields: Incomplete

def swap32(x): ...
def get_base_class_and_magic_number(lib_file, seek: Incomplete | None = None): ...
def read_data(struct_class, lib_file): ...
def extract_macosx_min_system_version(path_to_lib): ...
def read_mach_header(lib_file, seek: Incomplete | None = None):
    """
    This funcition parse mach-O header and extract
    information about minimal system version

    :param lib_file: reference to opened library file with pointer
    """
def parse_version(version): ...
def calculate_macosx_platform_tag(archive_root, platform_tag):
    """
    Calculate proper macosx platform tag basing on files which are included to wheel

    Example platform tag `macosx-10.14-x86_64`
    """
