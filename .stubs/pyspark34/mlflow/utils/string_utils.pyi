def strip_prefix(original, prefix): ...
def strip_suffix(original, suffix): ...
def is_string_type(item): ...
def generate_feature_name_if_not_string(s): ...
def truncate_str_from_middle(s, max_length): ...

cmd_meta: str
cmd_meta_or_space: str
cmd_meta_inside_quotes: str

def mslex_quote(s, for_cmd: bool = True):
    """
    Quote a string for use as a command line argument in DOS or Windows.

    On windows, before a command line argument becomes a char* in a
    program's argv, it must be parsed by both cmd.exe, and by
    CommandLineToArgvW.

    If for_cmd is true, then this will quote the string so it will
    be parsed correctly by cmd.exe and then by CommandLineToArgvW.

    If for_cmd is false, then this will quote the string so it will
    be parsed correctly when passed directly to CommandLineToArgvW.

    For some strings there is no way to quote them so they will
    parse correctly in both situations.
    """
def quote(s): ...
