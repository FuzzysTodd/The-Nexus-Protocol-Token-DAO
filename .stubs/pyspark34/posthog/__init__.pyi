import datetime
from _typeshed import Incomplete
from posthog.client import Client as Client
from posthog.version import VERSION as VERSION
from typing import Callable, Dict

__version__ = VERSION
api_key: str
host: str
on_error: Callable
debug: bool
send: bool
sync_mode: bool
disabled: bool
personal_api_key: str
project_api_key: str
poll_interval: int
disable_geoip: bool
default_client: Incomplete

def capture(distinct_id: str, event: str, properties: Dict | None = None, context: Dict | None = None, timestamp: datetime.datetime | None = None, uuid: str | None = None, groups: Dict | None = None, send_feature_flags: bool = False, disable_geoip: bool | None = None) -> None:
    """
    Capture allows you to capture anything a user does within your system, which you can later use in PostHog to find patterns in usage, work out which features to improve or where people are giving up.

    A `capture` call requires
    - `distinct id` which uniquely identifies your user
    - `event name` to specify the event
    - We recommend using [verb] [noun], like `movie played` or `movie updated` to easily identify what your events mean later on.

    Optionally you can submit
    - `properties`, which can be a dict with any information you'd like to add
    - `groups`, which is a dict of group type -> group key mappings

    For example:
    ```python
    posthog.capture('distinct id', 'opened app')
    posthog.capture('distinct id', 'movie played', {'movie_id': '123', 'category': 'romcom'})

    posthog.capture('distinct id', 'purchase', groups={'company': 'id:5'})
    ```
    """
def identify(distinct_id: str, properties: Dict | None = None, context: Dict | None = None, timestamp: datetime.datetime | None = None, uuid: str | None = None, disable_geoip: bool | None = None) -> None:
    """
    Identify lets you add metadata on your users so you can more easily identify who they are in PostHog, and even do things like segment users by these properties.

    An `identify` call requires
    - `distinct id` which uniquely identifies your user
    - `properties` with a dict with any key: value pairs

    For example:
    ```python
    posthog.identify('distinct id', {
        'email': 'dwayne@gmail.com',
        'name': 'Dwayne Johnson'
    })
    ```
    """
def set(distinct_id: str, properties: Dict | None = None, context: Dict | None = None, timestamp: datetime.datetime | None = None, uuid: str | None = None, disable_geoip: bool | None = None) -> None:
    """
    Set properties on a user record.
    This will overwrite previous people property values, just like `identify`.

     A `set` call requires
     - `distinct id` which uniquely identifies your user
     - `properties` with a dict with any key: value pairs

     For example:
     ```python
     posthog.set('distinct id', {
         'current_browser': 'Chrome',
     })
     ```
    """
def set_once(distinct_id: str, properties: Dict | None = None, context: Dict | None = None, timestamp: datetime.datetime | None = None, uuid: str | None = None, disable_geoip: bool | None = None) -> None:
    """
    Set properties on a user record, only if they do not yet exist.
    This will not overwrite previous people property values, unlike `identify`.

     A `set_once` call requires
     - `distinct id` which uniquely identifies your user
     - `properties` with a dict with any key: value pairs

     For example:
     ```python
     posthog.set_once('distinct id', {
         'referred_by': 'friend',
     })
     ```
    """
def group_identify(group_type: str, group_key: str, properties: Dict | None = None, context: Dict | None = None, timestamp: datetime.datetime | None = None, uuid: str | None = None, disable_geoip: bool | None = None) -> None:
    """
    Set properties on a group

     A `group_identify` call requires
     - `group_type` type of your group
     - `group_key` unique identifier of the group
     - `properties` with a dict with any key: value pairs

     For example:
     ```python
     posthog.group_identify('company', 5, {
         'employees': 11,
     })
     ```
    """
def alias(previous_id: str, distinct_id: str, context: Dict | None = None, timestamp: datetime.datetime | None = None, uuid: str | None = None, disable_geoip: bool | None = None) -> None:
    '''
    To marry up whatever a user does before they sign up or log in with what they do after you need to make an alias call. This will allow you to answer questions like "Which marketing channels leads to users churning after a month?" or "What do users do on our website before signing up?"

    In a purely back-end implementation, this means whenever an anonymous user does something, you\'ll want to send a session ID ([Django](https://stackoverflow.com/questions/526179/in-django-how-can-i-find-out-the-request-session-sessionid-and-use-it-as-a-vari), [Flask](https://stackoverflow.com/questions/15156132/flask-login-how-to-get-session-id)) with the capture call. Then, when that users signs up, you want to do an alias call with the session ID and the newly created user ID.

    The same concept applies for when a user logs in.

    An `alias` call requires
    - `previous distinct id` the unique ID of the user before
    - `distinct id` the current unique id

    For example:
    ```python
    posthog.alias(\'anonymous session id\', \'distinct id\')
    ```
    '''
def feature_enabled(key: str, distinct_id: str, groups: dict = {}, person_properties: dict = {}, group_properties: dict = {}, only_evaluate_locally: bool = False, send_feature_flag_events: bool = True, disable_geoip: bool | None = None) -> bool:
    '''
    Use feature flags to enable or disable features for users.

    For example:
    ```python
    if posthog.feature_enabled(\'beta feature\', \'distinct id\'):
        # do something
    if posthog.feature_enabled(\'groups feature\', \'distinct id\', groups={"organization": "5"}):
        # do something
    ```

    You can call `posthog.load_feature_flags()` before to make sure you\'re not doing unexpected requests.
    '''
def get_feature_flag(key: str, distinct_id: str, groups: dict = {}, person_properties: dict = {}, group_properties: dict = {}, only_evaluate_locally: bool = False, send_feature_flag_events: bool = True, disable_geoip: bool | None = None):
    '''
    Get feature flag variant for users. Used with experiments.
    Example:
    ```python
    if posthog.get_feature_flag(\'beta-feature\', \'distinct_id\') == \'test-variant\':
        # do test variant code
    if posthog.get_feature_flag(\'beta-feature\', \'distinct_id\') == \'control\':
        # do control code
    ```

    `groups` are a mapping from group type to group key. So, if you have a group type of "organization" and a group key of "5",
    you would pass groups={"organization": "5"}.

    `group_properties` take the format: { group_type_name: { group_properties } }

    So, for example, if you have the group type "organization" and the group key "5", with the properties name, and employee count,
    you\'ll send these as:

    ```python
        group_properties={"organization": {"name": "PostHog", "employees": 11}}
    ```
    '''
def get_all_flags(distinct_id: str, groups: dict = {}, person_properties: dict = {}, group_properties: dict = {}, only_evaluate_locally: bool = False, disable_geoip: bool | None = None):
    """
    Get all flags for a given user.
    Example:
    ```python
    flags = posthog.get_all_flags('distinct_id')
    ```

    flags are key-value pairs where the key is the flag key and the value is the flag variant, or True, or False.
    """
def get_feature_flag_payload(key, distinct_id, match_value: Incomplete | None = None, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, send_feature_flag_events: bool = True, disable_geoip: bool | None = None): ...
def get_all_flags_and_payloads(distinct_id, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, disable_geoip: bool | None = None): ...
def feature_flag_definitions():
    """Returns loaded feature flags, if any. Helpful for debugging what flag information you have loaded."""
def page(*args, **kwargs) -> None:
    """Send a page call."""
def screen(*args, **kwargs) -> None:
    """Send a screen call."""
def flush() -> None:
    """Tell the client to flush."""
def join() -> None:
    """Block program until the client clears the queue"""
def shutdown() -> None:
    """Flush all messages and cleanly shutdown the client"""

class Posthog(Client): ...
