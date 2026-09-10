from torch.utils.data.datapipes.datapipe import DataChunk

__all__ = ['DataChunkDF']

class DataChunkDF(DataChunk):
    """
        DataChunkDF iterating over individual items inside of DataFrame containers,
        to access DataFrames user `raw_iterator`
    """
    def __iter__(self): ...
    def __len__(self) -> int: ...
