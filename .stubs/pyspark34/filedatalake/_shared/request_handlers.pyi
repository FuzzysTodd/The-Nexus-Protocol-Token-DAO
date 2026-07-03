from typing import Dict

def serialize_iso(attr):
    """Serialize Datetime object into ISO-8601 formatted string.

    :param Datetime attr: Object to be serialized.
    :rtype: str
    :raises: ValueError if format invalid.
    """
def get_length(data): ...
def read_length(data): ...
def validate_and_format_range_headers(start_range, end_range, start_range_required: bool = True, end_range_required: bool = True, check_content_md5: bool = False, align_to_page: bool = False): ...
def add_metadata_headers(metadata: Dict[str, str] | None = None) -> Dict[str, str]: ...
def serialize_batch_body(requests, batch_id):
    """
    --<delimiter>
    <subrequest>
    --<delimiter>
    <subrequest>    (repeated as needed)
    --<delimiter>--

    Serializes the requests in this batch to a single HTTP mixed/multipart body.

    :param list[~azure.core.pipeline.transport.HttpRequest] requests:
        a list of sub-request for the batch request
    :param str batch_id:
        to be embedded in batch sub-request delimiter
    :return: The body bytes for this batch.
    """
