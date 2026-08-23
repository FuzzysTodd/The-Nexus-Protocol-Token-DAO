def load_class_extensions(current_module, extension_key, extension_class_validator) -> None:
    """Load all registered extensions under the `extension_key` namespace in entry_points.

    Attributes:
        current_module: The module itself where extension classes should be added.
        extension_key: The identifier as string for the entry_points to register within the current_module.
        extension_class_validator: A function(class) -> bool, that checks the class for correctness
          before it is registered.
    """
