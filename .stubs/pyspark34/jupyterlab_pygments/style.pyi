from _typeshed import Incomplete
from pygments.style import Style

class JupyterStyle(Style):
    '''
    A pygments style using JupyterLab CSS variables.

    The goal is to mimick JupyterLab\'s codemirror theme.

    Known impossibilities:

    - With pygments, the dot in `foo.bar` is considered an Operator (class: \'o\'),
      while in codemirror, it is bare text.
    - With pygments, in both `from foo import bar`, and `foo.bar`, "bar" is
      considered a Name (class: \'n\'), while in coremirror, the latter is a property.

Available CSS variables are

  --jp-mirror-editor-keyword-color
  --jp-mirror-editor-atom-color
  --jp-mirror-editor-number-color
  --jp-mirror-editor-def-color
  --jp-mirror-editor-variable-color
  --jp-mirror-editor-variable-2-color
  --jp-mirror-editor-variable-3-color
  --jp-mirror-editor-punctuation-color
  --jp-mirror-editor-property-color
  --jp-mirror-editor-operator-color
  --jp-mirror-editor-comment-color
  --jp-mirror-editor-string-color
  --jp-mirror-editor-string-2-color
  --jp-mirror-editor-meta-color
  --jp-mirror-editor-qualifier-color
  --jp-mirror-editor-builtin-color
  --jp-mirror-editor-bracket-color
  --jp-mirror-editor-tag-color
  --jp-mirror-editor-attribute-color
  --jp-mirror-editor-header-color
  --jp-mirror-editor-quote-color
  --jp-mirror-editor-link-color
  --jp-mirror-editor-error-color
    '''
    default_style: str
    background_color: str
    highlight_color: str
    styles: Incomplete
