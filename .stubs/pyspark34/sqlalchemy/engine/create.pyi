from . import base as base
from .. import event as event, exc as exc, util as util
from ..log import _EchoFlagType
from ..pool import ConnectionPoolEntry as ConnectionPoolEntry, Pool as Pool, _CreatorFnType, _CreatorWRecFnType, _ResetStyleArgType
from ..sql import compiler as compiler
from ..util import immutabledict as immutabledict
from ..util.typing import Literal as Literal
from .base import Engine as Engine
from .interfaces import DBAPIConnection as DBAPIConnection, IsolationLevel as IsolationLevel, _ExecuteOptions, _ParamStyle
from .mock import create_mock_engine as create_mock_engine
from .url import URL as URL
from typing import Any, Callable, Dict, List, Type, overload

@overload
def create_engine(url: str | URL, *, connect_args: Dict[Any, Any] = ..., convert_unicode: bool = ..., creator: _CreatorFnType | _CreatorWRecFnType = ..., echo: _EchoFlagType = ..., echo_pool: _EchoFlagType = ..., enable_from_linting: bool = ..., execution_options: _ExecuteOptions = ..., future: Literal[True], hide_parameters: bool = ..., implicit_returning: Literal[True] = ..., insertmanyvalues_page_size: int = ..., isolation_level: IsolationLevel = ..., json_deserializer: Callable[..., Any] = ..., json_serializer: Callable[..., Any] = ..., label_length: int | None = ..., logging_name: str = ..., max_identifier_length: int | None = ..., max_overflow: int = ..., module: Any | None = ..., paramstyle: _ParamStyle | None = ..., pool: Pool | None = ..., poolclass: Type[Pool] | None = ..., pool_logging_name: str = ..., pool_pre_ping: bool = ..., pool_size: int = ..., pool_recycle: int = ..., pool_reset_on_return: _ResetStyleArgType | None = ..., pool_timeout: float = ..., pool_use_lifo: bool = ..., plugins: List[str] = ..., query_cache_size: int = ..., use_insertmanyvalues: bool = ..., **kwargs: Any) -> Engine: ...
@overload
def create_engine(url: str | URL, **kwargs: Any) -> Engine: ...
def engine_from_config(configuration: Dict[str, Any], prefix: str = 'sqlalchemy.', **kwargs: Any) -> Engine:
    '''Create a new Engine instance using a configuration dictionary.

    The dictionary is typically produced from a config file.

    The keys of interest to ``engine_from_config()`` should be prefixed, e.g.
    ``sqlalchemy.url``, ``sqlalchemy.echo``, etc.  The \'prefix\' argument
    indicates the prefix to be searched for.  Each matching key (after the
    prefix is stripped) is treated as though it were the corresponding keyword
    argument to a :func:`_sa.create_engine` call.

    The only required key is (assuming the default prefix) ``sqlalchemy.url``,
    which provides the :ref:`database URL <database_urls>`.

    A select set of keyword arguments will be "coerced" to their
    expected type based on string values.    The set of arguments
    is extensible per-dialect using the ``engine_config_types`` accessor.

    :param configuration: A dictionary (typically produced from a config file,
        but this is not a requirement).  Items whose keys start with the value
        of \'prefix\' will have that prefix stripped, and will then be passed to
        :func:`_sa.create_engine`.

    :param prefix: Prefix to match and then strip from keys
        in \'configuration\'.

    :param kwargs: Each keyword argument to ``engine_from_config()`` itself
        overrides the corresponding item taken from the \'configuration\'
        dictionary.  Keyword arguments should *not* be prefixed.

    '''
@overload
def create_pool_from_url(url: str | URL, *, poolclass: Type[Pool] | None = ..., logging_name: str = ..., pre_ping: bool = ..., size: int = ..., recycle: int = ..., reset_on_return: _ResetStyleArgType | None = ..., timeout: float = ..., use_lifo: bool = ..., **kwargs: Any) -> Pool: ...
@overload
def create_pool_from_url(url: str | URL, **kwargs: Any) -> Pool: ...
