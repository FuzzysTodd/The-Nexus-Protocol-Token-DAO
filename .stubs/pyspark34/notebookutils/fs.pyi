from typing import Any, Dict, List, Optional, Union

__all__ = [
    'help', 'cp', 'mv', 'ls', 'mkdirs', 'put', 'head', 'append', 'rm', 'exists',
    'mountToDriverNode', 'unmountFromDriverNode', 'mount', 'unmount', 'mounts',
    'refreshMounts', 'getMountPath', 'fastcp', 'nbResPath'
]

def help(method_name: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.fs module or the specified method.

    Examples:
    notebookutils.fs.help()
    notebookutils.fs.help("mount")
    :param method_name: The name of the method to get help with.
    """

def cp(src: str, dest: str, recurse: bool = False) -> bool:
    """
    Copy a file or directory.
    
    :param src: Source path
    :param dest: Destination path
    :param recurse: Whether to copy recursively
    :return: True if successful
    """

def mv(src: str, dest: str, create_path: bool = False, overwrite: bool = False) -> bool:
    """
    Move a file or directory.
    
    :param src: Source path
    :param dest: Destination path
    :param create_path: Whether to create the destination path
    :param overwrite: Whether to overwrite existing files
    :return: True if successful
    """

def ls(dir: str) -> List[Any]:
    """
    List files and directories.
    
    :param dir: Directory path to list
    :return: List of file/directory information
    """

def mkdirs(dir: str) -> bool:
    """
    Create directories.
    
    :param dir: Directory path to create
    :return: True if successful
    """

def put(file: str, content: str, overwrite: bool = False) -> bool:
    """
    Write content to a file.
    
    :param file: File path
    :param content: Content to write
    :param overwrite: Whether to overwrite existing file
    :return: True if successful
    """

def head(file: str, max_bytes: int = 102400) -> str:
    """
    Read the beginning of a file.
    
    :param file: File path
    :param max_bytes: Maximum bytes to read
    :return: File content
    """

def append(file: str, content: str, createFileIfNotExists: bool = False) -> bool:
    """
    Append content to a file.
    
    :param file: File path
    :param content: Content to append
    :param createFileIfNotExists: Whether to create file if it doesn't exist
    :return: True if successful
    """

def rm(dir: str, recurse: bool = False) -> bool:
    """
    Remove a file or directory.
    
    :param dir: Path to remove
    :param recurse: Whether to remove recursively
    :return: True if successful
    """

def exists(file: str) -> bool:
    """
    Check if a file or directory exists.
    
    :param file: Path to check
    :return: True if exists
    """

def mountToDriverNode(source: str, mountPoint: str, extraConfigs: Dict[str, str] = {}) -> bool:
    """
    Mount a remote storage directory to the driver node.
    
    :param source: Source URI
    :param mountPoint: Mount point path
    :param extraConfigs: Additional configuration
    :return: True if successful
    """

def unmountFromDriverNode(mountPoint: str) -> bool:
    """
    Unmount from driver node.
    
    :param mountPoint: Mount point to unmount
    :return: True if successful
    """

def mount(source: str, mountPoint: str, extraConfigs: Dict[str, str] = {}) -> bool:
    """
    Mount a remote storage directory.
    
    :param source: Source URI
    :param mountPoint: Mount point path
    :param extraConfigs: Additional configuration
    :return: True if successful
    """

def unmount(mountPoint: str, extraOptions: Dict[str, Any] = {}) -> bool:
    """
    Unmount a mount point.
    
    :param mountPoint: Mount point to unmount
    :param extraOptions: Additional options
    :return: True if successful
    """

def mounts(extraOptions: Dict[str, Any] = {}) -> List[Any]:
    """
    List all mount points.
    
    :param extraOptions: Additional options
    :return: List of mount information
    """

def refreshMounts() -> bool:
    """
    Refresh mount information.
    
    :return: True if successful
    """

def getMountPath(mountPoint: str, scope: str = "") -> str:
    """
    Get the actual path for a mount point.
    
    :param mountPoint: Mount point
    :param scope: Scope parameter
    :return: Actual path
    """

def fastcp(src: str, dest: str, recurse: bool = True, extraConfigs: Dict[str, str] = {}) -> bool:
    """
    Fast copy operation for large data transfers.
    
    :param src: Source path
    :param dest: Destination path
    :param recurse: Whether to copy recursively
    :param extraConfigs: Additional configuration
    :return: True if successful
    """

def nbResPath() -> str:
    """
    Get the notebook resource path.
    
    :return: Notebook resource path
    """
