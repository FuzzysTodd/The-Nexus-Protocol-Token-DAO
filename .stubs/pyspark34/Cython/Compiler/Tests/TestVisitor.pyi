from Cython.Compiler.ModuleNode import ModuleNode as ModuleNode
from Cython.Compiler.ParseTreeTransforms import AnalyseDeclarationsTransform as AnalyseDeclarationsTransform, AnalyseExpressionsTransform as AnalyseExpressionsTransform, InterpretCompilerDirectives as InterpretCompilerDirectives, NormalizeTree as NormalizeTree
from Cython.Compiler.Symtab import ModuleScope as ModuleScope
from Cython.Compiler.Visitor import MethodDispatcherTransform as MethodDispatcherTransform
from Cython.TestUtils import TransformTest as TransformTest

class TestMethodDispatcherTransform(TransformTest):
    def test_builtin_method(self): ...
    def test_binop_method(self): ...
