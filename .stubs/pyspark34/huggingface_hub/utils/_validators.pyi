from ._typing import CallableT as CallableT
from _typeshed import Incomplete
from typing import Any, Dict

REPO_ID_REGEX: Incomplete

class HFValidationError(ValueError):
    """Generic exception thrown by `huggingface_hub` validators.

    Inherits from [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError).
    """

def validate_hf_hub_args(fn: CallableT) -> CallableT:
    '''Validate values received as argument for any public method of `huggingface_hub`.

    The goal of this decorator is to harmonize validation of arguments reused
    everywhere. By default, all defined validators are tested.

    Validators:
        - [`~utils.validate_repo_id`]: `repo_id` must be `"repo_name"`
          or `"namespace/repo_name"`. Namespace is a username or an organization.
        - [`~utils.smoothly_deprecate_use_auth_token`]: Use `token` instead of
          `use_auth_token` (only if `use_auth_token` is not expected by the decorated
          function - in practice, always the case in `huggingface_hub`).

    Example:
    ```py
    >>> from huggingface_hub.utils import validate_hf_hub_args

    >>> @validate_hf_hub_args
    ... def my_cool_method(repo_id: str):
    ...     print(repo_id)

    >>> my_cool_method(repo_id="valid_repo_id")
    valid_repo_id

    >>> my_cool_method("other..repo..id")
    huggingface_hub.utils._validators.HFValidationError: Cannot have -- or .. in repo_id: \'other..repo..id\'.

    >>> my_cool_method(repo_id="other..repo..id")
    huggingface_hub.utils._validators.HFValidationError: Cannot have -- or .. in repo_id: \'other..repo..id\'.

    >>> @validate_hf_hub_args
    ... def my_cool_auth_method(token: str):
    ...     print(token)

    >>> my_cool_auth_method(token="a token")
    "a token"

    >>> my_cool_auth_method(use_auth_token="a use_auth_token")
    "a use_auth_token"

    >>> my_cool_auth_method(token="a token", use_auth_token="a use_auth_token")
    UserWarning: Both `token` and `use_auth_token` are passed (...)
    "a token"
    ```

    Raises:
        [`~utils.HFValidationError`]:
            If an input is not valid.
    '''
def validate_repo_id(repo_id: str) -> None:
    '''Validate `repo_id` is valid.

    This is not meant to replace the proper validation made on the Hub but rather to
    avoid local inconsistencies whenever possible (example: passing `repo_type` in the
    `repo_id` is forbidden).

    Rules:
    - Between 1 and 96 characters.
    - Either "repo_name" or "namespace/repo_name"
    - [a-zA-Z0-9] or "-", "_", "."
    - "--" and ".." are forbidden

    Valid: `"foo"`, `"foo/bar"`, `"123"`, `"Foo-BAR_foo.bar123"`

    Not valid: `"datasets/foo/bar"`, `".repo_id"`, `"foo--bar"`, `"foo.git"`

    Example:
    ```py
    >>> from huggingface_hub.utils import validate_repo_id
    >>> validate_repo_id(repo_id="valid_repo_id")
    >>> validate_repo_id(repo_id="other..repo..id")
    huggingface_hub.utils._validators.HFValidationError: Cannot have -- or .. in repo_id: \'other..repo..id\'.
    ```

    Discussed in https://github.com/huggingface/huggingface_hub/issues/1008.
    In moon-landing (internal repository):
    - https://github.com/huggingface/moon-landing/blob/main/server/lib/Names.ts#L27
    - https://github.com/huggingface/moon-landing/blob/main/server/views/components/NewRepoForm/NewRepoForm.svelte#L138
    '''
def smoothly_deprecate_use_auth_token(fn_name: str, has_token: bool, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Smoothly deprecate `use_auth_token` in the `huggingface_hub` codebase.

    The long-term goal is to remove any mention of `use_auth_token` in the codebase in
    favor of a unique and less verbose `token` argument. This will be done a few steps:

    0. Step 0: methods that require a read-access to the Hub use the `use_auth_token`
       argument (`str`, `bool` or `None`). Methods requiring write-access have a `token`
       argument (`str`, `None`). This implicit rule exists to be able to not send the
       token when not necessary (`use_auth_token=False`) even if logged in.

    1. Step 1: we want to harmonize everything and use `token` everywhere (supporting
       `token=False` for read-only methods). In order not to break existing code, if
       `use_auth_token` is passed to a function, the `use_auth_token` value is passed
       as `token` instead, without any warning.
       a. Corner case: if both `use_auth_token` and `token` values are passed, a warning
          is thrown and the `use_auth_token` value is ignored.

    2. Step 2: Once it is release, we should push downstream libraries to switch from
       `use_auth_token` to `token` as much as possible, but without throwing a warning
       (e.g. manually create issues on the corresponding repos).

    3. Step 3: After a transitional period (6 months e.g. until April 2023?), we update
       `huggingface_hub` to throw a warning on `use_auth_token`. Hopefully, very few
       users will be impacted as it would have already been fixed.
       In addition, unit tests in `huggingface_hub` must be adapted to expect warnings
       to be thrown (but still use `use_auth_token` as before).

    4. Step 4: After a normal deprecation cycle (3 releases ?), remove this validator.
       `use_auth_token` will definitely not be supported.
       In addition, we update unit tests in `huggingface_hub` to use `token` everywhere.

    This has been discussed in:
    - https://github.com/huggingface/huggingface_hub/issues/1094.
    - https://github.com/huggingface/huggingface_hub/pull/928
    - (related) https://github.com/huggingface/huggingface_hub/pull/1064
    """
