def clone_keras_layers(model, start_layer, stop_layer):
    """ Clones the keras layers between the start and stop layer as a new model.
        """
def split_keras_model(model, layer):
    """ Splits the keras model around layer into two models.

    This is done such that model2(model1(X)) = model(X)
    and mode11(X) == layer(X)
    """
