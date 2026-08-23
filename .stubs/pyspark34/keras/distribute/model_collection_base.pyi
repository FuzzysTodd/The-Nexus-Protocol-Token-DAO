class ModelAndInput:
    """Base class to provide model and its corresponding inputs."""
    def get_model(self) -> None:
        """Returns a compiled keras model object, together with output name.

        Returns:
          model: a keras model object
          output_name: a string for the name of the output layer
        """
    def get_data(self) -> None:
        """Returns data for training and predicting.

        Returns:
          x_train: data used for training
          y_train: label used for training
          x_predict: data used for predicting
        """
    def get_batch_size(self) -> None:
        """Returns the batch_size used by the model."""
