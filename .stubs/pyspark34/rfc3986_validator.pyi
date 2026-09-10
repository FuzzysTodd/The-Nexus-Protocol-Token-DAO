__all__ = ['validate_rfc3986']

def validate_rfc3986(url, rule: str = 'URI'):
    """
    Validates strings according to RFC3986

    :param url: String cointaining URI to validate
    :param rule: It could be 'URI' (default) or 'URI_reference'.
    :return: True or False
    """
