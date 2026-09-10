__all__ = ['get_env_var']

def get_env_var(key, as_type, env):
    """
    Get the environment variable option.

    :param key: the config key requested
    :param as_type: the type we would like to convert it to
    :param env: environment variables to use
    :return:
    """
