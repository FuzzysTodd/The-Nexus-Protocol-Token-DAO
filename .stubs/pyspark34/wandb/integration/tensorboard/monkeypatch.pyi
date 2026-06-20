TENSORBOARD_C_MODULE: str
TENSORBOARD_X_MODULE: str
TENSORFLOW_PY_MODULE: str
TENSORBOARD_WRITER_MODULE: str
TENSORBOARD_PYTORCH_MODULE: str

def unpatch() -> None: ...
def patch(save: bool = True, tensorboard_x: bool | None = None, pytorch: bool | None = None, root_logdir: str = '') -> None: ...
