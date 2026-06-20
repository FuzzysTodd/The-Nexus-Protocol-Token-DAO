from _typeshed import Incomplete

ALLOWED_CSS_PROPERTIES: Incomplete
ALLOWED_SVG_PROPERTIES: Incomplete

class CSSSanitizer:
    allowed_css_properties: Incomplete
    allowed_svg_properties: Incomplete
    def __init__(self, allowed_css_properties=..., allowed_svg_properties=...) -> None: ...
    def sanitize_css(self, style):
        """Sanitizes css in style tags"""
