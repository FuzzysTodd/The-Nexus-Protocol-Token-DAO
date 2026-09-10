from _typeshed import Incomplete
from pathlib import Path as Path
from torch import nn

class TorchModel(nn.Module):
    conv1: Incomplete
    conv2: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    fc3: Incomplete
    relu1: Incomplete
    relu2: Incomplete
    relu3: Incomplete
    relu4: Incomplete
    pool1: Incomplete
    pool2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

use_cuda: Incomplete
device: Incomplete
train_loader: Incomplete
test_loader: Incomplete

def trainer(model, optimizer, criterion) -> None: ...
def evaluator(model) -> None: ...
def test_trt(engine) -> None: ...
