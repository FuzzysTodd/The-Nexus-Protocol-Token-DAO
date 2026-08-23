from _typeshed import Incomplete
from ctypes import Structure
from send2trash.compat import binary_type as binary_type
from send2trash.util import preprocess_paths as preprocess_paths

Foundation: Incomplete
CoreServices: Incomplete
GetMacOSStatusCommentString: Incomplete
FSPathMakeRefWithOptions: Incomplete
FSMoveObjectToTrashSync: Incomplete
kFSPathMakeRefDefaultOptions: int
kFSPathMakeRefDoNotFollowLeafSymlink: int
kFSFileOperationDefaultOptions: int
kFSFileOperationOverwrite: int
kFSFileOperationSkipSourcePermissionErrors: int
kFSFileOperationDoNotMoveAcrossVolumes: int
kFSFileOperationSkipPreflight: int

class FSRef(Structure): ...

def check_op_result(op_result) -> None: ...
def send2trash(paths) -> None: ...
