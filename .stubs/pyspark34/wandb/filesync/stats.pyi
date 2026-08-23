from typing import NamedTuple

class FileStats(NamedTuple):
    deduped: bool
    total: int
    uploaded: int
    failed: bool
    artifact_file: bool

class Summary(NamedTuple):
    uploaded_bytes: int
    total_bytes: int
    deduped_bytes: int

class FileCountsByCategory(NamedTuple):
    artifact: int
    wandb: int
    media: int
    other: int

class Stats:
    def __init__(self) -> None: ...
    def init_file(self, save_name: str, size: int, is_artifact_file: bool = False) -> None: ...
    def set_file_deduped(self, save_name: str) -> None: ...
    def update_uploaded_file(self, save_name: str, total_uploaded: int) -> None: ...
    def update_failed_file(self, save_name: str) -> None: ...
    def summary(self) -> Summary: ...
    def file_counts_by_category(self) -> FileCountsByCategory: ...
