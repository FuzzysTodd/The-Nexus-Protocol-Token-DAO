import os
import torch
from .graph import Graph, PythonCode
from _typeshed import Incomplete
from torch.package import Importer, PackageExporter, PackageImporter
from typing import Any, Dict

__all__ = ['reduce_graph_module', 'reduce_package_graph_module', 'reduce_deploy_graph_module', 'GraphModule']

class _EvalCacheLoader:
    eval_cache: Incomplete
    next_id: int
    def __init__(self) -> None: ...
    def cache(self, src: str, globals: Dict[str, Any]):
        """Store the source in a private cache, and add a lazy entry in linecache
        that allows the source to be retrieved by 'filename'.

        Args:
            src (str): The module source to cache
            globals (dict): The module globals

        Returns:
            str: The cache key (and dummy filename) generated for src.
        """
    def get_source(self, module_name) -> str | None: ...

def reduce_graph_module(body: Dict[Any, Any], import_block: str) -> torch.nn.Module: ...
def reduce_package_graph_module(importer: PackageImporter, body: Dict[Any, Any], generated_module_name: str) -> torch.nn.Module: ...
def reduce_deploy_graph_module(importer: PackageImporter, body: Dict[Any, Any], import_block: str) -> torch.nn.Module: ...

class _WrappedCall:
    cls: Incomplete
    cls_call: Incomplete
    def __init__(self, cls, cls_call) -> None: ...
    def __call__(self, obj, *args, **kwargs): ...

class GraphModule(torch.nn.Module):
    """
    GraphModule is an nn.Module generated from an fx.Graph. Graphmodule has a
    ``graph`` attribute, as well as ``code`` and ``forward`` attributes generated
    from that ``graph``.

    .. warning::

        When ``graph`` is reassigned, ``code`` and ``forward`` will be automatically
        regenerated. However, if you edit the contents of the ``graph`` without reassigning
        the ``graph`` attribute itself, you must call ``recompile()`` to update the generated
        code.
    """
    def __new__(cls, *args, **kwargs): ...
    training: Incomplete
    meta: Incomplete
    def __init__(self, root: torch.nn.Module | Dict[str, Any], graph: Graph, class_name: str = 'GraphModule') -> None:
        """
        Construct a GraphModule.

        Args:

            root (Union[torch.nn.Module, Dict[str, Any]):
                ``root`` can either be an nn.Module instance or a Dict mapping strings to any attribute type.
                In the case that ``root`` is a Module, any references to Module-based objects (via qualified
                name) in the Graph's Nodes' ``target`` field will be copied over from the respective place
                within ``root``'s Module hierarchy into the GraphModule's module hierarchy.
                In the case that ``root`` is a dict, the qualified name found in a Node's ``target`` will be
                looked up directly in the dict's keys. The object mapped to by the Dict will be copied
                over into the appropriate place within the GraphModule's module hierarchy.

            graph (Graph): ``graph`` contains the nodes this GraphModule should use for code generation

            class_name (str): ``name`` denotes the name of this GraphModule for debugging purposes. If it's unset, all
                error messages will report as originating from ``GraphModule``. It may be helpful to set this
                to ``root``'s original name or a name that makes sense within the context of your transform.
        """
    __jit_unused_properties__: Incomplete
    @property
    def graph(self) -> Graph:
        """
        Return the ``Graph`` underlying this ``GraphModule``
        """
    @graph.setter
    def graph(self, g: Graph) -> None:
        """
        Set the underlying ``Graph`` for this ``GraphModule``. This will internally
        recompile the ``GraphModule`` so that the generated ``forward()`` function
        corresponds to ``g``
        """
    def to_folder(self, folder: str | os.PathLike, module_name: str = 'FxModule'):
        """Dumps out module to ``folder`` with ``module_name`` so that it can be
        imported with ``from <folder> import <module_name>``

        Args:

            folder (Union[str, os.PathLike]): The folder to write the code out to

            module_name (str): Top-level name to use for the ``Module`` while
                writing out the code
        """
    def add_submodule(self, target: str, m: torch.nn.Module) -> bool:
        """
        Adds the given submodule to ``self``.

        This installs empty Modules where none exist yet if they are
        subpaths of ``target``.

        Args:
            target: The fully-qualified string name of the new submodule
                (See example in ``nn.Module.get_submodule`` for how to
                specify a fully-qualified string.)
            m: The submodule itself; the actual object we want to
                install in the current Module

        Return:
            bool: Whether or not the submodule could be inserted. For
                this method to return True, each object in the chain
                denoted by ``target`` must either a) not exist yet,
                or b) reference an ``nn.Module`` (not a parameter or
                other attribute)
        """
    def delete_submodule(self, target: str) -> bool:
        """
        Deletes the given submodule from ``self``.

        The module will not be deleted if ``target`` is not a valid
        target.

        Args:
            target: The fully-qualified string name of the new submodule
                (See example in ``nn.Module.get_submodule`` for how to
                specify a fully-qualified string.)

        Returns:
            bool: Whether or not the target string referenced a
                submodule we want to delete. A return value of ``False``
                means that the ``target`` was not a valid reference to
                a submodule.
        """
    def delete_all_unused_submodules(self) -> None:
        '''
        Deletes all unused submodules from ``self``.

        A Module is considered "used" if any one of the following is
        true:
        1. It has children that are used
        2. Its forward is called directly via a ``call_module`` node
        3. It has a non-Module attribute that is used from a
        ``get_attr`` node

        This method can be called to clean up an ``nn.Module`` without
        manually calling ``delete_submodule`` on each unused submodule.
        '''
    @property
    def code(self) -> str:
        """
        Return the Python code generated from the ``Graph`` underlying this
        ``GraphModule``.
        """
    def recompile(self) -> PythonCode:
        """
        Recompile this GraphModule from its ``graph`` attribute. This should be
        called after editing the contained ``graph``, otherwise the generated
        code of this ``GraphModule`` will be out of date.
        """
    def __reduce_deploy__(self, importer: Importer): ...
    def __reduce_package__(self, exporter: PackageExporter): ...
    def __reduce__(self):
        """
        Serialization of GraphModule. We serialize only the generated code, not
        the underlying ``Graph``. This is because ``Graph`` does not have on-disk
        backward-compatibility guarantees, whereas Python source code does.
        On the deserialization side, we symbolically trace through the generated
        code to regenerate the underlying ``Graph``
        """
    def __deepcopy__(self, memo): ...
    def __copy__(self): ...
    def print_readable(self, print_output: bool = True):
        """
        Return the Python code generated for current GraphModule and its children GraphModules
        """
