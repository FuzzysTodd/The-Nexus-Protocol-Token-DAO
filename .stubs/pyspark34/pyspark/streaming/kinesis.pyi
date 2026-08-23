from _typeshed import Incomplete
from pyspark.storagelevel import StorageLevel
from pyspark.streaming import DStream
from pyspark.streaming.context import StreamingContext
from typing import Callable, TypeVar, overload

__all__ = ['KinesisUtils', 'InitialPositionInStream', 'MetricsLevel', 'utf8_decoder']

class InitialPositionInStream:
    LATEST: Incomplete
    TRIM_HORIZON: Incomplete

class MetricsLevel:
    DETAILED: Incomplete
    SUMMARY: Incomplete
    NONE: Incomplete
T = TypeVar('T')

def utf8_decoder(s: bytes | None) -> str | None:
    """Decode the unicode as UTF-8"""

class KinesisUtils:
    @staticmethod
    @overload
    def createStream(ssc: StreamingContext, kinesisAppName: str, streamName: str, endpointUrl: str, regionName: str, initialPositionInStream: str, checkpointInterval: int, metricsLevel: int = ..., storageLevel: StorageLevel = ..., awsAccessKeyId: str | None = ..., awsSecretKey: str | None = ..., *, stsAssumeRoleArn: str | None = ..., stsSessionName: str | None = ..., stsExternalId: str | None = ...) -> DStream[str | None]: ...
    @staticmethod
    @overload
    def createStream(ssc: StreamingContext, kinesisAppName: str, streamName: str, endpointUrl: str, regionName: str, initialPositionInStream: str, checkpointInterval: int, metricsLevel: int = ..., storageLevel: StorageLevel = ..., awsAccessKeyId: str | None = ..., awsSecretKey: str | None = ..., decoder: Callable[[bytes | None], T] = ..., stsAssumeRoleArn: str | None = ..., stsSessionName: str | None = ..., stsExternalId: str | None = ...) -> DStream[T]: ...
