from sympy.core import Add as Add, Basic as Basic, Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.traversal import preorder_traversal as preorder_traversal

def sub_pre(e):
    """ Replace y - x with -(x - y) if -1 can be extracted from y - x.
    """
def sub_post(e):
    """ Replace 1*-1*x with -x.
    """
