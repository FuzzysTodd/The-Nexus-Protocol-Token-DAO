from functorch import functionalize as functionalize
from torch._functorch.batch_norm_replacement import replace_all_batch_norm_modules_ as replace_all_batch_norm_modules_
from torch._functorch.eager_transforms import hessian as hessian, jacfwd as jacfwd, jvp as jvp
from torch._functorch.vmap import chunk_vmap as chunk_vmap
