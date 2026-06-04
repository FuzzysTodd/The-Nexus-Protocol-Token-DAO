import abc
from _typeshed import Incomplete
from abc import abstractmethod

class Context(metaclass=abc.ABCMeta):
    """Interface defining information available at process time"""
    @abstractmethod
    def get_message_id(self):
        """Return the messageid of the current message that we are processing"""
    @abstractmethod
    def get_message_key(self):
        """Return the key of the current message that we are processing"""
    @abstractmethod
    def get_message_eventtime(self):
        """Return the event time of the current message that we are processing"""
    @abstractmethod
    def get_message_properties(self):
        """Return the message properties kv map of the current message that we are processing"""
    @abstractmethod
    def get_current_message_topic_name(self):
        """Returns the topic name of the message that we are processing"""
    @abstractmethod
    def get_function_tenant(self):
        """Returns the tenant of the message that's being processed"""
    @abstractmethod
    def get_function_namespace(self):
        """Returns the namespace of the message that's being processed"""
    @abstractmethod
    def get_function_name(self):
        """Returns the function name that we are a part of"""
    @abstractmethod
    def get_function_id(self):
        """Returns the function id that we are a part of"""
    @abstractmethod
    def get_instance_id(self):
        """Returns the instance id that is executing the function"""
    @abstractmethod
    def get_function_version(self):
        """Returns the version of function that we are executing"""
    @abstractmethod
    def get_logger(self):
        """Returns the logger object that can be used to do logging"""
    @abstractmethod
    def get_user_config_value(self, key):
        """Returns the value of the user-defined config. If the key doesn't exist, None is returned"""
    @abstractmethod
    def get_user_config_map(self):
        """Returns the entire user-defined config as a dict
        (the dict will be empty if no user-defined config is supplied)"""
    @abstractmethod
    def get_secret(self, secret_name):
        """Returns the secret value associated with the name. None if nothing was found"""
    @abstractmethod
    def get_partition_key(self):
        """Returns partition key of the input message is one exists"""
    @abstractmethod
    def record_metric(self, metric_name, metric_value):
        """Records the metric_value. metric_value has to satisfy isinstance(metric_value, numbers.Number)"""
    @abstractmethod
    def publish(self, topic_name, message, serde_class_name: str = 'serde.IdentitySerDe', properties: Incomplete | None = None, compression_type: Incomplete | None = None, callback: Incomplete | None = None, message_conf: Incomplete | None = None):
        """Publishes message to topic_name by first serializing the message using serde_class_name serde
        The message will have properties specified if any

        The available options for message_conf:

          properties,
          partition_key,
          sequence_id,
          replication_clusters,
          disable_replication,
          event_timestamp

        """
    @abstractmethod
    def get_input_topics(self):
        """Returns the input topics of function"""
    @abstractmethod
    def get_output_topic(self):
        """Returns the output topic of function"""
    @abstractmethod
    def get_output_serde_class_name(self):
        """return output Serde class"""
    @abstractmethod
    def ack(self, msgid, topic):
        """ack this message id"""
    @abstractmethod
    def incr_counter(self, key, amount):
        """incr the counter of a given key in the managed state"""
    @abstractmethod
    def get_counter(self, key):
        """get the counter of a given key in the managed state"""
    @abstractmethod
    def del_counter(self, key):
        """delete the counter of a given key in the managed state"""
    @abstractmethod
    def put_state(self, key, value):
        """update the value of a given key in the managed state"""
    @abstractmethod
    def get_state(self, key):
        """get the value of a given key in the managed state"""
