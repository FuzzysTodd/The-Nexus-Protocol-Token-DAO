__all__ = ['TunerCommandChannel']

class TunerCommandChannel:
    '''
    A channel to communicate with NNI manager.

    Each NNI experiment has a channel URL for tuner/assessor/strategy algorithm.
    The channel can only be connected once, so for each Python side :class:`~nni.experiment.Experiment` object,
    there should be exactly one corresponding ``TunerCommandChannel`` instance.

    :meth:`connect` must be invoked before sending or receiving data.

    The constructor does not have side effect so ``TunerCommandChannel`` can be created anywhere.
    But :meth:`connect` requires an initialized NNI manager, or otherwise the behavior is unpredictable.

    :meth:`_send` and :meth:`_receive` are underscore-prefixed because their signatures are scheduled to change by v3.0.

    Parameters
    ----------
    url
        The command channel URL.
        For now it must be like ``"ws://localhost:8080/tuner"`` or ``"ws://localhost:8080/url-prefix/tuner"``.
    '''
    def __init__(self, url: str) -> None: ...
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
