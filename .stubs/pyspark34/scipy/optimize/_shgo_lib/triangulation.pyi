from _typeshed import Incomplete

class Complex:
    dim: Incomplete
    bounds: Incomplete
    symmetry: Incomplete
    gen: int
    perm_cycle: int
    H: Incomplete
    V: Incomplete
    generation_cycle: int
    hgr: Incomplete
    hgrd: int
    performance: Incomplete
    def __init__(self, dim, func, func_args=(), symmetry: bool = False, bounds: Incomplete | None = None, g_cons: Incomplete | None = None, g_args=()) -> None: ...
    def __call__(self): ...
    origin: Incomplete
    supremum: Incomplete
    C0: Incomplete
    def n_cube(self, dim, symmetry: bool = False, printout: bool = False) -> None:
        """
        Generate the simplicial triangulation of the N-D hypercube
        containing 2**n vertices
        """
    def perm(self, i_parents, x_parents, xi) -> None: ...
    def perm_symmetry(self, i_s, x_parents, xi) -> None: ...
    centroid: Incomplete
    centroid_added: bool
    def add_centroid(self) -> None:
        """Split the central edge between the origin and supremum of
        a cell and add the new vertex to the complex"""
    structure: Incomplete
    def incidence(self) -> None: ...
    graph: Incomplete
    def graph_map(self) -> None:
        """ Make a list of size 2**n + 1 where an entry is a vertex
        incidence, each list element contains a list of indexes
        corresponding to that entries neighbors"""
    def sub_generate_cell(self, C_i, gen):
        """Subgenerate a cell `C_i` of generation `gen` and
        homology group rank `hgr`."""
    def split_generation(self):
        """
        Run sub_generate_cell for every cell in the current complex self.gen
        """
    def construct_hypercube(self, origin, supremum, gen, hgr, printout: bool = False):
        """
        Build a hypercube with triangulations symmetric to C0.

        Parameters
        ----------
        origin : vec
        supremum : vec (tuple)
        gen : generation
        hgr : parent homology group rank
        """
    def split_simplex_symmetry(self, S, gen) -> None:
        """
        Split a hypersimplex S into two sub simplices by building a hyperplane
        which connects to a new vertex on an edge (the longest edge in
        dim = {2, 3}) and every other vertex in the simplex that is not
        connected to the edge being split.

        This function utilizes the knowledge that the problem is specified
        with symmetric constraints

        The longest edge is tracked by an ordering of the
        vertices in every simplices, the edge between first and second
        vertex is the longest edge to be split in the next iteration.
        """
    def plot_complex(self) -> None:
        """
             Here, C is the LIST of simplexes S in the
             2- or 3-D complex

             To plot a single simplex S in a set C, use e.g., [C[0]]
        """

class VertexGroup:
    p_gen: Incomplete
    p_hgr: Incomplete
    hg_n: Incomplete
    hg_d: Incomplete
    C: Incomplete
    def __init__(self, p_gen, p_hgr) -> None: ...
    def __call__(self): ...
    def add_vertex(self, V) -> None: ...
    def homology_group_rank(self):
        """
        Returns the homology group order of the current cell
        """
    hgd: Incomplete
    def homology_group_differential(self):
        """
        Returns the difference between the current homology group of the
        cell and its parent group
        """
    def polytopial_sperner_lemma(self) -> None:
        """
        Returns the number of stationary points theoretically contained in the
        cell based information currently known about the cell
        """
    def print_out(self) -> None:
        """
        Print the current cell to console
        """

class Cell(VertexGroup):
    """
    Contains a cell that is symmetric to the initial hypercube triangulation
    """
    origin: Incomplete
    supremum: Incomplete
    centroid: Incomplete
    def __init__(self, p_gen, p_hgr, origin, supremum) -> None: ...

class Simplex(VertexGroup):
    """
    Contains a simplex that is symmetric to the initial symmetry constrained
    hypersimplex triangulation
    """
    generation_cycle: Incomplete
    def __init__(self, p_gen, p_hgr, generation_cycle, dim) -> None: ...

class Vertex:
    x: Incomplete
    order: Incomplete
    x_a: Incomplete
    feasible: bool
    f: Incomplete
    nn: Incomplete
    fval: Incomplete
    check_min: bool
    index: Incomplete
    def __init__(self, x, bounds: Incomplete | None = None, func: Incomplete | None = None, func_args=(), g_cons: Incomplete | None = None, g_cons_args=(), nn: Incomplete | None = None, index: Incomplete | None = None) -> None: ...
    def __hash__(self): ...
    def connect(self, v) -> None: ...
    def disconnect(self, v) -> None: ...
    def minimiser(self):
        """Check whether this vertex is strictly less than all its neighbors"""
    def print_out(self) -> None: ...

class VertexCache:
    cache: Incomplete
    func: Incomplete
    g_cons: Incomplete
    g_cons_args: Incomplete
    func_args: Incomplete
    bounds: Incomplete
    nfev: int
    size: int
    index: int
    def __init__(self, func, func_args=(), bounds: Incomplete | None = None, g_cons: Incomplete | None = None, g_cons_args=(), indexed: bool = True) -> None: ...
    def __getitem__(self, x, indexed: bool = True): ...
