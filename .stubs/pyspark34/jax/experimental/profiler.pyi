from jax._src.lib import xla_client as xla_client

def get_profiled_instructions_proto(tensorboard_dir: str) -> bytes:
    """Gets the serialized profiled instructions proto from profile.

  Restore the xplane from the tensorboard dir and convert it to profiled
  [ProfiledInstructionsProto](https://github.com/openxla/xla/blob/main/third_party/tsl/tsl/profiler/protobuf/profiled_instructions.proto).
  The result is non-empty only when running on Nvidia GPU.

  Args:
    tensorboard_dir: The directory contains the profile trace, it is in the
      format of `<tb's log_dir>/plugin/profile/<run_dir>/`.

  Returns:
    Serialized
    [ProfiledInstructionsProto](https://github.com/openxla/xla/blob/main/third_party/tsl/tsl/profiler/protobuf/profiled_instructions.proto).
  """
