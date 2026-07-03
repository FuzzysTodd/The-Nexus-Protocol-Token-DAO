import abc
from .utils import canonicalize_version as canonicalize_version
from .version import Version as Version
from typing import Callable, Iterable, Iterator, TypeVar

UnparsedVersion = Version | str
UnparsedVersionVar = TypeVar('UnparsedVersionVar', bound=UnparsedVersion)
CallableOperator = Callable[[Version, str], bool]

class InvalidSpecifier(ValueError):
    '''
    Raised when attempting to create a :class:`Specifier` with a specifier
    string that is invalid.

    >>> Specifier("lolwat")
    Traceback (most recent call last):
        ...
    packaging.specifiers.InvalidSpecifier: Invalid specifier: \'lolwat\'
    '''

class BaseSpecifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __hash__(self) -> int:
        """
        Returns a hash value for this Specifier-like object.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Returns a boolean representing whether or not the two Specifier-like
        objects are equal.

        :param other: The other object to check against.
        """
    @property
    @abc.abstractmethod
    def prereleases(self) -> bool | None:
        """Whether or not pre-releases as a whole are allowed.

        This can be set to either ``True`` or ``False`` to explicitly enable or disable
        prereleases or it can be set to ``None`` (the default) to use default semantics.
        """
    @prereleases.setter
    def prereleases(self, value: bool) -> None:
        """Setter for :attr:`prereleases`.

        :param value: The value to set.
        """
    @abc.abstractmethod
    def contains(self, item: str, prereleases: bool | None = None) -> bool:
        """
        Determines if the given item is contained within this specifier.
        """
    @abc.abstractmethod
    def filter(self, iterable: Iterable[UnparsedVersionVar], prereleases: bool | None = None) -> Iterator[UnparsedVersionVar]:
        """
        Takes an iterable of items and filters them so that only items which
        are contained within this specifier are allowed in it.
        """

class Specifier(BaseSpecifier):
    """This class abstracts handling of version specifiers.

    .. tip::

        It is generally not required to instantiate this manually. You should instead
        prefer to work with :class:`SpecifierSet` instead, which can parse
        comma-separated version specifiers (which is what package metadata contains).
    """
    def __init__(self, spec: str = '', prereleases: bool | None = None) -> None:
        """Initialize a Specifier instance.

        :param spec:
            The string representation of a specifier which will be parsed and
            normalized before use.
        :param prereleases:
            This tells the specifier if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.
        :raises InvalidSpecifier:
            If the given specifier is invalid (i.e. bad syntax).
        """
    @property
    def prereleases(self) -> bool: ...
    @prereleases.setter
    def prereleases(self, value: bool) -> None: ...
    @property
    def operator(self) -> str:
        '''The operator of this specifier.

        >>> Specifier("==1.2.3").operator
        \'==\'
        '''
    @property
    def version(self) -> str:
        '''The version of this specifier.

        >>> Specifier("==1.2.3").version
        \'1.2.3\'
        '''
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool:
        '''Whether or not the two Specifier-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> Specifier("==1.2.3") == Specifier("== 1.2.3.0")
        True
        >>> (Specifier("==1.2.3", prereleases=False) ==
        ...  Specifier("==1.2.3", prereleases=True))
        True
        >>> Specifier("==1.2.3") == "==1.2.3"
        True
        >>> Specifier("==1.2.3") == Specifier("==1.2.4")
        False
        >>> Specifier("==1.2.3") == Specifier("~=1.2.3")
        False
        '''
    def __contains__(self, item: str | Version) -> bool:
        '''Return whether or not the item is contained in this specifier.

        :param item: The item to check for.

        This is used for the ``in`` operator and behaves the same as
        :meth:`contains` with no ``prereleases`` argument passed.

        >>> "1.2.3" in Specifier(">=1.2.3")
        True
        >>> Version("1.2.3") in Specifier(">=1.2.3")
        True
        >>> "1.0.0" in Specifier(">=1.2.3")
        False
        >>> "1.3.0a1" in Specifier(">=1.2.3")
        False
        >>> "1.3.0a1" in Specifier(">=1.2.3", prereleases=True)
        True
        '''
    def contains(self, item: UnparsedVersion, prereleases: bool | None = None) -> bool:
        '''Return whether or not the item is contained in this specifier.

        :param item:
            The item to check for, which can be a version string or a
            :class:`Version` instance.
        :param prereleases:
            Whether or not to match prereleases with this Specifier. If set to
            ``None`` (the default), it uses :attr:`prereleases` to determine
            whether or not prereleases are allowed.

        >>> Specifier(">=1.2.3").contains("1.2.3")
        True
        >>> Specifier(">=1.2.3").contains(Version("1.2.3"))
        True
        >>> Specifier(">=1.2.3").contains("1.0.0")
        False
        >>> Specifier(">=1.2.3").contains("1.3.0a1")
        False
        >>> Specifier(">=1.2.3", prereleases=True).contains("1.3.0a1")
        True
        >>> Specifier(">=1.2.3").contains("1.3.0a1", prereleases=True)
        True
        '''
    def filter(self, iterable: Iterable[UnparsedVersionVar], prereleases: bool | None = None) -> Iterator[UnparsedVersionVar]:
        '''Filter items in the given iterable, that match the specifier.

        :param iterable:
            An iterable that can contain version strings and :class:`Version` instances.
            The items in the iterable will be filtered according to the specifier.
        :param prereleases:
            Whether or not to allow prereleases in the returned iterator. If set to
            ``None`` (the default), it will be intelligently decide whether to allow
            prereleases or not (based on the :attr:`prereleases` attribute, and
            whether the only versions matching are prereleases).

        This method is smarter than just ``filter(Specifier().contains, [...])``
        because it implements the rule from :pep:`440` that a prerelease item
        SHOULD be accepted if no other versions match the given specifier.

        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.3", "1.5a1"]))
        [\'1.3\']
        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.2.3", "1.3", Version("1.4")]))
        [\'1.2.3\', \'1.3\', <Version(\'1.4\')>]
        >>> list(Specifier(">=1.2.3").filter(["1.2", "1.5a1"]))
        [\'1.5a1\']
        >>> list(Specifier(">=1.2.3").filter(["1.3", "1.5a1"], prereleases=True))
        [\'1.3\', \'1.5a1\']
        >>> list(Specifier(">=1.2.3", prereleases=True).filter(["1.3", "1.5a1"]))
        [\'1.3\', \'1.5a1\']
        '''

class SpecifierSet(BaseSpecifier):
    """This class abstracts handling of a set of version specifiers.

    It can be passed a single specifier (``>=3.0``), a comma-separated list of
    specifiers (``>=3.0,!=3.1``), or no specifier at all.
    """
    def __init__(self, specifiers: str = '', prereleases: bool | None = None) -> None:
        """Initialize a SpecifierSet instance.

        :param specifiers:
            The string representation of a specifier or a comma-separated list of
            specifiers which will be parsed and normalized before use.
        :param prereleases:
            This tells the SpecifierSet if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.

        :raises InvalidSpecifier:
            If the given ``specifiers`` are not parseable than this exception will be
            raised.
        """
    @property
    def prereleases(self) -> bool | None: ...
    @prereleases.setter
    def prereleases(self, value: bool) -> None: ...
    def __hash__(self) -> int: ...
    def __and__(self, other: SpecifierSet | str) -> SpecifierSet:
        '''Return a SpecifierSet which is a combination of the two sets.

        :param other: The other object to combine with.

        >>> SpecifierSet(">=1.0.0,!=1.0.1") & \'<=2.0.0,!=2.0.1\'
        <SpecifierSet(\'!=1.0.1,!=2.0.1,<=2.0.0,>=1.0.0\')>
        >>> SpecifierSet(">=1.0.0,!=1.0.1") & SpecifierSet(\'<=2.0.0,!=2.0.1\')
        <SpecifierSet(\'!=1.0.1,!=2.0.1,<=2.0.0,>=1.0.0\')>
        '''
    def __eq__(self, other: object) -> bool:
        '''Whether or not the two SpecifierSet-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> (SpecifierSet(">=1.0.0,!=1.0.1", prereleases=False) ==
        ...  SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True))
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == ">=1.0.0,!=1.0.1"
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1") == SpecifierSet(">=1.0.0,!=1.0.2")
        False
        '''
    def __len__(self) -> int:
        """Returns the number of specifiers in this specifier set."""
    def __iter__(self) -> Iterator[Specifier]:
        '''
        Returns an iterator over all the underlying :class:`Specifier` instances
        in this specifier set.

        >>> sorted(SpecifierSet(">=1.0.0,!=1.0.1"), key=str)
        [<Specifier(\'!=1.0.1\')>, <Specifier(\'>=1.0.0\')>]
        '''
    def __contains__(self, item: UnparsedVersion) -> bool:
        '''Return whether or not the item is contained in this specifier.

        :param item: The item to check for.

        This is used for the ``in`` operator and behaves the same as
        :meth:`contains` with no ``prereleases`` argument passed.

        >>> "1.2.3" in SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> Version("1.2.3") in SpecifierSet(">=1.0.0,!=1.0.1")
        True
        >>> "1.0.1" in SpecifierSet(">=1.0.0,!=1.0.1")
        False
        >>> "1.3.0a1" in SpecifierSet(">=1.0.0,!=1.0.1")
        False
        >>> "1.3.0a1" in SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True)
        True
        '''
    def contains(self, item: UnparsedVersion, prereleases: bool | None = None, installed: bool | None = None) -> bool:
        '''Return whether or not the item is contained in this SpecifierSet.

        :param item:
            The item to check for, which can be a version string or a
            :class:`Version` instance.
        :param prereleases:
            Whether or not to match prereleases with this SpecifierSet. If set to
            ``None`` (the default), it uses :attr:`prereleases` to determine
            whether or not prereleases are allowed.

        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.2.3")
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains(Version("1.2.3"))
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.0.1")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.3.0a1")
        False
        >>> SpecifierSet(">=1.0.0,!=1.0.1", prereleases=True).contains("1.3.0a1")
        True
        >>> SpecifierSet(">=1.0.0,!=1.0.1").contains("1.3.0a1", prereleases=True)
        True
        '''
    def filter(self, iterable: Iterable[UnparsedVersionVar], prereleases: bool | None = None) -> Iterator[UnparsedVersionVar]:
        '''Filter items in the given iterable, that match the specifiers in this set.

        :param iterable:
            An iterable that can contain version strings and :class:`Version` instances.
            The items in the iterable will be filtered according to the specifier.
        :param prereleases:
            Whether or not to allow prereleases in the returned iterator. If set to
            ``None`` (the default), it will be intelligently decide whether to allow
            prereleases or not (based on the :attr:`prereleases` attribute, and
            whether the only versions matching are prereleases).

        This method is smarter than just ``filter(SpecifierSet(...).contains, [...])``
        because it implements the rule from :pep:`440` that a prerelease item
        SHOULD be accepted if no other versions match the given specifier.

        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.3", "1.5a1"]))
        [\'1.3\']
        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.3", Version("1.4")]))
        [\'1.3\', <Version(\'1.4\')>]
        >>> list(SpecifierSet(">=1.2.3").filter(["1.2", "1.5a1"]))
        []
        >>> list(SpecifierSet(">=1.2.3").filter(["1.3", "1.5a1"], prereleases=True))
        [\'1.3\', \'1.5a1\']
        >>> list(SpecifierSet(">=1.2.3", prereleases=True).filter(["1.3", "1.5a1"]))
        [\'1.3\', \'1.5a1\']

        An "empty" SpecifierSet will filter items based on the presence of prerelease
        versions in the set.

        >>> list(SpecifierSet("").filter(["1.3", "1.5a1"]))
        [\'1.3\']
        >>> list(SpecifierSet("").filter(["1.5a1"]))
        [\'1.5a1\']
        >>> list(SpecifierSet("", prereleases=True).filter(["1.3", "1.5a1"]))
        [\'1.3\', \'1.5a1\']
        >>> list(SpecifierSet("").filter(["1.3", "1.5a1"], prereleases=True))
        [\'1.3\', \'1.5a1\']
        '''
