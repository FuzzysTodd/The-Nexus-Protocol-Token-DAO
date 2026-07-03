from _typeshed import Incomplete
from nni.nas.benchmarks.utils import json_dumps as json_dumps
from peewee import Model

proxy: Incomplete

class Nb201TrialConfig(Model):
    """
    Trial config for NAS-Bench-201.

    Attributes
    ----------
    arch : dict
        A dict with keys ``0_1``, ``0_2``, ``0_3``, ``1_2``, ``1_3``, ``2_3``, each of which
        is an operator chosen from :const:`nni.nas.benchmark.nasbench201.NONE`,
        :const:`nni.nas.benchmark.nasbench201.SKIP_CONNECT`,
        :const:`nni.nas.benchmark.nasbench201.CONV_1X1`,
        :const:`nni.nas.benchmark.nasbench201.CONV_3X3` and :const:`nni.nas.benchmark.nasbench201.AVG_POOL_3X3`.
    num_epochs : int
        Number of epochs planned for this trial. Should be one of 12 and 200.
    num_channels: int
        Number of channels for initial convolution. 16 by default.
    num_cells: int
        Number of cells per stage. 5 by default.
    dataset: str
        Dataset used for training and evaluation. NAS-Bench-201 provides the following 4 options:
        ``cifar10-valid`` (training data is splited into 25k for training and 25k for validation,
        validation data is used for test), ``cifar10`` (training data is used in training, validation
        data is splited into 5k for validation and 5k for testing), ``cifar100`` (same protocol as ``cifar10``),
        and ``imagenet16-120`` (a subset of 120 classes in ImageNet, downscaled to 16x16, using training data
        for training, 6k images from validation set for validation and the other 6k for testing).
    """
    arch: Incomplete
    num_epochs: Incomplete
    num_channels: Incomplete
    num_cells: Incomplete
    dataset: Incomplete
    class Meta:
        database = proxy

class Nb201TrialStats(Model):
    """
    Computation statistics for NAS-Bench-201. Each corresponds to one trial.

    Attributes
    ----------
    config : Nb201TrialConfig
        Setup for this trial data.
    seed : int
        Random seed selected, for reproduction.
    train_acc : float
        Final accuracy on training data, ranging from 0 to 100.
    valid_acc : float
        Final accuracy on validation data, ranging from 0 to 100.
    test_acc : float
        Final accuracy on test data, ranging from 0 to 100.
    ori_test_acc : float
        Test accuracy on original validation set (10k for CIFAR and 12k for Imagenet16-120),
        ranging from 0 to 100.
    train_loss : float or None
        Final cross entropy loss on training data. Note that loss could be NaN, in which case
        this attributed will be None.
    valid_loss : float or None
        Final cross entropy loss on validation data.
    test_loss : float or None
        Final cross entropy loss on test data.
    ori_test_loss : float or None
        Final cross entropy loss on original validation set.
    parameters : float
        Number of trainable parameters in million.
    latency : float
        Latency in seconds.
    flops : float
        FLOPs in million.
    training_time : float
        Duration of training in seconds.
    valid_evaluation_time : float
        Time elapsed to evaluate on validation set.
    test_evaluation_time : float
        Time elapsed to evaluate on test set.
    ori_test_evaluation_time : float
        Time elapsed to evaluate on original test set.
    """
    config: Incomplete
    seed: Incomplete
    train_acc: Incomplete
    valid_acc: Incomplete
    test_acc: Incomplete
    ori_test_acc: Incomplete
    train_loss: Incomplete
    valid_loss: Incomplete
    test_loss: Incomplete
    ori_test_loss: Incomplete
    parameters: Incomplete
    latency: Incomplete
    flops: Incomplete
    training_time: Incomplete
    valid_evaluation_time: Incomplete
    test_evaluation_time: Incomplete
    ori_test_evaluation_time: Incomplete
    class Meta:
        database = proxy

class Nb201IntermediateStats(Model):
    """
    Intermediate statistics for NAS-Bench-201.

    Attributes
    ----------
    trial : Nb201TrialStats
        Corresponding trial.
    current_epoch : int
        Elapsed epochs.
    train_acc : float
        Current accuracy on training data, ranging from 0 to 100.
    valid_acc : float
        Current accuracy on validation data, ranging from 0 to 100.
    test_acc : float
        Current accuracy on test data, ranging from 0 to 100.
    ori_test_acc : float
        Test accuracy on original validation set (10k for CIFAR and 12k for Imagenet16-120),
        ranging from 0 to 100.
    train_loss : float or None
        Current cross entropy loss on training data.
    valid_loss : float or None
        Current cross entropy loss on validation data.
    test_loss : float or None
        Current cross entropy loss on test data.
    ori_test_loss : float or None
        Current cross entropy loss on original validation set.
    """
    trial: Incomplete
    current_epoch: Incomplete
    train_acc: Incomplete
    valid_acc: Incomplete
    test_acc: Incomplete
    ori_test_acc: Incomplete
    train_loss: Incomplete
    valid_loss: Incomplete
    test_loss: Incomplete
    ori_test_loss: Incomplete
    class Meta:
        database = proxy
