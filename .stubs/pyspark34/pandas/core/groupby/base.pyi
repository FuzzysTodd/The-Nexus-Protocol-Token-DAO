import dataclasses
from _typeshed import Incomplete
from typing import Hashable

@dataclasses.dataclass(order=True, frozen=True)
class OutputKey:
    label: Hashable
    position: int
    def __init__(self, label, position) -> None: ...

plotting_methods: Incomplete
cythonized_kernels: Incomplete
reduction_kernels: Incomplete
transformation_kernels: Incomplete
groupby_other_methods: Incomplete
transform_kernel_allowlist: Incomplete
