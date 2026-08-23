from _typeshed import Incomplete

class Package:
    name: Incomplete
    subPackages: Incomplete
    modules: Incomplete
    objectsExposed: Incomplete
    classesDefined: Incomplete
    functionsDefined: Incomplete
    constantsDefined: Incomplete
    importedModules: Incomplete
    importedPackages: Incomplete
    def __init__(self, name) -> None: ...
    def toJson(self): ...
    def append_package_or_module(self, metadata, is_package) -> None: ...

class Module:
    name: Incomplete
    functions: Incomplete
    classes: Incomplete
    members: Incomplete
    objectsExposed: Incomplete
    def __init__(self, name) -> None: ...
    def toJson(self): ...

class Class:
    name: Incomplete
    baseClassNames: Incomplete
    innerClasses: Incomplete
    instanceMembers: Incomplete
    staticMembers: Incomplete
    instanceFunctions: Incomplete
    staticFunctions: Incomplete
    def __init__(self, name) -> None: ...
    def toJson(self): ...

class Function:
    signature: Incomplete
    returnType: str
    def __init__(self, signature) -> None: ...
    def toJson(self): ...

class Member:
    name: Incomplete
    type: Incomplete
    def __init__(self, name, tpe: str = '') -> None: ...
    def toJson(self): ...

def FormatFunctionSignature(signature: str): ...
def GetChildren(node): ...
def GetFuncNameBySignature(signature): ...
def IsPrivateName(name: str): ...
