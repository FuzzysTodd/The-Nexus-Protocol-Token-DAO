from .templateexporter import TemplateExporter as TemplateExporter

class PythonExporter(TemplateExporter):
    """
    Exports a Python code file.
    Note that the file produced will have a shebang of '#!/usr/bin/env python'
    regardless of the actual python version used in the notebook.
    """
    output_mimetype: str
