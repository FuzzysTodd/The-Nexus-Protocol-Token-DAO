from typing import Mapping

def parse_connection_string(conn_str: str, case_sensitive_keys: bool = False) -> Mapping[str, str]:
    """Parses the connection string into a dict of its component parts, with the option of preserving case
    of keys, and validates that each key in the connection string has a provided value. If case of keys
    is not preserved (ie. `case_sensitive_keys=False`), then a dict with LOWERCASE KEYS will be returned.

    :param str conn_str: String with connection details provided by Azure services.
    :param bool case_sensitive_keys: Indicates whether the casing of the keys will be preserved. When `False`(the
        default), all keys will be lower-cased. If set to `True`, the original casing of the keys will be preserved.
    :rtype: Mapping
    :returns: Dict of connection string key/value pairs.
    :raises:
        ValueError: if each key in conn_str does not have a corresponding value and
            for other bad formatting of connection strings - including duplicate
            args, bad syntax, etc.
    """
