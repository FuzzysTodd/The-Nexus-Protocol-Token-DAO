from _typeshed import Incomplete

path_tokenizer: Incomplete

def iterchildren(node, attr_name): ...
def type_name(node): ...
def parse_func(next, token): ...
def handle_func_not(next, token):
    """
    not(...)
    """
def handle_name(next, token):
    """
    /NodeName/
    or
    func(...)
    """
def handle_star(next, token):
    """
    /*/
    """
def handle_dot(next, token):
    """
    /./
    """
def handle_descendants(next, token):
    """
    //...
    """
def handle_attribute(next, token): ...
def parse_path_value(next): ...
def handle_predicate(next, token): ...
def logical_and(lhs_selects, rhs_select): ...

operations: Incomplete
functions: Incomplete

def iterfind(node, path): ...
def find_first(node, path): ...
def find_all(node, path): ...
