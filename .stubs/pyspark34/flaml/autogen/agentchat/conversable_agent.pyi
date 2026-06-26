from .agent import Agent as Agent
from _typeshed import Incomplete
from flaml.autogen import oai as oai
from flaml.autogen.code_utils import DEFAULT_MODEL as DEFAULT_MODEL, UNKNOWN as UNKNOWN, execute_code as execute_code, extract_code as extract_code, infer_lang as infer_lang
from typing import Any, Callable, Dict, List, Tuple, Type

class ConversableAgent(Agent):
    '''(In preview) A class for generic conversable agents which can be configured as assistant or user proxy.

    After receiving each message, the agent will send a reply to the sender unless the msg is a termination msg.
    For example, AssistantAgent and UserProxyAgent are subclasses of this class,
    configured with different default settings.

    To modify auto reply, override `generate_reply` method.
    To disable/enable human response in every turn, set `human_input_mode` to "NEVER" or "ALWAYS".
    To modify the way to get human input, override `get_human_input` method.
    To modify the way to execute code blocks, single code block, or function call, override `execute_code_blocks`,
    `run_code`, and `execute_function` methods respectively.
    To customize the initial message when a conversation starts, override `generate_init_message` method.
    '''
    DEFAULT_CONFIG: Incomplete
    MAX_CONSECUTIVE_AUTO_REPLY: int
    llm_config: bool
    human_input_mode: Incomplete
    reply_at_receive: Incomplete
    def __init__(self, name: str, system_message: str | None = 'You are a helpful AI Assistant.', is_termination_msg: Callable[[Dict], bool] | None = None, max_consecutive_auto_reply: int | None = None, human_input_mode: str | None = 'TERMINATE', function_map: Dict[str, Callable] | None = None, code_execution_config: Dict | bool | None = None, llm_config: Dict | bool | None = None, default_auto_reply: str | Dict | None | None = '') -> None:
        '''
        Args:
            name (str): name of the agent.
            system_message (str): system message for the ChatCompletion inference.
            is_termination_msg (function): a function that takes a message in the form of a dictionary
                and returns a boolean value indicating if this received message is a termination message.
                The dict can contain the following keys: "content", "role", "name", "function_call".
            max_consecutive_auto_reply (int): the maximum number of consecutive auto replies.
                default to None (no limit provided, class attribute MAX_CONSECUTIVE_AUTO_REPLY will be used as the limit in this case).
                When set to 0, no auto reply will be generated.
            human_input_mode (str): whether to ask for human inputs every time a message is received.
                Possible values are "ALWAYS", "TERMINATE", "NEVER".
                (1) When "ALWAYS", the agent prompts for human input every time a message is received.
                    Under this mode, the conversation stops when the human input is "exit",
                    or when is_termination_msg is True and there is no human input.
                (2) When "TERMINATE", the agent only prompts for human input only when a termination message is received or
                    the number of auto reply reaches the max_consecutive_auto_reply.
                (3) When "NEVER", the agent will never prompt for human input. Under this mode, the conversation stops
                    when the number of auto reply reaches the max_consecutive_auto_reply or when is_termination_msg is True.
            function_map (dict[str, callable]): Mapping function names (passed to openai) to callable functions.
            code_execution_config (dict or False): config for the code execution.
                To disable code execution, set to False. Otherwise, set to a dictionary with the following keys:
                - work_dir (Optional, str): The working directory for the code execution.
                    If None, a default working directory will be used.
                    The default working directory is the "extensions" directory under
                    "path_to_flaml/autogen".
                - use_docker (Optional, list, str or bool): The docker image to use for code execution.
                    If a list or a str of image name(s) is provided, the code will be executed in a docker container
                    with the first image successfully pulled.
                    If None, False or empty, the code will be executed in the current environment.
                    Default is True, which will be converted into a list.
                    If the code is executed in the current environment,
                    the code must be trusted.
                - timeout (Optional, int): The maximum execution time in seconds.
                - last_n_messages (Experimental, Optional, int): The number of messages to look back for code execution. Default to 1.
            llm_config (dict or False): llm inference configuration.
                Please refer to [autogen.Completion.create](/docs/reference/autogen/oai/completion#create)
                for available options.
                To disable llm-based auto reply, set to False.
            default_auto_reply (str or dict or None): default auto reply when no code execution or llm-based reply is generated.
        '''
    def register_reply(self, trigger: Type[Agent] | str | Agent | Callable[[Agent], bool] | List, reply_func: Callable, position: int | None = 0, config: Any | None = None, reset_config: Callable | None = None):
        """Register a reply function.

        The reply function will be called when the trigger matches the sender.
        The function registered later will be checked earlier by default.
        To change the order, set the position to a positive integer.

        Args:
            trigger (Agent class, str, Agent instance, callable, or list): the trigger.
                - If a class is provided, the reply function will be called when the sender is an instance of the class.
                - If a string is provided, the reply function will be called when the sender's name matches the string.
                - If an agent instance is provided, the reply function will be called when the sender is the agent instance.
                - If a callable is provided, the reply function will be called when the callable returns True.
                - If a list is provided, the reply function will be called when any of the triggers in the list is activated.
                - If None is provided, the reply function will be called only when the sender is None.
                Note: Be sure to register `None` as a trigger if you would like to trigger an auto-reply function with non-empty messages and `sender=None`.
            reply_func (Callable): the reply function.
                The function takes a recipient agent, a list of messages, a sender agent and a config as input and returns a reply message.
        ```python
        def reply_func(
            recipient: ConversableAgent,
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            config: Optional[Any] = None,
        ) -> Union[str, Dict, None]:
        ```
            position (int): the position of the reply function in the reply function list.
                The function registered later will be checked earlier by default.
                To change the order, set the position to a positive integer.
            config (Any): the config to be passed to the reply function.
                When an agent is reset, the config will be reset to the original value.
            reset_config (Callable): the function to reset the config.
                The function returns None. Signature: ```def reset_config(config: Any)```
        """
    @property
    def system_message(self):
        """Return the system message."""
    def update_system_message(self, system_message: str):
        """Update the system message.

        Args:
            system_message (str): system message for the ChatCompletion inference.
        """
    def update_max_consecutive_auto_reply(self, value: int, sender: Agent | None = None):
        """Update the maximum number of consecutive auto replies.

        Args:
            value (int): the maximum number of consecutive auto replies.
            sender (Agent): when the sender is provided, only update the max_consecutive_auto_reply for that sender.
        """
    def max_consecutive_auto_reply(self, sender: Agent | None = None) -> int:
        """The maximum number of consecutive auto replies."""
    @property
    def chat_messages(self) -> Dict[str, List[Dict]]:
        """A dictionary of conversations from name to list of ChatCompletion messages."""
    def last_message(self, agent: Agent | None = None) -> Dict:
        """The last message exchanged with the agent.

        Args:
            agent (Agent): The agent in the conversation.
                If None and more than one agent's conversations are found, an error will be raised.
                If None and only one conversation is found, the last message of the only conversation will be returned.

        Returns:
            The last message exchanged with the agent.
        """
    @property
    def use_docker(self) -> bool | str | None:
        """Bool value of whether to use docker to execute the code,
        or str value of the docker image name to use, or None when code execution is disabled.
        """
    def send(self, message: Dict | str, recipient: Agent, request_reply: bool | None = None, silent: bool | None = False) -> bool:
        '''Send a message to another agent.

        Args:
            message (dict or str): message to be sent.
                The message could contain the following fields (either content or function_call must be provided):
                - content (str): the content of the message.
                - function_call (str): the name of the function to be called.
                - name (str): the name of the function to be called.
                - role (str): the role of the message, any role that is not "function"
                    will be modified to "assistant".
                - context (dict): the context of the message, which will be passed to
                    [autogen.Completion.create](../oai/Completion#create).
                    For example, one agent can send a message A as:
        ```python
        {
            "content": lambda context: context["use_tool_msg"],
            "context": {
                "use_tool_msg": "Use tool X if they are relevant."
            }
        }
        ```
                    Next time, one agent can send a message B with a different "use_tool_msg".
                    Then the content of message A will be refreshed to the new "use_tool_msg".
                    So effectively, this provides a way for an agent to send a "link" and modify
                    the content of the "link" later.
            recipient (Agent): the recipient of the message.
            request_reply (bool or None): whether to request a reply from the recipient.
            silent (bool or None): (Experimental) whether to print the message sent.

        Raises:
            ValueError: if the message can\'t be converted into a valid ChatCompletion message.
        '''
    async def a_send(self, message: Dict | str, recipient: Agent, request_reply: bool | None = None, silent: bool | None = False) -> bool:
        '''(async) Send a message to another agent.

        Args:
            message (dict or str): message to be sent.
                The message could contain the following fields (either content or function_call must be provided):
                - content (str): the content of the message.
                - function_call (str): the name of the function to be called.
                - name (str): the name of the function to be called.
                - role (str): the role of the message, any role that is not "function"
                    will be modified to "assistant".
                - context (dict): the context of the message, which will be passed to
                    [autogen.Completion.create](../oai/Completion#create).
                    For example, one agent can send a message A as:
        ```python
        {
            "content": lambda context: context["use_tool_msg"],
            "context": {
                "use_tool_msg": "Use tool X if they are relevant."
            }
        }
        ```
                    Next time, one agent can send a message B with a different "use_tool_msg".
                    Then the content of message A will be refreshed to the new "use_tool_msg".
                    So effectively, this provides a way for an agent to send a "link" and modify
                    the content of the "link" later.
            recipient (Agent): the recipient of the message.
            request_reply (bool or None): whether to request a reply from the recipient.
            silent (bool or None): (Experimental) whether to print the message sent.

        Raises:
            ValueError: if the message can\'t be converted into a valid ChatCompletion message.
        '''
    def receive(self, message: Dict | str, sender: Agent, request_reply: bool | None = None, silent: bool | None = False):
        '''Receive a message from another agent.

        Once a message is received, this function sends a reply to the sender or stop.
        The reply can be generated automatically or entered manually by a human.

        Args:
            message (dict or str): message from the sender. If the type is dict, it may contain the following reserved fields (either content or function_call need to be provided).
                1. "content": content of the message, can be None.
                2. "function_call": a dictionary containing the function name and arguments.
                3. "role": role of the message, can be "assistant", "user", "function".
                    This field is only needed to distinguish between "function" or "assistant"/"user".
                4. "name": In most cases, this field is not needed. When the role is "function", this field is needed to indicate the function name.
                5. "context" (dict): the context of the message, which will be passed to
                    [autogen.Completion.create](../oai/Completion#create).
            sender: sender of an Agent instance.
            request_reply (bool or None): whether a reply is requested from the sender.
                If None, the value is determined by `self.reply_at_receive[sender]`.
            silent (bool or None): (Experimental) whether to print the message received.

        Raises:
            ValueError: if the message can\'t be converted into a valid ChatCompletion message.
        '''
    async def a_receive(self, message: Dict | str, sender: Agent, request_reply: bool | None = None, silent: bool | None = False):
        '''(async) Receive a message from another agent.

        Once a message is received, this function sends a reply to the sender or stop.
        The reply can be generated automatically or entered manually by a human.

        Args:
            message (dict or str): message from the sender. If the type is dict, it may contain the following reserved fields (either content or function_call need to be provided).
                1. "content": content of the message, can be None.
                2. "function_call": a dictionary containing the function name and arguments.
                3. "role": role of the message, can be "assistant", "user", "function".
                    This field is only needed to distinguish between "function" or "assistant"/"user".
                4. "name": In most cases, this field is not needed. When the role is "function", this field is needed to indicate the function name.
                5. "context" (dict): the context of the message, which will be passed to
                    [autogen.Completion.create](../oai/Completion#create).
            sender: sender of an Agent instance.
            request_reply (bool or None): whether a reply is requested from the sender.
                If None, the value is determined by `self.reply_at_receive[sender]`.
            silent (bool or None): (Experimental) whether to print the message received.

        Raises:
            ValueError: if the message can\'t be converted into a valid ChatCompletion message.
        '''
    def initiate_chat(self, recipient: ConversableAgent, clear_history: bool | None = True, silent: bool | None = False, **context):
        '''Initiate a chat with the recipient agent.

        Reset the consecutive auto reply counter.
        If `clear_history` is True, the chat history with the recipient agent will be cleared.
        `generate_init_message` is called to generate the initial message for the agent.

        Args:
            recipient: the recipient agent.
            clear_history (bool): whether to clear the chat history with the agent.
            silent (bool or None): (Experimental) whether to print the messages for this conversation.
            **context: any context information.
                "message" needs to be provided if the `generate_init_message` method is not overridden.
        '''
    async def a_initiate_chat(self, recipient: ConversableAgent, clear_history: bool | None = True, silent: bool | None = False, **context):
        '''(async) Initiate a chat with the recipient agent.

        Reset the consecutive auto reply counter.
        If `clear_history` is True, the chat history with the recipient agent will be cleared.
        `generate_init_message` is called to generate the initial message for the agent.

        Args:
            recipient: the recipient agent.
            clear_history (bool): whether to clear the chat history with the agent.
            silent (bool or None): (Experimental) whether to print the messages for this conversation.
            **context: any context information.
                "message" needs to be provided if the `generate_init_message` method is not overridden.
        '''
    def reset(self) -> None:
        """Reset the agent."""
    def stop_reply_at_receive(self, sender: Agent | None = None):
        """Reset the reply_at_receive of the sender."""
    def reset_consecutive_auto_reply_counter(self, sender: Agent | None = None):
        """Reset the consecutive_auto_reply_counter of the sender."""
    def clear_history(self, agent: Agent | None = None):
        """Clear the chat history of the agent.

        Args:
            agent: the agent with whom the chat history to clear. If None, clear the chat history with all agents.
        """
    def generate_oai_reply(self, messages: List[Dict] | None = None, sender: Agent | None = None, config: Any | None = None) -> Tuple[bool, str | Dict | None]:
        """Generate a reply using autogen.oai."""
    def generate_code_execution_reply(self, messages: List[Dict] | None = None, sender: Agent | None = None, config: Any | None = None):
        """Generate a reply using code execution."""
    def generate_function_call_reply(self, messages: List[Dict] | None = None, sender: Agent | None = None, config: Any | None = None):
        """Generate a reply using function call."""
    def check_termination_and_human_reply(self, messages: List[Dict] | None = None, sender: Agent | None = None, config: Any | None = None) -> Tuple[bool, str | Dict | None]:
        """Check if the conversation should be terminated, and if human reply is provided."""
    def generate_reply(self, messages: List[Dict] | None = None, sender: Agent | None = None, exclude: List[Callable] | None = None) -> str | Dict | None:
        """Reply based on the conversation history and the sender.

        Either messages or sender must be provided.
        Register a reply_func with `None` as one trigger for it to be activated when `messages` is non-empty and `sender` is `None`.
        Use registered auto reply functions to generate replies.
        By default, the following functions are checked in order:
        1. check_termination_and_human_reply
        2. generate_function_call_reply
        3. generate_code_execution_reply
        4. generate_oai_reply
        Every function returns a tuple (final, reply).
        When a function returns final=False, the next function will be checked.
        So by default, termination and human reply will be checked first.
        If not terminating and human reply is skipped, execute function or code and return the result.
        AI replies are generated only when no code execution is performed.

        Args:
            messages: a list of messages in the conversation history.
            default_reply (str or dict): default reply.
            sender: sender of an Agent instance.
            exclude: a list of functions to exclude.

        Returns:
            str or dict or None: reply. None if no reply is generated.
        """
    async def a_generate_reply(self, messages: List[Dict] | None = None, sender: Agent | None = None, exclude: List[Callable] | None = None) -> str | Dict | None:
        """(async) Reply based on the conversation history and the sender.

        Either messages or sender must be provided.
        Register a reply_func with `None` as one trigger for it to be activated when `messages` is non-empty and `sender` is `None`.
        Use registered auto reply functions to generate replies.
        By default, the following functions are checked in order:
        1. check_termination_and_human_reply
        2. generate_function_call_reply
        3. generate_code_execution_reply
        4. generate_oai_reply
        Every function returns a tuple (final, reply).
        When a function returns final=False, the next function will be checked.
        So by default, termination and human reply will be checked first.
        If not terminating and human reply is skipped, execute function or code and return the result.
        AI replies are generated only when no code execution is performed.

        Args:
            messages: a list of messages in the conversation history.
            default_reply (str or dict): default reply.
            sender: sender of an Agent instance.
            exclude: a list of functions to exclude.

        Returns:
            str or dict or None: reply. None if no reply is generated.
        """
    def get_human_input(self, prompt: str) -> str:
        """Get human input.

        Override this method to customize the way to get human input.

        Args:
            prompt (str): prompt for the human input.

        Returns:
            str: human input.
        """
    def run_code(self, code, **kwargs):
        """Run the code and return the result.

        Override this function to modify the way to run the code.
        Args:
            code (str): the code to be executed.
            **kwargs: other keyword arguments.

        Returns:
            A tuple of (exitcode, logs, image).
            exitcode (int): the exit code of the code execution.
            logs (str): the logs of the code execution.
            image (str or None): the docker image used for the code execution.
        """
    def execute_code_blocks(self, code_blocks):
        """Execute the code blocks and return the result."""
    def execute_function(self, func_call):
        '''Execute a function call and return the result.

        Override this function to modify the way to execute a function call.

        Args:
            func_call: a dictionary extracted from openai message at key "function_call" with keys "name" and "arguments".

        Returns:
            A tuple of (is_exec_success, result_dict).
            is_exec_success (boolean): whether the execution is successful.
            result_dict: a dictionary with keys "name", "role", and "content". Value of "role" is "function".
        '''
    def generate_init_message(self, **context) -> str | Dict:
        '''Generate the initial message for the agent.

        Override this function to customize the initial message based on user\'s request.
        If not overriden, "message" needs to be provided in the context.
        '''
    def register_function(self, function_map: Dict[str, Callable]):
        """Register functions to the agent.

        Args:
            function_map: a dictionary mapping function names to functions.
        """
