from .utils import EnvType as EnvType
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from markdown_it import MarkdownIt as MarkdownIt
from markdown_it._compat import DATACLASS_KWARGS as DATACLASS_KWARGS
from typing import Generic, TypeVar, TypedDict

class StateBase:
    env: Incomplete
    md: Incomplete
    def __init__(self, src: str, md: MarkdownIt, env: EnvType) -> None: ...
    @property
    def src(self) -> str: ...
    @src.setter
    def src(self, value: str) -> None: ...
    @property
    def srcCharCode(self) -> tuple[int, ...]: ...

class RuleOptionsType(TypedDict, total=False):
    alt: list[str]
RuleFuncTv = TypeVar('RuleFuncTv')

@dataclass(**DATACLASS_KWARGS)
class Rule(Generic[RuleFuncTv]):
    name: str
    enabled: bool
    fn: RuleFuncTv = ...
    alt: list[str]
    def __init__(self, name, enabled, fn, alt) -> None: ...

class Ruler(Generic[RuleFuncTv]):
    __rules__: Incomplete
    __cache__: Incomplete
    def __init__(self) -> None: ...
    def __find__(self, name: str) -> int:
        """Find rule index by name"""
    def __compile__(self) -> None:
        """Build rules lookup cache"""
    def at(self, ruleName: str, fn: RuleFuncTv, options: RuleOptionsType | None = None) -> None:
        """Replace rule by name with new function & options.

        :param ruleName: rule name to replace.
        :param fn: new rule function.
        :param options: new rule options (not mandatory).
        :raises: KeyError if name not found
        """
    def before(self, beforeName: str, ruleName: str, fn: RuleFuncTv, options: RuleOptionsType | None = None) -> None:
        """Add new rule to chain before one with given name.

        :param beforeName: new rule will be added before this one.
        :param ruleName: new rule will be added before this one.
        :param fn: new rule function.
        :param options: new rule options (not mandatory).
        :raises: KeyError if name not found
        """
    def after(self, afterName: str, ruleName: str, fn: RuleFuncTv, options: RuleOptionsType | None = None) -> None:
        """Add new rule to chain after one with given name.

        :param afterName: new rule will be added after this one.
        :param ruleName: new rule will be added after this one.
        :param fn: new rule function.
        :param options: new rule options (not mandatory).
        :raises: KeyError if name not found
        """
    def push(self, ruleName: str, fn: RuleFuncTv, options: RuleOptionsType | None = None) -> None:
        """Push new rule to the end of chain.

        :param ruleName: new rule will be added to the end of chain.
        :param fn: new rule function.
        :param options: new rule options (not mandatory).

        """
    def enable(self, names: str | Iterable[str], ignoreInvalid: bool = False) -> list[str]:
        """Enable rules with given names.

        :param names: name or list of rule names to enable.
        :param ignoreInvalid: ignore errors when rule not found
        :raises: KeyError if name not found and not ignoreInvalid
        :return: list of found rule names
        """
    def enableOnly(self, names: str | Iterable[str], ignoreInvalid: bool = False) -> list[str]:
        """Enable rules with given names, and disable everything else.

        :param names: name or list of rule names to enable.
        :param ignoreInvalid: ignore errors when rule not found
        :raises: KeyError if name not found and not ignoreInvalid
        :return: list of found rule names
        """
    def disable(self, names: str | Iterable[str], ignoreInvalid: bool = False) -> list[str]:
        """Disable rules with given names.

        :param names: name or list of rule names to enable.
        :param ignoreInvalid: ignore errors when rule not found
        :raises: KeyError if name not found and not ignoreInvalid
        :return: list of found rule names
        """
    def getRules(self, chainName: str = '') -> list[RuleFuncTv]:
        """Return array of active functions (rules) for given chain name.
        It analyzes rules configuration, compiles caches if not exists and returns result.

        Default chain name is `''` (empty string). It can't be skipped.
        That's done intentionally, to keep signature monomorphic for high speed.

        """
    def get_all_rules(self) -> list[str]:
        """Return all available rule names."""
    def get_active_rules(self) -> list[str]:
        """Return the active rule names."""
