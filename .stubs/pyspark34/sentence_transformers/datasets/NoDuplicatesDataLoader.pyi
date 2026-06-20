from _typeshed import Incomplete

class NoDuplicatesDataLoader:
    batch_size: Incomplete
    data_pointer: int
    collate_fn: Incomplete
    train_examples: Incomplete
    def __init__(self, train_examples, batch_size) -> None:
        """
        A special data loader to be used with MultipleNegativesRankingLoss.
        The data loader ensures that there are no duplicate sentences within the same batch
        """
    def __iter__(self): ...
    def __len__(self) -> int: ...
