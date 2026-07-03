from flaml.default import greedy as greedy
from flaml.default.regret import build_regret as build_regret, load_result as load_result
from flaml.version import __version__ as __version__

regret_bound: float

def config_predictor_tuple(tasks, configs, meta_features, regret_matrix):
    """Config predictor represented in tuple.

    The returned tuple consists of (meta_features, preferences, proc).

    Returns:
        meta_features_norm: A dataframe of normalized meta features, each column for a task.
        preferences: A dataframe of sorted configuration indicies by their performance per task (column).
        regret_matrix: A dataframe of the configuration(row)-task(column) regret matrix.
    """
def build_portfolio(meta_features, regret, strategy):
    '''Build a portfolio from meta features and regret matrix.

    Args:
        meta_features: A dataframe of metafeatures matrix.
        regret: A dataframe of regret matrix.
        strategy: A str of the strategy, one of ("greedy", "greedy-feedback").
    '''
def load_json(filename):
    """Returns the contents of json file filename."""
def serialize(configs, regret, meta_features, output_file, config_path):
    """Store to disk all information FLAML-metalearn needs at runtime.

    configs: names of model configs
    regret: regret matrix
    meta_features: task metafeatures
    output_file: filename
    config_path: path containing config json files
    """
def main() -> None: ...
