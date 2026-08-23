from enum import Enum

class CommandType(Enum):
    Initialize: bytes
    RequestTrialJobs: bytes
    ReportMetricData: bytes
    ReportGpuInfo: bytes
    UpdateSearchSpace: bytes
    ImportData: bytes
    AddCustomizedTrialJob: bytes
    TrialEnd: bytes
    Terminate: bytes
    Ping: bytes
    Initialized: bytes
    NewTrialJob: bytes
    SendTrialJobParameter: bytes
    NoMoreTrialJobs: bytes
    KillTrialJob: bytes
    StdOut: bytes
    VersionCheck: bytes
