from _typeshed import Incomplete
from humanfriendly import InvalidDate as InvalidDate, InvalidLength as InvalidLength, InvalidSize as InvalidSize, InvalidTimespan as InvalidTimespan, Timer as Timer, coerce_boolean as coerce_boolean, coerce_pattern as coerce_pattern, format_length as format_length, format_number as format_number, format_path as format_path, format_size as format_size, format_timespan as format_timespan, parse_date as parse_date, parse_length as parse_length, parse_path as parse_path, parse_size as parse_size, parse_timespan as parse_timespan, prompts as prompts, round_number as round_number
from humanfriendly.case import CaseInsensitiveDict as CaseInsensitiveDict, CaseInsensitiveKey as CaseInsensitiveKey
from humanfriendly.cli import main as main
from humanfriendly.compat import StringIO as StringIO
from humanfriendly.decorators import cached as cached
from humanfriendly.deprecation import DeprecationProxy as DeprecationProxy, define_aliases as define_aliases, deprecated_args as deprecated_args, get_aliases as get_aliases
from humanfriendly.prompts import TooManyInvalidReplies as TooManyInvalidReplies, prompt_for_choice as prompt_for_choice, prompt_for_confirmation as prompt_for_confirmation, prompt_for_input as prompt_for_input
from humanfriendly.sphinx import deprecation_note_callback as deprecation_note_callback, man_role as man_role, pypi_role as pypi_role, setup as setup, special_methods_callback as special_methods_callback, usage_message_callback as usage_message_callback
from humanfriendly.tables import format_pretty_table as format_pretty_table, format_robust_table as format_robust_table, format_rst_table as format_rst_table, format_smart_table as format_smart_table
from humanfriendly.terminal import ANSI_CSI as ANSI_CSI, ANSI_ERASE_LINE as ANSI_ERASE_LINE, ANSI_HIDE_CURSOR as ANSI_HIDE_CURSOR, ANSI_RESET as ANSI_RESET, ANSI_SGR as ANSI_SGR, ANSI_SHOW_CURSOR as ANSI_SHOW_CURSOR, ansi_strip as ansi_strip, ansi_style as ansi_style, ansi_width as ansi_width, ansi_wrap as ansi_wrap, clean_terminal_output as clean_terminal_output, connected_to_terminal as connected_to_terminal, find_terminal_size as find_terminal_size, get_pager_command as get_pager_command, message as message, output as output, show_pager as show_pager, terminal_supports_colors as terminal_supports_colors, warning as warning
from humanfriendly.terminal.html import html_to_ansi as html_to_ansi
from humanfriendly.terminal.spinners import AutomaticSpinner as AutomaticSpinner, Spinner as Spinner
from humanfriendly.testing import CallableTimedOut as CallableTimedOut, CaptureOutput as CaptureOutput, MockedProgram as MockedProgram, PatchedAttribute as PatchedAttribute, PatchedItem as PatchedItem, TemporaryDirectory as TemporaryDirectory, TestCase as TestCase, retry as retry, run_cli as run_cli, skip_on_raise as skip_on_raise, touch as touch
from humanfriendly.text import compact as compact, compact_empty_lines as compact_empty_lines, concatenate as concatenate, dedent as dedent, generate_slug as generate_slug, pluralize as pluralize, random_string as random_string, trim_empty_lines as trim_empty_lines
from humanfriendly.usage import find_meta_variables as find_meta_variables, format_usage as format_usage, parse_usage as parse_usage, render_usage as render_usage

class HumanFriendlyTestCase(TestCase):
    """Container for the `humanfriendly` test suite."""
    def test_case_insensitive_dict(self) -> None:
        """Test the CaseInsensitiveDict class."""
    def test_case_insensitive_key(self) -> None:
        """Test the CaseInsensitiveKey class."""
    def test_capture_output(self) -> None:
        """Test the CaptureOutput class."""
    def test_skip_on_raise(self) -> None:
        """Test the skip_on_raise() decorator."""
    def test_retry_raise(self):
        """Test :func:`~humanfriendly.testing.retry()` based on assertion errors."""
    def test_retry_return(self):
        """Test :func:`~humanfriendly.testing.retry()` based on return values."""
    def test_mocked_program(self) -> None:
        """Test :class:`humanfriendly.testing.MockedProgram`."""
    def test_temporary_directory(self) -> None:
        """Test :class:`humanfriendly.testing.TemporaryDirectory`."""
    def test_touch(self) -> None:
        """Test :func:`humanfriendly.testing.touch()`."""
    def test_patch_attribute(self) -> None:
        """Test :class:`humanfriendly.testing.PatchedAttribute`."""
    def test_patch_item(self) -> None:
        """Test :class:`humanfriendly.testing.PatchedItem`."""
    def test_run_cli_intercepts_exit(self):
        """Test that run_cli() intercepts SystemExit."""
    def test_run_cli_intercepts_error(self) -> None:
        """Test that run_cli() intercepts exceptions."""
    def run_cli_raise_other(self) -> None:
        """run_cli() sample that raises an exception."""
    def test_run_cli_intercepts_output(self):
        """Test that run_cli() intercepts output."""
    def test_caching_decorator(self):
        """Test the caching decorator."""
    def test_compact(self) -> None:
        """Test :func:`humanfriendly.text.compact()`."""
    def test_compact_empty_lines(self) -> None:
        """Test :func:`humanfriendly.text.compact_empty_lines()`."""
    def test_dedent(self) -> None:
        """Test :func:`humanfriendly.text.dedent()`."""
    def test_pluralization(self) -> None:
        """Test :func:`humanfriendly.text.pluralize()`."""
    def test_generate_slug(self) -> None:
        """Test :func:`humanfriendly.text.generate_slug()`."""
    def test_boolean_coercion(self) -> None:
        """Test :func:`humanfriendly.coerce_boolean()`."""
    def test_pattern_coercion(self) -> None:
        """Test :func:`humanfriendly.coerce_pattern()`."""
    def test_format_timespan(self) -> None:
        """Test :func:`humanfriendly.format_timespan()`."""
    def test_parse_timespan(self) -> None:
        """Test :func:`humanfriendly.parse_timespan()`."""
    def test_parse_date(self) -> None:
        """Test :func:`humanfriendly.parse_date()`."""
    def test_format_size(self) -> None:
        """Test :func:`humanfriendly.format_size()`."""
    def test_parse_size(self) -> None:
        """Test :func:`humanfriendly.parse_size()`."""
    def test_format_length(self) -> None:
        """Test :func:`humanfriendly.format_length()`."""
    def test_parse_length(self) -> None:
        """Test :func:`humanfriendly.parse_length()`."""
    def test_format_number(self) -> None:
        """Test :func:`humanfriendly.format_number()`."""
    def test_round_number(self) -> None:
        """Test :func:`humanfriendly.round_number()`."""
    def test_format_path(self) -> None:
        """Test :func:`humanfriendly.format_path()`."""
    def test_parse_path(self) -> None:
        """Test :func:`humanfriendly.parse_path()`."""
    def test_pretty_tables(self) -> None:
        """Test :func:`humanfriendly.tables.format_pretty_table()`."""
    def test_robust_tables(self) -> None:
        """Test :func:`humanfriendly.tables.format_robust_table()`."""
    def test_smart_tables(self) -> None:
        """Test :func:`humanfriendly.tables.format_smart_table()`."""
    def test_rst_tables(self) -> None:
        """Test :func:`humanfriendly.tables.format_rst_table()`."""
    def test_concatenate(self) -> None:
        """Test :func:`humanfriendly.text.concatenate()`."""
    def test_split(self) -> None:
        """Test :func:`humanfriendly.text.split()`."""
    def test_timer(self) -> None:
        """Test :func:`humanfriendly.Timer`."""
    def test_spinner(self) -> None:
        """Test :func:`humanfriendly.Spinner`."""
    def test_automatic_spinner(self) -> None:
        """
        Test :func:`humanfriendly.AutomaticSpinner`.

        There's not a lot to test about the :class:`.AutomaticSpinner` class,
        but by at least running it here we are assured that the code functions
        on all supported Python versions. :class:`.AutomaticSpinner` is built
        on top of the :class:`.Spinner` class so at least we also have the
        tests for the :class:`.Spinner` class to back us up.
        """
    def test_prompt_for_choice(self):
        """Test :func:`humanfriendly.prompts.prompt_for_choice()`."""
    def test_prompt_for_confirmation(self):
        """Test :func:`humanfriendly.prompts.prompt_for_confirmation()`."""
    def test_prompt_for_input(self) -> None:
        """Test :func:`humanfriendly.prompts.prompt_for_input()`."""
    def test_cli(self) -> None:
        """Test the command line interface."""
    def test_ansi_style(self) -> None:
        """Test :func:`humanfriendly.terminal.ansi_style()`."""
    def test_ansi_width(self) -> None:
        """Test :func:`humanfriendly.terminal.ansi_width()`."""
    def test_ansi_wrap(self) -> None:
        """Test :func:`humanfriendly.terminal.ansi_wrap()`."""
    def test_html_to_ansi(self):
        """Test the :func:`humanfriendly.terminal.html_to_ansi()` function."""
    def test_generate_output(self) -> None:
        """Test the :func:`humanfriendly.terminal.output()` function."""
    def test_generate_message(self) -> None:
        """Test the :func:`humanfriendly.terminal.message()` function."""
    def test_generate_warning(self) -> None:
        """Test the :func:`humanfriendly.terminal.warning()` function."""
    def ignore_coverage_warning(self, stream):
        """
        Filter out coverage.py warning from standard error.

        This is intended to remove the following line from the lines captured
        on the standard error stream:

        Coverage.py warning: No data was collected. (no-data-collected)
        """
    def test_clean_output(self) -> None:
        """Test :func:`humanfriendly.terminal.clean_terminal_output()`."""
    def test_find_terminal_size(self) -> None:
        """Test :func:`humanfriendly.terminal.find_terminal_size()`."""
    def test_terminal_capabilities(self) -> None:
        """Test the functions that check for terminal capabilities."""
    def test_show_pager(self) -> None:
        """Test :func:`humanfriendly.terminal.show_pager()`."""
    def test_get_pager_command(self) -> None:
        """Test :func:`humanfriendly.terminal.get_pager_command()`."""
    def test_find_meta_variables(self) -> None:
        """Test :func:`humanfriendly.usage.find_meta_variables()`."""
    def test_parse_usage_simple(self) -> None:
        """Test :func:`humanfriendly.usage.parse_usage()` (a simple case)."""
    def test_parse_usage_tricky(self) -> None:
        """Test :func:`humanfriendly.usage.parse_usage()` (a tricky case)."""
    def test_parse_usage_commas(self) -> None:
        """Test :func:`humanfriendly.usage.parse_usage()` against option labels containing commas."""
    def preprocess_parse_result(self, text):
        """Ignore leading/trailing whitespace in usage parsing tests."""
    def test_format_usage(self) -> None:
        """Test :func:`humanfriendly.usage.format_usage()`."""
    def test_render_usage(self) -> None:
        """Test :func:`humanfriendly.usage.render_usage()`."""
    def test_deprecated_args(self):
        """Test the deprecated_args() decorator function."""
    def test_alias_proxy_deprecation_warning(self) -> None:
        """Test that the DeprecationProxy class emits deprecation warnings."""
    def test_alias_proxy_sphinx_compensation(self) -> None:
        """Test that the DeprecationProxy class emits deprecation warnings."""
    def test_alias_proxy_sphinx_integration(self) -> None:
        """Test that aliases can be injected into generated documentation."""
    callbacks: Incomplete
    roles: Incomplete
    def test_sphinx_customizations(self) -> None:
        """Test the :mod:`humanfriendly.sphinx` module."""
    def docstring_is_reformatted(self, entity):
        """Check whether :func:`.usage_message_callback()` reformats a module's docstring."""

def normalize_timestamp(value, ndigits: int = 1):
    """
    Round timestamps to the given number of digits.

    This helps to make the test suite less sensitive to timing issues caused by
    multitasking, processor scheduling, etc.
    """
