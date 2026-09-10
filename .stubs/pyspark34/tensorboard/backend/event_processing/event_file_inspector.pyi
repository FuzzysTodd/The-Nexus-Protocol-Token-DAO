import dataclasses
from _typeshed import Incomplete
from tensorboard.backend.event_processing import event_accumulator as event_accumulator, event_file_loader as event_file_loader, io_wrapper as io_wrapper
from tensorboard.compat import tf as tf
from tensorboard.compat.proto import event_pb2 as event_pb2
from typing import Any, Generator, Mapping

SUMMARY_TYPE_TO_FIELD: Incomplete
TAG_FIELDS: Incomplete
LONG_FIELDS: Incomplete
SHORT_FIELDS: Incomplete
TRACKED_FIELDS: Incomplete
PRINT_SEPARATOR: Incomplete

@dataclasses.dataclass(frozen=True)
class Observation:
    """Contains the data within each Event file that the inspector cares about.

    The inspector accumulates Observations as it processes events.

    Attributes:
      step: Global step of the event.
      wall_time: Timestamp of the event in seconds.
      tag: Tag name associated with the event.
    """
    step: int
    wall_time: float
    tag: str
    def __init__(self, step, wall_time, tag) -> None: ...

@dataclasses.dataclass(frozen=True)
class InspectionUnit:
    """Created for each organizational structure in the event files.

    An InspectionUnit is visible in the final terminal output. For instance, one
    InspectionUnit is created for each subdirectory in logdir. When asked to inspect
    a single event file, there may only be one InspectionUnit.

    Attributes:
      name: Name of the organizational unit that will be printed to console.
      generator: A generator that yields `Event` protos.
      field_to_obs: A mapping from string fields to `Observations` that the inspector
        creates.
    """
    name: str
    generator: Generator[event_pb2.Event, Any, Any]
    field_to_obs: Mapping[str, Observation]
    def __init__(self, name, generator, field_to_obs) -> None: ...

def get_field_to_observations_map(generator, query_for_tag: str = ''):
    """Return a field to `Observations` dict for the event generator.

    Args:
      generator: A generator over event protos.
      query_for_tag: A string that if specified, only create observations for
        events with this tag name.

    Returns:
      A dict mapping keys in `TRACKED_FIELDS` to an `Observation` list.
    """
def get_unique_tags(field_to_obs):
    """Returns a dictionary of tags that a user could query over.

    Args:
      field_to_obs: Dict that maps string field to `Observation` list.

    Returns:
      A dict that maps keys in `TAG_FIELDS` to a list of string tags present in
      the event files. If the dict does not have any observations of the type,
      maps to an empty list so that we can render this to console.
    """
def print_dict(d, show_missing: bool = True) -> None:
    """Prints a shallow dict to console.

    Args:
      d: Dict to print.
      show_missing: Whether to show keys with empty values.
    """
def get_dict_to_print(field_to_obs):
    """Transform the field-to-obs mapping into a printable dictionary.

    Args:
      field_to_obs: Dict that maps string field to `Observation` list.

    Returns:
      A dict with the keys and values to print to console.
    """
def get_out_of_order(list_of_numbers):
    '''Returns elements that break the monotonically non-decreasing trend.

    This is used to find instances of global step values that are "out-of-order",
    which may trigger TensorBoard event discarding logic.

    Args:
      list_of_numbers: A list of numbers.

    Returns:
      A list of tuples in which each tuple are two elements are adjacent, but the
      second element is lower than the first.
    '''
def generators_from_logdir(logdir):
    """Returns a list of event generators for subdirectories with event files.

    The number of generators returned should equal the number of directories
    within logdir that contain event files. If only logdir contains event files,
    returns a list of length one.

    Args:
      logdir: A log directory that contains event files.

    Returns:
      List of event generators for each subdirectory with event files.
    """
def generator_from_event_file(event_file):
    """Returns a generator that yields events from an event file."""
def get_inspection_units(logdir: str = '', event_file: str = '', tag: str = ''):
    """Returns a list of InspectionUnit objects given either logdir or
    event_file.

    If logdir is given, the number of InspectionUnits should equal the
    number of directories or subdirectories that contain event files.

    If event_file is given, the number of InspectionUnits should be 1.

    Args:
      logdir: A log directory that contains event files.
      event_file: Or, a particular event file path.
      tag: An optional tag name to query for.

    Returns:
      A list of InspectionUnit objects.
    """
def inspect(logdir: str = '', event_file: str = '', tag: str = '') -> None:
    """Main function for inspector that prints out a digest of event files.

    Args:
      logdir: A log directory that contains event files.
      event_file: Or, a particular event file path.
      tag: An optional tag name to query for.

    Raises:
      ValueError: If neither logdir and event_file are given, or both are given.
    """
