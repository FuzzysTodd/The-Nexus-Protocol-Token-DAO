from tensorboard.compat import tf as tf
from tensorboard.plugins.projector.projector_config_pb2 import EmbeddingInfo as EmbeddingInfo, ProjectorConfig as ProjectorConfig, SpriteMetadata as SpriteMetadata

def visualize_embeddings(logdir, config):
    """Stores a config file used by the embedding projector.

    Args:
      logdir: Directory into which to store the config file, as a `str`.
        For compatibility, can also be a `tf.compat.v1.summary.FileWriter`
        object open at the desired logdir.
      config: `tf.contrib.tensorboard.plugins.projector.ProjectorConfig`
        proto that holds the configuration for the projector such as paths to
        checkpoint files and metadata files for the embeddings. If
        `config.model_checkpoint_path` is none, it defaults to the
        `logdir` used by the summary_writer.

    Raises:
      ValueError: If the summary writer does not have a `logdir`.
    """
