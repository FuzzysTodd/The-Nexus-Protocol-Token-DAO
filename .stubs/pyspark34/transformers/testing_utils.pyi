import os
import unittest
from .deepspeed import is_deepspeed_available as is_deepspeed_available
from .integrations import is_clearml_available as is_clearml_available, is_fairscale_available as is_fairscale_available, is_optuna_available as is_optuna_available, is_ray_available as is_ray_available, is_sigopt_available as is_sigopt_available, is_wandb_available as is_wandb_available
from .utils import is_accelerate_available as is_accelerate_available, is_apex_available as is_apex_available, is_bitsandbytes_available as is_bitsandbytes_available, is_bs4_available as is_bs4_available, is_cython_available as is_cython_available, is_decord_available as is_decord_available, is_detectron2_available as is_detectron2_available, is_faiss_available as is_faiss_available, is_flax_available as is_flax_available, is_ftfy_available as is_ftfy_available, is_ipex_available as is_ipex_available, is_jumanpp_available as is_jumanpp_available, is_keras_nlp_available as is_keras_nlp_available, is_librosa_available as is_librosa_available, is_natten_available as is_natten_available, is_onnx_available as is_onnx_available, is_pandas_available as is_pandas_available, is_phonemizer_available as is_phonemizer_available, is_pyctcdecode_available as is_pyctcdecode_available, is_pytesseract_available as is_pytesseract_available, is_pytorch_quantization_available as is_pytorch_quantization_available, is_rjieba_available as is_rjieba_available, is_safetensors_available as is_safetensors_available, is_scipy_available as is_scipy_available, is_sentencepiece_available as is_sentencepiece_available, is_soundfile_availble as is_soundfile_availble, is_spacy_available as is_spacy_available, is_sudachi_available as is_sudachi_available, is_tensorflow_probability_available as is_tensorflow_probability_available, is_tensorflow_text_available as is_tensorflow_text_available, is_tf2onnx_available as is_tf2onnx_available, is_tf_available as is_tf_available, is_timm_available as is_timm_available, is_tokenizers_available as is_tokenizers_available, is_torch_available as is_torch_available, is_torch_bf16_cpu_available as is_torch_bf16_cpu_available, is_torch_bf16_gpu_available as is_torch_bf16_gpu_available, is_torch_neuroncore_available as is_torch_neuroncore_available, is_torch_tensorrt_fx_available as is_torch_tensorrt_fx_available, is_torch_tf32_available as is_torch_tf32_available, is_torch_tpu_available as is_torch_tpu_available, is_torchaudio_available as is_torchaudio_available, is_torchdynamo_available as is_torchdynamo_available, is_vision_available as is_vision_available
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Iterator, List, Optional, Union

SMALL_MODEL_IDENTIFIER: str
DUMMY_UNKNOWN_IDENTIFIER: str
DUMMY_DIFF_TOKENIZER_IDENTIFIER: str
USER: str
ENDPOINT_STAGING: str
TOKEN: str

def parse_flag_from_env(key, default: bool = False): ...
def parse_int_from_env(key, default: Incomplete | None = None): ...
def is_pt_tf_cross_test(test_case):
    """
    Decorator marking a test as a test that control interactions between PyTorch and TensorFlow.

    PT+TF tests are skipped by default and we can run only them by setting RUN_PT_TF_CROSS_TESTS environment variable
    to a truthy value and selecting the is_pt_tf_cross_test pytest mark.

    """
def is_pt_flax_cross_test(test_case):
    """
    Decorator marking a test as a test that control interactions between PyTorch and Flax

    PT+FLAX tests are skipped by default and we can run only them by setting RUN_PT_FLAX_CROSS_TESTS environment
    variable to a truthy value and selecting the is_pt_flax_cross_test pytest mark.

    """
def is_staging_test(test_case):
    """
    Decorator marking a test as a staging test.

    Those tests will run using the staging environment of huggingface.co instead of the real model hub.
    """
def slow(test_case):
    """
    Decorator marking a test as slow.

    Slow tests are skipped by default. Set the RUN_SLOW environment variable to a truthy value to run them.

    """
def tooslow(test_case):
    '''
    Decorator marking a test as too slow.

    Slow tests are skipped while they\'re in the process of being fixed. No test should stay tagged as "tooslow" as
    these will not be tested by the CI.

    '''
def custom_tokenizers(test_case):
    """
    Decorator marking a test for a custom tokenizer.

    Custom tokenizers require additional dependencies, and are skipped by default. Set the RUN_CUSTOM_TOKENIZERS
    environment variable to a truthy value to run them.
    """
def require_bs4(test_case):
    """
    Decorator marking a test that requires BeautifulSoup4. These tests are skipped when BeautifulSoup4 isn't installed.
    """
def require_git_lfs(test_case):
    """
    Decorator marking a test that requires git-lfs.

    git-lfs requires additional dependencies, and tests are skipped by default. Set the RUN_GIT_LFS_TESTS environment
    variable to a truthy value to run them.
    """
def require_accelerate(test_case):
    """
    Decorator marking a test that requires accelerate. These tests are skipped when accelerate isn't installed.
    """
def require_safetensors(test_case):
    """
    Decorator marking a test that requires safetensors. These tests are skipped when safetensors isn't installed.
    """
def require_rjieba(test_case):
    """
    Decorator marking a test that requires rjieba. These tests are skipped when rjieba isn't installed.
    """
def require_tf2onnx(test_case): ...
def require_onnx(test_case): ...
def require_timm(test_case):
    """
    Decorator marking a test that requires Timm.

    These tests are skipped when Timm isn't installed.

    """
def require_natten(test_case):
    """
    Decorator marking a test that requires NATTEN.

    These tests are skipped when NATTEN isn't installed.

    """
def require_torch(test_case):
    """
    Decorator marking a test that requires PyTorch.

    These tests are skipped when PyTorch isn't installed.

    """
def require_torch_or_tf(test_case):
    """
    Decorator marking a test that requires PyTorch or TensorFlow.

    These tests are skipped when neither PyTorch not TensorFlow is installed.

    """
def require_intel_extension_for_pytorch(test_case):
    """
    Decorator marking a test that requires Intel Extension for PyTorch.

    These tests are skipped when Intel Extension for PyTorch isn't installed or it does not match current PyTorch
    version.

    """
def require_tensorflow_probability(test_case):
    """
    Decorator marking a test that requires TensorFlow probability.

    These tests are skipped when TensorFlow probability isn't installed.

    """
def require_torchaudio(test_case):
    """
    Decorator marking a test that requires torchaudio. These tests are skipped when torchaudio isn't installed.
    """
def require_tf(test_case):
    """
    Decorator marking a test that requires TensorFlow. These tests are skipped when TensorFlow isn't installed.
    """
def require_flax(test_case):
    """
    Decorator marking a test that requires JAX & Flax. These tests are skipped when one / both are not installed
    """
def require_sentencepiece(test_case):
    """
    Decorator marking a test that requires SentencePiece. These tests are skipped when SentencePiece isn't installed.
    """
def require_scipy(test_case):
    """
    Decorator marking a test that requires Scipy. These tests are skipped when SentencePiece isn't installed.
    """
def require_tokenizers(test_case):
    """
    Decorator marking a test that requires 🤗 Tokenizers. These tests are skipped when 🤗 Tokenizers isn't installed.
    """
def require_tensorflow_text(test_case):
    """
    Decorator marking a test that requires tensorflow_text. These tests are skipped when tensroflow_text isn't
    installed.
    """
def require_keras_nlp(test_case):
    """
    Decorator marking a test that requires keras_nlp. These tests are skipped when keras_nlp isn't installed.
    """
def require_pandas(test_case):
    """
    Decorator marking a test that requires pandas. These tests are skipped when pandas isn't installed.
    """
def require_pytesseract(test_case):
    """
    Decorator marking a test that requires PyTesseract. These tests are skipped when PyTesseract isn't installed.
    """
def require_pytorch_quantization(test_case):
    """
    Decorator marking a test that requires PyTorch Quantization Toolkit. These tests are skipped when PyTorch
    Quantization Toolkit isn't installed.
    """
def require_vision(test_case):
    """
    Decorator marking a test that requires the vision dependencies. These tests are skipped when torchaudio isn't
    installed.
    """
def require_ftfy(test_case):
    """
    Decorator marking a test that requires ftfy. These tests are skipped when ftfy isn't installed.
    """
def require_spacy(test_case):
    """
    Decorator marking a test that requires SpaCy. These tests are skipped when SpaCy isn't installed.
    """
def require_decord(test_case):
    """
    Decorator marking a test that requires decord. These tests are skipped when decord isn't installed.
    """
def require_torch_multi_gpu(test_case):
    '''
    Decorator marking a test that requires a multi-GPU setup (in PyTorch). These tests are skipped on a machine without
    multiple GPUs.

    To run *only* the multi_gpu tests, assuming all test names contain multi_gpu: $ pytest -sv ./tests -k "multi_gpu"
    '''
def require_torch_non_multi_gpu(test_case):
    """
    Decorator marking a test that requires 0 or 1 GPU setup (in PyTorch).
    """
def require_torch_up_to_2_gpus(test_case):
    """
    Decorator marking a test that requires 0 or 1 or 2 GPU setup (in PyTorch).
    """
def require_torch_tpu(test_case):
    """
    Decorator marking a test that requires a TPU (in PyTorch).
    """
def require_torch_neuroncore(test_case):
    """
    Decorator marking a test that requires NeuronCore (in PyTorch).
    """

torch_device: Incomplete
jax_device: Incomplete

def require_torchdynamo(test_case):
    """Decorator marking a test that requires TorchDynamo"""
def require_torch_tensorrt_fx(test_case):
    """Decorator marking a test that requires Torch-TensorRT FX"""
def require_torch_gpu(test_case):
    """Decorator marking a test that requires CUDA and PyTorch."""
def require_torch_bf16_gpu(test_case):
    """Decorator marking a test that requires torch>=1.10, using Ampere GPU or newer arch with cuda>=11.0"""
def require_torch_bf16_cpu(test_case):
    """Decorator marking a test that requires torch>=1.10, using CPU."""
def require_torch_tf32(test_case):
    """Decorator marking a test that requires Ampere or a newer GPU arch, cuda>=11 and torch>=1.7."""
def require_detectron2(test_case):
    """Decorator marking a test that requires detectron2."""
def require_faiss(test_case):
    """Decorator marking a test that requires faiss."""
def require_optuna(test_case):
    """
    Decorator marking a test that requires optuna.

    These tests are skipped when optuna isn't installed.

    """
def require_ray(test_case):
    """
    Decorator marking a test that requires Ray/tune.

    These tests are skipped when Ray/tune isn't installed.

    """
def require_sigopt(test_case):
    """
    Decorator marking a test that requires SigOpt.

    These tests are skipped when SigOpt isn't installed.

    """
def require_wandb(test_case):
    """
    Decorator marking a test that requires wandb.

    These tests are skipped when wandb isn't installed.

    """
def require_clearml(test_case):
    """
    Decorator marking a test requires clearml.

    These tests are skipped when clearml isn't installed.

    """
def require_soundfile(test_case):
    """
    Decorator marking a test that requires soundfile

    These tests are skipped when soundfile isn't installed.

    """
def require_deepspeed(test_case):
    """
    Decorator marking a test that requires deepspeed
    """
def require_fairscale(test_case):
    """
    Decorator marking a test that requires fairscale
    """
def require_apex(test_case):
    """
    Decorator marking a test that requires apex
    """
def require_bitsandbytes(test_case):
    """
    Decorator for bits and bytes (bnb) dependency
    """
def require_phonemizer(test_case):
    """
    Decorator marking a test that requires phonemizer
    """
def require_pyctcdecode(test_case):
    """
    Decorator marking a test that requires pyctcdecode
    """
def require_librosa(test_case):
    """
    Decorator marking a test that requires librosa
    """
def cmd_exists(cmd): ...
def require_usr_bin_time(test_case):
    """
    Decorator marking a test that requires `/usr/bin/time`
    """
def require_sudachi(test_case):
    """
    Decorator marking a test that requires sudachi
    """
def require_jumanpp(test_case):
    """
    Decorator marking a test that requires jumanpp
    """
def require_cython(test_case):
    """
    Decorator marking a test that requires jumanpp
    """
def get_gpu_count():
    """
    Return the number of available gpus (regardless of whether torch, tf or jax is used)
    """
def get_tests_dir(append_path: Incomplete | None = None):
    """
    Args:
        append_path: optional path to append to the tests dir path

    Return:
        The full path to the `tests` dir, so that the tests can be invoked from anywhere. Optionally `append_path` is
        joined after the `tests` dir the former is provided.

    """
def apply_print_resets(buf): ...
def assert_screenout(out, what) -> None: ...

class CaptureStd:
    '''
    Context manager to capture:

        - stdout: replay it, clean it up and make it available via `obj.out`
        - stderr: replay it and make it available via `obj.err`

    Args:
        out (`bool`, *optional*, defaults to `True`): Whether to capture stdout or not.
        err (`bool`, *optional*, defaults to `True`): Whether to capture stderr or not.
        replay (`bool`, *optional*, defaults to `True`): Whether to replay or not.
            By default each captured stream gets replayed back on context\'s exit, so that one can see what the test was
            doing. If this is a not wanted behavior and the captured data shouldn\'t be replayed, pass `replay=False` to
            disable this feature.

    Examples:

    ```python
    # to capture stdout only with auto-replay
    with CaptureStdout() as cs:
        print("Secret message")
    assert "message" in cs.out

    # to capture stderr only with auto-replay
    import sys

    with CaptureStderr() as cs:
        print("Warning: ", file=sys.stderr)
    assert "Warning" in cs.err

    # to capture both streams with auto-replay
    with CaptureStd() as cs:
        print("Secret message")
        print("Warning: ", file=sys.stderr)
    assert "message" in cs.out
    assert "Warning" in cs.err

    # to capture just one of the streams, and not the other, with auto-replay
    with CaptureStd(err=False) as cs:
        print("Secret message")
    assert "message" in cs.out
    # but best use the stream-specific subclasses

    # to capture without auto-replay
    with CaptureStd(replay=False) as cs:
        print("Secret message")
    assert "message" in cs.out
    ```'''
    replay: Incomplete
    out_buf: Incomplete
    out: str
    err_buf: Incomplete
    err: str
    def __init__(self, out: bool = True, err: bool = True, replay: bool = True) -> None: ...
    out_old: Incomplete
    err_old: Incomplete
    def __enter__(self): ...
    def __exit__(self, *exc) -> None: ...

class CaptureStdout(CaptureStd):
    """Same as CaptureStd but captures only stdout"""
    def __init__(self, replay: bool = True) -> None: ...

class CaptureStderr(CaptureStd):
    """Same as CaptureStd but captures only stderr"""
    def __init__(self, replay: bool = True) -> None: ...

class CaptureLogger:
    '''
    Context manager to capture `logging` streams

    Args:
        logger: \'logging` logger object

    Returns:
        The captured output is available via `self.out`

    Example:

    ```python
    >>> from transformers import logging
    >>> from transformers.testing_utils import CaptureLogger

    >>> msg = "Testing 1, 2, 3"
    >>> logging.set_verbosity_info()
    >>> logger = logging.get_logger("transformers.models.bart.tokenization_bart")
    >>> with CaptureLogger(logger) as cl:
    ...     logger.info(msg)
    >>> assert cl.out, msg + "
"
    ```
    '''
    logger: Incomplete
    io: Incomplete
    sh: Incomplete
    out: str
    def __init__(self, logger) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc) -> None: ...

def LoggingLevel(level) -> Generator[None, None, None]:
    '''
    This is a context manager to temporarily change transformers modules logging level to the desired value and have it
    restored to the original setting at the end of the scope.

    Example:

    ```python
    with LoggingLevel(logging.INFO):
        AutoModel.from_pretrained("gpt2")  # calls logger.info() several times
    ```
    '''
def ExtendSysPath(path: Union[str, os.PathLike]) -> Iterator[None]:
    '''
    Temporary add given path to `sys.path`.

    Usage :

    ```python
    with ExtendSysPath("/path/to/dir"):
        mymodule = importlib.import_module("mymodule")
    ```
    '''

class TestCasePlus(unittest.TestCase):
    '''
    This class extends *unittest.TestCase* with additional features.

    Feature 1: A set of fully resolved important file and dir path accessors.

    In tests often we need to know where things are relative to the current test file, and it\'s not trivial since the
    test could be invoked from more than one directory or could reside in sub-directories with different depths. This
    class solves this problem by sorting out all the basic paths and provides easy accessors to them:

    - `pathlib` objects (all fully resolved):

       - `test_file_path` - the current test file path (=`__file__`)
       - `test_file_dir` - the directory containing the current test file
       - `tests_dir` - the directory of the `tests` test suite
       - `examples_dir` - the directory of the `examples` test suite
       - `repo_root_dir` - the directory of the repository
       - `src_dir` - the directory of `src` (i.e. where the `transformers` sub-dir resides)

    - stringified paths---same as above but these return paths as strings, rather than `pathlib` objects:

       - `test_file_path_str`
       - `test_file_dir_str`
       - `tests_dir_str`
       - `examples_dir_str`
       - `repo_root_dir_str`
       - `src_dir_str`

    Feature 2: Flexible auto-removable temporary dirs which are guaranteed to get removed at the end of test.

    1. Create a unique temporary dir:

    ```python
    def test_whatever(self):
        tmp_dir = self.get_auto_remove_tmp_dir()
    ```

    `tmp_dir` will contain the path to the created temporary dir. It will be automatically removed at the end of the
    test.


    2. Create a temporary dir of my choice, ensure it\'s empty before the test starts and don\'t
    empty it after the test.

    ```python
    def test_whatever(self):
        tmp_dir = self.get_auto_remove_tmp_dir("./xxx")
    ```

    This is useful for debug when you want to monitor a specific directory and want to make sure the previous tests
    didn\'t leave any data in there.

    3. You can override the first two options by directly overriding the `before` and `after` args, leading to the
        following behavior:

    `before=True`: the temporary dir will always be cleared at the beginning of the test.

    `before=False`: if the temporary dir already existed, any existing files will remain there.

    `after=True`: the temporary dir will always be deleted at the end of the test.

    `after=False`: the temporary dir will always be left intact at the end of the test.

    Note 1: In order to run the equivalent of `rm -r` safely, only subdirs of the project repository checkout are
    allowed if an explicit `tmp_dir` is used, so that by mistake no `/tmp` or similar important part of the filesystem
    will get nuked. i.e. please always pass paths that start with `./`

    Note 2: Each test can register multiple temporary dirs and they all will get auto-removed, unless requested
    otherwise.

    Feature 3: Get a copy of the `os.environ` object that sets up `PYTHONPATH` specific to the current test suite. This
    is useful for invoking external programs from the test suite - e.g. distributed training.


    ```python
    def test_whatever(self):
        env = self.get_env()
    ```'''
    teardown_tmp_dirs: Incomplete
    def setUp(self) -> None: ...
    @property
    def test_file_path(self): ...
    @property
    def test_file_path_str(self): ...
    @property
    def test_file_dir(self): ...
    @property
    def test_file_dir_str(self): ...
    @property
    def tests_dir(self): ...
    @property
    def tests_dir_str(self): ...
    @property
    def examples_dir(self): ...
    @property
    def examples_dir_str(self): ...
    @property
    def repo_root_dir(self): ...
    @property
    def repo_root_dir_str(self): ...
    @property
    def src_dir(self): ...
    @property
    def src_dir_str(self): ...
    def get_env(self):
        """
        Return a copy of the `os.environ` object that sets up `PYTHONPATH` correctly, depending on the test suite it's
        invoked from. This is useful for invoking external programs from the test suite - e.g. distributed training.

        It always inserts `./src` first, then `./tests` or `./examples` depending on the test suite type and finally
        the preset `PYTHONPATH` if any (all full resolved paths).

        """
    def get_auto_remove_tmp_dir(self, tmp_dir: Incomplete | None = None, before: Incomplete | None = None, after: Incomplete | None = None):
        """
        Args:
            tmp_dir (`string`, *optional*):
                if `None`:

                   - a unique temporary path will be created
                   - sets `before=True` if `before` is `None`
                   - sets `after=True` if `after` is `None`
                else:

                   - `tmp_dir` will be created
                   - sets `before=True` if `before` is `None`
                   - sets `after=False` if `after` is `None`
            before (`bool`, *optional*):
                If `True` and the `tmp_dir` already exists, make sure to empty it right away if `False` and the
                `tmp_dir` already exists, any existing files will remain there.
            after (`bool`, *optional*):
                If `True`, delete the `tmp_dir` at the end of the test if `False`, leave the `tmp_dir` and its contents
                intact at the end of the test.

        Returns:
            tmp_dir(`string`): either the same value as passed via *tmp_dir* or the path to the auto-selected tmp dir
        """
    def python_one_liner_max_rss(self, one_liner_str):
        '''
        Runs the passed python one liner (just the code) and returns how much max cpu memory was used to run the
        program.

        Args:
            one_liner_str (`string`):
                a python one liner code that gets passed to `python -c`

        Returns:
            max cpu memory bytes used to run the program. This value is likely to vary slightly from run to run.

        Requirements:
            this helper needs `/usr/bin/time` to be installed (`apt install time`)

        Example:

        ```
        one_liner_str = \'from transformers import AutoModel; AutoModel.from_pretrained("t5-large")\'
        max_rss = self.python_one_liner_max_rss(one_liner_str)
        ```
        '''
    def tearDown(self) -> None: ...

def mockenv(**kwargs):
    '''
    this is a convenience wrapper, that allows this ::

    @mockenv(RUN_SLOW=True, USE_TF=False) def test_something():
        run_slow = os.getenv("RUN_SLOW", False) use_tf = os.getenv("USE_TF", False)

    '''
def mockenv_context(*remove, **update) -> Generator[None, None, None]:
    """
    Temporarily updates the `os.environ` dictionary in-place. Similar to mockenv

    The `os.environ` dictionary is updated in-place so that the modification is sure to work in all situations.

    Args:
      remove: Environment variables to remove.
      update: Dictionary of environment variables and values to add/update.
    """

pytest_opt_registered: Incomplete

def pytest_addoption_shared(parser) -> None:
    """
    This function is to be called from `conftest.py` via `pytest_addoption` wrapper that has to be defined there.

    It allows loading both `conftest.py` files at once without causing a failure due to adding the same `pytest`
    option.

    """
def pytest_terminal_summary_main(tr, id):
    """
    Generate multiple reports at the end of test suite run - each report goes into a dedicated file in the current
    directory. The report files are prefixed with the test suite name.

    This function emulates --duration and -rA pytest arguments.

    This function is to be called from `conftest.py` via `pytest_terminal_summary` wrapper that has to be defined
    there.

    Args:
    - tr: `terminalreporter` passed from `conftest.py`
    - id: unique id like `tests` or `examples` that will be incorporated into the final reports filenames - this is
      needed as some jobs have multiple runs of pytest, so we can't have them overwrite each other.

    NB: this functions taps into a private _pytest API and while unlikely, it could break should pytest do internal
    changes - also it calls default internal methods of terminalreporter which can be hijacked by various `pytest-`
    plugins and interfere.

    """

class _RunOutput:
    returncode: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    def __init__(self, returncode, stdout, stderr) -> None: ...

def execute_subprocess_async(cmd, env: Incomplete | None = None, stdin: Incomplete | None = None, timeout: int = 180, quiet: bool = False, echo: bool = True) -> _RunOutput: ...
def pytest_xdist_worker_id():
    """
    Returns an int value of worker's numerical id under `pytest-xdist`'s concurrent workers `pytest -n N` regime, or 0
    if `-n 1` or `pytest-xdist` isn't being used.
    """
def get_torch_dist_unique_port():
    """
    Returns a port number that can be fed to `torch.distributed.launch`'s `--master_port` argument.

    Under `pytest-xdist` it adds a delta number based on a worker id so that concurrent tests don't try to use the same
    port at once.
    """
def nested_simplify(obj, decimals: int = 3):
    """
    Simplifies an object by rounding float numbers, and downcasting tensors/numpy arrays to get simple equality test
    within tests.
    """
def check_json_file_has_correct_format(file_path) -> None: ...
def to_2tuple(x): ...

class SubprocessCallException(Exception): ...

def run_command(command: List[str], return_stdout: bool = False):
    """
    Runs `command` with `subprocess.check_output` and will potentially return the `stdout`. Will also properly capture
    if an error occured while running `command`
    """

class RequestCounter:
    """
    Helper class that will count all requests made online.
    """
    head_request_count: int
    get_request_count: int
    other_request_count: int
    old_request: Incomplete
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs) -> None: ...
    def new_request(self, method, **kwargs): ...

def is_flaky(max_attempts: int = 5, wait_before_retry: Optional[float] = None):
    """
    To decorate flaky tests. They will be retried on failures.

    Args:
        max_attempts (`int`, *optional*, defaults to 5):
            The maximum number of attempts to retry the flaky test.
        wait_before_retry (`float`, *optional*):
            If provided, will wait that number of seconds before retrying the test.
    """
def run_test_in_subprocess(test_case, target_func, inputs: Incomplete | None = None, timeout: int = 600) -> None:
    """
    To run a test in a subprocess. In particular, this can avoid (GPU) memory issue.

    Args:
        test_case (`unittest.TestCase`):
            The test that will run `target_func`.
        target_func (`Callable`):
            The function implementing the actual testing logic.
        inputs (`dict`, *optional*, defaults to `None`):
            The inputs that will be passed to `target_func` through an (input) queue.
        timeout (`int`, *optional*, defaults to 600):
            The timeout (in seconds) that will be passed to the input and output queues.
    """
