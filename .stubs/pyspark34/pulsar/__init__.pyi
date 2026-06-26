from pulsar.exceptions import *
from _pulsar import BatchReceivePolicy as BatchReceivePolicy, BatchingType as BatchingType, CompressionType as CompressionType, ConsumerType as ConsumerType, DeadLetterPolicyBuilder as DeadLetterPolicyBuilder, InitialPosition as InitialPosition, KeySharedMode as KeySharedMode, KeySharedPolicy as KeySharedPolicy, LoggerLevel as LoggerLevel, PartitionsRoutingMode as PartitionsRoutingMode, ProducerAccessMode as ProducerAccessMode, RegexSubscriptionMode as RegexSubscriptionMode, Result as Result
from _typeshed import Incomplete
from pulsar import schema as schema
from pulsar.__about__ import __version__ as __version__
from pulsar.functions.context import Context as Context
from pulsar.functions.function import Function as Function
from pulsar.functions.serde import IdentitySerDe as IdentitySerDe, PickleSerDe as PickleSerDe, SerDe as SerDe
from typing import List, Tuple

class MessageId:
    """
    Represents a message id.

    Attributes
    ----------

    earliest:
        Represents the earliest message stored in a topic
    latest:
        Represents the latest message published on a topic
    """
    def __init__(self, partition: int = -1, ledger_id: int = -1, entry_id: int = -1, batch_index: int = -1) -> None: ...
    earliest: Incomplete
    latest: Incomplete
    def ledger_id(self): ...
    def entry_id(self): ...
    def batch_index(self): ...
    def partition(self): ...
    def serialize(self):
        """
        Returns a bytes representation of the message id.
        This byte sequence can be stored and later deserialized.
        """
    @staticmethod
    def deserialize(message_id_bytes):
        """
        Deserialize a message id object from a previously
        serialized bytes sequence.
        """

class Message:
    """
    Message objects are returned by a consumer, either by calling `receive` or
    through a listener.
    """
    def data(self):
        """
        Returns object typed bytes with the payload of the message.
        """
    def value(self):
        """
        Returns object with the de-serialized version of the message content
        """
    def properties(self):
        """
        Return the properties attached to the message. Properties are
        application-defined key/value pairs that will be attached to the
        message.
        """
    def partition_key(self):
        """
        Get the partitioning key for the message.
        """
    def publish_timestamp(self):
        """
        Get the timestamp in milliseconds with the message publish time.
        """
    def event_timestamp(self):
        """
        Get the timestamp in milliseconds with the message event time.
        """
    def message_id(self):
        """
        The message ID that can be used to refer to this particular message.
        """
    def topic_name(self):
        """
        Get the topic Name from which this message originated from
        """
    def redelivery_count(self):
        """
        Get the redelivery count for this message
        """
    def schema_version(self):
        """
        Get the schema version for this message
        """

class MessageBatch:
    def __init__(self) -> None: ...
    def with_message_id(self, msg_id): ...
    def parse_from(self, data, size): ...

class Authentication:
    """
    Authentication provider object. Used to load authentication from an external
    shared library.
    """
    auth: Incomplete
    def __init__(self, dynamicLibPath, authParamsString) -> None:
        """
        Create the authentication provider instance.

        Parameters
        ----------

        dynamicLibPath: str
            Path to the authentication provider shared library (such as ``tls.so``)
        authParamsString: str
            Comma-separated list of provider-specific configuration params
        """

class AuthenticationTLS(Authentication):
    """
    TLS Authentication implementation
    """
    auth: Incomplete
    def __init__(self, certificate_path, private_key_path) -> None:
        """
        Create the TLS authentication provider instance.

        Parameters
        ----------

        certificate_path: str
            Path to the public certificate
        private_key_path: str
            Path to private TLS key
        """

class AuthenticationToken(Authentication):
    """
    Token based authentication implementation
    """
    auth: Incomplete
    def __init__(self, token) -> None:
        """
        Create the token authentication provider instance.

        Parameters
        ----------

        token
            A string containing the token or a functions that provides a string with the token
        """

class AuthenticationAthenz(Authentication):
    """
    Athenz Authentication implementation
    """
    auth: Incomplete
    def __init__(self, auth_params_string) -> None:
        """
        Create the Athenz authentication provider instance.

        Parameters
        ----------

        auth_params_string: str
            JSON encoded configuration for Athenz client
        """

class AuthenticationOauth2(Authentication):
    """
    Oauth2 Authentication implementation
    """
    auth: Incomplete
    def __init__(self, auth_params_string: str) -> None:
        '''
        Create the Oauth2 authentication provider instance.

        You can create the instance by setting the necessary fields in the JSON string.

        .. code-block:: python

            auth = AuthenticationOauth2(\'{"issuer_url": "xxx", "private_key": "yyy"}\')

        The valid JSON fields are:

        * issuer_url (required)
            The URL of the authentication provider which allows the Pulsar client to obtain an
            access token.
        * private_key (required)
            The URL to the JSON credentials file. It supports the following pattern formats:

            * ``/path/to/file``
            * ``file:///path/to/file``
            * ``file:/path/to/file``
            * ``data:application/json;base64,<base64-encoded-value>``

            The file content or the based64 encoded value is the encoded JSON string that contains
            the following fields:

            * ``client_id``
            * ``client_secret``
        * audience
            The OAuth 2.0 "resource server" identifier for a Pulsar cluster.
        * scope
            The scope of an access request.

        Parameters
        ----------
        auth_params_string : str
            JSON encoded configuration for Oauth2 client

        '''

class AuthenticationBasic(Authentication):
    """
    Basic Authentication implementation
    """
    auth: Incomplete
    def __init__(self, username: Incomplete | None = None, password: Incomplete | None = None, method: str = 'basic', auth_params_string: Incomplete | None = None) -> None:
        '''
        Create the Basic authentication provider instance.

        For example, if you want to create a basic authentication instance whose
        username is "my-user" and password is "my-pass", there are two ways:

        .. code-block:: python

            auth = AuthenticationBasic(\'my-user\', \'my-pass\')
            auth = AuthenticationBasic(auth_params_string=\'{"username": "my-user", "password": "my-pass"}\')


        Parameters
        ----------
        username : str, optional
        password : str, optional
        method : str, default=\'basic\'
            The authentication method name
        auth_params_string : str, optional
            The JSON presentation of all fields above. If it\'s not None, the other parameters will be ignored.
            Here is an example JSON presentation:

                {"username": "my-user", "password": "my-pass", "method": "oms3.0"}

            The ``username`` and ``password`` fields are required. If the "method" field is not set, it will be
            "basic" by default.
        '''

class ConsumerDeadLetterPolicy:
    '''
    Configuration for the "dead letter queue" feature in consumer.
    '''
    def __init__(self, max_redeliver_count: int, dead_letter_topic: str = None, initial_subscription_name: str = None) -> None:
        '''
        Wrapper DeadLetterPolicy.

        Parameters
        ----------
        max_redeliver_count: Maximum number of times that a message is redelivered before being sent to the dead letter queue.
            - The maxRedeliverCount must be greater than 0.
        dead_letter_topic: Name of the dead topic where the failing messages are sent.
            The default value is: sourceTopicName + "-" + subscriptionName + "-DLQ"
        initial_subscription_name: Name of the initial subscription name of the dead letter topic.
            If this field is not set, the initial subscription for the dead letter topic is not created.
            If this field is set but the broker\'s `allowAutoSubscriptionCreation` is disabled, the DLQ producer
            fails to be created.
        '''
    @property
    def dead_letter_topic(self) -> str:
        """
        Return the dead letter topic for dead letter policy.
        """
    @property
    def max_redeliver_count(self) -> int:
        """
        Return the max redeliver count for dead letter policy.
        """
    @property
    def initial_subscription_name(self) -> str:
        """
        Return the initial subscription name for dead letter policy.
        """
    def policy(self):
        """
        Returns the actual one DeadLetterPolicy.
        """

class Client:
    """
    The Pulsar client. A single client instance can be used to create producers
    and consumers on multiple topics.

    The client will share the same connection pool and threads across all
    producers and consumers.
    """
    def __init__(self, service_url, authentication: Incomplete | None = None, operation_timeout_seconds: int = 30, io_threads: int = 1, message_listener_threads: int = 1, concurrent_lookup_requests: int = 50000, log_conf_file_path: Incomplete | None = None, use_tls: bool = False, tls_trust_certs_file_path: Incomplete | None = None, tls_allow_insecure_connection: bool = False, tls_validate_hostname: bool = False, logger: Incomplete | None = None, connection_timeout_ms: int = 10000, listener_name: Incomplete | None = None) -> None:
        """
        Create a new Pulsar client instance.

        Parameters
        ----------

        service_url: str
            The Pulsar service url eg: pulsar://my-broker.com:6650/
        authentication: Authentication, optional
            Set the authentication provider to be used with the broker. Supported methods:

            * `AuthenticationTLS`
            * `AuthenticationToken`
            * `AuthenticationAthenz`
            * `AuthenticationOauth2`
        operation_timeout_seconds: int, default=30
            Set timeout on client operations (subscribe, create producer, close, unsubscribe).
        io_threads: int, default=1
            Set the number of IO threads to be used by the Pulsar client.
        message_listener_threads: int, default=1
            Set the number of threads to be used by the Pulsar client when delivering messages through
            message listener. The default is 1 thread per Pulsar client. If using more than 1 thread,
            messages for distinct ``message_listener``s will be delivered in different threads, however a
            single ``MessageListener`` will always be assigned to the same thread.
        concurrent_lookup_requests: int, default=50000
            Number of concurrent lookup-requests allowed on each broker connection to prevent overload
            on the broker.
        log_conf_file_path: str, optional
            This parameter is deprecated and makes no effect. It's retained only for compatibility.
            Use `logger` to customize a logger.
        use_tls: bool, default=False
            Configure whether to use TLS encryption on the connection. This setting is deprecated.
            TLS will be automatically enabled if the ``serviceUrl`` is set to ``pulsar+ssl://`` or ``https://``
        tls_trust_certs_file_path: str, optional
            Set the path to the trusted TLS certificate file. If empty defaults to certifi.
        tls_allow_insecure_connection: bool, default=False
            Configure whether the Pulsar client accepts untrusted TLS certificates from the broker.
        tls_validate_hostname: bool, default=False
            Configure whether the Pulsar client validates that the hostname of the endpoint,
            matches the common name on the TLS certificate presented by the endpoint.
        logger: optional
            Set a Python logger for this Pulsar client. Should be an instance of `logging.Logger`.
        connection_timeout_ms: int, default=10000
            Set timeout in milliseconds on TCP connections.
        listener_name: str, optional
            Listener name for lookup. Clients can use listenerName to choose one of the listeners as
            the service URL to create a connection to the broker as long as the network is accessible.
            ``advertisedListeners`` must be enabled in broker side.
        """
    def create_producer(self, topic, producer_name: Incomplete | None = None, schema=..., initial_sequence_id: Incomplete | None = None, send_timeout_millis: int = 30000, compression_type=..., max_pending_messages: int = 1000, max_pending_messages_across_partitions: int = 50000, block_if_queue_full: bool = False, batching_enabled: bool = False, batching_max_messages: int = 1000, batching_max_allowed_size_in_bytes=..., batching_max_publish_delay_ms: int = 10, chunking_enabled: bool = False, message_routing_mode=..., lazy_start_partitioned_producers: bool = False, properties: Incomplete | None = None, batching_type=..., encryption_key: Incomplete | None = None, crypto_key_reader: Incomplete | None = None, access_mode=...):
        """
        Create a new producer on a given topic.

        Parameters
        ----------

        topic: str
            The topic name
        producer_name: str, optional
            Specify a name for the producer. If not assigned, the system will generate a globally unique name
            which can be accessed with `Producer.producer_name()`. When specifying a name, it is app to the user
            to ensure that, for a given topic, the producer name is unique across all Pulsar's clusters.
        schema: pulsar.schema.Schema, default=pulsar.schema.BytesSchema
            Define the schema of the data that will be published by this producer, e.g,
            ``schema=JsonSchema(MyRecordClass)``.

            The schema will be used for two purposes:
                * Validate the data format against the topic defined schema
                * Perform serialization/deserialization between data and objects
        initial_sequence_id: int, optional
            Set the baseline for the sequence ids for messages published by the producer. First message will be
            using ``(initialSequenceId + 1)`` as its sequence id and subsequent messages will be assigned
            incremental sequence ids, if not otherwise specified.
        send_timeout_millis: int, default=30000
            If a message is not acknowledged by the server before the ``send_timeout`` expires, an error will be reported.
        compression_type: CompressionType, default=CompressionType.NONE
            Set the compression type for the producer. By default, message payloads are not compressed.

            Supported compression types:

            * CompressionType.LZ4
            * CompressionType.ZLib
            * CompressionType.ZSTD
            * CompressionType.SNAPPY

            ZSTD is supported since Pulsar 2.3. Consumers will need to be at least at that release in order to
            be able to receive messages compressed with ZSTD.

            SNAPPY is supported since Pulsar 2.4. Consumers will need to be at least at that release in order to
            be able to receive messages compressed with SNAPPY.
        max_pending_messages: int, default=1000
            Set the max size of the queue holding the messages pending to receive an acknowledgment from the broker.
        max_pending_messages_across_partitions: int, default=50000
            Set the max size of the queue holding the messages pending to receive an acknowledgment across partitions
            from the broker.
        block_if_queue_full: bool, default=False
            Set whether `send_async` operations should block when the outgoing message queue is full.
        message_routing_mode: PartitionsRoutingMode, default=PartitionsRoutingMode.RoundRobinDistribution
            Set the message routing mode for the partitioned producer.

            Supported modes:

            * ``PartitionsRoutingMode.RoundRobinDistribution``
            * ``PartitionsRoutingMode.UseSinglePartition``
        lazy_start_partitioned_producers: bool, default=False
            This config affects producers of partitioned topics only. It controls whether producers register
            and connect immediately to the owner broker of each partition or start lazily on demand. The internal
            producer of one partition is always started eagerly, chosen by the routing policy, but the internal
            producers of any additional partitions are started on demand, upon receiving their first message.

            Using this mode can reduce the strain on brokers for topics with large numbers of partitions and when
            the SinglePartition routing policy is used without keyed messages. Because producer connection can be
            on demand, this can produce extra send latency for the first messages of a given partition.
        properties: dict, optional
            Sets the properties for the producer. The properties associated with a producer can be used for identify
            a producer at broker side.
        batching_type: BatchingType, default=BatchingType.Default
            Sets the batching type for the producer.

            There are two batching type: DefaultBatching and KeyBasedBatching.

            DefaultBatching will batch single messages:
                (k1, v1), (k2, v1), (k3, v1), (k1, v2), (k2, v2), (k3, v2), (k1, v3), (k2, v3), (k3, v3)
            ... into single batch message:
                [(k1, v1), (k2, v1), (k3, v1), (k1, v2), (k2, v2), (k3, v2), (k1, v3), (k2, v3), (k3, v3)]

            KeyBasedBatching will batch incoming single messages:
                (k1, v1), (k2, v1), (k3, v1), (k1, v2), (k2, v2), (k3, v2), (k1, v3), (k2, v3), (k3, v3)
            ... into single batch message:
                [(k1, v1), (k1, v2), (k1, v3)], [(k2, v1), (k2, v2), (k2, v3)], [(k3, v1), (k3, v2), (k3, v3)]
        chunking_enabled: bool, default=False
            If message size is higher than allowed max publish-payload size by broker then chunking_enabled helps
            producer to split message into multiple chunks and publish them to broker separately and in order.
            So, it allows client to successfully publish large size of messages in pulsar.
        encryption_key: str, optional
            The key used for symmetric encryption, configured on the producer side
        crypto_key_reader: CryptoKeyReader, optional
            Symmetric encryption class implementation, configuring public key encryption messages for the producer
            and private key decryption messages for the consumer
        access_mode: ProducerAccessMode, optional
            Set the type of access mode that the producer requires on the topic.

            Supported modes:

            * Shared: By default multiple producers can publish on a topic.
            * Exclusive: Require exclusive access for producer.
                         Fail immediately if there's already a producer connected.
            * WaitForExclusive: Producer creation is pending until it can acquire exclusive access.
            * ExclusiveWithFencing: Acquire exclusive access for the producer.
                                    Any existing producer will be removed and invalidated immediately.
        """
    def subscribe(self, topic, subscription_name, consumer_type=..., schema=..., message_listener: Incomplete | None = None, receiver_queue_size: int = 1000, max_total_receiver_queue_size_across_partitions: int = 50000, consumer_name: Incomplete | None = None, unacked_messages_timeout_ms: Incomplete | None = None, broker_consumer_stats_cache_time_ms: int = 30000, negative_ack_redelivery_delay_ms: int = 60000, is_read_compacted: bool = False, properties: Incomplete | None = None, pattern_auto_discovery_period: int = 60, initial_position=..., crypto_key_reader: Incomplete | None = None, replicate_subscription_state_enabled: bool = False, max_pending_chunked_message: int = 10, auto_ack_oldest_chunked_message_on_queue_full: bool = False, start_message_id_inclusive: bool = False, batch_receive_policy: Incomplete | None = None, key_shared_policy: Incomplete | None = None, batch_index_ack_enabled: bool = False, regex_subscription_mode=..., dead_letter_policy: ConsumerDeadLetterPolicy = None):
        """
        Subscribe to the given topic and subscription combination.

        Parameters
        ----------

        topic:
            The name of the topic, list of topics or regex pattern. This method will accept these forms:
            * ``topic='my-topic'``
            * ``topic=['topic-1', 'topic-2', 'topic-3']``
            * ``topic=re.compile('persistent://public/default/topic-*')``
        subscription_name: str
            The name of the subscription.
        consumer_type: ConsumerType, default=ConsumerType.Exclusive
            Select the subscription type to be used when subscribing to the topic.
        schema: pulsar.schema.Schema, default=pulsar.schema.BytesSchema
            Define the schema of the data that will be received by this consumer.
        message_listener: optional
            Sets a message listener for the consumer. When the listener is set, the application will
            receive messages through it. Calls to ``consumer.receive()`` will not be allowed.
            The listener function needs to accept (consumer, message), for example:

            .. code-block:: python

                def my_listener(consumer, message):
                    # process message
                    consumer.acknowledge(message)
        receiver_queue_size: int, default=1000
            Sets the size of the consumer receive queue. The consumer receive queue controls how many messages can be
            accumulated by the consumer before the application calls `receive()`. Using a higher value could potentially
            increase the consumer throughput at the expense of higher memory utilization. Setting the consumer queue
            size to zero decreases the throughput of the consumer by disabling pre-fetching of messages.

            This approach improves the message distribution on shared subscription by pushing messages only to those
            consumers that are ready to process them. Neither receive with timeout nor partitioned topics can be used
            if the consumer queue size is zero. The `receive()` function call should not be interrupted when the
            consumer queue size is zero. The default value is 1000 messages and should work well for most use cases.
        max_total_receiver_queue_size_across_partitions: int, default=50000
            Set the max total receiver queue size across partitions. This setting will be used to reduce the
            receiver queue size for individual partitions
        consumer_name: str, optional
            Sets the consumer name.
        unacked_messages_timeout_ms: int, optional
            Sets the timeout in milliseconds for unacknowledged messages. The timeout needs to be greater than
            10 seconds. An exception is thrown if the given value is less than 10 seconds. If a successful
            acknowledgement is not sent within the timeout, all the unacknowledged messages are redelivered.
        negative_ack_redelivery_delay_ms: int, default=60000
            The delay after which to redeliver the messages that failed to be processed
            (with the ``consumer.negative_acknowledge()``)
        broker_consumer_stats_cache_time_ms: int, default=30000
            Sets the time duration for which the broker-side consumer stats will be cached in the client.
        is_read_compacted: bool, default=False
            Selects whether to read the compacted version of the topic
        properties: dict, optional
            Sets the properties for the consumer. The properties associated with a consumer can be used for
            identify a consumer at broker side.
        pattern_auto_discovery_period: int, default=60
            Periods of seconds for consumer to auto discover match topics.
        initial_position: InitialPosition, default=InitialPosition.Latest
          Set the initial position of a consumer when subscribing to the topic.
          It could be either: ``InitialPosition.Earliest`` or ``InitialPosition.Latest``.
        crypto_key_reader: CryptoKeyReader, optional
            Symmetric encryption class implementation, configuring public key encryption messages for the producer
            and private key decryption messages for the consumer
        replicate_subscription_state_enabled: bool, default=False
            Set whether the subscription status should be replicated.
        max_pending_chunked_message: int, default=10
          Consumer buffers chunk messages into memory until it receives all the chunks of the original message.
          While consuming chunk-messages, chunks from same message might not be contiguous in the stream, and they
          might be mixed with other messages' chunks. so, consumer has to maintain multiple buffers to manage
          chunks coming from different messages. This mainly happens when multiple publishers are publishing
          messages on the topic concurrently or publisher failed to publish all chunks of the messages.

          If it's zero, the pending chunked messages will not be limited.
        auto_ack_oldest_chunked_message_on_queue_full: bool, default=False
          Buffering large number of outstanding uncompleted chunked messages can create memory pressure, and it
          can be guarded by providing the maxPendingChunkedMessage threshold. See setMaxPendingChunkedMessage.
          Once, consumer reaches this threshold, it drops the outstanding unchunked-messages by silently acking
          if autoAckOldestChunkedMessageOnQueueFull is true else it marks them for redelivery.
        start_message_id_inclusive: bool, default=False
          Set the consumer to include the given position of any reset operation like Consumer::seek.
        batch_receive_policy: class ConsumerBatchReceivePolicy
          Set the batch collection policy for batch receiving.
        key_shared_policy: class ConsumerKeySharedPolicy
            Set the key shared policy for use when the ConsumerType is KeyShared.
        batch_index_ack_enabled: Enable the batch index acknowledgement.
            It should be noted that this option can only work when the broker side also enables the batch index
            acknowledgement. See the `acknowledgmentAtBatchIndexLevelEnabled` config in `broker.conf`.
        regex_subscription_mode: RegexSubscriptionMode, optional
            Set the regex subscription mode for use when the topic is a regex pattern.

            Supported modes:

            * PersistentOnly: By default only subscribe to persistent topics.
            * NonPersistentOnly: Only subscribe to non-persistent topics.
            * AllTopics: Subscribe to both persistent and non-persistent topics.
        dead_letter_policy: class ConsumerDeadLetterPolicy
          Set dead letter policy for consumer.
          By default, some messages are redelivered many times, even to the extent that they can never be
          stopped. By using the dead letter mechanism, messages have the max redelivery count, when they're
          exceeding the maximum number of redeliveries. Messages are sent to dead letter topics and acknowledged
          automatically.
        """
    def create_reader(self, topic, start_message_id, schema=..., reader_listener: Incomplete | None = None, receiver_queue_size: int = 1000, reader_name: Incomplete | None = None, subscription_role_prefix: Incomplete | None = None, is_read_compacted: bool = False, crypto_key_reader: Incomplete | None = None):
        """
        Create a reader on a particular topic

        Parameters
        ----------

        topic:
            The name of the topic.
        start_message_id:
            The initial reader positioning is done by specifying a message id. The options are:

            * ``MessageId.earliest``:

            Start reading from the earliest message available in the topic

            * ``MessageId.latest``:

            Start reading from the end topic, only getting messages published after the reader was created

            * ``MessageId``:

            When passing a particular message id, the reader will position itself on that specific position.
            The first message to be read will be the message next to the specified messageId.
            Message id can be serialized into a string and deserialized back into a `MessageId` object:

               .. code-block:: python

                   # Serialize to string
                   s = msg.message_id().serialize()

                   # Deserialize from string
                   msg_id = MessageId.deserialize(s)
        schema: pulsar.schema.Schema, default=pulsar.schema.BytesSchema
            Define the schema of the data that will be received by this reader.
        reader_listener: optional
            Sets a message listener for the reader. When the listener is set, the application will receive messages
            through it. Calls to ``reader.read_next()`` will not be allowed. The listener function needs to accept
            (reader, message), for example:

            .. code-block:: python

                def my_listener(reader, message):
                    # process message
                    pass
        receiver_queue_size: int, default=1000
            Sets the size of the reader receive queue. The reader receive queue controls how many messages can be
            accumulated by the reader before the application calls `read_next()`. Using a higher value could
            potentially increase the reader throughput at the expense of higher memory utilization.
        reader_name: str, optional
            Sets the reader name.
        subscription_role_prefix: str, optional
            Sets the subscription role prefix.
        is_read_compacted: bool, default=False
            Selects whether to read the compacted version of the topic
        crypto_key_reader: CryptoKeyReader, optional
            Symmetric encryption class implementation, configuring public key encryption messages for the producer
            and private key decryption messages for the consumer
        """
    def get_topic_partitions(self, topic):
        """
        Get the list of partitions for a given topic.

        If the topic is partitioned, this will return a list of partition names. If the topic is not
        partitioned, the returned list will contain the topic name itself.

        This can be used to discover the partitions and create Reader, Consumer or Producer
        instances directly on a particular partition.

        Parameters
        ----------

        topic: str
            the topic name to lookup

        Returns
        -------
        list
            a list of partition name
        """
    def shutdown(self) -> None:
        """
        Perform immediate shutdown of Pulsar client.

        Release all resources and close all producer, consumer, and readers without waiting
        for ongoing operations to complete.
        """
    def close(self) -> None:
        """
        Close the client and all the associated producers and consumers
        """

class Producer:
    """
    The Pulsar message producer, used to publish messages on a topic.

    Examples
    --------

    .. code-block:: python

        import pulsar

        client = pulsar.Client('pulsar://localhost:6650')
        producer = client.create_producer('my-topic')
        for i in range(10):
            producer.send(('Hello-%d' % i).encode('utf-8'))
        client.close()
    """
    def topic(self):
        """
        Return the topic which producer is publishing to
        """
    def producer_name(self):
        """
        Return the producer name which could have been assigned by the
        system or specified by the client
        """
    def last_sequence_id(self):
        """
        Get the last sequence id that was published by this producer.

        This represents either the automatically assigned or custom sequence id
        (set on the ``MessageBuilder``) that was published and acknowledged by the broker.

        After recreating a producer with the same producer name, this will return the
        last message that was published in the previous producer session, or -1 if
        there was no message ever published.
        """
    def send(self, content, properties: Incomplete | None = None, partition_key: Incomplete | None = None, sequence_id: Incomplete | None = None, replication_clusters: Incomplete | None = None, disable_replication: bool = False, event_timestamp: Incomplete | None = None, deliver_at: Incomplete | None = None, deliver_after: Incomplete | None = None):
        """
        Publish a message on the topic. Blocks until the message is acknowledged

        Returns a `MessageId` object that represents where the message is persisted.

        Parameters
        ----------

        content:
            A ``bytes`` object with the message payload.
        properties: optional
            A dict of application-defined string properties.
        partition_key: optional
            Sets the partition key for message routing. A hash of this key is used
            to determine the message's topic partition.
        sequence_id:  optional
            Specify a custom sequence id for the message being published.
        replication_clusters:  optional
          Override namespace replication clusters. Note that it is the caller's responsibility to provide valid
          cluster names and that all clusters have been previously configured as topics. Given an empty list,
          the message will replicate according to the namespace configuration.
        disable_replication: bool, default=False
            Do not replicate this message.
        event_timestamp: optional
            Timestamp in millis of the timestamp of event creation
        deliver_at: optional
            Specify the message should not be delivered earlier than the specified timestamp.
            The timestamp is milliseconds and based on UTC
        deliver_after: optional
            Specify a delay in timedelta for the delivery of the messages.
        """
    def send_async(self, content, callback, properties: Incomplete | None = None, partition_key: Incomplete | None = None, sequence_id: Incomplete | None = None, replication_clusters: Incomplete | None = None, disable_replication: bool = False, event_timestamp: Incomplete | None = None, deliver_at: Incomplete | None = None, deliver_after: Incomplete | None = None) -> None:
        """
        Send a message asynchronously.

        Examples
        --------

        The ``callback`` will be invoked once the message has been acknowledged by the broker.

        .. code-block:: python

            import pulsar

            client = pulsar.Client('pulsar://localhost:6650')
            producer = client.create_producer(
                            'my-topic',
                            block_if_queue_full=True,
                            batching_enabled=True,
                            batching_max_publish_delay_ms=10)

            def callback(res, msg_id):
                print('Message published res=%s', res)

            while True:
                producer.send_async(('Hello-%d' % i).encode('utf-8'), callback)

            client.close()


        When the producer queue is full, by default the message will be rejected
        and the callback invoked with an error code.


        Parameters
        ----------

        content
            A `bytes` object with the message payload.
        callback
            A callback that is invoked once the message has been acknowledged by the broker.
        properties: optional
            A dict of application0-defined string properties.
        partition_key: optional
            Sets the partition key for the message routing. A hash of this key is
            used to determine the message's topic partition.
        sequence_id: optional
            Specify a custom sequence id for the message being published.
        replication_clusters: optional
            Override namespace replication clusters. Note that it is the caller's responsibility
            to provide valid cluster names and that all clusters have been previously configured
            as topics. Given an empty list, the message will replicate per the namespace configuration.
        disable_replication: optional
            Do not replicate this message.
        event_timestamp: optional
            Timestamp in millis of the timestamp of event creation
        deliver_at: optional
            Specify the message should not be delivered earlier than the specified timestamp.
        deliver_after: optional
            Specify a delay in timedelta for the delivery of the messages.
        """
    def flush(self) -> None:
        """
        Flush all the messages buffered in the client and wait until all messages have been
        successfully persisted
        """
    def close(self) -> None:
        """
        Close the producer.
        """
    def is_connected(self):
        """
        Check if the producer is connected or not.
        """

class Consumer:
    '''
    Pulsar consumer.

    Examples
    --------

    .. code-block:: python

        import pulsar

        client = pulsar.Client(\'pulsar://localhost:6650\')
        consumer = client.subscribe(\'my-topic\', \'my-subscription\')
        while True:
            msg = consumer.receive()
            try:
                print("Received message \'{}\' id=\'{}\'".format(msg.data(), msg.message_id()))
                consumer.acknowledge(msg)
            except Exception:
                consumer.negative_acknowledge(msg)
        client.close()
    '''
    def topic(self):
        """
        Return the topic this consumer is subscribed to.
        """
    def subscription_name(self):
        """
        Return the subscription name.
        """
    def unsubscribe(self):
        """
        Unsubscribe the current consumer from the topic.

        This method will block until the operation is completed. Once the
        consumer is unsubscribed, no more messages will be received and
        subsequent new messages will not be retained for this consumer.

        This consumer object cannot be reused.
        """
    def receive(self, timeout_millis: Incomplete | None = None):
        """
        Receive a single message.

        If a message is not immediately available, this method will block until
        a new message is available.

        Parameters
        ----------

        timeout_millis: int, optional
            If specified, the receiver will raise an exception if a message is not available within the timeout.
        """
    def batch_receive(self):
        """
        Batch receiving messages.

        This calls blocks until has enough messages or wait timeout, more details to see {@link BatchReceivePolicy}.
        """
    def acknowledge(self, message) -> None:
        """
        Acknowledge the reception of a single message.

        This method will block until an acknowledgement is sent to the broker.
        After that, the message will not be re-delivered to this consumer.

        Parameters
        ----------
        message : Message, _pulsar.Message, _pulsar.MessageId
            The received message or message id.

        Raises
        ------
        OperationNotSupported
             if ``message`` is not allowed to acknowledge
        """
    def acknowledge_cumulative(self, message) -> None:
        """
        Acknowledge the reception of all the messages in the stream up to (and
        including) the provided message.

        This method will block until an acknowledgement is sent to the broker.
        After that, the messages will not be re-delivered to this consumer.

        Parameters
        ----------

        message:
            The received message or message id.

        Raises
        ------
        CumulativeAcknowledgementNotAllowedError
            if the consumer type is ConsumerType.KeyShared or ConsumerType.Shared
        """
    def negative_acknowledge(self, message) -> None:
        '''
        Acknowledge the failure to process a single message.

        When a message is "negatively acked" it will be marked for redelivery after
        some fixed delay. The delay is configurable when constructing the consumer
        with {@link ConsumerConfiguration#setNegativeAckRedeliveryDelayMs}.

        This call is not blocking.

        Parameters
        ----------

        message:
            The received message or message id.
        '''
    def pause_message_listener(self) -> None:
        """
        Pause receiving messages via the ``message_listener`` until `resume_message_listener()` is called.
        """
    def resume_message_listener(self) -> None:
        """
        Resume receiving the messages via the message listener.
        Asynchronously receive all the messages enqueued from the time
        `pause_message_listener()` was called.
        """
    def redeliver_unacknowledged_messages(self) -> None:
        """
        Redelivers all the unacknowledged messages. In failover mode, the
        request is ignored if the consumer is not active for the given topic. In
        shared mode, the consumer's messages to be redelivered are distributed
        across all the connected consumers. This is a non-blocking call and
        doesn't throw an exception. In case the connection breaks, the messages
        are redelivered after reconnect.
        """
    def seek(self, messageid) -> None:
        """
        Reset the subscription associated with this consumer to a specific message id or publish timestamp.
        The message id can either be a specific message or represent the first or last messages in the topic.
        Note: this operation can only be done on non-partitioned topics. For these, one can rather perform the
        seek() on the individual partitions.

        Parameters
        ----------

        messageid:
            The message id for seek, OR an integer event time to seek to
        """
    def close(self) -> None:
        """
        Close the consumer.
        """
    def is_connected(self):
        """
        Check if the consumer is connected or not.
        """
    def get_last_message_id(self):
        """
        Get the last message id.
        """

class ConsumerBatchReceivePolicy:
    """
    Batch receive policy can limit the number and bytes of messages in a single batch,
    and can specify a timeout for waiting for enough messages for this batch.

    A batch receive action is completed as long as any one of the conditions (the batch has enough number
    or size of messages, or the waiting timeout is passed) are met.
    """
    def __init__(self, max_num_message, max_num_bytes, timeout_ms) -> None:
        """
        Wrapper BatchReceivePolicy.

        Parameters
        ----------

        max_num_message: Max num message, if less than 0, it means no limit. default: -1
        max_num_bytes: Max num bytes, if less than 0, it means no limit. default: 10 * 1024 * 1024
        timeout_ms: If less than 0, it means no limit. default: 100
        """
    def policy(self):
        """
        Returns the actual one BatchReceivePolicy.
        """

class ConsumerKeySharedPolicy:
    """
    Consumer key shared policy is used to configure the consumer behaviour when the ConsumerType is KeyShared.
    """
    def __init__(self, key_shared_mode: KeySharedMode = ..., allow_out_of_order_delivery: bool = False, sticky_ranges: List[Tuple[int, int]] | None = None) -> None:
        """
        Wrapper KeySharedPolicy.

        Parameters
        ----------

        key_shared_mode: KeySharedMode, optional
            Set the key shared mode. eg: KeySharedMode.Sticky or KeysharedMode.AutoSplit

        allow_out_of_order_delivery: bool, optional
            Set whether to allow for out of order delivery
            If it is enabled, it relaxes the ordering requirement and allows the broker to send out-of-order
            messages in case of failures. This makes it faster for new consumers to join without being stalled by
            an existing slow consumer.

            If this is True, a single consumer still receives all keys, but they may come in different orders.

        sticky_ranges: List[Tuple[int, int]], optional
            Set the ranges used with sticky mode. The integers can be from 0 to 2^16 (0 <= val < 65,536)
        """
    @property
    def key_shared_mode(self) -> KeySharedMode:
        """
        Returns the key shared mode
        """
    @property
    def allow_out_of_order_delivery(self) -> bool:
        """
        Returns whether out of order delivery is enabled
        """
    @property
    def sticky_ranges(self) -> List[Tuple[int, int]]:
        """
        Returns the actual sticky ranges
        """
    def policy(self):
        """
        Returns the actual KeySharedPolicy.
        """

class Reader:
    """
    Pulsar topic reader.
    """
    def topic(self):
        """
        Return the topic this reader is reading from.
        """
    def read_next(self, timeout_millis: Incomplete | None = None):
        """
        Read a single message.

        If a message is not immediately available, this method will block until
        a new message is available.

        Parameters
        ----------

        timeout_millis: int, optional
            If specified, the receiver will raise an exception if a message is not available within the timeout.
        """
    def has_message_available(self):
        """
        Check if there is any message available to read from the current position.
        """
    def seek(self, messageid) -> None:
        """
        Reset this reader to a specific message id or publish timestamp.
        The message id can either be a specific message or represent the first or last messages in the topic.
        Note: this operation can only be done on non-partitioned topics. For these, one can rather perform the
        seek() on the individual partitions.

        Parameters
        ----------

        messageid:
            The message id for seek, OR an integer event time to seek to
        """
    def close(self) -> None:
        """
        Close the reader.
        """
    def is_connected(self):
        """
        Check if the reader is connected or not.
        """

class CryptoKeyReader:
    """
    Default crypto key reader implementation
    """
    cryptoKeyReader: Incomplete
    def __init__(self, public_key_path, private_key_path) -> None:
        """
        Create crypto key reader.

        Parameters
        ----------

        public_key_path: str
            Path to the public key
        private_key_path: str
            Path to private key
        """

class ConsoleLogger:
    """
    Logger that writes on standard output

    Attributes
    ----------

    log_level:
        The logging level, eg: ``pulsar.LoggerLevel.Info``
    """
    log_level: Incomplete
    def __init__(self, log_level=...) -> None: ...

class FileLogger:
    """
    Logger that writes into a file

    Attributes
    ----------

    log_level:
        The logging level, eg: ``pulsar.LoggerLevel.Info``
    log_file:
        The file where to write the logs
    """
    log_level: Incomplete
    log_file: Incomplete
    def __init__(self, log_level, log_file) -> None: ...
