from _typeshed import Incomplete
from pyspark.errors.error_classes import ERROR_CLASSES_MAP as ERROR_CLASSES_MAP
from typing import Dict

class ErrorClassesReader:
    """
    A reader to load error information from error_classes.py.
    """
    error_info_map: Incomplete
    def __init__(self) -> None: ...
    def get_error_message(self, error_class: str, message_parameters: Dict[str, str]) -> str:
        """
        Returns the completed error message by applying message parameters to the message template.
        """
    def get_message_template(self, error_class: str) -> str:
        '''
        Returns the message template for corresponding error class from error_classes.py.

        For example,
        when given `error_class` is "EXAMPLE_ERROR_CLASS",
        and corresponding error class in error_classes.py looks like the below:

        .. code-block:: python

            "EXAMPLE_ERROR_CLASS" : {
              "message" : [
                "Problem <A> because of <B>."
              ]
            }

        In this case, this function returns:
        "Problem <A> because of <B>."

        For sub error class, when given `error_class` is "EXAMPLE_ERROR_CLASS.SUB_ERROR_CLASS",
        and corresponding error class in error_classes.py looks like the below:

        .. code-block:: python

            "EXAMPLE_ERROR_CLASS" : {
              "message" : [
                "Problem <A> because of <B>."
              ],
              "subClass" : {
                "SUB_ERROR_CLASS" : {
                  "message" : [
                    "Do <C> to fix the problem."
                  ]
                }
              }
            }

        In this case, this function returns:
        "Problem <A> because <B>. Do <C> to fix the problem."
        '''
