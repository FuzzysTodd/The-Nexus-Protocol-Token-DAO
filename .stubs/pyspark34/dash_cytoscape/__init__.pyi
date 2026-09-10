from ._imports_ import *
from . import utils as utils
from _typeshed import Incomplete

package: Incomplete
package_name: Incomplete
__version__: Incomplete

def load_extra_layouts() -> None:
    """
    Load 3rd party layouts that are not included by default with Cytoscape. You can find the
    documentation about those layouts here:
        - `cose-bilkent`: https://github.com/cytoscape/cytoscape.js-cose-bilkent
        - `cola`: https://github.com/cytoscape/cytoscape.js-cola
        - `euler`: https://github.com/cytoscape/cytoscape.js-dagre
        - `spread`: https://github.com/cytoscape/cytoscape.js-spread
        - `dagre`: https://github.com/cytoscape/cytoscape.js-dagre
        - `klay`: https://github.com/cytoscape/cytoscape.js-klay

    Example:

    ```
    import dash
    import dash_html_components as html
    import dash_cytoscape as cyto

    cyto.load_extra_layouts()

    app = dash.Dash(__name__)

    app.layout = html.Div([
        cyto.Cytoscape(...),
    ])
    ```

    Be careful about using the extra layouts when not necessary, since they require supplementary
    bandwidth for loading, which impacts the startup time of the app.
    """
