from .command_utils import install_package_command as install_package_command
from .common_utils import print_error as print_error

def check_environment():
    """check if paramiko is installed"""
def copy_remote_directory_to_local(sftp, remote_path, local_path) -> None:
    """copy remote directory to local machine"""
def create_ssh_sftp_client(host_ip, port, username, password, ssh_key_path, passphrase):
    """create ssh client"""
def remove_remote_directory(sftp, directory) -> None:
    """remove a directory in remote machine"""
