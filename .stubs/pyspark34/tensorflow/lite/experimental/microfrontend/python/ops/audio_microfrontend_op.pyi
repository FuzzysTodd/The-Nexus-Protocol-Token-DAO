from tensorflow.lite.experimental.microfrontend.ops import gen_audio_microfrontend_op as gen_audio_microfrontend_op
from tensorflow.python.framework import dtypes as dtypes, load_library as load_library, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.platform import resource_loader as resource_loader
from tensorflow.python.util.tf_export import tf_export as tf_export

def audio_microfrontend(audio, sample_rate: int = 16000, window_size: int = 25, window_step: int = 10, num_channels: int = 32, upper_band_limit: float = 7500.0, lower_band_limit: float = 125.0, smoothing_bits: int = 10, even_smoothing: float = 0.025, odd_smoothing: float = 0.06, min_signal_remaining: float = 0.05, enable_pcan: bool = True, pcan_strength: float = 0.95, pcan_offset: float = 80.0, gain_bits: int = 21, enable_log: bool = True, scale_shift: int = 6, left_context: int = 0, right_context: int = 0, frame_stride: int = 1, zero_padding: bool = False, out_scale: int = 1, out_type=...):
    """Audio Microfrontend Op.

  This Op converts a sequence of audio data into one or more
  feature vectors containing filterbanks of the input. The
  conversion process uses a lightweight library to perform:

  1. A slicing window function
  2. Short-time FFTs
  3. Filterbank calculations
  4. Noise reduction
  5. PCAN Auto Gain Control
  6. Logarithmic scaling

  Args:
    audio: 1D Tensor, int16 audio data in temporal ordering.
    sample_rate: Integer, the sample rate of the audio in Hz.
    window_size: Integer, length of desired time frames in ms.
    window_step: Integer, length of step size for the next frame in ms.
    num_channels: Integer, the number of filterbank channels to use.
    upper_band_limit: Float, the highest frequency included in the filterbanks.
    lower_band_limit: Float, the lowest frequency included in the filterbanks.
    smoothing_bits: Int, scale up signal by 2^(smoothing_bits) before reduction.
    even_smoothing: Float, smoothing coefficient for even-numbered channels.
    odd_smoothing: Float, smoothing coefficient for odd-numbered channels.
    min_signal_remaining: Float, fraction of signal to preserve in smoothing.
    enable_pcan: Bool, enable PCAN auto gain control.
    pcan_strength: Float, gain normalization exponent.
    pcan_offset: Float, positive value added in the normalization denominator.
    gain_bits: Int, number of fractional bits in the gain.
    enable_log: Bool, enable logarithmic scaling of filterbanks.
    scale_shift: Integer, scale filterbanks by 2^(scale_shift).
    left_context: Integer, number of preceding frames to attach to each frame.
    right_context: Integer, number of preceding frames to attach to each frame.
    frame_stride: Integer, M frames to skip over, where output[n] = frame[n*M].
    zero_padding: Bool, if left/right context is out-of-bounds, attach frame of
      zeroes. Otherwise, frame[0] or frame[size-1] will be copied.
    out_scale: Integer, divide all filterbanks by this number.
    out_type: DType, type of the output Tensor, defaults to UINT16.

  Returns:
    filterbanks: 2D Tensor, each row is a time frame, each column is a channel.

  Raises:
    ValueError: If the audio tensor is not explicitly a vector.
  """
