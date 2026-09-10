from _typeshed import Incomplete
from openai import File as File, FineTune as FineTune

WANDB_AVAILABLE: bool

class WandbLogger:
    """
    Log fine-tunes to [Weights & Biases](https://wandb.me/openai-docs)
    """
    @classmethod
    def sync(cls, id: Incomplete | None = None, n_fine_tunes: Incomplete | None = None, project: str = 'GPT-3', entity: Incomplete | None = None, force: bool = False, **kwargs_wandb_init):
        '''
        Sync fine-tunes to Weights & Biases.
        :param id: The id of the fine-tune (optional)
        :param n_fine_tunes: Number of most recent fine-tunes to log when an id is not provided. By default, every fine-tune is synced.
        :param project: Name of the project where you\'re sending runs. By default, it is "GPT-3".
        :param entity: Username or team name where you\'re sending runs. By default, your default entity is used, which is usually your username.
        :param force: Forces logging and overwrite existing wandb run of the same fine-tune.
        '''
