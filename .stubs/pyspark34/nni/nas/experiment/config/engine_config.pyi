from dataclasses import dataclass
from nni.experiment.config.base import ConfigBase
from typing import List

__all__ = ['ExecutionEngineConfig', 'BaseEngineConfig', 'OneshotEngineConfig', 'PyEngineConfig', 'CgoEngineConfig', 'BenchmarkEngineConfig']

@dataclass(init=False)
class ExecutionEngineConfig(ConfigBase):
    name: str

@dataclass(init=False)
class PyEngineConfig(ExecutionEngineConfig):
    name: str = ...

@dataclass(init=False)
class OneshotEngineConfig(ExecutionEngineConfig):
    name: str = ...

@dataclass(init=False)
class BaseEngineConfig(ExecutionEngineConfig):
    name: str = ...
    dummy_input: List[int] | None = ...

@dataclass(init=False)
class CgoEngineConfig(ExecutionEngineConfig):
    name: str = ...
    max_concurrency_cgo: int | None = ...
    batch_waiting_time: int | None = ...
    dummy_input: List[int] | None = ...

@dataclass(init=False)
class BenchmarkEngineConfig(ExecutionEngineConfig):
    name: str = ...
    benchmark: str | None = ...
