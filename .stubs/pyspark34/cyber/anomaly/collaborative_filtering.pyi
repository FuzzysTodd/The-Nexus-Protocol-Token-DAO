from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext
from pyspark.ml import Estimator, Transformer
from pyspark.sql import DataFrame
from typing import Tuple

class AccessAnomalyConfig:
    """
    Define default values for AccessAnomaly Params
    """
    default_tenant_col: str
    default_user_col: str
    default_res_col: str
    default_likelihood_col: str
    default_output_col: str
    default_rank: int
    default_max_iter: int
    default_reg_param: float
    default_num_blocks: Incomplete
    default_separate_tenants: bool
    default_low_value: float
    default_high_value: float
    default_apply_implicit_cf: bool
    default_alpha: float
    default_complementset_factor: int
    default_neg_score: float

class _UserResourceFeatureVectorMapping:
    """
    Private class used to pass the mappings as calculated by the AccessAnomaliesEstimator.
    An object representing the user and resource models
    (mapping from name to latent vector)
    and the relevant column names
    """
    tenant_col: Incomplete
    user_col: Incomplete
    user_vec_col: Incomplete
    res_col: Incomplete
    res_vec_col: Incomplete
    history_access_df: Incomplete
    user2component_mappings_df: Incomplete
    res2component_mappings_df: Incomplete
    user_feature_vector_mapping_df: Incomplete
    res_feature_vector_mapping_df: Incomplete
    def __init__(self, tenant_col: str, user_col: str, user_vec_col: str, res_col: str, res_vec_col: str, history_access_df: DataFrame | None, user2component_mappings_df: DataFrame | None, res2component_mappings_df: DataFrame | None, user_feature_vector_mapping_df: DataFrame, res_feature_vector_mapping_df: DataFrame) -> None: ...
    def replace_mappings(self, user_feature_vector_mapping_df: DataFrame | None = None, res_feature_vector_mapping_df: DataFrame | None = None):
        """
        create a new model replacing the user and resource models with new ones (optional)

        :param user_feature_vector_mapping_df: optional new user model mapping names to latent vectors
        :param res_feature_vector_mapping_df: optional new resource model mapping names to latent vectors
        :return:
        """
    def check(self):
        """
        check the validity of the model
        :return: boolean value where True indicating the verification succeeded
        """

class AccessAnomalyModel(Transformer):
    outputCol: Incomplete
    user_res_feature_vector_mapping: Incomplete
    has_components: Incomplete
    preserve_history: bool
    def __init__(self, userResourceFeatureVectorMapping: _UserResourceFeatureVectorMapping, outputCol: str) -> None: ...
    def save(self, path: str, path_suffix: str = '', output_format: str = 'parquet'): ...
    @staticmethod
    def load(spark: SQLContext, path: str, output_format: str = 'parquet') -> AccessAnomalyModel: ...
    @property
    def tenant_col(self): ...
    @property
    def user_col(self): ...
    @property
    def user_vec_col(self): ...
    @property
    def res_col(self): ...
    @property
    def res_vec_col(self): ...
    @property
    def user_mapping_df(self): ...
    @property
    def res_mapping_df(self): ...

class ConnectedComponents:
    tenant_col: Incomplete
    user_col: Incomplete
    res_col: Incomplete
    component_col_name: Incomplete
    def __init__(self, tenantCol: str, userCol: str, res_col: str, componentColName: str = 'component') -> None: ...
    def transform(self, df: DataFrame) -> Tuple[DataFrame, DataFrame]: ...

class AccessAnomaly(Estimator):
    """
    This is the AccessAnomaly, a pyspark.ml.Estimator which
    creates the AccessAnomalyModel which is a pyspark.ml.Transformer
    """
    tenantCol: Incomplete
    userCol: Incomplete
    resCol: Incomplete
    likelihoodCol: Incomplete
    outputCol: Incomplete
    rankParam: Incomplete
    maxIter: Incomplete
    regParam: Incomplete
    numBlocks: Incomplete
    separateTenants: Incomplete
    lowValue: Incomplete
    highValue: Incomplete
    applyImplicitCf: Incomplete
    alphaParam: Incomplete
    complementsetFactor: Incomplete
    negScore: Incomplete
    historyAccessDf: Incomplete
    def __init__(self, tenantCol: str = ..., userCol: str = ..., resCol: str = ..., likelihoodCol: str = ..., outputCol: str = ..., rankParam: int = ..., maxIter: int = ..., regParam: float = ..., numBlocks: int | None = ..., separateTenants: bool = ..., lowValue: float | None = ..., highValue: float | None = ..., applyImplicitCf: bool = ..., alphaParam: float | None = None, complementsetFactor: int | None = None, negScore: float | None = None, historyAccessDf: DataFrame | None = None) -> None: ...
    @property
    def indexed_user_col(self): ...
    @property
    def user_vec_col(self): ...
    @property
    def indexed_res_col(self): ...
    @property
    def res_vec_col(self): ...
    @property
    def scaled_likelihood_col(self): ...
    def create_spark_model_vectors_df(self, df: DataFrame) -> _UserResourceFeatureVectorMapping: ...

class ModelNormalizeTransformer:
    """
    Given a UserResourceCfDataframeModel this class creates and returns
    a new normalized UserResourceCfDataframeModel which has an anomaly score
    with a mean of 0.0 and standard deviation of 1.0 when applied on the given dataframe
    """
    access_df: Incomplete
    rank: Incomplete
    def __init__(self, access_df: DataFrame, rank: int) -> None: ...
    def transform(self, user_res_cf_df_model: _UserResourceFeatureVectorMapping) -> _UserResourceFeatureVectorMapping: ...
