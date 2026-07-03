from .. import SentenceTransformer as SentenceTransformer
from ..readers import InputExample as InputExample
from _typeshed import Incomplete
from torch.utils.data import Dataset
from typing import List

logger: Incomplete

class ParallelSentencesDataset(Dataset):
    """
    This dataset reader can be used to read-in parallel sentences, i.e., it reads in a file with tab-seperated sentences with the same
    sentence in different languages. For example, the file can look like this (EN\tDE\tES):
    hello world     hallo welt  hola mundo
    second sentence zweiter satz    segunda oración

    The sentence in the first column will be mapped to a sentence embedding using the given the embedder. For example,
    embedder is a mono-lingual sentence embedding method for English. The sentences in the other languages will also be
    mapped to this English sentence embedding.

    When getting a sample from the dataset, we get one sentence with the according sentence embedding for this sentence.

    teacher_model can be any class that implement an encode function. The encode function gets a list of sentences and
    returns a list of sentence embeddings
    """
    student_model: Incomplete
    teacher_model: Incomplete
    datasets: Incomplete
    datasets_iterator: Incomplete
    datasets_tokenized: Incomplete
    dataset_indices: Incomplete
    copy_dataset_indices: Incomplete
    cache: Incomplete
    batch_size: Incomplete
    use_embedding_cache: Incomplete
    embedding_cache: Incomplete
    num_sentences: int
    def __init__(self, student_model: SentenceTransformer, teacher_model: SentenceTransformer, batch_size: int = 8, use_embedding_cache: bool = True) -> None:
        """
        Parallel sentences dataset reader to train student model given a teacher model
        :param student_model: Student sentence embedding model that should be trained
        :param teacher_model: Teacher model, that provides the sentence embeddings for the first column in the dataset file
        """
    def load_data(self, filepath: str, weight: int = 100, max_sentences: int = None, max_sentence_length: int = 128):
        """
        Reads in a tab-seperated .txt/.csv/.tsv or .gz file. The different columns contain the different translations of the sentence in the first column

        :param filepath: Filepath to the file
        :param weight: If more than one dataset is loaded with load_data: With which frequency should data be sampled from this dataset?
        :param max_sentences: Max number of lines to be read from filepath
        :param max_sentence_length: Skip the example if one of the sentences is has more characters than max_sentence_length
        :param batch_size: Size for encoding parallel sentences
        :return:
        """
    def add_dataset(self, parallel_sentences: List[List[str]], weight: int = 100, max_sentences: int = None, max_sentence_length: int = 128): ...
    def generate_data(self) -> None: ...
    def next_entry(self, data_idx): ...
    def get_embeddings(self, sentences): ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...
