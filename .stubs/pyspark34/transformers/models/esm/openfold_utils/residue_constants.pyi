import numpy as np
from _typeshed import Incomplete
from typing import Dict, List, Mapping, NamedTuple, Sequence, Tuple

ca_ca: float
chi_angles_atoms: Dict[str, List[List[str]]]
chi_angles_mask: List[List[float]]
chi_pi_periodic: List[List[float]]
rigid_group_atom_positions: Dict[str, List[Tuple[str, int, Tuple[float, float, float]]]]
residue_atoms: Dict[str, List[str]]
residue_atom_renaming_swaps: Dict[str, Dict[str, str]]
van_der_waals_radius: Dict[str, float]

class Bond(NamedTuple):
    atom1_name: Incomplete
    atom2_name: Incomplete
    length: Incomplete
    stddev: Incomplete

class BondAngle(NamedTuple):
    atom1_name: Incomplete
    atom2_name: Incomplete
    atom3name: Incomplete
    angle_rad: Incomplete
    stddev: Incomplete

def map_structure_with_atom_order(in_list: list, first_call: bool = True) -> list: ...
def load_stereo_chemical_props() -> Tuple[Mapping[str, List[Bond]], Mapping[str, List[Bond]], Mapping[str, List[BondAngle]]]:
    '''Load stereo_chemical_props.txt into a nice structure.

    Load literature values for bond lengths and bond angles and translate bond angles into the length of the opposite
    edge of the triangle ("residue_virtual_bonds").

    Returns:
      residue_bonds: dict that maps resname --> list of Bond tuples residue_virtual_bonds: dict that maps resname -->
      list of Bond tuples residue_bond_angles: dict that maps resname --> list of BondAngle tuples
    '''

between_res_bond_length_c_n: Tuple[float, float]
between_res_bond_length_stddev_c_n: Tuple[float, float]
between_res_cos_angles_c_n_ca: Tuple[float, float]
between_res_cos_angles_ca_c_n: Tuple[float, float]
atom_types: List[str]
atom_order: Dict[str, int]
atom_type_num: Incomplete
restype_name_to_atom14_names: Dict[str, List[str]]
restypes: List[str]
restype_order: Dict[str, int]
restype_num: Incomplete
unk_restype_index = restype_num
restypes_with_x: List[str]
restype_order_with_x: Dict[str, int]

def sequence_to_onehot(sequence: str, mapping: Mapping[str, int], map_unknown_to_x: bool = False) -> np.ndarray:
    """Maps the given sequence into a one-hot encoded matrix.

    Args:
      sequence: An amino acid sequence.
      mapping: A dictionary mapping amino acids to integers.
      map_unknown_to_x: If True, any amino acid that is not in the mapping will be
        mapped to the unknown amino acid 'X'. If the mapping doesn't contain amino acid 'X', an error will be thrown.
        If False, any amino acid not in the mapping will throw an error.

    Returns:
      A numpy array of shape (seq_len, num_unique_aas) with one-hot encoding of the sequence.

    Raises:
      ValueError: If the mapping doesn't contain values from 0 to
        num_unique_aas - 1 without any gaps.
    """

restype_1to3: Dict[str, str]
restype_3to1: Dict[str, str]
unk_restype: str
resnames: List[str]
resname_to_idx: Dict[str, int]
HHBLITS_AA_TO_ID: Dict[str, int]
ID_TO_HHBLITS_AA: Dict[int, str]
restypes_with_x_and_gap: List[str]
MAP_HHBLITS_AATYPE_TO_OUR_AATYPE: Tuple[int, ...]
STANDARD_ATOM_MASK: Incomplete

def chi_angle_atom(atom_index: int) -> np.ndarray:
    """Define chi-angle rigid groups via one-hot representations."""

chi_atom_1_one_hot: Incomplete
chi_atom_2_one_hot: Incomplete
chi_angles_atom_indices_list: List[List[List[str]]]
chi_angles_atom_indices_ours: list
chi_angles_atom_indices: Incomplete
chi_groups_for_atom: Dict[Tuple[str, str], List[Tuple[int, int]]]
restype_atom37_to_rigid_group: Incomplete
restype_atom37_mask: Incomplete
restype_atom37_rigid_group_positions: Incomplete
restype_atom14_to_rigid_group: Incomplete
restype_atom14_mask: Incomplete
restype_atom14_rigid_group_positions: Incomplete
restype_rigid_group_default_frame: Incomplete

def make_atom14_dists_bounds(overlap_tolerance: float = 1.5, bond_length_tolerance_factor: int = 15) -> Dict[str, np.ndarray]:
    """compute upper and lower bounds for bonds to assess violations."""

restype_atom14_ambiguous_atoms: Incomplete
restype_atom14_ambiguous_atoms_swap_idx: np.ndarray

def aatype_to_str_sequence(aatype: Sequence[int]) -> str: ...
