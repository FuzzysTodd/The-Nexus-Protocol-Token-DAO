from typing import Any

__all__ = ['physical_constants', 'value', 'unit', 'precision', 'find', 'ConstantWarning']

physical_constants: dict[str, tuple[float, str, float]]

class ConstantWarning(DeprecationWarning):
    """Accessing a constant no longer in current CODATA data set"""

def value(key: str) -> float:
    """
    Value in physical_constants indexed by key

    Parameters
    ----------
    key : Python string
        Key in dictionary `physical_constants`

    Returns
    -------
    value : float
        Value in `physical_constants` corresponding to `key`

    Examples
    --------
    >>> from scipy import constants
    >>> constants.value('elementary charge')
    1.602176634e-19

    """
def unit(key: str) -> str:
    """
    Unit in physical_constants indexed by key

    Parameters
    ----------
    key : Python string
        Key in dictionary `physical_constants`

    Returns
    -------
    unit : Python string
        Unit in `physical_constants` corresponding to `key`

    Examples
    --------
    >>> from scipy import constants
    >>> constants.unit('proton mass')
    'kg'

    """
def precision(key: str) -> float:
    """
    Relative precision in physical_constants indexed by key

    Parameters
    ----------
    key : Python string
        Key in dictionary `physical_constants`

    Returns
    -------
    prec : float
        Relative precision in `physical_constants` corresponding to `key`

    Examples
    --------
    >>> from scipy import constants
    >>> constants.precision('proton mass')
    5.1e-37

    """
def find(sub: str | None = None, disp: bool = False) -> Any:
    """
    Return list of physical_constant keys containing a given string.

    Parameters
    ----------
    sub : str
        Sub-string to search keys for. By default, return all keys.
    disp : bool
        If True, print the keys that are found and return None.
        Otherwise, return the list of keys without printing anything.

    Returns
    -------
    keys : list or None
        If `disp` is False, the list of keys is returned.
        Otherwise, None is returned.

    Examples
    --------
    >>> from scipy.constants import find, physical_constants

    Which keys in the ``physical_constants`` dictionary contain 'boltzmann'?

    >>> find('boltzmann')
    ['Boltzmann constant',
     'Boltzmann constant in Hz/K',
     'Boltzmann constant in eV/K',
     'Boltzmann constant in inverse meter per kelvin',
     'Stefan-Boltzmann constant']

    Get the constant called 'Boltzmann constant in Hz/K':

    >>> physical_constants['Boltzmann constant in Hz/K']
    (20836619120.0, 'Hz K^-1', 0.0)

    Find constants with 'radius' in the key:

    >>> find('radius')
    ['Bohr radius',
     'classical electron radius',
     'deuteron rms charge radius',
     'proton rms charge radius']
    >>> physical_constants['classical electron radius']
    (2.8179403262e-15, 'm', 1.3e-24)

    """
