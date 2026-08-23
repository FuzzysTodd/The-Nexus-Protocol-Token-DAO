import gradio as gr
from .utils import experimental as experimental, is_gradio_available as is_gradio_available
from _typeshed import Incomplete
from typing import Callable

class WebhooksServer:
    '''
    The [`WebhooksServer`] class lets you create an instance of a Gradio app that can receive Huggingface webhooks.
    These webhooks can be registered using the [`~WebhooksServer.add_webhook`] decorator. Webhook endpoints are added to
    the app as a POST endpoint to the FastAPI router. Once all the webhooks are registered, the `run` method has to be
    called to start the app.

    It is recommended to accept [`WebhookPayload`] as the first argument of the webhook function. It is a Pydantic
    model that contains all the information about the webhook event. The data will be parsed automatically for you.

    Check out the [webhooks guide](../guides/webhooks_server) for a step-by-step tutorial on how to setup your
    WebhooksServer and deploy it on a Space.

    <Tip warning={true}>

    `WebhooksServer` is experimental. Its API is subject to change in the future.

    </Tip>

    <Tip warning={true}>

    You must have `gradio` installed to use `WebhooksServer` (`pip install --upgrade gradio`).

    </Tip>

    Args:
        ui (`gradio.Blocks`, optional):
            A Gradio UI instance to be used as the Space landing page. If `None`, a UI displaying instructions
            about the configured webhooks is created.
        webhook_secret (`str`, optional):
            A secret key to verify incoming webhook requests. You can set this value to any secret you want as long as
            you also configure it in your [webhooks settings panel](https://huggingface.co/settings/webhooks). You
            can also set this value as the `WEBHOOK_SECRET` environment variable. If no secret is provided, the
            webhook endpoints are opened without any security.

    Example:

        ```python
        import gradio as gr
        from huggingface_hub import WebhooksServer, WebhookPayload

        with gr.Blocks() as ui:
            ...

        app = WebhooksServer(ui=ui, webhook_secret="my_secret_key")

        @app.add_webhook("/say_hello")
        async def hello(payload: WebhookPayload):
            return {"message": "hello"}

        app.run()
        ```
    '''
    def __new__(cls, *args, **kwargs) -> WebhooksServer: ...
    webhook_secret: Incomplete
    registered_webhooks: Incomplete
    def __init__(self, ui: gr.Blocks | None = None, webhook_secret: str | None = None) -> None: ...
    def add_webhook(self, path: str | None = None) -> Callable:
        '''
        Decorator to add a webhook to the [`WebhooksServer`] server.

        Args:
            path (`str`, optional):
                The URL path to register the webhook function. If not provided, the function name will be used as the
                path. In any case, all webhooks are registered under `/webhooks`.

        Raises:
            ValueError: If the provided path is already registered as a webhook.

        Example:
            ```python
            from huggingface_hub import WebhooksServer, WebhookPayload

            app = WebhooksServer()

            @app.add_webhook
            async def trigger_training(payload: WebhookPayload):
                if payload.repo.type == "dataset" and payload.event.action == "update":
                    # Trigger a training job if a dataset is updated
                    ...

            app.run()
        ```
        '''
    def run(self) -> None:
        """Starts the Gradio app with the FastAPI server and registers the webhooks."""

def webhook_endpoint(path: str | None = None) -> Callable:
    '''Decorator to start a [`WebhooksServer`] and register the decorated function as a webhook endpoint.

    This is a helper to get started quickly. If you need more flexibility (custom landing page or webhook secret),
    you can use [`WebhooksServer`] directly. You can register multiple webhook endpoints (to the same server) by using
    this decorator multiple times.

    Check out the [webhooks guide](../guides/webhooks_server) for a step-by-step tutorial on how to setup your
    server and deploy it on a Space.

    <Tip warning={true}>

    `webhook_endpoint` is experimental. Its API is subject to change in the future.

    </Tip>

    <Tip warning={true}>

    You must have `gradio` installed to use `webhook_endpoint` (`pip install --upgrade gradio`).

    </Tip>

    Args:
        path (`str`, optional):
            The URL path to register the webhook function. If not provided, the function name will be used as the path.
            In any case, all webhooks are registered under `/webhooks`.

    Examples:
        The default usage is to register a function as a webhook endpoint. The function name will be used as the path.
        The server will be started automatically at exit (i.e. at the end of the script).

        ```python
        from huggingface_hub import webhook_endpoint, WebhookPayload

        @webhook_endpoint
        async def trigger_training(payload: WebhookPayload):
            if payload.repo.type == "dataset" and payload.event.action == "update":
                # Trigger a training job if a dataset is updated
                ...

        # Server is automatically started at the end of the script.
        ```

        Advanced usage: register a function as a webhook endpoint and start the server manually. This is useful if you
        are running it in a notebook.

        ```python
        from huggingface_hub import webhook_endpoint, WebhookPayload

        @webhook_endpoint
        async def trigger_training(payload: WebhookPayload):
            if payload.repo.type == "dataset" and payload.event.action == "update":
                # Trigger a training job if a dataset is updated
                ...

        # Start the server manually
        trigger_training.run()
        ```
    '''
