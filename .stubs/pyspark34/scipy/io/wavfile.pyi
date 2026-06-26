from enum import IntEnum

__all__ = ['WavFileWarning', 'read', 'write']

class WavFileWarning(UserWarning): ...

class WAVE_FORMAT(IntEnum):
    """
    WAVE form wFormatTag IDs

    Complete list is in mmreg.h in Windows 10 SDK.  ALAC and OPUS are the
    newest additions, in v10.0.14393 2016-07
    """
    UNKNOWN: int
    PCM: int
    ADPCM: int
    IEEE_FLOAT: int
    VSELP: int
    IBM_CVSD: int
    ALAW: int
    MULAW: int
    DTS: int
    DRM: int
    WMAVOICE9: int
    WMAVOICE10: int
    OKI_ADPCM: int
    DVI_ADPCM: int
    IMA_ADPCM: int
    MEDIASPACE_ADPCM: int
    SIERRA_ADPCM: int
    G723_ADPCM: int
    DIGISTD: int
    DIGIFIX: int
    DIALOGIC_OKI_ADPCM: int
    MEDIAVISION_ADPCM: int
    CU_CODEC: int
    HP_DYN_VOICE: int
    YAMAHA_ADPCM: int
    SONARC: int
    DSPGROUP_TRUESPEECH: int
    ECHOSC1: int
    AUDIOFILE_AF36: int
    APTX: int
    AUDIOFILE_AF10: int
    PROSODY_1612: int
    LRC: int
    DOLBY_AC2: int
    GSM610: int
    MSNAUDIO: int
    ANTEX_ADPCME: int
    CONTROL_RES_VQLPC: int
    DIGIREAL: int
    DIGIADPCM: int
    CONTROL_RES_CR10: int
    NMS_VBXADPCM: int
    CS_IMAADPCM: int
    ECHOSC3: int
    ROCKWELL_ADPCM: int
    ROCKWELL_DIGITALK: int
    XEBEC: int
    G721_ADPCM: int
    G728_CELP: int
    MSG723: int
    INTEL_G723_1: int
    INTEL_G729: int
    SHARP_G726: int
    MPEG: int
    RT24: int
    PAC: int
    MPEGLAYER3: int
    LUCENT_G723: int
    CIRRUS: int
    ESPCM: int
    VOXWARE: int
    CANOPUS_ATRAC: int
    G726_ADPCM: int
    G722_ADPCM: int
    DSAT: int
    DSAT_DISPLAY: int
    VOXWARE_BYTE_ALIGNED: int
    VOXWARE_AC8: int
    VOXWARE_AC10: int
    VOXWARE_AC16: int
    VOXWARE_AC20: int
    VOXWARE_RT24: int
    VOXWARE_RT29: int
    VOXWARE_RT29HW: int
    VOXWARE_VR12: int
    VOXWARE_VR18: int
    VOXWARE_TQ40: int
    VOXWARE_SC3: int
    VOXWARE_SC3_1: int
    SOFTSOUND: int
    VOXWARE_TQ60: int
    MSRT24: int
    G729A: int
    MVI_MVI2: int
    DF_G726: int
    DF_GSM610: int
    ISIAUDIO: int
    ONLIVE: int
    MULTITUDE_FT_SX20: int
    INFOCOM_ITS_G721_ADPCM: int
    CONVEDIA_G729: int
    CONGRUENCY: int
    SBC24: int
    DOLBY_AC3_SPDIF: int
    MEDIASONIC_G723: int
    PROSODY_8KBPS: int
    ZYXEL_ADPCM: int
    PHILIPS_LPCBB: int
    PACKED: int
    MALDEN_PHONYTALK: int
    RACAL_RECORDER_GSM: int
    RACAL_RECORDER_G720_A: int
    RACAL_RECORDER_G723_1: int
    RACAL_RECORDER_TETRA_ACELP: int
    NEC_AAC: int
    RAW_AAC1: int
    RHETOREX_ADPCM: int
    IRAT: int
    VIVO_G723: int
    VIVO_SIREN: int
    PHILIPS_CELP: int
    PHILIPS_GRUNDIG: int
    DIGITAL_G723: int
    SANYO_LD_ADPCM: int
    SIPROLAB_ACEPLNET: int
    SIPROLAB_ACELP4800: int
    SIPROLAB_ACELP8V3: int
    SIPROLAB_G729: int
    SIPROLAB_G729A: int
    SIPROLAB_KELVIN: int
    VOICEAGE_AMR: int
    G726ADPCM: int
    DICTAPHONE_CELP68: int
    DICTAPHONE_CELP54: int
    QUALCOMM_PUREVOICE: int
    QUALCOMM_HALFRATE: int
    TUBGSM: int
    MSAUDIO1: int
    WMAUDIO2: int
    WMAUDIO3: int
    WMAUDIO_LOSSLESS: int
    WMASPDIF: int
    UNISYS_NAP_ADPCM: int
    UNISYS_NAP_ULAW: int
    UNISYS_NAP_ALAW: int
    UNISYS_NAP_16K: int
    SYCOM_ACM_SYC008: int
    SYCOM_ACM_SYC701_G726L: int
    SYCOM_ACM_SYC701_CELP54: int
    SYCOM_ACM_SYC701_CELP68: int
    KNOWLEDGE_ADVENTURE_ADPCM: int
    FRAUNHOFER_IIS_MPEG2_AAC: int
    DTS_DS: int
    CREATIVE_ADPCM: int
    CREATIVE_FASTSPEECH8: int
    CREATIVE_FASTSPEECH10: int
    UHER_ADPCM: int
    ULEAD_DV_AUDIO: int
    ULEAD_DV_AUDIO_1: int
    QUARTERDECK: int
    ILINK_VC: int
    RAW_SPORT: int
    ESST_AC3: int
    GENERIC_PASSTHRU: int
    IPI_HSX: int
    IPI_RPELP: int
    CS2: int
    SONY_SCX: int
    SONY_SCY: int
    SONY_ATRAC3: int
    SONY_SPC: int
    TELUM_AUDIO: int
    TELUM_IA_AUDIO: int
    NORCOM_VOICE_SYSTEMS_ADPCM: int
    FM_TOWNS_SND: int
    MICRONAS: int
    MICRONAS_CELP833: int
    BTV_DIGITAL: int
    INTEL_MUSIC_CODER: int
    INDEO_AUDIO: int
    QDESIGN_MUSIC: int
    ON2_VP7_AUDIO: int
    ON2_VP6_AUDIO: int
    VME_VMPCM: int
    TPC: int
    LIGHTWAVE_LOSSLESS: int
    OLIGSM: int
    OLIADPCM: int
    OLICELP: int
    OLISBC: int
    OLIOPR: int
    LH_CODEC: int
    LH_CODEC_CELP: int
    LH_CODEC_SBC8: int
    LH_CODEC_SBC12: int
    LH_CODEC_SBC16: int
    NORRIS: int
    ISIAUDIO_2: int
    SOUNDSPACE_MUSICOMPRESS: int
    MPEG_ADTS_AAC: int
    MPEG_RAW_AAC: int
    MPEG_LOAS: int
    NOKIA_MPEG_ADTS_AAC: int
    NOKIA_MPEG_RAW_AAC: int
    VODAFONE_MPEG_ADTS_AAC: int
    VODAFONE_MPEG_RAW_AAC: int
    MPEG_HEAAC: int
    VOXWARE_RT24_SPEECH: int
    SONICFOUNDRY_LOSSLESS: int
    INNINGS_TELECOM_ADPCM: int
    LUCENT_SX8300P: int
    LUCENT_SX5363S: int
    CUSEEME: int
    NTCSOFT_ALF2CM_ACM: int
    DVM: int
    DTS2: int
    MAKEAVIS: int
    DIVIO_MPEG4_AAC: int
    NOKIA_ADAPTIVE_MULTIRATE: int
    DIVIO_G726: int
    LEAD_SPEECH: int
    LEAD_VORBIS: int
    WAVPACK_AUDIO: int
    OGG_VORBIS_MODE_1: int
    OGG_VORBIS_MODE_2: int
    OGG_VORBIS_MODE_3: int
    OGG_VORBIS_MODE_1_PLUS: int
    OGG_VORBIS_MODE_2_PLUS: int
    OGG_VORBIS_MODE_3_PLUS: int
    ALAC: int
    OPUS: int
    FAAD_AAC: int
    AMR_NB: int
    AMR_WB: int
    AMR_WP: int
    GSM_AMR_CBR: int
    GSM_AMR_VBR_SID: int
    COMVERSE_INFOSYS_G723_1: int
    COMVERSE_INFOSYS_AVQSBC: int
    COMVERSE_INFOSYS_SBC: int
    SYMBOL_G729_A: int
    VOICEAGE_AMR_WB: int
    INGENIENT_G726: int
    MPEG4_AAC: int
    ENCORE_G726: int
    ZOLL_ASAO: int
    SPEEX_VOICE: int
    VIANIX_MASC: int
    WM9_SPECTRUM_ANALYZER: int
    WMF_SPECTRUM_ANAYZER: int
    GSM_610: int
    GSM_620: int
    GSM_660: int
    GSM_690: int
    GSM_ADAPTIVE_MULTIRATE_WB: int
    POLYCOM_G722: int
    POLYCOM_G728: int
    POLYCOM_G729_A: int
    POLYCOM_SIREN: int
    GLOBAL_IP_ILBC: int
    RADIOTIME_TIME_SHIFT_RADIO: int
    NICE_ACA: int
    NICE_ADPCM: int
    VOCORD_G721: int
    VOCORD_G726: int
    VOCORD_G722_1: int
    VOCORD_G728: int
    VOCORD_G729: int
    VOCORD_G729_A: int
    VOCORD_G723_1: int
    VOCORD_LBC: int
    NICE_G728: int
    FRACE_TELECOM_G729: int
    CODIAN: int
    FLAC: int
    EXTENSIBLE: int
    DEVELOPMENT: int

def read(filename, mmap: bool = False):
    '''
    Open a WAV file.

    Return the sample rate (in samples/sec) and data from an LPCM WAV file.

    Parameters
    ----------
    filename : string or open file handle
        Input WAV file.
    mmap : bool, optional
        Whether to read data as memory-mapped (default: False).  Not compatible
        with some bit depths; see Notes.  Only to be used on real files.

        .. versionadded:: 0.12.0

    Returns
    -------
    rate : int
        Sample rate of WAV file.
    data : numpy array
        Data read from WAV file. Data-type is determined from the file;
        see Notes.  Data is 1-D for 1-channel WAV, or 2-D of shape
        (Nsamples, Nchannels) otherwise. If a file-like input without a
        C-like file descriptor (e.g., :class:`python:io.BytesIO`) is
        passed, this will not be writeable.

    Notes
    -----
    Common data types: [1]_

    =====================  ===========  ===========  =============
         WAV format            Min          Max       NumPy dtype
    =====================  ===========  ===========  =============
    32-bit floating-point  -1.0         +1.0         float32
    32-bit integer PCM     -2147483648  +2147483647  int32
    24-bit integer PCM     -2147483648  +2147483392  int32
    16-bit integer PCM     -32768       +32767       int16
    8-bit integer PCM      0            255          uint8
    =====================  ===========  ===========  =============

    WAV files can specify arbitrary bit depth, and this function supports
    reading any integer PCM depth from 1 to 64 bits.  Data is returned in the
    smallest compatible numpy int type, in left-justified format.  8-bit and
    lower is unsigned, while 9-bit and higher is signed.

    For example, 24-bit data will be stored as int32, with the MSB of the
    24-bit data stored at the MSB of the int32, and typically the least
    significant byte is 0x00.  (However, if a file actually contains data past
    its specified bit depth, those bits will be read and output, too. [2]_)

    This bit justification and sign matches WAV\'s native internal format, which
    allows memory mapping of WAV files that use 1, 2, 4, or 8 bytes per sample
    (so 24-bit files cannot be memory-mapped, but 32-bit can).

    IEEE float PCM in 32- or 64-bit format is supported, with or without mmap.
    Values exceeding [-1, +1] are not clipped.

    Non-linear PCM (mu-law, A-law) is not supported.

    References
    ----------
    .. [1] IBM Corporation and Microsoft Corporation, "Multimedia Programming
       Interface and Data Specifications 1.0", section "Data Format of the
       Samples", August 1991
       http://www.tactilemedia.com/info/MCI_Control_Info.html
    .. [2] Adobe Systems Incorporated, "Adobe Audition 3 User Guide", section
       "Audio file formats: 24-bit Packed Int (type 1, 20-bit)", 2007

    Examples
    --------
    >>> from os.path import dirname, join as pjoin
    >>> from scipy.io import wavfile
    >>> import scipy.io

    Get the filename for an example .wav file from the tests/data directory.

    >>> data_dir = pjoin(dirname(scipy.io.__file__), \'tests\', \'data\')
    >>> wav_fname = pjoin(data_dir, \'test-44100Hz-2ch-32bit-float-be.wav\')

    Load the .wav file contents.

    >>> samplerate, data = wavfile.read(wav_fname)
    >>> print(f"number of channels = {data.shape[1]}")
    number of channels = 2
    >>> length = data.shape[0] / samplerate
    >>> print(f"length = {length}s")
    length = 0.01s

    Plot the waveform.

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> time = np.linspace(0., length, data.shape[0])
    >>> plt.plot(time, data[:, 0], label="Left channel")
    >>> plt.plot(time, data[:, 1], label="Right channel")
    >>> plt.legend()
    >>> plt.xlabel("Time [s]")
    >>> plt.ylabel("Amplitude")
    >>> plt.show()

    '''
def write(filename, rate, data) -> None:
    '''
    Write a NumPy array as a WAV file.

    Parameters
    ----------
    filename : string or open file handle
        Output wav file.
    rate : int
        The sample rate (in samples/sec).
    data : ndarray
        A 1-D or 2-D NumPy array of either integer or float data-type.

    Notes
    -----
    * Writes a simple uncompressed WAV file.
    * To write multiple-channels, use a 2-D array of shape
      (Nsamples, Nchannels).
    * The bits-per-sample and PCM/float will be determined by the data-type.

    Common data types: [1]_

    =====================  ===========  ===========  =============
         WAV format            Min          Max       NumPy dtype
    =====================  ===========  ===========  =============
    32-bit floating-point  -1.0         +1.0         float32
    32-bit PCM             -2147483648  +2147483647  int32
    16-bit PCM             -32768       +32767       int16
    8-bit PCM              0            255          uint8
    =====================  ===========  ===========  =============

    Note that 8-bit PCM is unsigned.

    References
    ----------
    .. [1] IBM Corporation and Microsoft Corporation, "Multimedia Programming
       Interface and Data Specifications 1.0", section "Data Format of the
       Samples", August 1991
       http://www.tactilemedia.com/info/MCI_Control_Info.html

    Examples
    --------
    Create a 100Hz sine wave, sampled at 44100Hz.
    Write to 16-bit PCM, Mono.

    >>> from scipy.io.wavfile import write
    >>> import numpy as np
    >>> samplerate = 44100; fs = 100
    >>> t = np.linspace(0., 1., samplerate)
    >>> amplitude = np.iinfo(np.int16).max
    >>> data = amplitude * np.sin(2. * np.pi * fs * t)
    >>> write("example.wav", samplerate, data.astype(np.int16))

    '''
