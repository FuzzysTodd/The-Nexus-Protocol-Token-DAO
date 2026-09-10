from _typeshed import Incomplete
from mlflow.server.auth.entities import ExperimentPermission as ExperimentPermission, RegisteredModelPermission as RegisteredModelPermission, User as User
from mlflow.server.auth.routes import CREATE_EXPERIMENT_PERMISSION as CREATE_EXPERIMENT_PERMISSION, CREATE_REGISTERED_MODEL_PERMISSION as CREATE_REGISTERED_MODEL_PERMISSION, CREATE_USER as CREATE_USER, DELETE_EXPERIMENT_PERMISSION as DELETE_EXPERIMENT_PERMISSION, DELETE_REGISTERED_MODEL_PERMISSION as DELETE_REGISTERED_MODEL_PERMISSION, DELETE_USER as DELETE_USER, GET_EXPERIMENT_PERMISSION as GET_EXPERIMENT_PERMISSION, GET_REGISTERED_MODEL_PERMISSION as GET_REGISTERED_MODEL_PERMISSION, GET_USER as GET_USER, UPDATE_EXPERIMENT_PERMISSION as UPDATE_EXPERIMENT_PERMISSION, UPDATE_REGISTERED_MODEL_PERMISSION as UPDATE_REGISTERED_MODEL_PERMISSION, UPDATE_USER_ADMIN as UPDATE_USER_ADMIN, UPDATE_USER_PASSWORD as UPDATE_USER_PASSWORD
from mlflow.utils.rest_utils import http_request_safe as http_request_safe

class AuthServiceClient:
    """
    Client of an MLflow Tracking Server that enabled the default basic authentication plugin.
    It is recommended to use :py:func:`mlflow.server.get_app_client()` to instantiate this class.
    See https://mlflow.org/docs/latest/auth.html for more information.
    """
    tracking_uri: Incomplete
    def __init__(self, tracking_uri: str) -> None:
        """
        :param tracking_uri: Address of local or remote tracking server.
        """
    def create_user(self, username: str, password: str):
        '''
        Create a new user.

        :param username: The username.
        :param password: The user\'s password. Must not be empty string.

        :return: A single :py:class:`mlflow.server.auth.entities.User` object.
                 Raises ``RestException`` if the username is already taken.

        .. code-block:: python
            :caption: Example

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            user = client.create_user("newuser", "newpassword")
            print("user_id: {}".format(user.id))
            print("username: {}".format(user.username))
            print("password_hash: {}".format(user.password_hash))
            print("is_admin: {}".format(user.is_admin))

        .. code-block:: text
            :caption: Output

            user_id: 3
            username: newuser
            password_hash: REDACTED
            is_admin: False
        '''
    def get_user(self, username: str):
        '''
        Get a user with a specific username.

        :param username: The username.

        :return: A single :py:class:`mlflow.server.auth.entities.User` object.
                 Raises ``RestException`` if the user does not exist.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")

            user = client.get_user("newuser")
            print("user_id: {}".format(user.id))
            print("username: {}".format(user.username))
            print("password_hash: {}".format(user.password_hash))
            print("is_admin: {}".format(user.is_admin))

        .. code-block:: text
            :caption: Output

            user_id: 3
            username: newuser
            password_hash: REDACTED
            is_admin: False
        '''
    def update_user_password(self, username: str, password: str):
        '''
        Update the password of a specific user.

        :param username: The username.
        :param password: The new password.

        :return: None. Raises ``RestException`` if the user does not exist.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")

            client.update_user_password("newuser", "anotherpassword")
        '''
    def update_user_admin(self, username: str, is_admin: bool):
        '''
        Update the admin status of a specific user.

        :param username: The username.
        :param is_admin: The new admin status.

        :return: None. Raises ``RestException`` if the user does not exist.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")

            client.update_user_admin("newuser", True)
        '''
    def delete_user(self, username: str):
        '''
        Delete a specific user.

        :param username: The username.

        :return: None. Raises ``RestException`` if the user does not exist.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")

            client.delete_user("newuser")
        '''
    def create_experiment_permission(self, experiment_id: str, username: str, permission: str):
        '''
        Create a permission on an experiment for a user.

        :param experiment_id: The id of the experiment.
        :param username: The username.
        :param permission: Permission to grant.
            Must be one of "READ", "EDIT", "MANAGE" and "NO_PERMISSIONS".

        :return: A single :py:class:`mlflow.server.auth.entities.ExperimentPermission` object.
                 Raises ``RestException`` if the user does not exist,
                 or a permission already exists for this experiment user pair,
                 or if the permission is invalid.
                 Does not require ``experiment_id`` to be an existing experiment.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            ep = client.create_experiment_permission("myexperiment", "newuser", "READ")
            print("experiment_id: {}".format(ep.experiment_id))
            print("user_id: {}".format(ep.user_id))
            print("permission: {}".format(ep.permission))

        .. code-block:: text
            :caption: Output

            experiment_id: myexperiment
            user_id: 3
            permission: READ
        '''
    def get_experiment_permission(self, experiment_id: str, username: str):
        '''
        Get an experiment permission for a user.

        :param experiment_id: The id of the experiment.
        :param username: The username.

        :return: A single :py:class:`mlflow.server.auth.entities.ExperimentPermission` object.
                 Raises ``RestException`` if the user does not exist,
                 or no permission exists for this experiment user pair.
                 Note that the default permission will still be effective even if
                 no permission exists.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            client.create_experiment_permission("myexperiment", "newuser", "READ")
            ep = client.get_experiment_permission("myexperiment", "newuser")
            print("experiment_id: {}".format(ep.experiment_id))
            print("user_id: {}".format(ep.user_id))
            print("permission: {}".format(ep.permission))

        .. code-block:: text
            :caption: Output

            experiment_id: myexperiment
            user_id: 3
            permission: READ
        '''
    def update_experiment_permission(self, experiment_id: str, username: str, permission: str):
        '''
        Update an existing experiment permission for a user.

        :param experiment_id: The id of the experiment.
        :param username: The username.
        :param permission: New permission to grant.
            Must be one of "READ", "EDIT", "MANAGE" and "NO_PERMISSIONS".

        :return: None. Raises ``RestException`` if the user does not exist,
                 or no permission exists for this experiment user pair,
                 or if the permission is invalid.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            client.create_experiment_permission("myexperiment", "newuser", "READ")
            client.update_experiment_permission("myexperiment", "newuser", "EDIT")
        '''
    def delete_experiment_permission(self, experiment_id: str, username: str):
        '''
        Delete an existing experiment permission for a user.

        :param experiment_id: The id of the experiment.
        :param username: The username.

        :return: None. Raises ``RestException`` if the user does not exist,
                 or no permission exists for this experiment user pair,
                 or if the permission is invalid.
                 Note that the default permission will still be effective even
                 after the permission has been deleted.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            client.create_experiment_permission("myexperiment", "newuser", "READ")
            client.delete_experiment_permission("myexperiment", "newuser")
        '''
    def create_registered_model_permission(self, name: str, username: str, permission: str):
        '''
        Create a permission on an registered model for a user.

        :param name: The name of the registered model.
        :param username: The username.
        :param permission: Permission to grant.
            Must be one of "READ", "EDIT", "MANAGE" and "NO_PERMISSIONS".

        :return: A single :py:class:`mlflow.server.auth.entities.RegisteredModelPermission` object.
                 Raises ``RestException`` if the user does not exist,
                 or a permission already exists for this registered model user pair,
                 or if the permission is invalid.
                 Does not require ``name`` to be an existing registered model.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            rmp = client.create_registered_model_permission("myregisteredmodel", "newuser", "READ")
            print("name: {}".format(rmp.name))
            print("user_id: {}".format(rmp.user_id))
            print("permission: {}".format(rmp.permission))

        .. code-block:: text
            :caption: Output

            name: myregisteredmodel
            user_id: 3
            permission: READ
        '''
    def get_registered_model_permission(self, name: str, username: str):
        '''
        Get an registered model permission for a user.

        :param name: The name of the registered model.
        :param username: The username.

        :return: A single :py:class:`mlflow.server.auth.entities.RegisteredModelPermission` object.
                 Raises ``RestException`` if the user does not exist,
                 or no permission exists for this registered model user pair.
                 Note that the default permission will still be effective even if
                 no permission exists.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            client.create_registered_model_permission("myregisteredmodel", "newuser", "READ")
            rmp = client.get_registered_model_permission("myregisteredmodel", "newuser")
            print("name: {}".format(rmp.name))
            print("user_id: {}".format(rmp.user_id))
            print("permission: {}".format(rmp.permission))

        .. code-block:: text
            :caption: Output

            name: myregisteredmodel
            user_id: 3
            permission: READ
        '''
    def update_registered_model_permission(self, name: str, username: str, permission: str):
        '''
        Update an existing registered model permission for a user.

        :param name: The name of the registered model.
        :param username: The username.
        :param permission: New permission to grant.
            Must be one of "READ", "EDIT", "MANAGE" and "NO_PERMISSIONS".

        :return: None. Raises ``RestException`` if the user does not exist,
                 or no permission exists for this registered model user pair,
                 or if the permission is invalid.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            client.create_registered_model_permission("myregisteredmodel", "newuser", "READ")
            client.update_registered_model_permission("myregisteredmodel", "newuser", "EDIT")
        '''
    def delete_registered_model_permission(self, name: str, username: str):
        '''
        Delete an existing registered model permission for a user.

        :param name: The name of the registered model.
        :param username: The username.

        :return: None. Raises ``RestException`` if the user does not exist,
                 or no permission exists for this registered model user pair,
                 or if the permission is invalid.
                 Note that the default permission will still be effective even
                 after the permission has been deleted.

        .. code-block:: bash
            :caption: Example

            export MLFLOW_TRACKING_USERNAME=admin
            export MLFLOW_TRACKING_PASSWORD=password

        .. code-block:: python

            from mlflow.server.auth.client import AuthServiceClient

            client = AuthServiceClient("tracking_uri")
            client.create_user("newuser", "newpassword")
            client.create_registered_model_permission("myregisteredmodel", "newuser", "READ")
            client.delete_registered_model_permission("myregisteredmodel", "newuser")
        '''
