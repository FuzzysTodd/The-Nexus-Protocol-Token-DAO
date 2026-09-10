from ..util import import_from_string as import_from_string
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Dict, List, Tuple

class Asym(nn.Sequential):
    sub_modules: Incomplete
    allow_empty_key: Incomplete
    def __init__(self, sub_modules: Dict[str, List[nn.Module]], allow_empty_key: bool = True) -> None:
        """
        This model allows to create asymmetric SentenceTransformer models, that apply different models depending on the specified input key.

        In the below example, we create two different Dense models for 'query' and 'doc'. Text that is passed as {'query': 'My query'} will
        be passed along along the first Dense model, and text that will be passed as {'doc': 'My document'} will use the other Dense model.

        Note, that when you call encode(), that only inputs of the same type can be encoded. Mixed-Types cannot be encoded.

        Example::
            word_embedding_model = models.Transformer(model_name)
            pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
            asym_model = models.Asym({'query': [models.Dense(word_embedding_model.get_word_embedding_dimension(), 128)], 'doc': [models.Dense(word_embedding_model.get_word_embedding_dimension(), 128)]})
            model = SentenceTransformer(modules=[word_embedding_model, pooling_model, asym_model])

            model.encode([{'query': 'Q1'}, {'query': 'Q2'}]
            model.encode([{'doc': 'Doc1'}, {'doc': 'Doc2'}]

            #You can train it with InputExample like this. Note, that the order must always be the same:
            train_example = InputExample(texts=[{'query': 'Train query', 'doc': 'Doc query'}], label=1)


        :param sub_modules: Dict in the format str -> List[models]. The models in the specified list will be applied for input marked with the respective key.
        :param allow_empty_key: If true, inputs without a key can be processed. If false, an exception will be thrown if no key is specified.
        """
    def forward(self, features: Dict[str, Tensor]): ...
    def get_sentence_embedding_dimension(self) -> int: ...
    def save(self, output_path) -> None: ...
    def tokenize(self, texts: List[str] | List[Tuple[str, str]]):
        """
        Tokenizes a text and maps tokens to token-ids
        """
    @staticmethod
    def load(input_path): ...
