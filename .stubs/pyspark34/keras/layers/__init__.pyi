from keras.engine.base_layer import Layer as Layer
from keras.engine.base_preprocessing_layer import PreprocessingLayer as PreprocessingLayer
from keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers import serialization as serialization
from keras.layers.activation.elu import ELU as ELU
from keras.layers.activation.leaky_relu import LeakyReLU as LeakyReLU
from keras.layers.activation.prelu import PReLU as PReLU
from keras.layers.activation.relu import ReLU as ReLU
from keras.layers.activation.softmax import Softmax as Softmax
from keras.layers.activation.thresholded_relu import ThresholdedReLU as ThresholdedReLU
from keras.layers.attention.additive_attention import AdditiveAttention as AdditiveAttention
from keras.layers.attention.attention import Attention as Attention
from keras.layers.attention.multi_head_attention import MultiHeadAttention as MultiHeadAttention
from keras.layers.convolutional.conv1d import Conv1D as Conv1D, Convolution1D as Convolution1D
from keras.layers.convolutional.conv1d_transpose import Conv1DTranspose as Conv1DTranspose, Convolution1DTranspose as Convolution1DTranspose
from keras.layers.convolutional.conv2d import Conv2D as Conv2D, Convolution2D as Convolution2D
from keras.layers.convolutional.conv2d_transpose import Conv2DTranspose as Conv2DTranspose, Convolution2DTranspose as Convolution2DTranspose
from keras.layers.convolutional.conv3d import Conv3D as Conv3D, Convolution3D as Convolution3D
from keras.layers.convolutional.conv3d_transpose import Conv3DTranspose as Conv3DTranspose, Convolution3DTranspose as Convolution3DTranspose
from keras.layers.convolutional.depthwise_conv1d import DepthwiseConv1D as DepthwiseConv1D
from keras.layers.convolutional.depthwise_conv2d import DepthwiseConv2D as DepthwiseConv2D
from keras.layers.convolutional.separable_conv1d import SeparableConv1D as SeparableConv1D, SeparableConvolution1D as SeparableConvolution1D
from keras.layers.convolutional.separable_conv2d import SeparableConv2D as SeparableConv2D, SeparableConvolution2D as SeparableConvolution2D
from keras.layers.core.activation import Activation as Activation
from keras.layers.core.dense import Dense as Dense
from keras.layers.core.einsum_dense import EinsumDense as EinsumDense
from keras.layers.core.embedding import Embedding as Embedding
from keras.layers.core.identity import Identity as Identity
from keras.layers.core.lambda_layer import Lambda as Lambda
from keras.layers.core.masking import Masking as Masking
from keras.layers.core.tf_op_layer import ClassMethod as ClassMethod, InstanceMethod as InstanceMethod, InstanceProperty as InstanceProperty, SlicingOpLambda as SlicingOpLambda, TFOpLambda as TFOpLambda
from keras.layers.kernelized import RandomFourierFeatures as RandomFourierFeatures
from keras.layers.locally_connected.locally_connected1d import LocallyConnected1D as LocallyConnected1D
from keras.layers.locally_connected.locally_connected2d import LocallyConnected2D as LocallyConnected2D
from keras.layers.merging.add import Add as Add, add as add
from keras.layers.merging.average import Average as Average, average as average
from keras.layers.merging.concatenate import Concatenate as Concatenate, concatenate as concatenate
from keras.layers.merging.dot import Dot as Dot, dot as dot
from keras.layers.merging.maximum import Maximum as Maximum, maximum as maximum
from keras.layers.merging.minimum import Minimum as Minimum, minimum as minimum
from keras.layers.merging.multiply import Multiply as Multiply, multiply as multiply
from keras.layers.merging.subtract import Subtract as Subtract, subtract as subtract
from keras.layers.normalization.batch_normalization import SyncBatchNormalization as SyncBatchNormalization
from keras.layers.normalization.batch_normalization_v1 import BatchNormalization as BatchNormalization
from keras.layers.normalization.group_normalization import GroupNormalization as GroupNormalization
from keras.layers.normalization.layer_normalization import LayerNormalization as LayerNormalization
from keras.layers.normalization.unit_normalization import UnitNormalization as UnitNormalization
from keras.layers.pooling.average_pooling1d import AveragePooling1D as AveragePooling1D, AvgPool1D as AvgPool1D
from keras.layers.pooling.average_pooling2d import AveragePooling2D as AveragePooling2D, AvgPool2D as AvgPool2D
from keras.layers.pooling.average_pooling3d import AveragePooling3D as AveragePooling3D, AvgPool3D as AvgPool3D
from keras.layers.pooling.global_average_pooling1d import GlobalAveragePooling1D as GlobalAveragePooling1D, GlobalAvgPool1D as GlobalAvgPool1D
from keras.layers.pooling.global_average_pooling2d import GlobalAveragePooling2D as GlobalAveragePooling2D, GlobalAvgPool2D as GlobalAvgPool2D
from keras.layers.pooling.global_average_pooling3d import GlobalAveragePooling3D as GlobalAveragePooling3D, GlobalAvgPool3D as GlobalAvgPool3D
from keras.layers.pooling.global_max_pooling1d import GlobalMaxPool1D as GlobalMaxPool1D, GlobalMaxPooling1D as GlobalMaxPooling1D
from keras.layers.pooling.global_max_pooling2d import GlobalMaxPool2D as GlobalMaxPool2D, GlobalMaxPooling2D as GlobalMaxPooling2D
from keras.layers.pooling.global_max_pooling3d import GlobalMaxPool3D as GlobalMaxPool3D, GlobalMaxPooling3D as GlobalMaxPooling3D
from keras.layers.pooling.max_pooling1d import MaxPool1D as MaxPool1D, MaxPooling1D as MaxPooling1D
from keras.layers.pooling.max_pooling2d import MaxPool2D as MaxPool2D, MaxPooling2D as MaxPooling2D
from keras.layers.pooling.max_pooling3d import MaxPool3D as MaxPool3D, MaxPooling3D as MaxPooling3D
from keras.layers.preprocessing.category_encoding import CategoryEncoding as CategoryEncoding
from keras.layers.preprocessing.discretization import Discretization as Discretization
from keras.layers.preprocessing.hashed_crossing import HashedCrossing as HashedCrossing
from keras.layers.preprocessing.hashing import Hashing as Hashing
from keras.layers.preprocessing.image_preprocessing import CenterCrop as CenterCrop, RandomBrightness as RandomBrightness, RandomContrast as RandomContrast, RandomCrop as RandomCrop, RandomFlip as RandomFlip, RandomHeight as RandomHeight, RandomRotation as RandomRotation, RandomTranslation as RandomTranslation, RandomWidth as RandomWidth, RandomZoom as RandomZoom, Rescaling as Rescaling, Resizing as Resizing
from keras.layers.preprocessing.integer_lookup import IntegerLookup as IntegerLookup
from keras.layers.preprocessing.normalization import Normalization as Normalization
from keras.layers.preprocessing.string_lookup import StringLookup as StringLookup
from keras.layers.preprocessing.text_vectorization import TextVectorization as TextVectorization
from keras.layers.regularization.activity_regularization import ActivityRegularization as ActivityRegularization
from keras.layers.regularization.alpha_dropout import AlphaDropout as AlphaDropout
from keras.layers.regularization.dropout import Dropout as Dropout
from keras.layers.regularization.gaussian_dropout import GaussianDropout as GaussianDropout
from keras.layers.regularization.gaussian_noise import GaussianNoise as GaussianNoise
from keras.layers.regularization.spatial_dropout1d import SpatialDropout1D as SpatialDropout1D
from keras.layers.regularization.spatial_dropout2d import SpatialDropout2D as SpatialDropout2D
from keras.layers.regularization.spatial_dropout3d import SpatialDropout3D as SpatialDropout3D
from keras.layers.reshaping.cropping1d import Cropping1D as Cropping1D
from keras.layers.reshaping.cropping2d import Cropping2D as Cropping2D
from keras.layers.reshaping.cropping3d import Cropping3D as Cropping3D
from keras.layers.reshaping.flatten import Flatten as Flatten
from keras.layers.reshaping.permute import Permute as Permute
from keras.layers.reshaping.repeat_vector import RepeatVector as RepeatVector
from keras.layers.reshaping.reshape import Reshape as Reshape
from keras.layers.reshaping.up_sampling1d import UpSampling1D as UpSampling1D
from keras.layers.reshaping.up_sampling2d import UpSampling2D as UpSampling2D
from keras.layers.reshaping.up_sampling3d import UpSampling3D as UpSampling3D
from keras.layers.reshaping.zero_padding1d import ZeroPadding1D as ZeroPadding1D
from keras.layers.reshaping.zero_padding2d import ZeroPadding2D as ZeroPadding2D
from keras.layers.reshaping.zero_padding3d import ZeroPadding3D as ZeroPadding3D
from keras.layers.rnn.abstract_rnn_cell import AbstractRNNCell as AbstractRNNCell
from keras.layers.rnn.base_rnn import RNN as RNN
from keras.layers.rnn.base_wrapper import Wrapper as Wrapper
from keras.layers.rnn.bidirectional import Bidirectional as Bidirectional
from keras.layers.rnn.cell_wrappers import DeviceWrapper as DeviceWrapper, DropoutWrapper as DropoutWrapper, ResidualWrapper as ResidualWrapper
from keras.layers.rnn.conv_lstm1d import ConvLSTM1D as ConvLSTM1D
from keras.layers.rnn.conv_lstm2d import ConvLSTM2D as ConvLSTM2D
from keras.layers.rnn.conv_lstm3d import ConvLSTM3D as ConvLSTM3D
from keras.layers.rnn.cudnn_gru import CuDNNGRU as CuDNNGRU
from keras.layers.rnn.cudnn_lstm import CuDNNLSTM as CuDNNLSTM
from keras.layers.rnn.gru_v1 import GRU as GRU, GRUCell as GRUCell
from keras.layers.rnn.lstm_v1 import LSTM as LSTM, LSTMCell as LSTMCell
from keras.layers.rnn.simple_rnn import SimpleRNN as SimpleRNN, SimpleRNNCell as SimpleRNNCell
from keras.layers.rnn.stacked_rnn_cells import StackedRNNCells as StackedRNNCells
from keras.layers.rnn.time_distributed import TimeDistributed as TimeDistributed
from keras.layers.serialization import deserialize as deserialize, deserialize_from_json as deserialize_from_json, get_builtin_layer as get_builtin_layer, serialize as serialize

BatchNormalizationV2 = BatchNormalization
BatchNormalizationV1 = BatchNormalization
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
