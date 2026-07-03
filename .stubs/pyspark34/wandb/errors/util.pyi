from . import AuthenticationError as AuthenticationError, CommError as CommError, Error as Error, UnsupportedError as UnsupportedError, UsageError as UsageError
from _typeshed import Incomplete
from wandb.proto import wandb_internal_pb2 as pb

to_exception_map: Incomplete
from_exception_map: Incomplete

class ProtobufErrorHandler:
    """Converts protobuf errors to exceptions and vice versa."""
    @staticmethod
    def to_exception(error: pb.ErrorInfo) -> Error | None:
        """Convert a protobuf error to an exception.

        Args:
            error: The protobuf error to convert.

        Returns:
            The corresponding exception.

        """
    @classmethod
    def from_exception(cls, exc: Error) -> pb.ErrorInfo:
        """Convert an wandb error to a protobuf error message.

        Args:
            exc: The exception to convert.

        Returns:
            The corresponding protobuf error message.
        """
