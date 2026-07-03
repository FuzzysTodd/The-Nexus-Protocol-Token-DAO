from .openai_utils import get_key as get_key
from _typeshed import Incomplete
from flaml import BlendSearch as BlendSearch, tune as tune
from flaml.automl.logger import logger_formatter as logger_formatter
from flaml.tune.space import is_constant as is_constant
from openai import Completion as openai_Completion
from typing import Callable, Dict, List

ERROR: Incomplete
openai_Completion = object
logger: Incomplete

class Completion(openai_Completion):
    """A class for OpenAI completion API.

    It also supports: ChatCompletion, Azure OpenAI API.
    """
    chat_models: Incomplete
    price1K: Incomplete
    default_search_space: Incomplete
    seed: int
    cache_path: Incomplete
    retry_time: int
    retry_timeout: int
    request_timeout: int
    openai_completion_class: Incomplete
    optimization_budget: Incomplete
    @classmethod
    def set_cache(cls, seed: int | None = 41, cache_path_root: str | None = '.cache'):
        """Set cache path.

        Args:
            seed (int, Optional): The integer identifier for the pseudo seed.
                Results corresponding to different seeds will be cached in different places.
            cache_path (str, Optional): The root path for the cache.
                The complete cache path will be {cache_path}/{seed}.
        """
    @classmethod
    def clear_cache(cls, seed: int | None = None, cache_path_root: str | None = '.cache'):
        """Clear cache.

        Args:
            seed (int, Optional): The integer identifier for the pseudo seed.
                If omitted, all caches under cache_path_root will be cleared.
            cache_path (str, Optional): The root path for the cache.
                The complete cache path will be {cache_path}/{seed}.
        """
    @classmethod
    def tune(cls, data: List[Dict], metric: str, mode: str, eval_func: Callable, log_file_name: str | None = None, inference_budget: float | None = None, optimization_budget: float | None = None, num_samples: int | None = 1, logging_level: int | None = ..., **config):
        '''Tune the parameters for the OpenAI API call.

        TODO: support parallel tuning with ray or spark.
        TODO: support agg_method as in test

        Args:
            data (list): The list of data points.
            metric (str): The metric to optimize.
            mode (str): The optimization mode, "min" or "max.
            eval_func (Callable): The evaluation function for responses.
                The function should take a list of responses and a data point as input,
                and return a dict of metrics. For example,

        ```python
        def eval_func(responses, **data):
            solution = data["solution"]
            success_list = []
            n = len(responses)
            for i in range(n):
                response = responses[i]
                succeed = is_equiv_chain_of_thought(response, solution)
                success_list.append(succeed)
            return {
                "expected_success": 1 - pow(1 - sum(success_list) / n, n),
                "success": any(s for s in success_list),
            }
        ```

            log_file_name (str, optional): The log file.
            inference_budget (float, optional): The inference budget, dollar per instance.
            optimization_budget (float, optional): The optimization budget, dollar in total.
            num_samples (int, optional): The number of samples to evaluate.
                -1 means no hard restriction in the number of trials
                and the actual number is decided by optimization_budget. Defaults to 1.
            logging_level (optional): logging level. Defaults to logging.WARNING.
            **config (dict): The search space to update over the default search.
                For prompt, please provide a string/Callable or a list of strings/Callables.
                    - If prompt is provided for chat models, it will be converted to messages under role "user".
                    - Do not provide both prompt and messages for chat models, but provide either of them.
                    - A string template will be used to generate a prompt for each data instance
                      using `prompt.format(**data)`.
                    - A callable template will be used to generate a prompt for each data instance
                      using `prompt(data)`.
                For stop, please provide a string, a list of strings, or a list of lists of strings.
                For messages (chat models only), please provide a list of messages (for a single chat prefix)
                or a list of lists of messages (for multiple choices of chat prefix to choose from).
                Each message should be a dict with keys "role" and "content". The value of "content" can be a string/Callable template.

        Returns:
            dict: The optimized hyperparameter setting.
            tune.ExperimentAnalysis: The tuning results.
        '''
    @classmethod
    def create(cls, context: Dict | None = None, use_cache: bool | None = True, config_list: List[Dict] | None = None, filter_func: Callable[[Dict, Dict, Dict], bool] | None = None, raise_on_ratelimit_or_timeout: bool | None = True, allow_format_str_template: bool | None = False, **config):
        '''Make a completion for a given context.

        Args:
            context (Dict, Optional): The context to instantiate the prompt.
                It needs to contain keys that are used by the prompt template or the filter function.
                E.g., `prompt="Complete the following sentence: {prefix}, context={"prefix": "Today I feel"}`.
                The actual prompt will be:
                "Complete the following sentence: Today I feel".
                More examples can be found at [templating](https://microsoft.github.io/autogen/docs/Use-Cases/enhanced_inference#templating).
            use_cache (bool, Optional): Whether to use cached responses.
            config_list (List, Optional): List of configurations for the completion to try.
                The first one that does not raise an error will be used.
                Only the differences from the default config need to be provided.
                E.g.,

        ```python
        response = oai.Completion.create(
            config_list=[
                {
                    "model": "gpt-4",
                    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
                    "api_type": "azure",
                    "api_base": os.environ.get("AZURE_OPENAI_API_BASE"),
                    "api_version": "2023-03-15-preview",
                },
                {
                    "model": "gpt-3.5-turbo",
                    "api_key": os.environ.get("OPENAI_API_KEY"),
                    "api_type": "open_ai",
                    "api_base": "https://api.openai.com/v1",
                },
                {
                    "model": "llama-7B",
                    "api_base": "http://127.0.0.1:8080",
                    "api_type": "open_ai",
                }
            ],
            prompt="Hi",
        )
        ```

            filter_func (Callable, Optional): A function that takes in the context, the config and the response and returns a boolean to indicate whether the response is valid. E.g.,

        ```python
        def yes_or_no_filter(context, config, response):
            return context.get("yes_or_no_choice", False) is False or any(
                text in ["Yes.", "No."] for text in oai.Completion.extract_text(response)
            )
        ```

            raise_on_ratelimit_or_timeout (bool, Optional): Whether to raise RateLimitError or Timeout when all configs fail.
                When set to False, -1 will be returned when all configs fail.
            allow_format_str_template (bool, Optional): Whether to allow format string template in the config.
            **config: Configuration for the openai API call. This is used as parameters for calling openai API.
                Besides the parameters for the openai API call, it can also contain a seed (int) for the cache.
                This is useful when implementing "controlled randomness" for the completion.
                Also, the "prompt" or "messages" parameter can contain a template (str or Callable) which will be instantiated with the context.

        Returns:
            Responses from OpenAI API, with additional fields.
                - `cost`: the total cost.
            When `config_list` is provided, the response will contain a few more fields:
                - `config_id`: the index of the config in the config_list that is used to generate the response.
                - `pass_filter`: whether the response passes the filter function. None if no filter is provided.
        '''
    @classmethod
    def instantiate(cls, template: str | None, context: Dict | None = None, allow_format_str_template: bool | None = False): ...
    @classmethod
    def test(cls, data, eval_func: Incomplete | None = None, use_cache: bool = True, agg_method: str = 'avg', return_responses_and_per_instance_result: bool = False, logging_level=..., **config):
        '''Evaluate the responses created with the config for the OpenAI API call.

        Args:
            data (list): The list of test data points.
            eval_func (Callable): The evaluation function for responses per data instance.
                The function should take a list of responses and a data point as input,
                and return a dict of metrics. You need to either provide a valid callable
                eval_func; or do not provide one (set None) but call the test function after
                calling the tune function in which a eval_func is provided.
                In the latter case we will use the eval_func provided via tune function.
                Defaults to None.

        ```python
        def eval_func(responses, **data):
            solution = data["solution"]
            success_list = []
            n = len(responses)
            for i in range(n):
                response = responses[i]
                succeed = is_equiv_chain_of_thought(response, solution)
                success_list.append(succeed)
            return {
                "expected_success": 1 - pow(1 - sum(success_list) / n, n),
                "success": any(s for s in success_list),
            }
        ```
            use_cache (bool, Optional): Whether to use cached responses. Defaults to True.
            agg_method (str, Callable or a dict of Callable): Result aggregation method (across
                multiple instances) for each of the metrics. Defaults to \'avg\'.
                An example agg_method in str:

        ```python
        agg_method = \'median\'
        ```
                An example agg_method in a Callable:

        ```python
        agg_method = np.median
        ```

                An example agg_method in a dict of Callable:

        ```python
        agg_method={\'median_success\': np.median, \'avg_success\': np.mean}
        ```

            return_responses_and_per_instance_result (bool): Whether to also return responses
                and per instance results in addition to the aggregated results.
            logging_level (optional): logging level. Defaults to logging.WARNING.
            **config (dict): parametes passed to the openai api call `create()`.

        Returns:
            None when no valid eval_func is provided in either test or tune;
            Otherwise, a dict of aggregated results, responses and per instance results if `return_responses_and_per_instance_result` is True;
            Otherwise, a dict of aggregated results (responses and per instance results are not returned).
        '''
    @classmethod
    def cost(cls, response: dict):
        """Compute the cost of an API call.

        Args:
            response (dict): The response from OpenAI API.

        Returns:
            The cost in USD. 0 if the model is not supported.
        """
    @classmethod
    def extract_text(cls, response: dict) -> List[str]:
        """Extract the text from a completion or chat response.

        Args:
            response (dict): The response from OpenAI API.

        Returns:
            A list of text in the responses.
        """
    @classmethod
    def extract_text_or_function_call(cls, response: dict) -> List[str]:
        """Extract the text or function calls from a completion or chat response.

        Args:
            response (dict): The response from OpenAI API.

        Returns:
            A list of text or function calls in the responses.
        """
    @classmethod
    @property
    def logged_history(cls) -> Dict:
        """Return the book keeping dictionary."""
    @classmethod
    def start_logging(cls, history_dict: Dict | None = None, compact: bool | None = True, reset_counter: bool | None = True):
        '''Start book keeping.

        Args:
            history_dict (Dict): A dictionary for book keeping.
                If no provided, a new one will be created.
            compact (bool): Whether to keep the history dictionary compact.
                Compact history contains one key per conversation, and the value is a dictionary
                like:
        ```python
        {
            "create_at": [0, 1],
            "cost": [0.1, 0.2],
        }
        ```
                where "created_at" is the index of API calls indicating the order of all the calls,
                and "cost" is the cost of each call. This example shows that the conversation is based
                on two API calls. The compact format is useful for condensing the history of a conversation.
                If compact is False, the history dictionary will contain all the API calls: the key
                is the index of the API call, and the value is a dictionary like:
        ```python
        {
            "request": request_dict,
            "response": response_dict,
        }
        ```
                where request_dict is the request sent to OpenAI API, and response_dict is the response.
                For a conversation containing two API calls, the non-compact history dictionary will be like:
        ```python
        {
            0: {
                "request": request_dict_0,
                "response": response_dict_0,
            },
            1: {
                "request": request_dict_1,
                "response": response_dict_1,
            },
        ```
                The first request\'s messages plus the response is equal to the second request\'s messages.
                For a conversation with many turns, the non-compact history dictionary has a quadratic size
                while the compact history dict has a linear size.
            reset_counter (bool): whether to reset the counter of the number of API calls.
        '''
    @classmethod
    def stop_logging(cls) -> None:
        """End book keeping."""

class ChatCompletion(Completion):
    """A class for OpenAI API ChatCompletion."""
    default_search_space: Incomplete
    openai_completion_class: Incomplete
