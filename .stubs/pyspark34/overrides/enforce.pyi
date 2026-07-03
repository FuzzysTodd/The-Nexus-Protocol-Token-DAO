from abc import ABCMeta

class EnforceOverridesMeta(ABCMeta):
    def __new__(mcls, name, bases, namespace, **kwargs): ...

class EnforceOverrides(metaclass=EnforceOverridesMeta):
    """Use this as the parent class for your custom classes"""
