from _typeshed import Incomplete
from tensorboard.plugins.hparams import api_pb2 as api_pb2, metadata as metadata

class Context:
    """Wraps the base_plugin.TBContext to stores additional data shared across
    API handlers for the HParams plugin backend.

    Before adding fields to this class, carefully consider whether the
    field truelly needs to be accessible to all API handlers or if it
    can be passed separately to the handler constructor. We want to
    avoid this class becoming a magic container of variables that have
    no better place. See http://wiki.c2.com/?MagicContainer
    """
    def __init__(self, tb_context, max_domain_discrete_len: int = 10) -> None:
        '''Instantiates a context.

        Args:
          tb_context: base_plugin.TBContext. The "base" context we extend.
          max_domain_discrete_len: int. Only used when computing the experiment
            from the session runs. The maximum number of disticnt values a string
            hyperparameter can have for us to populate its \'domain_discrete\' field.
            Typically, only tests should specify a value for this parameter.
        '''
    def experiment_from_metadata(self, ctx, experiment_id, hparams_run_to_tag_to_content):
        """Returns the experiment protobuffer defining the experiment.

        Accepts a dict containing the plugin contents for all summary tags
        associated with the hparams plugin, as an optimization for callers
        who already have this information available, so that this function
        can minimize its calls to the underlying `DataProvider`.

        This method first attempts to find a metadata.EXPERIMENT_TAG tag and
        retrieve the associated protobuffer. If no such tag is found, the method
        will attempt to build a minimal experiment protobuffer by scanning for
        all metadata.SESSION_START_INFO_TAG tags (to compute the hparam_infos
        field of the experiment) and for all scalar tags (to compute the
        metric_infos field of the experiment).

        Returns:
          The experiment protobuffer. If no tags are found from which an experiment
          protobuffer can be built (possibly, because the event data has not been
          completely loaded yet), returns an entirely empty experiment.
        """
    @property
    def tb_context(self): ...
    def hparams_metadata(self, ctx, experiment_id, run_tag_filter: Incomplete | None = None):
        """Reads summary metadata for all hparams time series.

        Args:
          experiment_id: String, from `plugin_util.experiment_id`.
          run_tag_filter: Optional `data.provider.RunTagFilter`, with
            the semantics as in `list_tensors`.

        Returns:
          A dict `d` such that `d[run][tag]` is a `bytes` value with the
          summary metadata content for the keyed time series.
        """
    def scalars_metadata(self, ctx, experiment_id):
        """Reads summary metadata for all scalar time series.

        Args:
          experiment_id: String, from `plugin_util.experiment_id`.

        Returns:
          A dict `d` such that `d[run][tag]` is a `bytes` value with the
          summary metadata content for the keyed time series.
        """
    def read_last_scalars(self, ctx, experiment_id, run_tag_filter):
        """Reads the most recent values from scalar time series.

        Args:
          experiment_id: String.
          run_tag_filter: Required `data.provider.RunTagFilter`, with
            the semantics as in `read_scalars`.

        Returns:
          A dict `d` such that `d[run][tag]` is a `provider.ScalarDatum`
          value, with keys only for runs and tags that actually had
          data, which may be a subset of what was requested.
        """
