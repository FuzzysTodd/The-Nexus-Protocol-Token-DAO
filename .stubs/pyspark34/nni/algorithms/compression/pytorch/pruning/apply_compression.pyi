from _typeshed import Incomplete

logger: Incomplete

def apply_compression_results(model, masks_file, map_location: Incomplete | None = None) -> None:
    """
    Apply the masks from ```masks_file``` to the model
    Note: this API is for inference, because it simply multiplies weights with
    corresponding masks when this API is called.

    Parameters
    ----------
    model : torch.nn.Module
        The model to be compressed
    masks_file : str
        The path of the mask file
    map_location : str
        the device on which masks are placed, same to map_location in ```torch.load```
    """
