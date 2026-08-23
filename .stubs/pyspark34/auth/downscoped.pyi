from _typeshed import Incomplete
from google.auth import credentials

class CredentialAccessBoundary:
    """Defines a Credential Access Boundary which contains a list of access boundary
    rules. Each rule contains information on the resource that the rule applies to,
    the upper bound of the permissions that are available on that resource and an
    optional condition to further restrict permissions.
    """
    def __init__(self, rules=[]) -> None:
        """Instantiates a Credential Access Boundary. A Credential Access Boundary
        can contain up to 10 access boundary rules.

        Args:
            rules (Sequence[google.auth.downscoped.AccessBoundaryRule]): The list of
                access boundary rules limiting the access that a downscoped credential
                will have.
        Raises:
            InvalidType: If any of the rules are not a valid type.
            InvalidValue: If the provided rules exceed the maximum allowed.
        """
    @property
    def rules(self):
        """Returns the list of access boundary rules defined on the Credential
        Access Boundary.

        Returns:
            Tuple[google.auth.downscoped.AccessBoundaryRule, ...]: The list of access
                boundary rules defined on the Credential Access Boundary. These are returned
                as an immutable tuple to prevent modification.
        """
    @rules.setter
    def rules(self, value) -> None:
        """Updates the current rules on the Credential Access Boundary. This will overwrite
        the existing set of rules.

        Args:
            value (Sequence[google.auth.downscoped.AccessBoundaryRule]): The list of
                access boundary rules limiting the access that a downscoped credential
                will have.
        Raises:
            InvalidType: If any of the rules are not a valid type.
            InvalidValue: If the provided rules exceed the maximum allowed.
        """
    def add_rule(self, rule) -> None:
        """Adds a single access boundary rule to the existing rules.

        Args:
            rule (google.auth.downscoped.AccessBoundaryRule): The access boundary rule,
                limiting the access that a downscoped credential will have, to be added to
                the existing rules.
        Raises:
            InvalidType: If any of the rules are not a valid type.
            InvalidValue: If the provided rules exceed the maximum allowed.
        """
    def to_json(self):
        """Generates the dictionary representation of the Credential Access Boundary.
        This uses the format expected by the Security Token Service API as documented in
        `Defining a Credential Access Boundary`_.

        .. _Defining a Credential Access Boundary:
            https://cloud.google.com/iam/docs/downscoping-short-lived-credentials#define-boundary

        Returns:
            Mapping: Credential Access Boundary Rule represented in a dictionary object.
        """

class AccessBoundaryRule:
    """Defines an access boundary rule which contains information on the resource that
    the rule applies to, the upper bound of the permissions that are available on that
    resource and an optional condition to further restrict permissions.
    """
    def __init__(self, available_resource, available_permissions, availability_condition: Incomplete | None = None) -> None:
        '''Instantiates a single access boundary rule.

        Args:
            available_resource (str): The full resource name of the Cloud Storage bucket
                that the rule applies to. Use the format
                "//storage.googleapis.com/projects/_/buckets/bucket-name".
            available_permissions (Sequence[str]): A list defining the upper bound that
                the downscoped token will have on the available permissions for the
                resource. Each value is the identifier for an IAM predefined role or
                custom role, with the prefix "inRole:". For example:
                "inRole:roles/storage.objectViewer".
                Only the permissions in these roles will be available.
            availability_condition (Optional[google.auth.downscoped.AvailabilityCondition]):
                Optional condition that restricts the availability of permissions to
                specific Cloud Storage objects.

        Raises:
            InvalidType: If any of the parameters are not of the expected types.
            InvalidValue: If any of the parameters are not of the expected values.
        '''
    @property
    def available_resource(self):
        """Returns the current available resource.

        Returns:
           str: The current available resource.
        """
    @available_resource.setter
    def available_resource(self, value) -> None:
        """Updates the current available resource.

        Args:
            value (str): The updated value of the available resource.

        Raises:
            google.auth.exceptions.InvalidType: If the value is not a string.
        """
    @property
    def available_permissions(self):
        """Returns the current available permissions.

        Returns:
           Tuple[str, ...]: The current available permissions. These are returned
               as an immutable tuple to prevent modification.
        """
    @available_permissions.setter
    def available_permissions(self, value) -> None:
        """Updates the current available permissions.

        Args:
            value (Sequence[str]): The updated value of the available permissions.

        Raises:
            InvalidType: If the value is not a list of strings.
            InvalidValue: If the value is not valid.
        """
    @property
    def availability_condition(self):
        """Returns the current availability condition.

        Returns:
           Optional[google.auth.downscoped.AvailabilityCondition]: The current
               availability condition.
        """
    @availability_condition.setter
    def availability_condition(self, value) -> None:
        """Updates the current availability condition.

        Args:
            value (Optional[google.auth.downscoped.AvailabilityCondition]): The updated
                value of the availability condition.

        Raises:
            google.auth.exceptions.InvalidType: If the value is not of type google.auth.downscoped.AvailabilityCondition
                or None.
        """
    def to_json(self):
        """Generates the dictionary representation of the access boundary rule.
        This uses the format expected by the Security Token Service API as documented in
        `Defining a Credential Access Boundary`_.

        .. _Defining a Credential Access Boundary:
            https://cloud.google.com/iam/docs/downscoping-short-lived-credentials#define-boundary

        Returns:
            Mapping: The access boundary rule represented in a dictionary object.
        """

class AvailabilityCondition:
    """An optional condition that can be used as part of a Credential Access Boundary
    to further restrict permissions."""
    def __init__(self, expression, title: Incomplete | None = None, description: Incomplete | None = None) -> None:
        '''Instantiates an availability condition using the provided expression and
        optional title or description.

        Args:
            expression (str): A condition expression that specifies the Cloud Storage
                objects where permissions are available. For example, this expression
                makes permissions available for objects whose name starts with "customer-a":
                "resource.name.startsWith(\'projects/_/buckets/example-bucket/objects/customer-a\')"
            title (Optional[str]): An optional short string that identifies the purpose of
                the condition.
            description (Optional[str]): Optional details about the purpose of the condition.

        Raises:
            InvalidType: If any of the parameters are not of the expected types.
            InvalidValue: If any of the parameters are not of the expected values.
        '''
    @property
    def expression(self):
        """Returns the current condition expression.

        Returns:
           str: The current conditon expression.
        """
    @expression.setter
    def expression(self, value) -> None:
        """Updates the current condition expression.

        Args:
            value (str): The updated value of the condition expression.

        Raises:
            google.auth.exceptions.InvalidType: If the value is not of type string.
        """
    @property
    def title(self):
        """Returns the current title.

        Returns:
           Optional[str]: The current title.
        """
    @title.setter
    def title(self, value) -> None:
        """Updates the current title.

        Args:
            value (Optional[str]): The updated value of the title.

        Raises:
            google.auth.exceptions.InvalidType: If the value is not of type string or None.
        """
    @property
    def description(self):
        """Returns the current description.

        Returns:
           Optional[str]: The current description.
        """
    @description.setter
    def description(self, value) -> None:
        """Updates the current description.

        Args:
            value (Optional[str]): The updated value of the description.

        Raises:
            google.auth.exceptions.InvalidType: If the value is not of type string or None.
        """
    def to_json(self):
        """Generates the dictionary representation of the availability condition.
        This uses the format expected by the Security Token Service API as documented in
        `Defining a Credential Access Boundary`_.

        .. _Defining a Credential Access Boundary:
            https://cloud.google.com/iam/docs/downscoping-short-lived-credentials#define-boundary

        Returns:
            Mapping[str, str]: The availability condition represented in a dictionary
                object.
        """

class Credentials(credentials.CredentialsWithQuotaProject):
    """Defines a set of Google credentials that are downscoped from an existing set
    of Google OAuth2 credentials. This is useful to restrict the Identity and Access
    Management (IAM) permissions that a short-lived credential can use.
    The common pattern of usage is to have a token broker with elevated access
    generate these downscoped credentials from higher access source credentials and
    pass the downscoped short-lived access tokens to a token consumer via some
    secure authenticated channel for limited access to Google Cloud Storage
    resources.
    """
    def __init__(self, source_credentials, credential_access_boundary, quota_project_id: Incomplete | None = None) -> None:
        """Instantiates a downscoped credentials object using the provided source
        credentials and credential access boundary rules.
        To downscope permissions of a source credential, a Credential Access Boundary
        that specifies which resources the new credential can access, as well as an
        upper bound on the permissions that are available on each resource, has to be
        defined. A downscoped credential can then be instantiated using the source
        credential and the Credential Access Boundary.

        Args:
            source_credentials (google.auth.credentials.Credentials): The source credentials
                to be downscoped based on the provided Credential Access Boundary rules.
            credential_access_boundary (google.auth.downscoped.CredentialAccessBoundary):
                The Credential Access Boundary which contains a list of access boundary
                rules. Each rule contains information on the resource that the rule applies to,
                the upper bound of the permissions that are available on that resource and an
                optional condition to further restrict permissions.
            quota_project_id (Optional[str]): The optional quota project ID.
        Raises:
            google.auth.exceptions.RefreshError: If the source credentials
                return an error on token refresh.
            google.auth.exceptions.OAuthError: If the STS token exchange
                endpoint returned an error during downscoped token generation.
        """
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    def with_quota_project(self, quota_project_id): ...
