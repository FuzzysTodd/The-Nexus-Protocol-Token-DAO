def BuildMessageAndEnumDescriptors(file_des, module) -> None:
    """Builds message and enum descriptors.

  Args:
    file_des: FileDescriptor of the .proto file
    module: Generated _pb2 module
  """
def BuildTopDescriptorsAndMessages(file_des, module_name, module):
    """Builds top level descriptors and message classes.

  Args:
    file_des: FileDescriptor of the .proto file
    module_name: str, the name of generated _pb2 module
    module: Generated _pb2 module
  """
def BuildServices(file_des, module_name, module) -> None:
    """Builds services classes and services stub class.

  Args:
    file_des: FileDescriptor of the .proto file
    module_name: str, the name of generated _pb2 module
    module: Generated _pb2 module
  """
