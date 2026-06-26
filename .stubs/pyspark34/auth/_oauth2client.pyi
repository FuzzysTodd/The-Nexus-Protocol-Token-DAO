def convert(credentials):
    """Convert oauth2client credentials to google-auth credentials.

    This class converts:

    - :class:`oauth2client.client.OAuth2Credentials` to
      :class:`google.oauth2.credentials.Credentials`.
    - :class:`oauth2client.client.GoogleCredentials` to
      :class:`google.oauth2.credentials.Credentials`.
    - :class:`oauth2client.service_account.ServiceAccountCredentials` to
      :class:`google.oauth2.service_account.Credentials`.
    - :class:`oauth2client.service_account._JWTAccessCredentials` to
      :class:`google.oauth2.service_account.Credentials`.
    - :class:`oauth2client.contrib.gce.AppAssertionCredentials` to
      :class:`google.auth.compute_engine.Credentials`.
    - :class:`oauth2client.contrib.appengine.AppAssertionCredentials` to
      :class:`google.auth.app_engine.Credentials`.

    Returns:
        google.auth.credentials.Credentials: The converted credentials.

    Raises:
        ValueError: If the credentials could not be converted.
    """
