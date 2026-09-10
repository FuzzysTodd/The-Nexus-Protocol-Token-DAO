from .features import FeatureType as FeatureType
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List

@dataclass
class Translation:
    """`FeatureConnector` for translations with fixed languages per example.
    Here for compatiblity with tfds.

    Args:
        languages (`dict`):
            A dictionary for each example mapping string language codes to string translations.

    Example:

    ```python
    >>> # At construction time:
    >>> datasets.features.Translation(languages=['en', 'fr', 'de'])
    >>> # During data generation:
    >>> yield {
    ...         'en': 'the cat',
    ...         'fr': 'le chat',
    ...         'de': 'die katze'
    ... }
    ```
    """
    languages: List[str]
    id: str | None = ...
    dtype: ClassVar[str] = ...
    pa_type: ClassVar[Any] = ...
    def __call__(self): ...
    def flatten(self) -> FeatureType | Dict[str, 'FeatureType']:
        """Flatten the Translation feature into a dictionary."""
    def __init__(self, languages, id) -> None: ...

@dataclass
class TranslationVariableLanguages:
    """`FeatureConnector` for translations with variable languages per example.
    Here for compatiblity with tfds.

    Args:
        languages (`dict`):
            A dictionary for each example mapping string language codes to one or more string translations.
            The languages present may vary from example to example.

    Returns:
        - `language` or `translation` (variable-length 1D `tf.Tensor` of `tf.string`):
            Language codes sorted in ascending order or plain text translations, sorted to align with language codes.

    Example:

    ```python
    >>> # At construction time:
    >>> datasets.features.TranslationVariableLanguages(languages=['en', 'fr', 'de'])
    >>> # During data generation:
    >>> yield {
    ...         'en': 'the cat',
    ...         'fr': ['le chat', 'la chatte,']
    ...         'de': 'die katze'
    ... }
    >>> # Tensor returned :
    >>> {
    ...         'language': ['en', 'de', 'fr', 'fr'],
    ...         'translation': ['the cat', 'die katze', 'la chatte', 'le chat'],
    ... }
    ```
    """
    languages: List | None = ...
    num_languages: int | None = ...
    id: str | None = ...
    dtype: ClassVar[str] = ...
    pa_type: ClassVar[Any] = ...
    def __post_init__(self) -> None: ...
    def __call__(self): ...
    def encode_example(self, translation_dict): ...
    def flatten(self) -> FeatureType | Dict[str, 'FeatureType']:
        """Flatten the TranslationVariableLanguages feature into a dictionary."""
    def __init__(self, languages, num_languages, id) -> None: ...
