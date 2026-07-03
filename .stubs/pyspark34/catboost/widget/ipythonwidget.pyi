from _typeshed import Incomplete
from ipywidgets import DOMWidget

class MetricWidget(DOMWidget):
    data: Incomplete

class MetricVisualizer(MetricWidget):
    def __init__(self, train_dirs, subdirs: bool = False) -> None: ...
    def start(self) -> None: ...
