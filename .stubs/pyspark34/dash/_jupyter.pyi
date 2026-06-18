from _typeshed import Incomplete

JupyterDisplayMode: Incomplete

class JupyterDash:
    """
    Interact with dash apps inside jupyter notebooks.
    """
    default_mode: JupyterDisplayMode
    alive_token: Incomplete
    inline_exceptions: bool
    def infer_jupyter_proxy_config(self) -> None:
        """
        Infer the current Jupyter server configuration. This will detect
        the proper request_pathname_prefix and server_url values to use when
        displaying Dash apps.Dash requests will be routed through the proxy.

        Requirements:

        In the classic notebook, this method requires the `dash` nbextension
        which should be installed automatically with the installation of the
        jupyter-dash Python package. You can see what notebook extensions are installed
        by running the following command:
            $ jupyter nbextension list

        In JupyterLab, this method requires the `@plotly/dash-jupyterlab` labextension. This
        extension should be installed automatically with the installation of the
        jupyter-dash Python package, but JupyterLab must be allowed to rebuild before
        the extension is activated (JupyterLab should automatically detect the
        extension and produce a popup dialog asking for permission to rebuild). You can
        see what JupyterLab extensions are installed by running the following command:
            $ jupyter labextension list
        """
    in_ipython: Incomplete
    in_colab: Incomplete
    def __init__(self) -> None: ...
    def run_app(self, app, mode: JupyterDisplayMode = None, width: str = '100%', height: int = 650, host: str = '127.0.0.1', port: int = 8050, server_url: Incomplete | None = None):
        '''
        :type app: dash.Dash
        :param mode: How to display the app on the notebook. One Of:
            ``"external"``: The URL of the app will be displayed in the notebook
                output cell. Clicking this URL will open the app in the default
                web browser.
            ``"inline"``: The app will be displayed inline in the notebook output cell
                in an iframe.
            ``"jupyterlab"``: The app will be displayed in a dedicate tab in the
                JupyterLab interface. Requires JupyterLab and the `jupyterlab-dash`
                extension.
        :param width: Width of app when displayed using mode="inline"
        :param height: Height of app when displayed using mode="inline"
        :param host: Host of the server
        :param port: Port used by the server
        :param server_url: Use if a custom url is required to display the app.
        '''
    @staticmethod
    def serve_alive(): ...
    def configure_callback_exception_handling(self, app, dev_tools_prune_errors):
        """Install traceback handling for callbacks"""
    @property
    def active(self): ...

jupyter_dash: Incomplete
