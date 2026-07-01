from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.base_preprocessing_layer import PreprocessingLayer as PreprocessingLayer
from tensorflow.python.keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers import serialization as serialization
from tensorflow.python.keras.layers.advanced_activations import ELU as ELU, LeakyReLU as LeakyReLU, PReLU as PReLU, ReLU as ReLU, Softmax as Softmax, ThresholdedReLU as ThresholdedReLU
from tensorflow.python.keras.layers.convolutional import Conv1D as Conv1D, Conv1DTranspose as Conv1DTranspose, Conv2D as Conv2D, Conv2DTranspose as Conv2DTranspose, Conv3D as Conv3D, Conv3DTranspose as Conv3DTranspose, Convolution1D as Convolution1D, Convolution2D as Convolution2D, Convolution2DTranspose as Convolution2DTranspose, Convolution3D as Convolution3D, Convolution3DTranspose as Convolution3DTranspose, Cropping1D as Cropping1D, Cropping2D as Cropping2D, Cropping3D as Cropping3D, DepthwiseConv2D as DepthwiseConv2D, SeparableConv1D as SeparableConv1D, SeparableConv2D as SeparableConv2D, SeparableConvolution1D as SeparableConvolution1D, SeparableConvolution2D as SeparableConvolution2D, UpSampling1D as UpSampling1D, UpSampling2D as UpSampling2D, UpSampling3D as UpSampling3D, ZeroPadding1D as ZeroPadding1D, ZeroPadding2D as ZeroPadding2D, ZeroPadding3D as ZeroPadding3D
from tensorflow.python.keras.layers.convolutional_recurrent import ConvLSTM2D as ConvLSTM2D
from tensorflow.python.keras.layers.core import Activation as Activation, ActivityRegularization as ActivityRegularization, Dense as Dense, Dropout as Dropout, Flatten as Flatten, Lambda as Lambda, Masking as Masking, Permute as Permute, RepeatVector as RepeatVector, Reshape as Reshape, SpatialDropout1D as SpatialDropout1D, SpatialDropout2D as SpatialDropout2D, SpatialDropout3D as SpatialDropout3D
from tensorflow.python.keras.layers.cudnn_recurrent import CuDNNGRU as CuDNNGRU, CuDNNLSTM as CuDNNLSTM
from tensorflow.python.keras.layers.dense_attention import AdditiveAttention as AdditiveAttention, Attention as Attention
from tensorflow.python.keras.layers.embeddings import Embedding as Embedding
from tensorflow.python.keras.layers.merge import Add as Add, Average as Average, Concatenate as Concatenate, Dot as Dot, Maximum as Maximum, Minimum as Minimum, Multiply as Multiply, Subtract as Subtract, add as add, average as average, concatenate as concatenate, dot as dot, maximum as maximum, minimum as minimum, multiply as multiply, subtract as subtract
from tensorflow.python.keras.layers.pooling import AveragePooling1D as AveragePooling1D, AveragePooling2D as AveragePooling2D, AveragePooling3D as AveragePooling3D, AvgPool1D as AvgPool1D, AvgPool2D as AvgPool2D, AvgPool3D as AvgPool3D, GlobalAveragePooling1D as GlobalAveragePooling1D, GlobalAveragePooling2D as GlobalAveragePooling2D, GlobalAveragePooling3D as GlobalAveragePooling3D, GlobalAvgPool1D as GlobalAvgPool1D, GlobalAvgPool2D as GlobalAvgPool2D, GlobalAvgPool3D as GlobalAvgPool3D, GlobalMaxPool1D as GlobalMaxPool1D, GlobalMaxPool2D as GlobalMaxPool2D, GlobalMaxPool3D as GlobalMaxPool3D, GlobalMaxPooling1D as GlobalMaxPooling1D, GlobalMaxPooling2D as GlobalMaxPooling2D, GlobalMaxPooling3D as GlobalMaxPooling3D, MaxPool1D as MaxPool1D, MaxPool2D as MaxPool2D, MaxPool3D as MaxPool3D, MaxPooling1D as MaxPooling1D, MaxPooling2D as MaxPooling2D, MaxPooling3D as MaxPooling3D
from tensorflow.python.keras.layers.recurrent import AbstractRNNCell as AbstractRNNCell, GRU as GRU, GRUCell as GRUCell, LSTM as LSTM, LSTMCell as LSTMCell, PeepholeLSTMCell as PeepholeLSTMCell, RNN as RNN, SimpleRNN as SimpleRNN, SimpleRNNCell as SimpleRNNCell, StackedRNNCells as StackedRNNCells
from tensorflow.python.keras.layers.rnn_cell_wrapper_v2 import DeviceWrapper as DeviceWrapper, DropoutWrapper as DropoutWrapper, ResidualWrapper as ResidualWrapper
from tensorflow.python.keras.layers.serialization import deserialize as deserialize, serialize as serialize

GRUV2 = GRU
GRUCellV2 = GRUCell
LSTMV2 = LSTM
LSTMCellV2 = LSTMCell
GRUV1 = GRU
GRUCellV1 = GRUCell
LSTMV1 = LSTM
LSTMCellV1 = LSTMCell

class VersionAwareLayers:
    """Utility to be used internally to access layers in a V1/V2-aware fashion.

  When using layers within the Keras codebase, under the constraint that
  e.g. `layers.BatchNormalization` should be the `BatchNormalization` version
  corresponding to the current runtime (TF1 or TF2), do not simply access
  `layers.BatchNormalization` since it would ignore e.g. an early
  `compat.v2.disable_v2_behavior()` call. Instead, use an instance
  of `VersionAwareLayers` (which you can use just like the `layers` module).
  """
    def __getattr__(self, name): ...
