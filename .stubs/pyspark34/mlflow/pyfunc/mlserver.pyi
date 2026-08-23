from typing import Dict, Tuple

MLServerMLflowRuntime: str
MLServerDefaultModelName: str

def get_cmd(model_uri: str, port: int = None, host: str = None, timeout: int = None, nworkers: int = None) -> Tuple[str, Dict[str, str]]: ...
