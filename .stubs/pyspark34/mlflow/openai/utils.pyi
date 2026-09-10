from _typeshed import Incomplete

TEST_CONTENT: str

class _MockResponse:
    status_code: Incomplete
    content: Incomplete
    headers: Incomplete
    text: Incomplete
    def __init__(self, status_code, json_data) -> None: ...
