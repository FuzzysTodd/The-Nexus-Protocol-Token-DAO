from torch.utils.benchmark import FuzzedParameter as FuzzedParameter, FuzzedSparseTensor as FuzzedSparseTensor, Fuzzer as Fuzzer, ParameterAlias as ParameterAlias

class UnaryOpSparseFuzzer(Fuzzer):
    def __init__(self, seed, dtype=..., cuda: bool = False) -> None: ...
