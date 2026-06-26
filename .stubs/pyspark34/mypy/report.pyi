import abc
import collections
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mypy import stats as stats
from mypy.defaults import REPORTER_NAMES as REPORTER_NAMES
from mypy.nodes import Expression as Expression, FuncDef as FuncDef, MypyFile as MypyFile
from mypy.options import Options as Options
from mypy.traverser import TraverserVisitor as TraverserVisitor
from mypy.types import Type as Type, TypeOfAny as TypeOfAny
from mypy.version import __version__ as __version__
from typing import Any, Callable, Iterator
from typing_extensions import Final, TypeAlias as _TypeAlias

LXML_INSTALLED: bool
type_of_any_name_map: Final[collections.OrderedDict[int, str]]
ReporterClasses: _TypeAlias
reporter_classes: Final[ReporterClasses]

class Reports:
    data_dir: Incomplete
    reporters: Incomplete
    named_reporters: Incomplete
    def __init__(self, data_dir: str, report_dirs: dict[str, str]) -> None: ...
    def add_report(self, report_type: str, report_dir: str) -> AbstractReporter: ...
    def file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def finish(self) -> None: ...

class AbstractReporter(metaclass=ABCMeta):
    output_dir: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    @abstractmethod
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    @abstractmethod
    def on_finish(self) -> None: ...

def register_reporter(report_name: str, reporter: Callable[[Reports, str], AbstractReporter], needs_lxml: bool = False) -> None: ...
def alias_reporter(source_reporter: str, target_reporter: str) -> None: ...
def should_skip_path(path: str) -> bool: ...
def iterate_python_lines(path: str) -> Iterator[tuple[int, str]]:
    """Return an iterator over (line number, line text) from a Python file."""

class FuncCounterVisitor(TraverserVisitor):
    counts: Incomplete
    def __init__(self) -> None: ...
    def visit_func_def(self, defn: FuncDef) -> None: ...

class LineCountReporter(AbstractReporter):
    counts: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class AnyExpressionsReporter(AbstractReporter):
    """Report frequencies of different kinds of Any types."""
    counts: Incomplete
    any_types_counter: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class LineCoverageVisitor(TraverserVisitor):
    source: Incomplete
    lines_covered: Incomplete
    def __init__(self, source: list[str]) -> None: ...
    def indentation_level(self, line_number: int) -> int | None:
        """Return the indentation of a line of the source (specified by
        zero-indexed line number). Returns None for blank lines or comments."""
    def visit_func_def(self, defn: FuncDef) -> None: ...

class LineCoverageReporter(AbstractReporter):
    """Exact line coverage reporter.

    This reporter writes a JSON dictionary with one field 'lines' to
    the file 'coverage.json' in the specified report directory. The
    value of that field is a dictionary which associates to each
    source file's absolute pathname the list of line numbers that
    belong to typed functions in that file.
    """
    lines_covered: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class FileInfo:
    name: Incomplete
    module: Incomplete
    counts: Incomplete
    def __init__(self, name: str, module: str) -> None: ...
    def total(self) -> int: ...
    def attrib(self) -> dict[str, str]: ...

class MemoryXmlReporter(AbstractReporter):
    """Internal reporter that generates XML in memory.

    This is used by all other XML-based reporters to avoid duplication.
    """
    xslt_html_path: Incomplete
    xslt_txt_path: Incomplete
    css_html_path: Incomplete
    schema: Incomplete
    last_xml: Incomplete
    files: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    control_fixer: Final[Incomplete]
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

def get_line_rate(covered_lines: int, total_lines: int) -> str: ...

class CoberturaPackage:
    """Container for XML and statistics mapping python modules to Cobertura package."""
    name: Incomplete
    classes: Incomplete
    packages: Incomplete
    total_lines: int
    covered_lines: int
    def __init__(self, name: str) -> None: ...
    def as_xml(self) -> Any: ...
    def add_packages(self, parent_element: Any) -> None: ...

class CoberturaXmlReporter(AbstractReporter):
    """Reporter for generating Cobertura compliant XML."""
    root: Incomplete
    doc: Incomplete
    root_package: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class AbstractXmlReporter(AbstractReporter, metaclass=abc.ABCMeta):
    """Internal abstract class for reporters that work via XML."""
    memory_xml: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...

class XmlReporter(AbstractXmlReporter):
    """Public reporter that exports XML.

    The produced XML files contain a reference to the absolute path
    of the html transform, so they will be locally viewable in a browser.

    However, there is a bug in Chrome and all other WebKit-based browsers
    that makes it fail from file:// URLs but work on http:// URLs.
    """
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class XsltHtmlReporter(AbstractXmlReporter):
    """Public reporter that exports HTML via XSLT.

    This is slightly different than running `xsltproc` on the .xml files,
    because it passes a parameter to rewrite the links.
    """
    xslt_html: Incomplete
    param_html: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class XsltTxtReporter(AbstractXmlReporter):
    """Public reporter that exports TXT via XSLT.

    Currently this only does the summary, not the individual reports.
    """
    xslt_txt: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...

class LinePrecisionReporter(AbstractReporter):
    """Report per-module line counts for typing precision.

    Each line is classified into one of these categories:

    * precise (fully type checked)
    * imprecise (Any types in a type component, such as List[Any])
    * any (something with an Any type, implicit or explicit)
    * empty (empty line, comment or docstring)
    * unanalyzed (mypy considers line unreachable)

    The meaning of these categories varies slightly depending on
    context.
    """
    files: Incomplete
    def __init__(self, reports: Reports, output_dir: str) -> None: ...
    def on_file(self, tree: MypyFile, modules: dict[str, MypyFile], type_map: dict[Expression, Type], options: Options) -> None: ...
    def on_finish(self) -> None: ...
