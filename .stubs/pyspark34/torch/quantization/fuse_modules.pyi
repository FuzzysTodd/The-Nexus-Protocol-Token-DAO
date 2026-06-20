from torch.ao.quantization.fuse_modules import fuse_known_modules as fuse_known_modules, fuse_modules as fuse_modules, get_fuser_method as get_fuser_method
from torch.ao.quantization.fuser_method_mappings import fuse_conv_bn as fuse_conv_bn, fuse_conv_bn_relu as fuse_conv_bn_relu
