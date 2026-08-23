from .agent import Agent as Agent
from .conversable_agent import ConversableAgent as ConversableAgent
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class GroupChat:
    """A group chat class that contains a list of agents and the maximum number of rounds."""
    agents: List[Agent]
    messages: List[Dict]
    max_round: int = ...
    admin_name: str = ...
    @property
    def agent_names(self) -> List[str]:
        """Return the names of the agents in the group chat."""
    def reset(self) -> None:
        """Reset the group chat."""
    def agent_by_name(self, name: str) -> Agent:
        """Find the next speaker based on the message."""
    def next_agent(self, agent: Agent) -> Agent:
        """Return the next agent in the list."""
    def select_speaker_msg(self):
        """Return the message for selecting the next speaker."""
    def select_speaker(self, last_speaker: Agent, selector: ConversableAgent):
        """Select the next speaker."""
    def __init__(self, agents, messages, max_round, admin_name) -> None: ...

class GroupChatManager(ConversableAgent):
    """(In preview) A chat manager agent that can manage a group chat of multiple agents."""
    def __init__(self, groupchat: GroupChat, name: str | None = 'chat_manager', max_consecutive_auto_reply: int | None = ..., human_input_mode: str | None = 'NEVER', system_message: str | None = 'Group chat manager.', **kwargs) -> None: ...
    def run_chat(self, messages: List[Dict] | None = None, sender: Agent | None = None, config: GroupChat | None = None) -> str | Dict | None:
        """Run a group chat."""
