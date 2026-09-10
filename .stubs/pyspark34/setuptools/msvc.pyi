from _typeshed import Incomplete
from setuptools.extern.more_itertools import unique_everseen as unique_everseen

class winreg:
    HKEY_USERS: Incomplete
    HKEY_CURRENT_USER: Incomplete
    HKEY_LOCAL_MACHINE: Incomplete
    HKEY_CLASSES_ROOT: Incomplete

PLAT_SPEC_TO_RUNTIME: Incomplete

def msvc14_get_vc_env(plat_spec):
    '''
    Patched "distutils._msvccompiler._get_vc_env" for support extra
    Microsoft Visual C++ 14.X compilers.

    Set environment without use of "vcvarsall.bat".

    Parameters
    ----------
    plat_spec: str
        Target architecture.

    Return
    ------
    dict
        environment
    '''

class PlatformInfo:
    """
    Current and Target Architectures information.

    Parameters
    ----------
    arch: str
        Target architecture.
    """
    current_cpu: Incomplete
    arch: Incomplete
    def __init__(self, arch) -> None: ...
    @property
    def target_cpu(self):
        """
        Return Target CPU architecture.

        Return
        ------
        str
            Target CPU
        """
    def target_is_x86(self):
        """
        Return True if target CPU is x86 32 bits..

        Return
        ------
        bool
            CPU is x86 32 bits
        """
    def current_is_x86(self):
        """
        Return True if current CPU is x86 32 bits..

        Return
        ------
        bool
            CPU is x86 32 bits
        """
    def current_dir(self, hidex86: bool = False, x64: bool = False):
        """
        Current platform specific subfolder.

        Parameters
        ----------
        hidex86: bool
            return '' and not '\x86' if architecture is x86.
        x64: bool
            return 'd' and not '\x07md64' if architecture is amd64.

        Return
        ------
        str
            subfolder: '\target', or '' (see hidex86 parameter)
        """
    def target_dir(self, hidex86: bool = False, x64: bool = False):
        """
        Target platform specific subfolder.

        Parameters
        ----------
        hidex86: bool
            return '' and not '\\x86' if architecture is x86.
        x64: bool
            return '\\x64' and not '\\amd64' if architecture is amd64.

        Return
        ------
        str
            subfolder: '\\current', or '' (see hidex86 parameter)
        """
    def cross_dir(self, forcex86: bool = False):
        """
        Cross platform specific subfolder.

        Parameters
        ----------
        forcex86: bool
            Use 'x86' as current architecture even if current architecture is
            not x86.

        Return
        ------
        str
            subfolder: '' if target architecture is current architecture,
            '\\current_target' if not.
        """

class RegistryInfo:
    '''
    Microsoft Visual Studio related registry information.

    Parameters
    ----------
    platform_info: PlatformInfo
        "PlatformInfo" instance.
    '''
    HKEYS: Incomplete
    pi: Incomplete
    def __init__(self, platform_info) -> None: ...
    @property
    def visualstudio(self):
        """
        Microsoft Visual Studio root registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def sxs(self):
        """
        Microsoft Visual Studio SxS registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def vc(self):
        """
        Microsoft Visual C++ VC7 registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def vs(self):
        """
        Microsoft Visual Studio VS7 registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def vc_for_python(self):
        """
        Microsoft Visual C++ for Python registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def microsoft_sdk(self):
        """
        Microsoft SDK registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def windows_sdk(self):
        """
        Microsoft Windows/Platform SDK registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def netfx_sdk(self):
        """
        Microsoft .NET Framework SDK registry key.

        Return
        ------
        str
            Registry key
        """
    @property
    def windows_kits_roots(self):
        """
        Microsoft Windows Kits Roots registry key.

        Return
        ------
        str
            Registry key
        """
    def microsoft(self, key, x86: bool = False):
        """
        Return key in Microsoft software registry.

        Parameters
        ----------
        key: str
            Registry key path where look.
        x86: str
            Force x86 software registry.

        Return
        ------
        str
            Registry key
        """
    def lookup(self, key, name):
        """
        Look for values in registry in Microsoft software registry.

        Parameters
        ----------
        key: str
            Registry key path where look.
        name: str
            Value name to find.

        Return
        ------
        str
            value
        """

class SystemInfo:
    '''
    Microsoft Windows and Visual Studio related system information.

    Parameters
    ----------
    registry_info: RegistryInfo
        "RegistryInfo" instance.
    vc_ver: float
        Required Microsoft Visual C++ version.
    '''
    WinDir: Incomplete
    ProgramFiles: Incomplete
    ProgramFilesx86: Incomplete
    ri: Incomplete
    pi: Incomplete
    known_vs_paths: Incomplete
    vs_ver: Incomplete
    def __init__(self, registry_info, vc_ver: Incomplete | None = None) -> None: ...
    def find_reg_vs_vers(self):
        """
        Find Microsoft Visual Studio versions available in registry.

        Return
        ------
        list of float
            Versions
        """
    def find_programdata_vs_vers(self):
        '''
        Find Visual studio 2017+ versions from information in
        "C:\\ProgramData\\Microsoft\\VisualStudio\\Packages\\_Instances".

        Return
        ------
        dict
            float version as key, path as value.
        '''
    @property
    def VSInstallDir(self):
        """
        Microsoft Visual Studio directory.

        Return
        ------
        str
            path
        """
    @property
    def VCInstallDir(self):
        """
        Microsoft Visual C++ directory.

        Return
        ------
        str
            path
        """
    @property
    def WindowsSdkVersion(self):
        """
        Microsoft Windows SDK versions for specified MSVC++ version.

        Return
        ------
        tuple of str
            versions
        """
    @property
    def WindowsSdkLastVersion(self):
        """
        Microsoft Windows SDK last version.

        Return
        ------
        str
            version
        """
    @property
    def WindowsSdkDir(self):
        """
        Microsoft Windows SDK directory.

        Return
        ------
        str
            path
        """
    @property
    def WindowsSDKExecutablePath(self):
        """
        Microsoft Windows SDK executable directory.

        Return
        ------
        str
            path
        """
    @property
    def FSharpInstallDir(self):
        """
        Microsoft Visual F# directory.

        Return
        ------
        str
            path
        """
    @property
    def UniversalCRTSdkDir(self):
        """
        Microsoft Universal CRT SDK directory.

        Return
        ------
        str
            path
        """
    @property
    def UniversalCRTSdkLastVersion(self):
        """
        Microsoft Universal C Runtime SDK last version.

        Return
        ------
        str
            version
        """
    @property
    def NetFxSdkVersion(self):
        """
        Microsoft .NET Framework SDK versions.

        Return
        ------
        tuple of str
            versions
        """
    @property
    def NetFxSdkDir(self):
        """
        Microsoft .NET Framework SDK directory.

        Return
        ------
        str
            path
        """
    @property
    def FrameworkDir32(self):
        """
        Microsoft .NET Framework 32bit directory.

        Return
        ------
        str
            path
        """
    @property
    def FrameworkDir64(self):
        """
        Microsoft .NET Framework 64bit directory.

        Return
        ------
        str
            path
        """
    @property
    def FrameworkVersion32(self):
        """
        Microsoft .NET Framework 32bit versions.

        Return
        ------
        tuple of str
            versions
        """
    @property
    def FrameworkVersion64(self):
        """
        Microsoft .NET Framework 64bit versions.

        Return
        ------
        tuple of str
            versions
        """

class EnvironmentInfo:
    '''
    Return environment variables for specified Microsoft Visual C++ version
    and platform : Lib, Include, Path and libpath.

    This function is compatible with Microsoft Visual C++ 9.0 to 14.X.

    Script created by analysing Microsoft environment configuration files like
    "vcvars[...].bat", "SetEnv.Cmd", "vcbuildtools.bat", ...

    Parameters
    ----------
    arch: str
        Target architecture.
    vc_ver: float
        Required Microsoft Visual C++ version. If not set, autodetect the last
        version.
    vc_min_ver: float
        Minimum Microsoft Visual C++ version.
    '''
    pi: Incomplete
    ri: Incomplete
    si: Incomplete
    def __init__(self, arch, vc_ver: Incomplete | None = None, vc_min_ver: int = 0) -> None: ...
    @property
    def vs_ver(self):
        """
        Microsoft Visual Studio.

        Return
        ------
        float
            version
        """
    @property
    def vc_ver(self):
        """
        Microsoft Visual C++ version.

        Return
        ------
        float
            version
        """
    @property
    def VSTools(self):
        """
        Microsoft Visual Studio Tools.

        Return
        ------
        list of str
            paths
        """
    @property
    def VCIncludes(self):
        """
        Microsoft Visual C++ & Microsoft Foundation Class Includes.

        Return
        ------
        list of str
            paths
        """
    @property
    def VCLibraries(self):
        """
        Microsoft Visual C++ & Microsoft Foundation Class Libraries.

        Return
        ------
        list of str
            paths
        """
    @property
    def VCStoreRefs(self):
        """
        Microsoft Visual C++ store references Libraries.

        Return
        ------
        list of str
            paths
        """
    @property
    def VCTools(self):
        """
        Microsoft Visual C++ Tools.

        Return
        ------
        list of str
            paths
        """
    @property
    def OSLibraries(self):
        """
        Microsoft Windows SDK Libraries.

        Return
        ------
        list of str
            paths
        """
    @property
    def OSIncludes(self):
        """
        Microsoft Windows SDK Include.

        Return
        ------
        list of str
            paths
        """
    @property
    def OSLibpath(self):
        """
        Microsoft Windows SDK Libraries Paths.

        Return
        ------
        list of str
            paths
        """
    @property
    def SdkTools(self):
        """
        Microsoft Windows SDK Tools.

        Return
        ------
        list of str
            paths
        """
    @property
    def SdkSetup(self):
        """
        Microsoft Windows SDK Setup.

        Return
        ------
        list of str
            paths
        """
    @property
    def FxTools(self):
        """
        Microsoft .NET Framework Tools.

        Return
        ------
        list of str
            paths
        """
    @property
    def NetFxSDKLibraries(self):
        """
        Microsoft .Net Framework SDK Libraries.

        Return
        ------
        list of str
            paths
        """
    @property
    def NetFxSDKIncludes(self):
        """
        Microsoft .Net Framework SDK Includes.

        Return
        ------
        list of str
            paths
        """
    @property
    def VsTDb(self):
        """
        Microsoft Visual Studio Team System Database.

        Return
        ------
        list of str
            paths
        """
    @property
    def MSBuild(self):
        """
        Microsoft Build Engine.

        Return
        ------
        list of str
            paths
        """
    @property
    def HTMLHelpWorkshop(self):
        """
        Microsoft HTML Help Workshop.

        Return
        ------
        list of str
            paths
        """
    @property
    def UCRTLibraries(self):
        """
        Microsoft Universal C Runtime SDK Libraries.

        Return
        ------
        list of str
            paths
        """
    @property
    def UCRTIncludes(self):
        """
        Microsoft Universal C Runtime SDK Include.

        Return
        ------
        list of str
            paths
        """
    @property
    def FSharp(self):
        """
        Microsoft Visual F#.

        Return
        ------
        list of str
            paths
        """
    @property
    def VCRuntimeRedist(self):
        """
        Microsoft Visual C++ runtime redistributable dll.

        Return
        ------
        str
            path
        """
    def return_env(self, exists: bool = True):
        """
        Return environment dict.

        Parameters
        ----------
        exists: bool
            It True, only return existing paths.

        Return
        ------
        dict
            environment
        """
