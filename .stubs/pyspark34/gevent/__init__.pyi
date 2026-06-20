import sys
from _typeshed import Incomplete
from gevent._config import config as config
from gevent._hub_local import get_hub as get_hub
from gevent._hub_primitives import iwait_on_objects as iwait, wait_on_objects as wait
from gevent.greenlet import Greenlet as Greenlet, joinall as joinall, killall as killall
from gevent.hub import GreenletExit as GreenletExit, getcurrent as getcurrent, idle as idle, kill as kill, reinit as reinit, signal as signal_handler, sleep as sleep, spawn_raw as spawn_raw
from gevent.timeout import Timeout as Timeout, with_timeout as with_timeout
from typing import NamedTuple

__all__ = ['Greenlet', 'GreenletExit', 'Timeout', 'config', 'get_hub', 'getcurrent', 'getswitchinterval', 'idle', 'iwait', 'joinall', 'kill', 'killall', 'reinit', 'setswitchinterval', 'signal_handler', 'sleep', 'spawn', 'spawn_later', 'spawn_raw', 'wait', 'with_timeout']

class _version_info(NamedTuple):
    major: Incomplete
    minor: Incomplete
    micro: Incomplete
    releaselevel: Incomplete
    serial: Incomplete
getswitchinterval = sys.getswitchinterval
setswitchinterval = sys.setswitchinterval
spawn: Incomplete
spawn_later: Incomplete
