from ._hl.attrs import AttributeManager as AttributeManager
from ._hl.base import HLObject as HLObject
from _typeshed import Incomplete

re_attr_match: Incomplete
re_item_match: Incomplete
re_object_match: Incomplete

def h5py_item_completer(context, command):
    """Compute possible item matches for dict-like objects"""
def h5py_attr_completer(context, command):
    """Compute possible attr matches for nested dict-like objects"""
def h5py_completer(self, event):
    """ Completer function to be loaded into IPython """
def load_ipython_extension(ip: Incomplete | None = None) -> None:
    """ Load completer function into IPython """
