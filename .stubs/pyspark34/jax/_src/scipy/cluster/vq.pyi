from jax import vmap as vmap
from jax._src.numpy.util import check_arraylike as check_arraylike, promote_dtypes_inexact as promote_dtypes_inexact

def vq(obs, code_book, check_finite: bool = True): ...
