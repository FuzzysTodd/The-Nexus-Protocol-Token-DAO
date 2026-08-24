from .base import Preprocessor
from _typeshed import Incomplete

__all__ = ['SanitizeHTML']

class SanitizeHTML(Preprocessor):
    """A preprocessor to sanitize html."""
    attributes: Incomplete
    tags: Incomplete
    styles: Incomplete
    strip: Incomplete
    strip_comments: Incomplete
    safe_output_keys: Incomplete
    sanitized_output_types: Incomplete
    def preprocess_cell(self, cell, resources, cell_index):
        """
        Sanitize potentially-dangerous contents of the cell.

        Cell Types:
          raw:
            Sanitize literal HTML
          markdown:
            Sanitize literal HTML
          code:
            Sanitize outputs that could result in code execution
        """
    def sanitize_code_outputs(self, outputs):
        """
        Sanitize code cell outputs.

        Removes 'text/javascript' fields from display_data outputs, and
        runs `sanitize_html_tags` over 'text/html'.
        """
    def sanitize_html_tags(self, html_str):
        """
        Sanitize a string containing raw HTML tags.
        """
