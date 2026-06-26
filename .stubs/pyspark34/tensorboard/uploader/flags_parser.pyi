from tensorboard.util import grpc_util as grpc_util

SUBCOMMAND_FLAG: str
SUBCOMMAND_KEY_UPLOAD: str
SUBCOMMAND_KEY_DELETE: str
SUBCOMMAND_KEY_LIST: str
SUBCOMMAND_KEY_EXPORT: str
SUBCOMMAND_KEY_UPDATE_METADATA: str
SUBCOMMAND_KEY_AUTH: str
AUTH_SUBCOMMAND_FLAG: str
AUTH_SUBCOMMAND_KEY_REVOKE: str
DEFAULT_ORIGIN: str

def define_flags(parser):
    """Configures flags on the provided argument parser.

    Integration point for `tensorboard.program`'s subcommand system.

    Args:
      parser: An `argparse.ArgumentParser` to be mutated.
    """
