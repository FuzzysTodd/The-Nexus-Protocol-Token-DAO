__all__ = ['ConfigBase']

class ConfigBase:
    """
    The abstract base class of experiment config classes.

    A config class should be a type-hinted dataclass inheriting ``ConfigBase``.
    Or for a training service config class, it can inherit ``TrainingServiceConfig``.

    .. code-block:: python

        @dataclass(init=False)
        class ExperimentConfig(ConfigBase):
            name: Optional[str]
            ...

    Subclasses are suggested to override ``_canonicalize()`` and ``_validate_canonical()`` methods.

    Users can create a config object with constructor or ``ConfigBase.load()``,
    validate its legality with ``ConfigBase.validate()``,
    and finally convert it to the format accepted by NNI manager with ``ConfigBase.json()``.

    Example usage:

    .. code-block:: python

        # when using Python API
        config1 = ExperimentConfig(trialCommand='...', trialConcurrency=1, ...)
        config1.validate()
        print(config1.json())

        # when using config file
        config2 = ExperimentConfig.load('examples/config.yml')
        config2.validate()
        print(config2.json())

    Config objects will remember where they are loaded; therefore relative paths can be resolved smartly.
    If a config object is created with constructor, the base path will be current working directory.
    If it is loaded with ``ConfigBase.load(path)``, the base path will be ``path``'s parent.

    .. attention::

        All the classes that inherit ``ConfigBase`` are not allowed to use ``from __future__ import annotations``,
        because ``ConfigBase`` uses ``typeguard`` to perform runtime check and it does not support lazy annotations.
    """
    def __init__(self, **kwargs) -> None:
        '''
        There are two common ways to use the constructor,
        directly writing kwargs and unpacking from JSON (YAML) object:

        .. code-block:: python

            config1 = AlgorithmConfig(name=\'TPE\', class_args={\'optimize_mode\': \'maximize\'})

            json = {\'name\': \'TPE\', \'classArgs\': {\'optimize_mode\': \'maximize\'}}
            config2 = AlgorithmConfig(**json)

        If the config class has fields whose type is another config class, or list of another config class,
        they will recursively load dict values.

        Because JSON objects can use "camelCase" for field names,
        cases and underscores in ``kwargs`` keys are ignored in this constructor.
        For example if a config class has a field ``hello_world``,
        then using ``hello_world=1``, ``helloWorld=1``, and ``_HELLOWORLD_=1`` in constructor
        will all assign to the same field.

        If ``kwargs`` contain extra keys, `AttributeError` will be raised.

        If ``kwargs`` do not have enough key, missing fields are silently set to `MISSING()`.
        You can use ``utils.is_missing()`` to check them.
        '''
    @classmethod
    def load(cls, path):
        """
        Load a YAML config file from file system.

        Since YAML is a superset of JSON, it can also load JSON files.

        This method raises exception if:

        - The file is not available
        - The file content is not valid YAML
        - Top level value of the YAML is not object
        - The YAML contains not supported fields

        It does not raise exception when the YAML misses fields or contains bad fields.

        Parameters
        ----------
        path : PathLike
            Path of the config file.

        Returns
        -------
        cls
            An object of ConfigBase subclass.
        """
    def canonical_copy(self):
        '''
        Create a "canonical" copy of the config, and validate it.

        This function is mainly used internally by NNI.

        Term explanation:
        The config schema for end users is more flexible than the format NNI manager accepts,
        so config classes have to deal with the conversion.
        Here we call the converted format "canonical".

        Returns
        -------
        type(self)
            A deep copy.
        '''
    def validate(self) -> None:
        """
        Validate legality of the config object. Raise exception if any error occurred.

        This function does **not** return truth value. Do not write ``if config.validate()``.

        Returns
        -------
        None
        """
    def json(self):
        """
        Convert the config to JSON object (not JSON string).

        In current implementation ``json()`` will invoke ``validate()``, but this might change in future version.
        It is recommended to call ``validate()`` before ``json()`` for now.

        Returns
        -------
        dict
            JSON object.
        """
    def __setattr__(self, name, value) -> None:
        """
        To prevent typo, config classes forbid assigning to attribute that is not a config field,
        unless it starts with underscore.
        """
