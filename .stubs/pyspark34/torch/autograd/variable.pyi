import torch

__all__ = ['VariableMeta', 'Variable']

class VariableMeta(type):
    def __instancecheck__(cls, other): ...

class Variable(torch._C._LegacyVariableBase, metaclass=VariableMeta): ...
