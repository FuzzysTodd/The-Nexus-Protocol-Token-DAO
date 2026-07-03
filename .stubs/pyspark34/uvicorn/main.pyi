import asyncio
import click
import os
import typing
from _typeshed import Incomplete
from uvicorn._types import ASGIApplication as ASGIApplication
from uvicorn.config import Config as Config, HTTPProtocolType as HTTPProtocolType, HTTP_PROTOCOLS as HTTP_PROTOCOLS, INTERFACES as INTERFACES, InterfaceType as InterfaceType, LIFESPAN as LIFESPAN, LOGGING_CONFIG as LOGGING_CONFIG, LOG_LEVELS as LOG_LEVELS, LOOP_SETUPS as LOOP_SETUPS, LifespanType as LifespanType, LoopSetupType as LoopSetupType, SSL_PROTOCOL_VERSION as SSL_PROTOCOL_VERSION, WSProtocolType as WSProtocolType, WS_PROTOCOLS as WS_PROTOCOLS
from uvicorn.server import Server as Server, ServerState as ServerState
from uvicorn.supervisors import ChangeReload as ChangeReload, Multiprocess as Multiprocess

LEVEL_CHOICES: Incomplete
HTTP_CHOICES: Incomplete
WS_CHOICES: Incomplete
LIFESPAN_CHOICES: Incomplete
LOOP_CHOICES: Incomplete
INTERFACE_CHOICES: Incomplete
STARTUP_FAILURE: int
logger: Incomplete

def print_version(ctx: click.Context, param: click.Parameter, value: bool) -> None: ...
def main(app: str, host: str, port: int, uds: str, fd: int, loop: LoopSetupType, http: HTTPProtocolType, ws: WSProtocolType, ws_max_size: int, ws_max_queue: int, ws_ping_interval: float, ws_ping_timeout: float, ws_per_message_deflate: bool, lifespan: LifespanType, interface: InterfaceType, reload: bool, reload_dirs: typing.List[str], reload_includes: typing.List[str], reload_excludes: typing.List[str], reload_delay: float, workers: int, env_file: str, log_config: str, log_level: str, access_log: bool, proxy_headers: bool, server_header: bool, date_header: bool, forwarded_allow_ips: str, root_path: str, limit_concurrency: int, backlog: int, limit_max_requests: int, timeout_keep_alive: int, timeout_graceful_shutdown: int | None, ssl_keyfile: str, ssl_certfile: str, ssl_keyfile_password: str, ssl_version: int, ssl_cert_reqs: int, ssl_ca_certs: str, ssl_ciphers: str, headers: typing.List[str], use_colors: bool, app_dir: str, h11_max_incomplete_event_size: int | None, factory: bool) -> None: ...
def run(app: ASGIApplication | typing.Callable | str, *, host: str = '127.0.0.1', port: int = 8000, uds: str | None = None, fd: int | None = None, loop: LoopSetupType = 'auto', http: typing.Type[asyncio.Protocol] | HTTPProtocolType = 'auto', ws: typing.Type[asyncio.Protocol] | WSProtocolType = 'auto', ws_max_size: int = 16777216, ws_max_queue: int = 32, ws_ping_interval: float | None = 20.0, ws_ping_timeout: float | None = 20.0, ws_per_message_deflate: bool = True, lifespan: LifespanType = 'auto', interface: InterfaceType = 'auto', reload: bool = False, reload_dirs: typing.List[str] | str | None = None, reload_includes: typing.List[str] | str | None = None, reload_excludes: typing.List[str] | str | None = None, reload_delay: float = 0.25, workers: int | None = None, env_file: str | os.PathLike | None = None, log_config: typing.Dict[str, typing.Any] | str | None = ..., log_level: str | int | None = None, access_log: bool = True, proxy_headers: bool = True, server_header: bool = True, date_header: bool = True, forwarded_allow_ips: typing.List[str] | str | None = None, root_path: str = '', limit_concurrency: int | None = None, backlog: int = 2048, limit_max_requests: int | None = None, timeout_keep_alive: int = 5, timeout_graceful_shutdown: int | None = None, ssl_keyfile: str | None = None, ssl_certfile: str | os.PathLike | None = None, ssl_keyfile_password: str | None = None, ssl_version: int = ..., ssl_cert_reqs: int = ..., ssl_ca_certs: str | None = None, ssl_ciphers: str = 'TLSv1', headers: typing.List[typing.Tuple[str, str]] | None = None, use_colors: bool | None = None, app_dir: str | None = None, factory: bool = False, h11_max_incomplete_event_size: int | None = None) -> None: ...
