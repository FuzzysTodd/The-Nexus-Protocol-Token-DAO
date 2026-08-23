import pytorch_lightning as pl
import torch
import torch.nn as nn
from _typeshed import Incomplete
from flaml import tune as tune
from flaml.automl.data import add_time_idx_col as add_time_idx_col
from flaml.automl.logger import logger as logger, logger_formatter as logger_formatter
from flaml.automl.time_series.ts_data import TimeSeriesDataset as TimeSeriesDataset
from flaml.automl.time_series.ts_model import TimeSeriesEstimator as TimeSeriesEstimator
from torch.utils.data import TensorDataset as TensorDataset

class Chomp1d(nn.Module):
    chomp_size: Incomplete
    def __init__(self, chomp_size) -> None: ...
    def forward(self, x): ...

class TemporalBlock(nn.Module):
    conv1: Incomplete
    chomp1: Incomplete
    relu1: Incomplete
    dropout1: Incomplete
    conv2: Incomplete
    chomp2: Incomplete
    relu2: Incomplete
    dropout2: Incomplete
    net: Incomplete
    downsample: Incomplete
    relu: Incomplete
    def __init__(self, n_inputs, n_outputs, kernel_size, stride, dilation, padding, dropout: float = 0.2) -> None: ...
    def init_weights(self) -> None: ...
    def forward(self, x): ...

class TCNForecaster(nn.Module):
    network: Incomplete
    linear: Incomplete
    def __init__(self, input_feature_num, num_outputs, num_channels, kernel_size: int = 2, dropout: float = 0.2) -> None: ...
    def forward(self, x): ...

class TCNForecasterLightningModule(pl.LightningModule):
    model: Incomplete
    learning_rate: Incomplete
    loss_fn: Incomplete
    def __init__(self, model: TCNForecaster, learning_rate: float = 0.001) -> None: ...
    def forward(self, x): ...
    def step(self, batch, batch_idx): ...
    def training_step(self, batch, batch_idx): ...
    def validation_step(self, batch, batch_idx): ...
    def configure_optimizers(self): ...

class DataframeDataset(torch.utils.data.Dataset):
    data: Incomplete
    sequence_length: Incomplete
    labels: Incomplete
    is_train: Incomplete
    def __init__(self, dataframe, target_column, features_columns, sequence_length, train: bool = True) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...

class TCNEstimator(TimeSeriesEstimator):
    """The class for tuning TCN Forecaster"""
    @classmethod
    def search_space(cls, data, task, pred_horizon, **params): ...
    def __init__(self, task: str = 'ts_forecast', n_jobs: int = 1, **params) -> None: ...
    batch_size: Incomplete
    horizon: Incomplete
    feature_cols: Incomplete
    target_col: Incomplete
    def fit(self, X_train: TimeSeriesDataset, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...
    def predict(self, X): ...
