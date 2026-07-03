from distutils import log as log, sysconfig as sysconfig
from distutils.ccompiler import CCompiler as CCompiler
from distutils.command.build_ext import build_ext as build_ext
from distutils.core import Distribution as Distribution, Extension as Extension
from distutils.dir_util import mkpath as mkpath
from distutils.errors import CompileError as CompileError, DistutilsSetupError as DistutilsSetupError, LinkError as LinkError
from distutils.log import set_threshold as set_threshold, set_verbosity as set_verbosity
