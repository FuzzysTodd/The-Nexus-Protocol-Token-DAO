def log_device_compatibility_check(policy_name) -> None:
    """Logs a compatibility check if the devices support the policy.

    Currently only logs for the policy mixed_float16. A log is shown only the
    first time this function is called.

    Args:
      policy_name: The name of the dtype policy.
    """
