from nbconvert.utils.base import NbConvertBase as NbConvertBase

class PostProcessorBase(NbConvertBase):
    """The base class for post processors."""
    def __call__(self, input_) -> None:
        """
        See def postprocess() ...
        """
    def postprocess(self, input_) -> None:
        """
        Post-process output from a writer.
        """
