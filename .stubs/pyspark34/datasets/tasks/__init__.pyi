from .audio_classificiation import AudioClassification as AudioClassification
from .automatic_speech_recognition import AutomaticSpeechRecognition as AutomaticSpeechRecognition
from .base import TaskTemplate as TaskTemplate
from .image_classification import ImageClassification as ImageClassification
from .language_modeling import LanguageModeling as LanguageModeling
from .question_answering import QuestionAnsweringExtractive as QuestionAnsweringExtractive
from .summarization import Summarization as Summarization
from .text_classification import TextClassification as TextClassification

__all__ = ['AutomaticSpeechRecognition', 'AudioClassification', 'ImageClassification', 'LanguageModeling', 'QuestionAnsweringExtractive', 'Summarization', 'TaskTemplate', 'TextClassification']
