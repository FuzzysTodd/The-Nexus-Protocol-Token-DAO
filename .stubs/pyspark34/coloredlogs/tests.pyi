from _typeshed import Incomplete
from collections.abc import Generator
from coloredlogs import CHROOT_FILES as CHROOT_FILES, ColoredFormatter as ColoredFormatter, NameNormalizer as NameNormalizer, decrease_verbosity as decrease_verbosity, find_defined_levels as find_defined_levels, find_handler as find_handler, find_hostname as find_hostname, find_program_name as find_program_name, find_username as find_username, get_level as get_level, increase_verbosity as increase_verbosity, install as install, is_verbose as is_verbose, level_to_number as level_to_number, match_stream_handler as match_stream_handler, parse_encoded_styles as parse_encoded_styles, set_level as set_level, walk_propagation_tree as walk_propagation_tree
from coloredlogs.converter import ColoredCronMailer as ColoredCronMailer, EIGHT_COLOR_PALETTE as EIGHT_COLOR_PALETTE, capture as capture, convert as convert
from coloredlogs.demo import demonstrate_colored_logging as demonstrate_colored_logging
from coloredlogs.syslog import SystemLogging as SystemLogging, is_syslog_supported as is_syslog_supported, match_syslog_handler as match_syslog_handler
from humanfriendly.testing import TestCase

PLAIN_TEXT_PATTERN: Incomplete
PATTERN_INCLUDING_MILLISECONDS: Incomplete

def setUpModule() -> None:
    """Speed up the tests by disabling the demo's artificial delay."""

class ColoredLogsTestCase(TestCase):
    """Container for the `coloredlogs` tests."""
    def find_system_log(self):
        """Find the system log file or skip the current test."""
    def test_level_to_number(self) -> None:
        """Make sure :func:`level_to_number()` works as intended."""
    def test_find_hostname(self) -> None:
        """Make sure :func:`~find_hostname()` works correctly."""
    def test_host_name_filter(self) -> None:
        """Make sure :func:`install()` integrates with :class:`~coloredlogs.HostNameFilter()`."""
    def test_program_name_filter(self) -> None:
        """Make sure :func:`install()` integrates with :class:`~coloredlogs.ProgramNameFilter()`."""
    def test_username_filter(self) -> None:
        """Make sure :func:`install()` integrates with :class:`~coloredlogs.UserNameFilter()`."""
    def test_system_logging(self):
        """Make sure the :class:`coloredlogs.syslog.SystemLogging` context manager works."""
    def test_system_logging_override(self) -> None:
        """Make sure the :class:`coloredlogs.syslog.is_syslog_supported` respects the override."""
    def test_syslog_shortcut_simple(self):
        """Make sure that ``coloredlogs.install(syslog=True)`` works."""
    def test_syslog_shortcut_enhanced(self):
        """Make sure that ``coloredlogs.install(syslog='warning')`` works."""
    def test_name_normalization(self) -> None:
        """Make sure :class:`~coloredlogs.NameNormalizer` works as intended."""
    def test_style_parsing(self):
        """Make sure :func:`~coloredlogs.parse_encoded_styles()` works as intended."""
    def test_is_verbose(self) -> None:
        """Make sure is_verbose() does what it should :-)."""
    def test_increase_verbosity(self) -> None:
        """Make sure increase_verbosity() respects default and custom levels."""
    def test_decrease_verbosity(self) -> None:
        """Make sure decrease_verbosity() respects default and custom levels."""
    def test_level_discovery(self) -> None:
        """Make sure find_defined_levels() always reports the levels defined in Python's standard library."""
    def test_walk_propagation_tree(self) -> None:
        """Make sure walk_propagation_tree() properly walks the tree of loggers."""
    def test_find_handler(self):
        """Make sure find_handler() works as intended."""
    def get_logger_tree(self):
        """Create and return a tree of loggers."""
    def test_support_for_milliseconds(self) -> None:
        """Make sure milliseconds are hidden by default but can be easily enabled."""
    def test_support_for_milliseconds_directive(self) -> None:
        """Make sure milliseconds using the ``%f`` directive are supported."""
    def test_plain_text_output_format(self) -> None:
        """Inspect the plain text output of coloredlogs."""
    def test_dynamic_stderr_lookup(self) -> None:
        """Make sure coloredlogs.install() uses StandardErrorHandler when possible."""
    def test_force_enable(self) -> None:
        """Make sure ANSI escape sequences can be forced (bypassing auto-detection)."""
    def test_auto_disable(self) -> None:
        """
        Make sure ANSI escape sequences are not emitted when logging output is being redirected.

        This is a regression test for https://github.com/xolox/python-coloredlogs/issues/100.

        It works as follows:

        1. We mock an interactive terminal using 'capturer' to ensure that this
           test works inside test drivers that capture output (like pytest).

        2. We launch a subprocess (to ensure a clean process state) where
           stderr is captured but stdout is not, emulating issue #100.

        3. The output captured on stderr contained ANSI escape sequences after
           this test was written and before the issue was fixed, so now this
           serves as a regression test for issue #100.
        """
    def test_env_disable(self) -> None:
        """Make sure ANSI escape sequences can be disabled using ``$NO_COLOR``."""
    def test_html_conversion(self) -> None:
        """Check the conversion from ANSI escape sequences to HTML."""
    def test_output_interception(self) -> None:
        """Test capturing of output from external commands."""
    def test_enable_colored_cron_mailer(self) -> None:
        """Test that automatic ANSI to HTML conversion when running under ``cron`` can be enabled."""
    def test_disable_colored_cron_mailer(self) -> None:
        """Test that automatic ANSI to HTML conversion when running under ``cron`` can be disabled."""
    def test_auto_install(self) -> None:
        """Test :func:`coloredlogs.auto_install()`."""
    def test_cli_demo(self) -> None:
        """Test the command line colored logging demonstration."""
    def test_cli_conversion(self) -> None:
        """Test the command line HTML conversion."""
    def test_empty_conversion(self) -> None:
        """
        Test that conversion of empty output produces no HTML.

        This test was added because I found that ``coloredlogs --convert`` when
        used in a cron job could cause cron to send out what appeared to be
        empty emails. On more careful inspection the body of those emails was
        ``<code></code>``. By not emitting the wrapper element when no other
        HTML is generated, cron will not send out an email.
        """
    def test_implicit_usage_message(self) -> None:
        """Test that the usage message is shown when no actions are given."""
    def test_explicit_usage_message(self) -> None:
        """Test that the usage message is shown when ``--help`` is given."""
    def test_custom_record_factory(self):
        """
        Test that custom LogRecord factories are supported.

        This test is a bit convoluted because the logging module suppresses
        exceptions. We monkey patch the method suspected of encountering
        exceptions so that we can tell after it was called whether any
        exceptions occurred (despite the exceptions not propagating).
        """

def check_contents(filename, contents, match) -> None:
    """Check if a line in a file contains an expected string."""
def main(*arguments, **options):
    """Wrap the command line interface to make it easier to test."""
def cleanup_handlers() -> Generator[None, None, None]:
    """Context manager to cleanup output handlers."""
