from torch.utils.benchmark import FuzzedParameter as FuzzedParameter, FuzzedTensor as FuzzedTensor, Fuzzer as Fuzzer, ParameterAlias as ParameterAlias

class UnaryOpFuzzer(Fuzzer):
    def __init__(self, seed, dtype=..., cuda: bool = False) -> None: ...
