from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Dict, Iterator, List

__all__ = ['InputError', 'openf', 'bcolors', 'GeneratedFileCleaner', 'match_extensions', 'matched_files_iter', 'preprocess_file_and_save_result', 'compute_stats', 'add_dim3', 'processKernelLaunches', 'find_closure_group', 'find_bracket_group', 'find_parentheses_group', 'replace_math_functions', 'hip_header_magic', 'replace_extern_shared', 'get_hip_file_path', 'is_out_of_place', 'is_pytorch_file', 'is_cusparse_file', 'is_caffe2_gpu_file', 'is_caffe2_gpu_file', 'Trie', 'preprocessor', 'file_specific_replacement', 'file_add_header', 'fix_static_global_kernels', 'extract_arguments', 'str2bool', 'hipify']

HipifyResult = Dict[str, str | None]
HipifyFinalResult = Dict[str, HipifyResult]

class InputError(Exception):
    message: Incomplete
    def __init__(self, message) -> None: ...

def openf(filename, mode): ...

class bcolors:
    HEADER: str
    OKBLUE: str
    OKGREEN: str
    WARNING: str
    FAIL: str
    ENDC: str
    BOLD: str
    UNDERLINE: str

class GeneratedFileCleaner:
    """Context Manager to clean up generated files"""
    keep_intermediates: Incomplete
    files_to_clean: Incomplete
    dirs_to_clean: Incomplete
    def __init__(self, keep_intermediates: bool = False) -> None: ...
    def __enter__(self): ...
    def open(self, fn, *args, **kwargs): ...
    def makedirs(self, dn, exist_ok: bool = False) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def match_extensions(filename: str, extensions: Iterable) -> bool:
    """Helper method to see if filename ends with certain extension"""
def matched_files_iter(root_path: str, includes: Iterable = (), ignores: Iterable = (), extensions: Iterable = (), out_of_place_only: bool = False, is_pytorch_extension: bool = False) -> Iterator[str]: ...
def preprocess_file_and_save_result(output_directory: str, filepath: str, all_files: Iterable, header_include_dirs: Iterable, stats: Dict[str, List], hip_clang_launch: bool, is_pytorch_extension: bool, clean_ctx: GeneratedFileCleaner, show_progress: bool) -> None: ...
def compute_stats(stats) -> None: ...
def add_dim3(kernel_string, cuda_kernel):
    """adds dim3() to the second and third arguments in the kernel launch"""
def processKernelLaunches(string, stats):
    """ Replace the CUDA style Kernel launches with the HIP style kernel launches."""
def find_closure_group(input_string, start, group):
    '''Generalization for finding a balancing closure group

         if group = ["(", ")"], then finds the first balanced parentheses.
         if group = ["{", "}"], then finds the first balanced bracket.

    Given an input string, a starting position in the input string, and the group type,
    find_closure_group returns the positions of group[0] and group[1] as a tuple.

    Example:
        >>> find_closure_group("(hi)", 0, ["(", ")"])
        (0, 3)
    '''
def find_bracket_group(input_string, start):
    """Finds the first balanced parantheses."""
def find_parentheses_group(input_string, start):
    """Finds the first balanced bracket."""
def replace_math_functions(input_string):
    """FIXME: Temporarily replace std:: invocations of math functions
        with non-std:: versions to prevent linker errors NOTE: This
        can lead to correctness issues when running tests, since the
        correct version of the math function (exp/expf) might not get
        called.  Plan is to remove this function once HIP supports
        std:: math function calls inside device code

    """
def hip_header_magic(input_string):
    '''If the file makes kernel builtin calls and does not include the cuda_runtime.h header,
    then automatically add an #include to match the "magic" includes provided by NVCC.
    TODO:
        Update logic to ignore cases where the cuda_runtime.h is included by another file.
    '''
def replace_extern_shared(input_string):
    '''Match extern __shared__ type foo[]; syntax and use HIP_DYNAMIC_SHARED() MACRO instead.
       https://github.com/ROCm-Developer-Tools/HIP/blob/master/docs/markdown/hip_kernel_language.md#__shared__
    Example:
        "extern __shared__ char smemChar[];" => "HIP_DYNAMIC_SHARED( char, smemChar)"
        "extern __shared__ unsigned char smem[];" => "HIP_DYNAMIC_SHARED( unsigned char, my_smem)"
    '''
def get_hip_file_path(rel_filepath, is_pytorch_extension: bool = False):
    """
    Returns the new name of the hipified file
    """
def is_out_of_place(rel_filepath): ...
def is_pytorch_file(rel_filepath): ...
def is_cusparse_file(rel_filepath): ...
def is_caffe2_gpu_file(rel_filepath): ...

class Trie:
    """Regex::Trie in Python. Creates a Trie out of a list of words. The trie can be exported to a Regex pattern.
    The corresponding Regex should match much faster than a simple Regex union."""
    data: Incomplete
    def __init__(self) -> None: ...
    def add(self, word) -> None: ...
    def dump(self): ...
    def quote(self, char): ...
    def pattern(self): ...

def preprocessor(output_directory: str, filepath: str, all_files: Iterable, header_include_dirs: Iterable, stats: Dict[str, List], hip_clang_launch: bool, is_pytorch_extension: bool, clean_ctx: GeneratedFileCleaner, show_progress: bool) -> HipifyResult:
    """ Executes the CUDA -> HIP conversion on the specified file. """
def file_specific_replacement(filepath, search_string, replace_string, strict: bool = False): ...
def file_add_header(filepath, header) -> None: ...
def fix_static_global_kernels(in_txt):
    """Static global kernels in HIP results in a compilation error."""
def extract_arguments(start, string):
    """ Return the list of arguments in the upcoming function parameter closure.
        Example:
        string (input): '(blocks, threads, 0, THCState_getCurrentStream(state))'
        arguments (output):
            '[{'start': 1, 'end': 7},
            {'start': 8, 'end': 16},
            {'start': 17, 'end': 19},
            {'start': 20, 'end': 53}]'
    """
def str2bool(v):
    """ArgumentParser doesn't support type=bool. Thus, this helper method will convert
    from possible string types to True / False."""
def hipify(project_directory: str, show_detailed: bool = False, extensions: Iterable = ('.cu', '.cuh', '.c', '.cc', '.cpp', '.h', '.in', '.hpp'), header_extensions: Iterable = ('.cuh', '.h', '.hpp'), output_directory: str = '', header_include_dirs: Iterable = (), includes: Iterable = ('*',), extra_files: Iterable = (), out_of_place_only: bool = False, ignores: Iterable = (), show_progress: bool = True, hip_clang_launch: bool = False, is_pytorch_extension: bool = False, hipify_extra_files_only: bool = False, clean_ctx: GeneratedFileCleaner | None = None) -> HipifyFinalResult: ...
