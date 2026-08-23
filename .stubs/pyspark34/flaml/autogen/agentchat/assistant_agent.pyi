from .conversable_agent import ConversableAgent as ConversableAgent
from typing import Callable, Dict

class AssistantAgent(ConversableAgent):
    '''(In preview) Assistant agent, designed to solve a task with LLM.

    AssistantAgent is a subclass of ConversableAgent configured with a default system message.
    The default system message is designed to solve a task with LLM,
    including suggesting python code blocks and debugging.
    `human_input_mode` is default to "NEVER"
    and `code_execution_config` is default to False.
    This agent doesn\'t execute code by default, and expects the user to execute the code.
    '''
    DEFAULT_SYSTEM_MESSAGE: str
    def __init__(self, name: str, system_message: str | None = ..., llm_config: Dict | bool | None = None, is_termination_msg: Callable[[Dict], bool] | None = None, max_consecutive_auto_reply: int | None = None, human_input_mode: str | None = 'NEVER', code_execution_config: Dict | bool | None = False, **kwargs) -> None:
        '''
        Args:
            name (str): agent name.
            system_message (str): system message for the ChatCompletion inference.
                Please override this attribute if you want to reprogram the agent.
            llm_config (dict): llm inference configuration.
                Please refer to [autogen.Completion.create](/docs/reference/autogen/oai/completion#create)
                for available options.
            is_termination_msg (function): a function that takes a message in the form of a dictionary
                and returns a boolean value indicating if this received message is a termination message.
                The dict can contain the following keys: "content", "role", "name", "function_call".
            max_consecutive_auto_reply (int): the maximum number of consecutive auto replies.
                default to None (no limit provided, class attribute MAX_CONSECUTIVE_AUTO_REPLY will be used as the limit in this case).
                The limit only plays a role when human_input_mode is not "ALWAYS".
            **kwargs (dict): Please refer to other kwargs in
                [ConversableAgent](conversable_agent#__init__).
        '''
