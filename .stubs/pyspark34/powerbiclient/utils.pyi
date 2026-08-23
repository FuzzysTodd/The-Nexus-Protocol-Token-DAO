from . import authentication as authentication
from .authentication import AuthenticationResult as AuthenticationResult, DeviceCodeLoginAuthentication as DeviceCodeLoginAuthentication
from .models import DataType as DataType
from _typeshed import Incomplete

MODULE_NAME: str
data_types_map_pandas: Incomplete
data_types_map_spark: Incomplete

def get_dataset_config(df, locale: str = 'en-US'):
    """ Utility method to get the dataset create configuration dict from a pandas. To be used as input for instantiating a quick visualization object.

    Args:
        df (object): Required.
            Pandas DataFrame instance
        locale (string): Optional.
            This value is used to evaluate the data and parse values of the given DataFrame. 
            Supported locales can be found here: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c?redirectedfrom=MSDN

    Returns:
        dict: dataset_create_config
    """
def pyspark_get_data_and_schema(df): ...
def pandas_get_data_and_schema(df): ...
def is_dataset_create_config_valid(dataset_create_config):
    """ Validate dataset_create_config

    Args:
        dataset_create_config (dict): Required.
            A dict representing the data used to create the report, formatted as IDatasetCreateConfiguration
            (See: https://learn.microsoft.com/en-us/javascript/api/overview/powerbi/embed-quick-report#step-11---create-a-dataset-without-a-data-source)

    Returns:
        bool: True if dataset_create_config is valid, False otherwise
    """
def is_dataset_create_config_items_valid(lst, expected_item_fields): ...
def get_access_token_details(powerbi_widget, auth: Incomplete | None = None):
    """ Get an access token
    Args:
        powerbi_widget (Report | QuickVisulize): Required.
            One of Power BI widget classes, can be Report or QuickVisualize
        auth (string or object): Optional.
            We have 3 authentication options to embed a Power BI report:
                - Access token (string)
                - Authentication object (object) - instance of AuthenticationResult (DeviceCodeLoginAuthentication or InteractiveLoginAuthentication)
                - If not provided, Power BI user will be authenticated using Device Flow authentication

    Returns:
        string: access_token
    """
