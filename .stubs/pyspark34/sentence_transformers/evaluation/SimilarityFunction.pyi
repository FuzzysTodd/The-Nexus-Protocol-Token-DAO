from enum import Enum

class SimilarityFunction(Enum):
    COSINE: int
    EUCLIDEAN: int
    MANHATTAN: int
    DOT_PRODUCT: int
