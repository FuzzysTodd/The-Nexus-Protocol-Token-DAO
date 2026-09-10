import pathlib
from _typeshed import Incomplete

def generate_deprecated_class_definition() -> None:
    """
    Generate a class definition listing the deprecated features.
    This is to allow static checks to ensure that proper field names are used.
    """
def get_pip_package_version(package_name: str) -> str: ...
def get_min_required_version(requirements_file_name: str, package_name: str) -> str: ...

package: str
package_version: Incomplete
requirements_file: str
requirements_min_version: Incomplete
protobuf_version: Incomplete
proto_root: Incomplete
tmp_out: pathlib.Path
ret: Incomplete
