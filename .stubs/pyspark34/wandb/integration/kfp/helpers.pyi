def add_wandb_visualization(run, mlpipeline_ui_metadata_path):
    """NOTE: To use this, you must modify your component to have an output called `mlpipeline_ui_metadata_path` AND call `wandb.init` yourself inside that component.

    Example usage:

    def my_component(..., mlpipeline_ui_metadata_path: OutputPath()):
        import wandb
        from wandb.integration.kfp.helpers import add_wandb_visualization

        with wandb.init() as run:
            add_wandb_visualization(run, mlpipeline_ui_metadata_path)

            ... # the rest of your code here
    """
