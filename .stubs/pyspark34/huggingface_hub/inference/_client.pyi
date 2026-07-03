import numpy as np
from PIL import Image as Image
from _typeshed import Incomplete
from huggingface_hub.constants import ALL_INFERENCE_API_FRAMEWORKS as ALL_INFERENCE_API_FRAMEWORKS, INFERENCE_ENDPOINT as INFERENCE_ENDPOINT, MAIN_INFERENCE_API_FRAMEWORKS as MAIN_INFERENCE_API_FRAMEWORKS
from huggingface_hub.inference._common import ContentT as ContentT, InferenceTimeoutError as InferenceTimeoutError, ModelStatus as ModelStatus, TASKS_EXPECTING_IMAGES as TASKS_EXPECTING_IMAGES
from huggingface_hub.inference._text_generation import TextGenerationParameters as TextGenerationParameters, TextGenerationRequest as TextGenerationRequest, TextGenerationResponse as TextGenerationResponse, TextGenerationStreamResponse as TextGenerationStreamResponse, raise_text_generation_error as raise_text_generation_error
from huggingface_hub.inference._types import ClassificationOutput as ClassificationOutput, ConversationalOutput as ConversationalOutput, FillMaskOutput as FillMaskOutput, ImageSegmentationOutput as ImageSegmentationOutput, ObjectDetectionOutput as ObjectDetectionOutput, QuestionAnsweringOutput as QuestionAnsweringOutput, TableQuestionAnsweringOutput as TableQuestionAnsweringOutput, TokenClassificationOutput as TokenClassificationOutput
from huggingface_hub.utils import BadRequestError as BadRequestError, build_hf_headers as build_hf_headers, get_session as get_session, hf_raise_for_status as hf_raise_for_status
from typing import Any, Dict, Iterable, List, Literal, overload

logger: Incomplete

class InferenceClient:
    """
    Initialize a new Inference Client.

    [`InferenceClient`] aims to provide a unified experience to perform inference. The client can be used
    seamlessly with either the (free) Inference API or self-hosted Inference Endpoints.

    Args:
        model (`str`, `optional`):
            The model to run inference with. Can be a model id hosted on the Hugging Face Hub, e.g. `bigcode/starcoder`
            or a URL to a deployed Inference Endpoint. Defaults to None, in which case a recommended model is
            automatically selected for the task.
        token (`str`, *optional*):
            Hugging Face token. Will default to the locally saved token. Pass `token=False` if you don't want to send
            your token to the server.
        timeout (`float`, `optional`):
            The maximum number of seconds to wait for a response from the server. Loading a new model in Inference
            API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.
        headers (`Dict[str, str]`, `optional`):
            Additional headers to send to the server. By default only the authorization and user-agent headers are sent.
            Values in this dictionary will override the default values.
        cookies (`Dict[str, str]`, `optional`):
            Additional cookies to send to the server.
    """
    model: Incomplete
    headers: Incomplete
    cookies: Incomplete
    timeout: Incomplete
    def __init__(self, model: str | None = None, token: str | bool | None = None, timeout: float | None = None, headers: Dict[str, str] | None = None, cookies: Dict[str, str] | None = None) -> None: ...
    @overload
    def post(self, *, json: str | Dict | List | None = None, data: ContentT | None = None, model: str | None = None, task: str | None = None, stream: Literal[False] = ...) -> bytes: ...
    @overload
    def post(self, *, json: str | Dict | List | None = None, data: ContentT | None = None, model: str | None = None, task: str | None = None, stream: Literal[True] = ...) -> Iterable[bytes]: ...
    def audio_classification(self, audio: ContentT, *, model: str | None = None) -> List[ClassificationOutput]:
        '''
        Perform audio classification on the provided audio content.

        Args:
            audio (Union[str, Path, bytes, BinaryIO]):
                The audio content to classify. It can be raw audio bytes, a local audio file, or a URL pointing to an
                audio file.
            model (`str`, *optional*):
                The model to use for audio classification. Can be a model ID hosted on the Hugging Face Hub
                or a URL to a deployed Inference Endpoint. If not provided, the default recommended model for
                audio classification will be used.

        Returns:
            `List[Dict]`: The classification output containing the predicted label and its confidence.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.audio_classification("audio.flac")
        [{\'score\': 0.4976358711719513, \'label\': \'hap\'}, {\'score\': 0.3677836060523987, \'label\': \'neu\'},...]
        ```
        '''
    def automatic_speech_recognition(self, audio: ContentT, *, model: str | None = None) -> str:
        '''
        Perform automatic speech recognition (ASR or audio-to-text) on the given audio content.

        Args:
            audio (Union[str, Path, bytes, BinaryIO]):
                The content to transcribe. It can be raw audio bytes, local audio file, or a URL to an audio file.
            model (`str`, *optional*):
                The model to use for ASR. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. If not provided, the default recommended model for ASR will be used.

        Returns:
            str: The transcribed text.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.automatic_speech_recognition("hello_world.flac")
        "hello world"
        ```
        '''
    def conversational(self, text: str, generated_responses: List[str] | None = None, past_user_inputs: List[str] | None = None, *, parameters: Dict[str, Any] | None = None, model: str | None = None) -> ConversationalOutput:
        '''
        Generate conversational responses based on the given input text (i.e. chat with the API).

        Args:
            text (`str`):
                The last input from the user in the conversation.
            generated_responses (`List[str]`, *optional*):
                A list of strings corresponding to the earlier replies from the model. Defaults to None.
            past_user_inputs (`List[str]`, *optional*):
                A list of strings corresponding to the earlier replies from the user. Should be the same length as
                `generated_responses`. Defaults to None.
            parameters (`Dict[str, Any]`, *optional*):
                Additional parameters for the conversational task. Defaults to None. For more details about the available
                parameters, please refer to [this page](https://huggingface.co/docs/api-inference/detailed_parameters#conversational-task)
            model (`str`, *optional*):
                The model to use for the conversational task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended conversational model will be used.
                Defaults to None.

        Returns:
            `Dict`: The generated conversational output.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> output = client.conversational("Hi, who are you?")
        >>> output
        {\'generated_text\': \'I am the one who knocks.\', \'conversation\': {\'generated_responses\': [\'I am the one who knocks.\'], \'past_user_inputs\': [\'Hi, who are you?\']}, \'warnings\': [\'Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.\']}
        >>> client.conversational(
        ...     "Wow, that\'s scary!",
        ...     generated_responses=output["conversation"]["generated_responses"],
        ...     past_user_inputs=output["conversation"]["past_user_inputs"],
        ... )
        ```
        '''
    def visual_question_answering(self, image: ContentT, question: str, *, model: str | None = None) -> List[str]:
        '''
        Answering open-ended questions based on an image.

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The input image for the context. It can be raw bytes, an image file, or a URL to an online image.
            question (`str`):
                Question to be answered.
            model (`str`, *optional*):
                The model to use for the visual question answering task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended visual question answering model will be used.
                Defaults to None.

        Returns:
            `List[Dict]`: a list of dictionaries containing the predicted label and associated probability.

        Raises:
            `InferenceTimeoutError`:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.visual_question_answering(
        ...     image="https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg",
        ...     question="What is the animal doing?"
        ... )
        [{\'score\': 0.778609573841095, \'answer\': \'laying down\'},{\'score\': 0.6957435607910156, \'answer\': \'sitting\'}, ...]
        ```
        '''
    def document_question_answering(self, image: ContentT, question: str, *, model: str | None = None) -> List[QuestionAnsweringOutput]:
        '''
        Answer questions on document images.

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The input image for the context. It can be raw bytes, an image file, or a URL to an online image.
            question (`str`):
                Question to be answered.
            model (`str`, *optional*):
                The model to use for the document question answering task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended document question answering model will be used.
                Defaults to None.

        Returns:
            `List[Dict]`: a list of dictionaries containing the predicted label, associated probability, word ids, and page number.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.document_question_answering(image="https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png", question="What is the invoice number?")
        [{\'score\': 0.42515629529953003, \'answer\': \'us-001\', \'start\': 16, \'end\': 16}]
        ```
        '''
    def feature_extraction(self, text: str, *, model: str | None = None) -> np.ndarray:
        '''
        Generate embeddings for a given text.

        Args:
            text (`str`):
                The text to embed.
            model (`str`, *optional*):
                The model to use for the conversational task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended conversational model will be used.
                Defaults to None.

        Returns:
            `np.ndarray`: The embedding representing the input text as a float32 numpy array.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.feature_extraction("Hi, who are you?")
        array([[ 2.424802  ,  2.93384   ,  1.1750331 , ...,  1.240499, -0.13776633, -0.7889173 ],
        [-0.42943227, -0.6364878 , -1.693462  , ...,  0.41978157, -2.4336355 ,  0.6162071 ],
        ...,
        [ 0.28552425, -0.928395  , -1.2077185 , ...,  0.76810825, -2.1069427 ,  0.6236161 ]], dtype=float32)
        ```
        '''
    def fill_mask(self, text: str, *, model: str | None = None) -> List[FillMaskOutput]:
        '''
        Fill in a hole with a missing word (token to be precise).

        Args:
            text (`str`):
                a string to be filled from, must contain the [MASK] token (check model card for exact name of the mask).
            model (`str`, *optional*):
                The model to use for the fill mask task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended fill mask model will be used.
                Defaults to None.

        Returns:
            `List[Dict]`: a list of fill mask output dictionaries containing the predicted label, associated
            probability, token reference, and completed text.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.fill_mask("The goal of life is <mask>.")
        [{\'score\': 0.06897063553333282,
        \'token\': 11098,
        \'token_str\': \' happiness\',
        \'sequence\': \'The goal of life is happiness.\'},
        {\'score\': 0.06554922461509705,
        \'token\': 45075,
        \'token_str\': \' immortality\',
        \'sequence\': \'The goal of life is immortality.\'}]
        ```
        '''
    def image_classification(self, image: ContentT, *, model: str | None = None) -> List[ClassificationOutput]:
        '''
        Perform image classification on the given image using the specified model.

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The image to classify. It can be raw bytes, an image file, or a URL to an online image.
            model (`str`, *optional*):
                The model to use for image classification. Can be a model ID hosted on the Hugging Face Hub or a URL to a
                deployed Inference Endpoint. If not provided, the default recommended model for image classification will be used.

        Returns:
            `List[Dict]`: a list of dictionaries containing the predicted label and associated probability.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.image_classification("https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/320px-Cute_dog.jpg")
        [{\'score\': 0.9779096841812134, \'label\': \'Blenheim spaniel\'}, ...]
        ```
        '''
    def image_segmentation(self, image: ContentT, *, model: str | None = None) -> List[ImageSegmentationOutput]:
        '''
        Perform image segmentation on the given image using the specified model.

        <Tip warning={true}>

        You must have `PIL` installed if you want to work with images (`pip install Pillow`).

        </Tip>

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The image to segment. It can be raw bytes, an image file, or a URL to an online image.
            model (`str`, *optional*):
                The model to use for image segmentation. Can be a model ID hosted on the Hugging Face Hub or a URL to a
                deployed Inference Endpoint. If not provided, the default recommended model for image segmentation will be used.

        Returns:
            `List[Dict]`: A list of dictionaries containing the segmented masks and associated attributes.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.image_segmentation("cat.jpg"):
        [{\'score\': 0.989008, \'label\': \'LABEL_184\', \'mask\': <PIL.PngImagePlugin.PngImageFile image mode=L size=400x300 at 0x7FDD2B129CC0>}, ...]
        ```
        '''
    def image_to_image(self, image: ContentT, prompt: str | None = None, *, negative_prompt: str | None = None, height: int | None = None, width: int | None = None, num_inference_steps: int | None = None, guidance_scale: float | None = None, model: str | None = None, **kwargs) -> Image:
        '''
        Perform image-to-image translation using a specified model.

        <Tip warning={true}>

        You must have `PIL` installed if you want to work with images (`pip install Pillow`).

        </Tip>

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The input image for translation. It can be raw bytes, an image file, or a URL to an online image.
            prompt (`str`, *optional*):
                The text prompt to guide the image generation.
            negative_prompt (`str`, *optional*):
                A negative prompt to guide the translation process.
            height (`int`, *optional*):
                The height in pixels of the generated image.
            width (`int`, *optional*):
                The width in pixels of the generated image.
            num_inference_steps (`int`, *optional*):
                The number of denoising steps. More denoising steps usually lead to a higher quality image at the
                expense of slower inference.
            guidance_scale (`float`, *optional*):
                Higher guidance scale encourages to generate images that are closely linked to the text `prompt`,
                usually at the expense of lower image quality.
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `Image`: The translated image.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> image = client.image_to_image("cat.jpg", prompt="turn the cat into a tiger")
        >>> image.save("tiger.jpg")
        ```
        '''
    def image_to_text(self, image: ContentT, *, model: str | None = None) -> str:
        '''
        Takes an input image and return text.

        Models can have very different outputs depending on your use case (image captioning, optical character recognition
        (OCR), Pix2Struct, etc). Please have a look to the model card to learn more about a model\'s specificities.

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The input image to caption. It can be raw bytes, an image file, or a URL to an online image..
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `str`: The generated text.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.image_to_text("cat.jpg")
        \'a cat standing in a grassy field \'
        >>> client.image_to_text("https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/320px-Cute_dog.jpg")
        \'a dog laying on the grass next to a flower pot \'
        ```
        '''
    def list_deployed_models(self, frameworks: None | str | Literal['all'] | List[str] = None) -> Dict[str, List[str]]:
        '''
        List models currently deployed on the Inference API service.

        This helper checks deployed models framework by framework. By default, it will check the 4 main frameworks that
        are supported and account for 95% of the hosted models. However, if you want a complete list of models you can
        specify `frameworks="all"` as input. Alternatively, if you know before-hand which framework you are interested
        in, you can also restrict to search to this one (e.g. `frameworks="text-generation-inference"`). The more
        frameworks are checked, the more time it will take.

        <Tip>

        This endpoint is mostly useful for discoverability. If you already know which model you want to use and want to
        check its availability, you can directly use [`~InferenceClient.get_model_status`].

        </Tip>

        Args:
            frameworks (`Literal["all"]` or `List[str]` or `str`, *optional*):
                The frameworks to filter on. By default only a subset of the available frameworks are tested. If set to
                "all", all available frameworks will be tested. It is also possible to provide a single framework or a
                custom set of frameworks to check.

        Returns:
            `Dict[str, List[str]]`: A dictionary mapping task names to a sorted list of model IDs.

        Example:
        ```python
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()

        # Discover zero-shot-classification models currently deployed
        >>> models = client.list_deployed_models()
        >>> models["zero-shot-classification"]
        [\'Narsil/deberta-large-mnli-zero-cls\', \'facebook/bart-large-mnli\', ...]

        # List from only 1 framework
        >>> client.list_deployed_models("text-generation-inference")
        {\'text-generation\': [\'bigcode/starcoder\', \'meta-llama/Llama-2-70b-chat-hf\', ...], ...}
        ```
        '''
    def object_detection(self, image: ContentT, *, model: str | None = None) -> List[ObjectDetectionOutput]:
        '''
        Perform object detection on the given image using the specified model.

        <Tip warning={true}>

        You must have `PIL` installed if you want to work with images (`pip install Pillow`).

        </Tip>

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The image to detect objects on. It can be raw bytes, an image file, or a URL to an online image.
            model (`str`, *optional*):
                The model to use for object detection. Can be a model ID hosted on the Hugging Face Hub or a URL to a
                deployed Inference Endpoint. If not provided, the default recommended model for object detection (DETR) will be used.

        Returns:
            `List[ObjectDetectionOutput]`: A list of dictionaries containing the bounding boxes and associated attributes.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.
            `ValueError`:
                If the request output is not a List.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.object_detection("people.jpg"):
        [{"score":0.9486683011054993,"label":"person","box":{"xmin":59,"ymin":39,"xmax":420,"ymax":510}}, ... ]
        ```
        '''
    def question_answering(self, question: str, context: str, *, model: str | None = None) -> QuestionAnsweringOutput:
        '''
        Retrieve the answer to a question from a given text.

        Args:
            question (`str`):
                Question to be answered.
            context (`str`):
                The context of the question.
            model (`str`):
                The model to use for the question answering task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint.

        Returns:
            `Dict`: a dictionary of question answering output containing the score, start index, end index, and answer.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.question_answering(question="What\'s my name?", context="My name is Clara and I live in Berkeley.")
        {\'score\': 0.9326562285423279, \'start\': 11, \'end\': 16, \'answer\': \'Clara\'}
        ```
        '''
    def sentence_similarity(self, sentence: str, other_sentences: List[str], *, model: str | None = None) -> List[float]:
        '''
        Compute the semantic similarity between a sentence and a list of other sentences by comparing their embeddings.

        Args:
            sentence (`str`):
                The main sentence to compare to others.
            other_sentences (`List[str]`):
                The list of sentences to compare to.
            model (`str`, *optional*):
                The model to use for the conversational task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended conversational model will be used.
                Defaults to None.

        Returns:
            `List[float]`: The embedding representing the input text.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.sentence_similarity(
        ...     "Machine learning is so easy.",
        ...     other_sentences=[
        ...         "Deep learning is so straightforward.",
        ...         "This is so difficult, like rocket science.",
        ...         "I can\'t believe how much I struggled with this.",
        ...     ],
        ... )
        [0.7785726189613342, 0.45876261591911316, 0.2906220555305481]
        ```
        '''
    def summarization(self, text: str, *, parameters: Dict[str, Any] | None = None, model: str | None = None) -> str:
        '''
        Generate a summary of a given text using a specified model.

        Args:
            text (`str`):
                The input text to summarize.
            parameters (`Dict[str, Any]`, *optional*):
                Additional parameters for summarization. Check out this [page](https://huggingface.co/docs/api-inference/detailed_parameters#summarization-task)
                for more details.
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `str`: The generated summary text.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.summarization("The Eiffel tower...")
        \'The Eiffel tower is one of the most famous landmarks in the world....\'
        ```
        '''
    def table_question_answering(self, table: Dict[str, Any], query: str, *, model: str | None = None) -> TableQuestionAnsweringOutput:
        '''
        Retrieve the answer to a question from information given in a table.

        Args:
            table (`str`):
                A table of data represented as a dict of lists where entries are headers and the lists are all the
                values, all lists must have the same size.
            query (`str`):
                The query in plain text that you want to ask the table.
            model (`str`):
                The model to use for the table-question-answering task. Can be a model ID hosted on the Hugging Face
                Hub or a URL to a deployed Inference Endpoint.

        Returns:
            `Dict`: a dictionary of table question answering output containing the answer, coordinates, cells and the aggregator used.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> query = "How many stars does the transformers repository have?"
        >>> table = {"Repository": ["Transformers", "Datasets", "Tokenizers"], "Stars": ["36542", "4512", "3934"]}
        >>> client.table_question_answering(table, query, model="google/tapas-base-finetuned-wtq")
        {\'answer\': \'AVERAGE > 36542\', \'coordinates\': [[0, 1]], \'cells\': [\'36542\'], \'aggregator\': \'AVERAGE\'}
        ```
        '''
    def tabular_classification(self, table: Dict[str, Any], *, model: str) -> List[str]:
        '''
        Classifying a target category (a group) based on a set of attributes.

        Args:
            table (`Dict[str, Any]`):
                Set of attributes to classify.
            model (`str`):
                The model to use for the tabular-classification task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint.

        Returns:
            `List`: a list of labels, one per row in the initial table.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> table = {
        ...     "fixed_acidity": ["7.4", "7.8", "10.3"],
        ...     "volatile_acidity": ["0.7", "0.88", "0.32"],
        ...     "citric_acid": ["0", "0", "0.45"],
        ...     "residual_sugar": ["1.9", "2.6", "6.4"],
        ...     "chlorides": ["0.076", "0.098", "0.073"],
        ...     "free_sulfur_dioxide": ["11", "25", "5"],
        ...     "total_sulfur_dioxide": ["34", "67", "13"],
        ...     "density": ["0.9978", "0.9968", "0.9976"],
        ...     "pH": ["3.51", "3.2", "3.23"],
        ...     "sulphates": ["0.56", "0.68", "0.82"],
        ...     "alcohol": ["9.4", "9.8", "12.6"],
        ... }
        >>> client.tabular_classification(table=table, model="julien-c/wine-quality")
        ["5", "5", "5"]
        ```
        '''
    def tabular_regression(self, table: Dict[str, Any], *, model: str) -> List[float]:
        '''
        Predicting a numerical target value given a set of attributes/features in a table.

        Args:
            table (`Dict[str, Any]`):
                Set of attributes stored in a table. The attributes used to predict the target can be both numerical and categorical.
            model (`str`):
                The model to use for the tabular-regression task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint.

        Returns:
            `List`: a list of predicted numerical target values.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> table = {
        ...     "Height": ["11.52", "12.48", "12.3778"],
        ...     "Length1": ["23.2", "24", "23.9"],
        ...     "Length2": ["25.4", "26.3", "26.5"],
        ...     "Length3": ["30", "31.2", "31.1"],
        ...     "Species": ["Bream", "Bream", "Bream"],
        ...     "Width": ["4.02", "4.3056", "4.6961"],
        ... }
        >>> client.tabular_regression(table, model="scikit-learn/Fish-Weight")
        [110, 120, 130]
        ```
        '''
    def text_classification(self, text: str, *, model: str | None = None) -> List[ClassificationOutput]:
        '''
        Perform text classification (e.g. sentiment-analysis) on the given text.

        Args:
            text (`str`):
                A string to be classified.
            model (`str`, *optional*):
                The model to use for the text classification task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended text classification model will be used.
                Defaults to None.

        Returns:
            `List[Dict]`: a list of dictionaries containing the predicted label and associated probability.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.text_classification("I like you")
        [{\'label\': \'POSITIVE\', \'score\': 0.9998695850372314}, {\'label\': \'NEGATIVE\', \'score\': 0.0001304351753788069}]
        ```
        '''
    @overload
    def text_generation(self, prompt: str, *, details: Literal[False] = ..., stream: Literal[False] = ..., model: str | None = None, do_sample: bool = False, max_new_tokens: int = 20, best_of: int | None = None, repetition_penalty: float | None = None, return_full_text: bool = False, seed: int | None = None, stop_sequences: List[str] | None = None, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None, truncate: int | None = None, typical_p: float | None = None, watermark: bool = False) -> str: ...
    @overload
    def text_generation(self, prompt: str, *, details: Literal[True] = ..., stream: Literal[False] = ..., model: str | None = None, do_sample: bool = False, max_new_tokens: int = 20, best_of: int | None = None, repetition_penalty: float | None = None, return_full_text: bool = False, seed: int | None = None, stop_sequences: List[str] | None = None, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None, truncate: int | None = None, typical_p: float | None = None, watermark: bool = False) -> TextGenerationResponse: ...
    @overload
    def text_generation(self, prompt: str, *, details: Literal[False] = ..., stream: Literal[True] = ..., model: str | None = None, do_sample: bool = False, max_new_tokens: int = 20, best_of: int | None = None, repetition_penalty: float | None = None, return_full_text: bool = False, seed: int | None = None, stop_sequences: List[str] | None = None, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None, truncate: int | None = None, typical_p: float | None = None, watermark: bool = False) -> Iterable[str]: ...
    @overload
    def text_generation(self, prompt: str, *, details: Literal[True] = ..., stream: Literal[True] = ..., model: str | None = None, do_sample: bool = False, max_new_tokens: int = 20, best_of: int | None = None, repetition_penalty: float | None = None, return_full_text: bool = False, seed: int | None = None, stop_sequences: List[str] | None = None, temperature: float | None = None, top_k: int | None = None, top_p: float | None = None, truncate: int | None = None, typical_p: float | None = None, watermark: bool = False) -> Iterable[TextGenerationStreamResponse]: ...
    def text_to_image(self, prompt: str, *, negative_prompt: str | None = None, height: float | None = None, width: float | None = None, num_inference_steps: float | None = None, guidance_scale: float | None = None, model: str | None = None, **kwargs) -> Image:
        '''
        Generate an image based on a given text using a specified model.

        <Tip warning={true}>

        You must have `PIL` installed if you want to work with images (`pip install Pillow`).

        </Tip>

        Args:
            prompt (`str`):
                The prompt to generate an image from.
            negative_prompt (`str`, *optional*):
                An optional negative prompt for the image generation.
            height (`float`, *optional*):
                The height in pixels of the image to generate.
            width (`float`, *optional*):
                The width in pixels of the image to generate.
            num_inference_steps (`int`, *optional*):
                The number of denoising steps. More denoising steps usually lead to a higher quality image at the
                expense of slower inference.
            guidance_scale (`float`, *optional*):
                Higher guidance scale encourages to generate images that are closely linked to the text `prompt`,
                usually at the expense of lower image quality.
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `Image`: The generated image.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()

        >>> image = client.text_to_image("An astronaut riding a horse on the moon.")
        >>> image.save("astronaut.png")

        >>> image = client.text_to_image(
        ...     "An astronaut riding a horse on the moon.",
        ...     negative_prompt="low resolution, blurry",
        ...     model="stabilityai/stable-diffusion-2-1",
        ... )
        >>> image.save("better_astronaut.png")
        ```
        '''
    def text_to_speech(self, text: str, *, model: str | None = None) -> bytes:
        '''
        Synthesize an audio of a voice pronouncing a given text.

        Args:
            text (`str`):
                The text to synthesize.
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `bytes`: The generated audio.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from pathlib import Path
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()

        >>> audio = client.text_to_speech("Hello world")
        >>> Path("hello_world.flac").write_bytes(audio)
        ```
        '''
    def token_classification(self, text: str, *, model: str | None = None) -> List[TokenClassificationOutput]:
        '''
        Perform token classification on the given text.
        Usually used for sentence parsing, either grammatical, or Named Entity Recognition (NER) to understand keywords contained within text.

        Args:
            text (`str`):
                A string to be classified.
            model (`str`, *optional*):
                The model to use for the token classification task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended token classification model will be used.
                Defaults to None.

        Returns:
            `List[Dict]`: List of token classification outputs containing the entity group, confidence score, word, start and end index.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.token_classification("My name is Sarah Jessica Parker but you can call me Jessica")
        [{\'entity_group\': \'PER\',
        \'score\': 0.9971321225166321,
        \'word\': \'Sarah Jessica Parker\',
        \'start\': 11,
        \'end\': 31},
        {\'entity_group\': \'PER\',
        \'score\': 0.9773476123809814,
        \'word\': \'Jessica\',
        \'start\': 52,
        \'end\': 59}]
        ```
        '''
    def translation(self, text: str, *, model: str | None = None) -> str:
        '''
        Convert text from one language to another.

        Check out https://huggingface.co/tasks/translation for more information on how to choose the best model for
        your specific use case. Source and target languages usually depends on the model.

        Args:
            text (`str`):
                A string to be translated.
            model (`str`, *optional*):
                The model to use for the translation task. Can be a model ID hosted on the Hugging Face Hub or a URL to
                a deployed Inference Endpoint. If not provided, the default recommended translation model will be used.
                Defaults to None.

        Returns:
            `str`: The generated translated text.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.translation("My name is Wolfgang and I live in Berlin")
        \'Mein Name ist Wolfgang und ich lebe in Berlin.\'
        >>> client.translation("My name is Wolfgang and I live in Berlin", model="Helsinki-NLP/opus-mt-en-fr")
        "Je m\'appelle Wolfgang et je vis à Berlin."
        ```
        '''
    def zero_shot_classification(self, text: str, labels: List[str], *, multi_label: bool = False, model: str | None = None) -> List[ClassificationOutput]:
        '''
        Provide as input a text and a set of candidate labels to classify the input text.

        Args:
            text (`str`):
                The input text to classify.
            labels (`List[str]`):
                List of string possible labels. There must be at least 2 labels.
            multi_label (`bool`):
                Boolean that is set to True if classes can overlap.
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `List[Dict]`: List of classification outputs containing the predicted labels and their confidence.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> text = (
        ...     "A new model offers an explanation for how the Galilean satellites formed around the solar system\'s"
        ...     "largest world. Konstantin Batygin did not set out to solve one of the solar system\'s most puzzling"
        ...     " mysteries when he went for a run up a hill in Nice, France."
        ... )
        >>> labels = ["space & cosmos", "scientific discovery", "microbiology", "robots", "archeology"]
        >>> client.zero_shot_classification(text, labels)
        [
            {"label": "scientific discovery", "score": 0.7961668968200684},
            {"label": "space & cosmos", "score": 0.18570658564567566},
            {"label": "microbiology", "score": 0.00730885099619627},
            {"label": "archeology", "score": 0.006258360575884581},
            {"label": "robots", "score": 0.004559356719255447},
        ]
        >>> client.zero_shot_classification(text, labels, multi_label=True)
        [
            {"label": "scientific discovery", "score": 0.9829297661781311},
            {"label": "space & cosmos", "score": 0.755190908908844},
            {"label": "microbiology", "score": 0.0005462635890580714},
            {"label": "archeology", "score": 0.00047131875180639327},
            {"label": "robots", "score": 0.00030448526376858354},
        ]
        ```
        '''
    def zero_shot_image_classification(self, image: ContentT, labels: List[str], *, model: str | None = None) -> List[ClassificationOutput]:
        '''
        Provide input image and text labels to predict text labels for the image.

        Args:
            image (`Union[str, Path, bytes, BinaryIO]`):
                The input image to caption. It can be raw bytes, an image file, or a URL to an online image.
            labels (`List[str]`):
                List of string possible labels. There must be at least 2 labels.
            model (`str`, *optional*):
                The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed
                Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

        Returns:
            `List[Dict]`: List of classification outputs containing the predicted labels and their confidence.

        Raises:
            [`InferenceTimeoutError`]:
                If the model is unavailable or the request times out.
            `HTTPError`:
                If the request fails with an HTTP error status code other than HTTP 503.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()

        >>> client.zero_shot_image_classification(
        ...     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/320px-Cute_dog.jpg",
        ...     labels=["dog", "cat", "horse"],
        ... )
        [{"label": "dog", "score": 0.956}, ...]
        ```
        '''
    def get_model_status(self, model: str | None = None) -> ModelStatus:
        '''
        Get the status of a model hosted on the Inference API.

        <Tip>

        This endpoint is mostly useful when you already know which model you want to use and want to check its
        availability. If you want to discover already deployed models, you should rather use [`~InferenceClient.list_deployed_models`].

        </Tip>

        Args:
            model (`str`, *optional*):
                Identifier of the model for witch the status gonna be checked. If model is not provided,
                the model associated with this instance of [`InferenceClient`] will be used. Only InferenceAPI service can be checked so the
                identifier cannot be a URL.


        Returns:
            [`ModelStatus`]: An instance of ModelStatus dataclass, containing information,
                         about the state of the model: load, state, compute type and framework.

        Example:
        ```py
        >>> from huggingface_hub import InferenceClient
        >>> client = InferenceClient()
        >>> client.get_model_status("bigcode/starcoder")
        ModelStatus(loaded=True, state=\'Loaded\', compute_type=\'gpu\', framework=\'text-generation-inference\')
        ```
        '''
