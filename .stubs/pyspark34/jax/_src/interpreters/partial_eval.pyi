import inspect
from _typeshed import Incomplete
from collections.abc import Generator, Hashable, Sequence
from contextlib import AbstractContextManager
from jax._src import ad_util as ad_util, api_util as api_util, core as core, dtypes as dtypes, effects as effects, linear_util as lu, profiler as profiler, source_info_util as source_info_util
from jax._src.api_util import flatten_fun_nokwargs as flatten_fun_nokwargs, flattened_fun_in_tree as flattened_fun_in_tree, fun_sourceinfo as fun_sourceinfo
from jax._src.config import config as config
from jax._src.core import AbstractValue as AbstractValue, Atom as Atom, ClosedJaxpr as ClosedJaxpr, ConcreteArray as ConcreteArray, DBIdx as DBIdx, DShapedArray as DShapedArray, DropVar as DropVar, InDBIdx as InDBIdx, InputType as InputType, Jaxpr as Jaxpr, JaxprEqn as JaxprEqn, Literal as Literal, OutDBIdx as OutDBIdx, OutputType as OutputType, Primitive as Primitive, ShapedArray as ShapedArray, Trace as Trace, Tracer as Tracer, Var as Var, get_aval as get_aval, get_referent as get_referent, mapped_aval as mapped_aval, new_jaxpr_eqn as new_jaxpr_eqn, raise_to_shaped as raise_to_shaped, unmapped_aval as unmapped_aval
from jax._src.state.types import AbstractRef as AbstractRef
from jax._src.tree_util import KeyPath as KeyPath, PyTreeDef as PyTreeDef, generate_key_paths as generate_key_paths, keystr as keystr, tree_unflatten as tree_unflatten, treedef_tuple as treedef_tuple
from jax._src.util import OrderedSet as OrderedSet, as_hashable_function as as_hashable_function, merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, toposort as toposort, unzip2 as unzip2, weakref_lru_cache as weakref_lru_cache
from typing import Any, Callable, NamedTuple
from weakref import ref

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

def identity(x): ...
TracerId = int
AvalId = int
ConstId = int

class PartialVal(tuple):
    """Partial value: either a known value or an unknown (abstract) value.

  Represented as a pair `(aval_opt, const)` of one of two kinds:
  * `(None, <Constant>)` indicates a known value, where the constant is either a
    Tracer or satisfies `core.valid_jaxtype(const)`;
  * `(<AbstractValue>, None)` indicates an unknown value characterized by an
    abstract value.
  """
    def __new__(cls, xs: tuple[AbstractValue | None, core.Value]): ...
    @classmethod
    def known(cls, const: core.Value) -> PartialVal: ...
    @classmethod
    def unknown(cls, aval: AbstractValue) -> PartialVal: ...
    def is_known(self) -> bool: ...
    def get_known(self) -> core.Value | None:
        """Get the known value, if known, else None."""
    def get_aval(self) -> AbstractValue:
        """Get AbstractValue directly (if unknown) or from the constant (known)."""

class JaxprTrace(Trace['JaxprTracer']):
    name_stack: Incomplete
    def __init__(self, *args, name_stack: source_info_util.NameStack) -> None: ...
    def pure(self, val: Any) -> JaxprTracer: ...
    def lift(self, val: Tracer) -> JaxprTracer: ...
    def sublift(self, val: JaxprTracer) -> JaxprTracer: ...
    def new_const(self, val) -> JaxprTracer: ...
    def new_instantiated_literal(self, val) -> JaxprTracer: ...
    def new_instantiated_const(self, val) -> JaxprTracer: ...
    def new_arg(self, pval: PartialVal) -> JaxprTracer: ...
    def instantiate_const(self, tracer: JaxprTracer) -> JaxprTracer: ...
    def instantiate_const_abstracted(self, tracer) -> JaxprTracer: ...
    def process_primitive(self, primitive, tracers, params): ...
    def default_process_primitive(self, primitive, tracers, params): ...
    def process_call(self, primitive, f, tracers, params): ...
    def process_map(self, primitive, f: lu.WrappedFun, tracers, params): ...
    def post_process_call(self, primitive, out_tracers, params): ...
    def post_process_map(self, primitive, out_tracers, params): ...
    def process_custom_jvp_call(self, prim, fun, jvp, tracers, *, symbolic_zeros): ...
    def post_process_custom_jvp_call(self, out_tracers, _) -> None: ...
    def process_custom_transpose(self, prim, call, tracers, **params): ...
    def process_custom_vjp_call(self, prim, f, fwd, bwd, tracers, out_trees, symbolic_zeros): ...
    def post_process_custom_vjp_call(self, out_tracers, _) -> None: ...

def partition_pvals(pvals: list[PartialVal]) -> tuple[list[bool], list[AbstractValue], list[Any]]: ...
def partial_eval_wrapper_nounits(in_knowns: Sequence[bool], in_avals: Sequence[AbstractValue], *in_consts: Any): ...
def trace_to_subjaxpr_nounits_dyn(main: core.MainTrace, in_knowns: Sequence[bool], in_type: InputType, instantiate: bool | Sequence[bool], *in_consts: Any): ...

custom_partial_eval_rules: dict[Primitive, Callable]
call_partial_eval_rules: dict[Primitive, Callable]
call_param_updaters: dict[Primitive, Callable]

def abstract_eval_fun(fun, *avals, debug_info: Incomplete | None = None, **params): ...

JaxprTracerRecipe: Incomplete

class JaxprTracer(Tracer):
    pval: Incomplete
    recipe: Incomplete
    def __init__(self, trace: JaxprTrace, pval: PartialVal, recipe: JaxprTracerRecipe | None) -> None: ...
    @property
    def aval(self) -> AbstractValue: ...
    @property
    def parents(self) -> Sequence[JaxprTracer]: ...
    def full_lower(self): ...
    def is_known(self): ...
    def get_referent(self): ...

def trace_to_jaxpr(fun: lu.WrappedFun, pvals: Sequence[PartialVal], instantiate: bool | Sequence[bool] = False) -> tuple[Jaxpr, list[PartialVal], list[core.Value]]:
    """
  Partially evaluate a function, building a jaxpr for un-evaluated computation.

  Args:
    fun: lu.WrappedFun representing the function to be partially evaluated. The
      function must be flattened, in the sense of accepting jaxpr type arguments
      and returning a flat list of jaxpr type outputs.
    pvals: sequence of PartialVals of length equal to the number of inputs to
      `fun` indicating which inputs are known or unknown.
    instantiate: optional bool or sequence of bools of length equal to the
      number of outputs of `fun` indicating which outputs should be forced to be
      treated as unknown and hence instantiated in the jaxpr. If a single bool,
      the value is applied to all outputs. Default False.

  Returns:
    A triple where the first element is a jaxpr representing the computation
    which depends on unknown inputs; the second element is a list of PartialVals
    of length equal to the length of the output of `fun` representing which
    outputs are known and unknown (along with their values and abstract values,
    respectively); the third element is a list of known residual values. The
    returned jaxpr takes as inputs the known residual values followed by values
    of the originally unknown inputs.
  """
def trace_to_jaxpr_nounits(fun: lu.WrappedFun, pvals: Sequence[PartialVal], instantiate: bool | Sequence[bool] = False) -> tuple[Jaxpr, list[PartialVal], list[core.Value]]: ...
def trace_to_subjaxpr_nounits(main: core.MainTrace, instantiate: bool | Sequence[bool], in_pvals: Sequence[PartialVal]): ...
def trace_to_subjaxpr_nounits_fwd(main: core.MainTrace, instantiate: bool | Sequence[bool], in_pvals: Sequence[PartialVal]): ...

class FreeVar(NamedTuple):
    val: Incomplete

class ConstVar(NamedTuple):
    val: Incomplete

class LambdaBinding(NamedTuple): ...

class JaxprEqnRecipe(NamedTuple):
    eqn_id: Any
    in_tracers: Sequence[JaxprTracer]
    out_tracer_refs: Sequence[ref[JaxprTracer]]
    out_avals: Sequence[core.AbstractValue]
    primitive: Primitive
    params: dict[str, Any]
    effects: core.Effects
    source_info: source_info_util.SourceInfo

def new_eqn_recipe(in_tracers: Sequence[JaxprTracer], out_tracers: Sequence[JaxprTracer], primitive: Primitive, params: dict[str, Any], effects: core.Effects, source_info: source_info_util.SourceInfo) -> JaxprEqnRecipe: ...
def recipe_to_eqn(getvar: Callable[[JaxprTracer], Atom], recipe: JaxprEqnRecipe) -> core.JaxprEqn: ...
def tracers_to_jaxpr(in_tracers: Sequence[JaxprTracer], out_tracers: Sequence[JaxprTracer]) -> tuple[Jaxpr, tuple[Any, ...], tuple[Any, ...]]:
    """Constructs Jaxpr given tracers for inputs and outputs.

  Params:
    in_tracers: the tracers that were created for the function inputs
    out_tracers: the tracers that were output by the function.

  Returns: a triple of a `Jaxpr`, a list of constant values corresponding to
    the `constvars` in the returned Jaxps, and a list of environment values.
    The vars for the environment values have been prepended to the Jaxpr's
    `invars`.
  """
def convert_constvars_jaxpr(jaxpr: Jaxpr) -> Jaxpr:
    """Moves the constvars to the start of invars."""
def convert_invars_to_constvars(jaxpr: Jaxpr, n: int) -> Jaxpr:
    """Move n invars to constvars. Like an inverse of convert_constvars_Jaxpr."""
def convert_envvars_to_constvars(jaxpr: Jaxpr, num_env_vars: int) -> Jaxpr: ...
def partial_eval_jaxpr_nounits(jaxpr: ClosedJaxpr, unknowns: Sequence[bool], instantiate: bool | Sequence[bool]) -> tuple[ClosedJaxpr, ClosedJaxpr, list[bool], list[AbstractValue]]:
    """Unzip a jaxpr in two by data dependence into 'known' and 'unknown' parts.

  That is, given a jaxpr and a sequence of booleans indicating which jaxpr
  inputs (i.e. invars) are considered unknown, produce two jaxprs, a list of
  booleans representing which of the original jaxpr's outputs are unknown (i.e.
  have a data dependence on an unknown input), and a list of abstract values
  representing residuals (part of the first jaxpr's output and the second
  jaxpr's input). The two jaxprs result from partitioning the original jaxpr's
  first-order primitive applications based on whether all the inputs to the
  application are known (in which case the application is represented in the
  'known' jaxpr and its result is considered known) or whether any inputs to the
  application are unknown (in which case the application is represented in the
  'unknown' jaxpr and its result is considered unknown). Higher-order primitives
  are recursively unzipped in two.

  The `instantiate` argument can be used to ensure some outputs are lifted into
  the 'unknown' jaxpr.

  For example, give an input jaxpr:

    { lambda ; a:f32[] b:f32[]. let
        c:f32[] = cos a
        d:f32[] = sin a
        e:f32[] = neg d
        f:f32[] = mul e b
      in (c, f) }

  then applying this function with `unknowns=[False, True]` and
  `instantiate=False` produces as an output triple:

    # jaxpr_known
    { lambda ; a:f32[]. let
       b:f32[] = cos a
       c:f32[] = sin a
       d:f32[] = neg c
     in (b, d) }

    # jaxpr_unknown
    { lambda ; a:f32[] b:f32[]. let c:f32[] = mul b a in (c,) }

    # out_unknowns
    [False, True]

  Notice in particular that the first output (jaxpr_known) contains all the
  primitive applications which do not have a data dependence on an unknown
  input. Also notice the input and output types: the input type of the first
  jaxpr produced represents the type of the known inputs of the original jaxpr,
  and the output type of the second jaxpr produced represents the type of the
  unknown outputs of the original jaxpr.

  In the above example, the output of jaxpr_known named `d` is a _residual_
  output, and corresponds to the input named `a` in jaxpr_unknown. In general,
  jaxpr_known will produce extra outputs (at the end of its output list)
  corresponding to intermediate values of the original jaxpr which must be
  passed to jaxpr_unknown (as leading inputs).
  """
def partial_eval_jaxpr_custom(jaxpr: Jaxpr, in_unknowns: Sequence[bool], in_inst: bool | Sequence[bool], ensure_out_unknowns: bool | Sequence[bool], ensure_out_inst: bool | Sequence[bool], saveable: Callable[..., RematCases_]) -> tuple[Jaxpr, Jaxpr, list[bool], list[bool], int]: ...
def partial_eval_jaxpr_stateful(jaxpr: Jaxpr, in_unknowns: Sequence[bool], in_inst: bool | Sequence[bool], ensure_out_unknowns: bool | Sequence[bool], ensure_out_inst: bool | Sequence[bool], saveable: Callable[..., RematCases_]) -> tuple[Jaxpr, Jaxpr, list[bool], list[bool], int, int]: ...
MemoryKind = str

class RecomputeType: ...

Recompute: Incomplete

class SaveableType: ...

Saveable: Incomplete

class Offloadable(NamedTuple):
    src: MemoryKind
    dst: MemoryKind
RematCases = RecomputeType | SaveableType | Offloadable
RematCases_ = RematCases | bool

def ensure_enum(case: bool | RematCases) -> RematCases: ...
PartialEvalCustomResult = tuple[JaxprEqn | None, JaxprEqn | None, Sequence[bool], Sequence[bool], list[Var]]
PartialEvalCustomRule = Callable[[Callable[..., RematCases_], Sequence[bool], Sequence[bool], JaxprEqn], PartialEvalCustomResult]
partial_eval_jaxpr_custom_rules: dict[Primitive, PartialEvalCustomRule]

def partial_eval_jaxpr_custom_rule_not_implemented(name: str, saveable: Callable[..., RematCases_], unks_in: Sequence[bool], inst_in: Sequence[bool], eqn: JaxprEqn) -> PartialEvalCustomResult: ...
ParamsUpdater = Callable[[Sequence[bool], Sequence[bool], Sequence[bool], Sequence[bool], int, dict, dict], tuple[dict, dict]]
ResAvalUpdater = Callable[[dict[str, Any], AbstractValue], AbstractValue]

def trivial_ctx(_) -> Generator[None, None, None]: ...
def call_partial_eval_custom_rule(jaxpr_param_name: str, params_updater: ParamsUpdater, saveable: Callable[..., RematCases_], unks_in: list[bool], inst_in: list[bool], eqn: JaxprEqn, *, res_aval: ResAvalUpdater = ..., ctx: Callable[[core.ParamDict], AbstractContextManager[None]] = ...) -> tuple[JaxprEqn, JaxprEqn, Sequence[bool], Sequence[bool], list[Var]]: ...
def closed_call_partial_eval_custom_rule(jaxpr_param_name: str, params_updater: ParamsUpdater, saveable: Callable[..., RematCases_], unks_in: list[bool], inst_in: list[bool], eqn: JaxprEqn, *, res_aval: ResAvalUpdater = ...) -> tuple[JaxprEqn, JaxprEqn, Sequence[bool], Sequence[bool], list[Var]]: ...
def dce_jaxpr(jaxpr: Jaxpr, used_outputs: Sequence[bool], instantiate: bool | Sequence[bool] = False) -> tuple[Jaxpr, list[bool]]: ...
def dce_jaxpr_consts(jaxpr: Jaxpr, used_outputs: Sequence[bool], instantiate: bool | Sequence[bool] = False) -> tuple[Jaxpr, list[bool], list[bool]]: ...
DCERule = Callable[[list[bool], JaxprEqn], tuple[list[bool], JaxprEqn | None]]
dce_rules: dict[Primitive, DCERule]

def dce_jaxpr_call_rule(used_outputs: list[bool], eqn: JaxprEqn) -> tuple[list[bool], JaxprEqn | None]: ...
def dce_jaxpr_closed_call_rule(used_outputs: list[bool], eqn: JaxprEqn) -> tuple[list[bool], JaxprEqn]: ...
def close_jaxpr(jaxpr: Jaxpr) -> ClosedJaxpr: ...
def move_binders_to_front(closed_jaxpr: ClosedJaxpr, to_move: Sequence[bool]) -> ClosedJaxpr:
    """Reorder `invars` by moving those indicated in `to_move` to the front."""
def move_binders_to_back(closed_jaxpr: ClosedJaxpr, to_move: Sequence[bool]) -> ClosedJaxpr:
    """Reorder `invars` by moving those indicated in `to_move` to the back."""

class DynamicJaxprTracer(core.Tracer):
    aval: Incomplete
    def __init__(self, trace, aval, line_info: Incomplete | None = None) -> None: ...
    def full_lower(self): ...
    def get_referent(self): ...

def make_jaxpr_effects(constvars, invars, outvars, eqns) -> effects.Effects: ...

class JaxprStackFrame:
    gensym: Callable[[AbstractValue], Var]
    tracer_to_var: dict[TracerId, Var]
    constid_to_tracer: dict[ConstId, Tracer]
    constvar_to_val: dict[Var, Any]
    tracers: list[DynamicJaxprTracer]
    eqns: list[JaxprEqn]
    invars: list[Var]
    effects: core.Effects
    debug_info: DebugInfo | None
    def __init__(self) -> None: ...
    def add_eqn(self, eqn: core.JaxprEqn): ...
    def to_jaxpr(self, out_tracers: Sequence[Tracer]) -> tuple[Jaxpr, list[Any]]: ...
    def to_jaxpr2(self, out_tracers): ...
    def newvar(self, aval): ...
    def find_progenitors(self, tracer): ...
ConstFoldRule = Callable[[list[Any | None], JaxprEqn], tuple[list[Any | None], JaxprEqn | None]]
const_fold_rules: dict[Primitive, ConstFoldRule]
ForwardingRule = Callable[[JaxprEqn], tuple[list[Var | None], JaxprEqn | None]]
forwarding_rules: dict[Primitive, ForwardingRule]

class DynamicJaxprTrace(core.Trace):
    @property
    def frame(self): ...
    def new_arg(self, aval): ...
    def new_const(self, c): ...
    pure = new_const
    lift = new_const
    def sublift(self, t): ...
    def getvar(self, tracer): ...
    def makevar(self, tracer): ...
    def instantiate_const(self, val): ...
    def process_primitive(self, primitive, tracers, params): ...
    def default_process_primitive(self, primitive, tracers, params): ...
    def process_call(self, call_primitive, f, explicit_tracers, params): ...
    def post_process_call(self, call_primitive, out_tracers, params) -> None: ...
    def process_map(self, map_primitive, f, tracers, params): ...
    def post_process_map(self, map_primitive, out_tracers, params) -> None: ...
    def process_custom_jvp_call(self, prim, fun, jvp, tracers, *, symbolic_zeros): ...
    def post_process_custom_jvp_call(self, out_tracers, _) -> None: ...
    def process_custom_vjp_call(self, prim, fun, fwd, bwd, tracers, out_trees, symbolic_zeros): ...
    def post_process_custom_vjp_call(self, out_tracers, _) -> None: ...
    def process_custom_transpose(self, prim, call, tracers, *, transpose, out_types, lin_tree, res_tree, out_tree): ...

custom_staging_rules: dict[Primitive, Callable]

class DebugInfo(NamedTuple):
    func_src_info: str | None
    signature: inspect.Signature | None
    in_tree: PyTreeDef | None
    out_tree: Callable[[], PyTreeDef] | None
    has_kwargs: bool
    traced_for: str

def debug_info(fn: Callable, in_tree: PyTreeDef | None, out_tree_thunk: Callable[[], PyTreeDef] | None, has_kwargs: bool, traced_for: str) -> DebugInfo: ...
def debug_info_final(fn: lu.WrappedFun, traced_for: str) -> DebugInfo:
    """Make a DebugInfo from data available to final-style primitives like pmap."""
def arg_info_all(dbg: DebugInfo) -> list[tuple[str, KeyPath]] | None: ...
def sig_info(dbg: DebugInfo) -> inspect.BoundArguments | None: ...
def result_info(dbg: DebugInfo) -> list[KeyPath] | None: ...
def trace_to_jaxpr_dynamic(fun: lu.WrappedFun, in_avals: Sequence[AbstractValue], debug_info: DebugInfo | None = None, *, keep_inputs: list[bool] | None = None) -> tuple[Jaxpr, list[AbstractValue], list[Any]]: ...
def trace_to_subjaxpr_dynamic(fun: lu.WrappedFun, main: core.MainTrace, in_avals: Sequence[AbstractValue], *, keep_inputs: Sequence[bool] | None = None, debug_info: DebugInfo | None = None) -> tuple[Jaxpr, list[AbstractValue], list[Any]]: ...
def trace_to_jaxpr_dynamic2(fun: lu.WrappedFun, debug_info: DebugInfo | None = None) -> tuple[Jaxpr, OutputType, list[Any]]: ...
def trace_to_subjaxpr_dynamic2(fun: lu.WrappedFun, main: core.MainTrace, debug_info: DebugInfo | None = None) -> tuple[Jaxpr, OutputType, list[Any]]: ...
def extend_jaxpr_stack(main, frame) -> Generator[None, None, None]: ...
def trace_to_jaxpr_final(fun: lu.WrappedFun, in_avals: Sequence[AbstractValue], debug_info: DebugInfo | None = None, keep_inputs: Sequence[bool] | None = None) -> tuple[Jaxpr, list[AbstractValue], list[Any]]: ...
def trace_to_jaxpr_final2(fun: lu.WrappedFun, debug_info: DebugInfo | None = None) -> tuple[Jaxpr, OutputType, list[Any]]: ...
AbstractedAxisName = Hashable
AbstractedAxesSpec = dict[int, AbstractedAxisName] | tuple[AbstractedAxisName, ...]

def infer_lambda_input_type(axes_specs: Sequence[AbstractedAxesSpec] | None, args: Sequence[Any]) -> InputType: ...

class TracerAsName:
    ref: Any
    def __init__(self, tracer) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
Const = Any
Val = Any

def pad_jaxpr(jaxpr: Jaxpr, consts: Sequence[Const]) -> tuple[Jaxpr, list[Const]]: ...

class BoundedAxisSize(NamedTuple):
    val: int | DynamicJaxprTracer
    bound: int

padding_rules: dict[Primitive, Callable]

def def_trivial_padding(prim: Primitive) -> None: ...
def call_padding_rule(prim, in_avals, out_avals, *args, call_jaxpr, **params): ...
def trace_to_subjaxpr(main: core.MainTrace, instantiate: bool | Sequence[bool], pvals: Sequence[PartialVal]): ...

partial_eval_jaxpr: Callable

def instantiate_const_at(trace: JaxprTrace, instantiate: bool, tracer): ...
