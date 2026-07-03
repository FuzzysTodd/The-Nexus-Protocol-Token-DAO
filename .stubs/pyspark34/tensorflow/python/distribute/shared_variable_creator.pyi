def make_fn(shared_variable_store, device_id):
    """Construct the variable creator function for device `device_id`.

  Constructs custom variable creator functions for the given device.
  On first device (device_id == 0), it creates the variable using the
  `next_creator`, and stores it in the provided `shared_variable_store`.
  On all other devices (device_id > 0), it tries to re-use the variable
  already created with the same name. If no such variable exists, it throws an
  error.
  Additionally, we de-uniquify variable names before checking for matches. This
  helps re-use variables which are intended to be the same but have different
  names due to variable uniquification happening upstream. Since this might
  mean we may have multiple variables with the same canonical name, we store
  them in a list per canonical name and return them in the same order as well.

  Args:
    shared_variable_store: A dictionary that we will use to store variables
      created on the first device, and re-used by creators for other devices.
    device_id: Integer index of the device whose creator should be
      constructed.

  Returns:
    An appropriate creator function based on device_id.

  """
