from _typeshed import Incomplete

DIGIT: str
ALPHA: str
HEXDIG: str
pct_encoded: Incomplete
unreserved: Incomplete
gen_delims: str
sub_delims: str
pchar: Incomplete
reserved: Incomplete
scheme: Incomplete
dec_octet: Incomplete
IPv4address: Incomplete
IPv6address: str
IPvFuture: Incomplete
IP_literal: Incomplete
reg_name: Incomplete
userinfo: Incomplete
host: Incomplete
port: Incomplete
authority: Incomplete
segment: Incomplete
segment_nz: Incomplete
segment_nz_nc: Incomplete
path_abempty: Incomplete
path_absolute: Incomplete
path_noscheme: Incomplete
path_rootless: Incomplete
path_empty: str
path: Incomplete
query: Incomplete
fragment: Incomplete
hier_part: Incomplete
relative_part: Incomplete
relative_ref: Incomplete
URI: Incomplete
URI_reference: Incomplete
absolute_URI: Incomplete

def is_uri(uri): ...
def is_uri_reference(uri): ...
def is_absolute_uri(uri): ...
