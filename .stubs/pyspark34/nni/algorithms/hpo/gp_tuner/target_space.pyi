from _typeshed import Incomplete

class TargetSpace:
    """
    Holds the param-space coordinates (X) and target values (Y)

    Parameters
    ----------
    pbounds : dict
        Dictionary with parameters names and legal values.

    random_state : int, RandomState, or None
        optionally specify a seed for a random number generator, by default None.
    """
    def __init__(self, pbounds, random_state: Incomplete | None = None) -> None: ...
    def __contains__(self, params) -> bool:
        """
        check if a parameter is already registered

        Parameters
        ----------
        params : numpy array

        Returns
        -------
        bool
            True if the parameter is already registered, else false
        """
    def len(self):
        """
        length of registered params and targets

        Returns
        -------
        int
        """
    @property
    def params(self):
        """
        registered parameters

        Returns
        -------
        numpy array
        """
    @property
    def target(self):
        """
        registered target values

        Returns
        -------
        numpy array
        """
    @property
    def dim(self):
        """
        dimension of parameters

        Returns
        -------
        int
        """
    @property
    def keys(self):
        """
        keys of parameters

        Returns
        -------
        numpy array
        """
    @property
    def bounds(self):
        """
        bounds of parameters

        Returns
        -------
        numpy array
        """
    def params_to_array(self, params):
        """
        dict to array

        Parameters
        ----------
        params : dict
            dict format of parameters

        Returns
        -------
        numpy array
            array format of parameters
        """
    def array_to_params(self, x):
        """
        array to dict

        maintain int type if the paramters is defined as int in search_space.json
        Parameters
        ----------
        x : numpy array
            array format of parameters

        Returns
        -------
        dict
            dict format of parameters
        """
    def register(self, params, target) -> None:
        """
        Append a point and its target value to the known data.

        Parameters
        ----------
        params : dict
            parameters

        target : float
            target function value
        """
    def random_sample(self):
        """
        Creates a random point within the bounds of the space.

        Returns
        -------
        numpy array
            one groupe of parameter
        """
    def max(self):
        """
        Get maximum target value found and its corresponding parameters.

        Returns
        -------
        dict
            target value and parameters, empty dict if nothing registered
        """
    def res(self):
        """
        Get all target values found and corresponding parameters.

        Returns
        -------
        list
            a list of target values and their corresponding parameters
        """
