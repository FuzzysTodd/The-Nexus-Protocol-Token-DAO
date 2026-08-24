import jax
import jax.numpy as jnp
import typing

class Rotation(typing.NamedTuple):
    """Rotation in 3 dimensions."""
    quat: jax.Array
    @classmethod
    def concatenate(cls, rotations: typing.Sequence):
        """Concatenate a sequence of `Rotation` objects."""
    @classmethod
    def from_euler(cls, seq: str, angles: jax.Array, degrees: bool = False):
        """Initialize from Euler angles."""
    @classmethod
    def from_matrix(cls, matrix: jax.Array):
        """Initialize from rotation matrix."""
    @classmethod
    def from_mrp(cls, mrp: jax.Array):
        """Initialize from Modified Rodrigues Parameters (MRPs)."""
    @classmethod
    def from_quat(cls, quat: jax.Array):
        """Initialize from quaternions."""
    @classmethod
    def from_rotvec(cls, rotvec: jax.Array, degrees: bool = False):
        """Initialize from rotation vectors."""
    @classmethod
    def identity(cls, num: int | None = None, dtype=...):
        """Get identity rotation(s)."""
    @classmethod
    def random(cls, random_key: jax.Array, num: int | None = None):
        """Generate uniformly distributed rotations."""
    def __getitem__(self, indexer):
        """Extract rotation(s) at given index(es) from object."""
    def __len__(self) -> int:
        """Number of rotations contained in this object."""
    def __mul__(self, other):
        """Compose this rotation with the other."""
    def apply(self, vectors: jax.Array, inverse: bool = False) -> jax.Array:
        """Apply this rotation to one or more vectors."""
    def as_euler(self, seq: str, degrees: bool = False):
        """Represent as Euler angles."""
    def as_matrix(self) -> jax.Array:
        """Represent as rotation matrix."""
    def as_mrp(self) -> jax.Array:
        """Represent as Modified Rodrigues Parameters (MRPs)."""
    def as_rotvec(self, degrees: bool = False) -> jax.Array:
        """Represent as rotation vectors."""
    def as_quat(self) -> jax.Array:
        """Represent as quaternions."""
    def inv(self):
        """Invert this rotation."""
    def magnitude(self) -> jax.Array:
        """Get the magnitude(s) of the rotation(s)."""
    def mean(self, weights: jax.Array | None = None):
        """Get the mean of the rotations."""
    @property
    def single(self) -> bool:
        """Whether this instance represents a single rotation."""

class Slerp(typing.NamedTuple):
    """Spherical Linear Interpolation of Rotations."""
    times: jnp.ndarray
    timedelta: jnp.ndarray
    rotations: Rotation
    rotvecs: jnp.ndarray
    @classmethod
    def init(cls, times: jax.Array, rotations: Rotation): ...
    def __call__(self, times: jax.Array):
        """Interpolate rotations."""
