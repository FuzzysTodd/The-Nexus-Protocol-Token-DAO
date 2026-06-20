from datetime import datetime
from typing import Any, Dict, Generic, TypeVar

__all__ = ['CloudEvent']

DataType = TypeVar('DataType')

class CloudEvent(Generic[DataType]):
    '''Properties of the CloudEvent 1.0 Schema.
    All required parameters must be populated in order to send to Azure.

    :param source: Required. Identifies the context in which an event happened. The combination of id and source must
     be unique for each distinct event. If publishing to a domain topic, source must be the domain topic name.
    :type source: str
    :param type: Required. Type of event related to the originating occurrence.
    :type type: str
    :keyword specversion: Optional. The version of the CloudEvent spec. Defaults to "1.0"
    :paramtype specversion: str
    :keyword data: Optional. Event data specific to the event type.
    :paramtype data: object
    :keyword time: Optional. The time (in UTC) the event was generated.
    :paramtype time: ~datetime.datetime
    :keyword dataschema: Optional. Identifies the schema that data adheres to.
    :paramtype dataschema: str
    :keyword datacontenttype: Optional. Content type of data value.
    :paramtype datacontenttype: str
    :keyword subject: Optional. This describes the subject of the event in the context of the event producer
     (identified by source).
    :paramtype subject: str
    :keyword id: Optional. An identifier for the event. The combination of id and source must be
     unique for each distinct event. If not provided, a random UUID will be generated and used.
    :paramtype id: Optional[str]
    :keyword extensions: Optional. A CloudEvent MAY include any number of additional context attributes
     with distinct names represented as key - value pairs. Each extension must be alphanumeric, lower cased
     and must not exceed the length of 20 characters.
    :paramtype extensions: Optional[dict]
    '''
    source: str
    type: str
    specversion: str
    id: str
    data: DataType | None
    time: datetime | None
    dataschema: str | None
    datacontenttype: str | None
    subject: str | None
    extensions: Dict[str, Any] | None
    def __init__(self, source: str, type: str, *, specversion: str | None = None, id: str | None = None, time: datetime | None = ..., datacontenttype: str | None = None, dataschema: str | None = None, subject: str | None = None, data: DataType | None = None, extensions: Dict[str, Any] | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def from_dict(cls, event: Dict[str, Any]) -> CloudEvent[DataType]:
        """Returns the deserialized CloudEvent object when a dict is provided.

        :param event: The dict representation of the event which needs to be deserialized.
        :type event: dict
        :rtype: CloudEvent
        :return: The deserialized CloudEvent object.
        """
    @classmethod
    def from_json(cls, event: Any) -> CloudEvent[DataType]:
        """
        Returns the deserialized CloudEvent object when a json payload is provided.
        :param event: The json string that should be converted into a CloudEvent. This can also be
         a storage QueueMessage, eventhub's EventData or ServiceBusMessage
        :type event: object
        :rtype: CloudEvent
        :return: The deserialized CloudEvent object.
        :raises ValueError: If the provided JSON is invalid.
        """
