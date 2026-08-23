__all__ = ['__upcast_float16_array', '__downcast_float128_array']

def __upcast_float16_array(x):
    """
    Used in _scipy_fft to upcast float16 to float32, 
    instead of float64, as mkl_fft would do"""
def __downcast_float128_array(x):
    """
    Used in _numpy_fft to unsafely downcast float128/complex256 to 
    complex128, instead of raising an error"""
