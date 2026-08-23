from pip._internal.distributions.base import AbstractDistribution as AbstractDistribution
from pip._internal.distributions.sdist import SourceDistribution as SourceDistribution
from pip._internal.distributions.wheel import WheelDistribution as WheelDistribution
from pip._internal.req.req_install import InstallRequirement as InstallRequirement

def make_distribution_for_install_requirement(install_req: InstallRequirement) -> AbstractDistribution:
    """Returns a Distribution for the given InstallRequirement"""
