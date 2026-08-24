from _typeshed import Incomplete

def starargs(f):
    """decorator to convert a many-arg function to a single-arg function"""
def random_seed(s: Incomplete | None = None) -> None:
    """sets the seed for calls to 'random()'"""
def random_state(module: str = 'random', new: bool = False, seed: str = '!'):
    """return a (optionally manually seeded) random generator

For a given module, return an object that has random number generation (RNG)
methods available.  If new=False, use the global copy of the RNG object.
If seed='!', do not reseed the RNG (using seed=None 'removes' any seeding).
If seed='*', use a seed that depends on the process id (PID); this is useful
for building RNGs that are different across multiple threads or processes.
    """
