from _typeshed import Incomplete

class LibSecretAgent:
    """A loader/saver built on top of low-level libsecret"""
    def __init__(self, schema_name, attributes, label: str = '', attribute_types: Incomplete | None = None, collection: Incomplete | None = None) -> None:
        """This agent is built on top of lower level libsecret API.

        Content stored via libsecret is associated with a bunch of attributes.

        :param string schema_name:
            Attributes would conceptually follow an existing schema.
            But this class will do it in the other way around,
            by automatically deriving a schema based on your attributes.
            However, you will still need to provide a schema_name.
            load() and save() will only operate on data with matching schema_name.

        :param dict attributes:
            Attributes are key-value pairs, represented as a Python dict here.
            They will be used to filter content during load() and save().
            Their arbitrary keys are strings.
            Their arbitrary values can MEAN strings, integers and booleans,
            but are always represented as strings, according to upstream sample:
            https://developer.gnome.org/libsecret/0.18/py-store-example.html

        :param string label:
            It will not be used during data lookup and filtering.
            It is only helpful when/if you visualize secrets by other viewers.

        :param dict attribute_types:
            Each key is the name of your each attribute.
            The corresponding value will be one of the following three:

            * Secret.SchemaAttributeType.STRING
            * Secret.SchemaAttributeType.INTEGER
            * Secret.SchemaAttributeType.BOOLEAN

            But if all your attributes are Secret.SchemaAttributeType.STRING,
            you do not need to provide this types definition at all.

        :param collection:
            The default value `None` means default collection.
        """
    def save(self, data):
        """Store data. Returns a boolean of whether operation was successful."""
    def load(self):
        """Load a password in the secret service, return None when found nothing"""
    def clear(self):
        """Returns a boolean of whether any passwords were removed"""

def trial_run() -> None:
    """This trial run will raise an exception if libsecret is not functioning.

    Even after you installed all the dependencies so that your script can start,
    or even if your previous run was successful, your script could fail next time,
    for example when it will be running inside a headless SSH session.

    You do not have to do trial_run. The exception would also be raised by save().
    """
