import typing as t
from .loader import Config as Config, DeferredConfig as DeferredConfig, LazyConfigValue as LazyConfigValue
from _typeshed import Incomplete
from traitlets.traitlets import Any as Any, Container as Container, Dict as Dict, HasTraits as HasTraits, Instance as Instance, TraitType as TraitType, default as default, observe as observe, observe_compat as observe_compat, validate as validate
from traitlets.utils import warnings as warnings
from traitlets.utils.bunch import Bunch as Bunch
from traitlets.utils.text import indent as indent, wrap_paragraphs as wrap_paragraphs

LoggerType: Incomplete

class ConfigurableError(Exception): ...
class MultipleInstanceError(ConfigurableError): ...

class Configurable(HasTraits):
    config: Incomplete
    parent: Incomplete
    def __init__(self, **kwargs: t.Any) -> None:
        """Create a configurable given a config config.

        Parameters
        ----------
        config : Config
            If this is empty, default values are used. If config is a
            :class:`Config` instance, it will be used to configure the
            instance.
        parent : Configurable instance, optional
            The parent Configurable instance of this object.

        Notes
        -----
        Subclasses of Configurable must call the :meth:`__init__` method of
        :class:`Configurable` *before* doing anything else and using
        :func:`super`::

            class MyConfigurable(Configurable):
                def __init__(self, config=None):
                    super(MyConfigurable, self).__init__(config=config)
                    # Then any other code you need to finish initialization.

        This ensures that instances will be configured properly.
        """
    @classmethod
    def section_names(cls) -> list[str]:
        """return section names as a list"""
    def update_config(self, config: Config) -> None:
        """Update config and load the new values"""
    @classmethod
    def class_get_help(cls, inst: HasTraits | None = None) -> str:
        """Get the help string for this class in ReST format.

        If `inst` is given, its current trait values will be used in place of
        class defaults.
        """
    @classmethod
    def class_get_trait_help(cls, trait: TraitType[t.Any, t.Any], inst: HasTraits | None = None, helptext: str | None = None) -> str:
        """Get the helptext string for a single trait.

        :param inst:
            If given, its current trait values will be used in place of
            the class default.
        :param helptext:
            If not given, uses the `help` attribute of the current trait.
        """
    @classmethod
    def class_print_help(cls, inst: HasTraits | None = None) -> None:
        """Get the help string for a single trait and print it."""
    @classmethod
    def class_config_section(cls, classes: t.Sequence[type[HasTraits]] | None = None) -> str:
        """Get the config section for this class.

        Parameters
        ----------
        classes : list, optional
            The list of other classes in the config file.
            Used to reduce redundant information.
        """
    @classmethod
    def class_config_rst_doc(cls) -> str:
        """Generate rST documentation for this class' config options.

        Excludes traits defined on parent classes.
        """

class LoggingConfigurable(Configurable):
    """A parent class for Configurables that log.

    Subclasses have a log trait, and the default behavior
    is to get the logger from the currently running Application.
    """
    log: Incomplete
CT = t.TypeVar('CT', bound='SingletonConfigurable')

class SingletonConfigurable(LoggingConfigurable):
    """A configurable that only allows one instance.

    This class is for classes that should only have one instance of itself
    or *any* subclass. To create and retrieve such a class use the
    :meth:`SingletonConfigurable.instance` method.
    """
    @classmethod
    def clear_instance(cls) -> None:
        """unset _instance for this class and singleton parents."""
    @classmethod
    def instance(cls, *args: t.Any, **kwargs: t.Any) -> CT:
        """Returns a global instance of this class.

        This method create a new instance if none have previously been created
        and returns a previously created instance is one already exists.

        The arguments and keyword arguments passed to this method are passed
        on to the :meth:`__init__` method of the class upon instantiation.

        Examples
        --------
        Create a singleton class using instance, and retrieve it::

            >>> from traitlets.config.configurable import SingletonConfigurable
            >>> class Foo(SingletonConfigurable): pass
            >>> foo = Foo.instance()
            >>> foo == Foo.instance()
            True

        Create a subclass that is retrieved using the base class instance::

            >>> class Bar(SingletonConfigurable): pass
            >>> class Bam(Bar): pass
            >>> bam = Bam.instance()
            >>> bam == Bar.instance()
            True
        """
    @classmethod
    def initialized(cls) -> bool:
        """Has an instance been created?"""
