import dataclasses
import numpy as np
from . import residue_constants as residue_constants
from typing import Any, List, Mapping, Optional, Sequence

FeatureDict = Mapping[str, np.ndarray]
ModelOutput = Mapping[str, Any]
PICO_TO_ANGSTROM: float

@dataclasses.dataclass(frozen=True)
class Protein:
    """Protein structure representation."""
    atom_positions: np.ndarray
    aatype: np.ndarray
    atom_mask: np.ndarray
    residue_index: np.ndarray
    b_factors: np.ndarray
    chain_index: Optional[np.ndarray] = ...
    remark: Optional[str] = ...
    parents: Optional[Sequence[str]] = ...
    parents_chain_index: Optional[Sequence[int]] = ...
    def __init__(self, atom_positions, aatype, atom_mask, residue_index, b_factors, chain_index, remark, parents, parents_chain_index) -> None: ...

def from_proteinnet_string(proteinnet_str: str) -> Protein: ...
def get_pdb_headers(prot: Protein, chain_id: int = 0) -> List[str]: ...
def add_pdb_headers(prot: Protein, pdb_str: str) -> str:
    """Add pdb headers to an existing PDB string. Useful during multi-chain
    recycling
    """
def to_pdb(prot: Protein) -> str:
    """Converts a `Protein` instance to a PDB string.

    Args:
      prot: The protein to convert to PDB.

    Returns:
      PDB string.
    """
def ideal_atom_mask(prot: Protein) -> np.ndarray:
    """Computes an ideal atom mask.

    `Protein.atom_mask` typically is defined according to the atoms that are reported in the PDB. This function
    computes a mask according to heavy atoms that should be present in the given sequence of amino acids.

    Args:
      prot: `Protein` whose fields are `numpy.ndarray` objects.

    Returns:
      An ideal atom mask.
    """
def from_prediction(features: FeatureDict, result: ModelOutput, b_factors: Optional[np.ndarray] = None, chain_index: Optional[np.ndarray] = None, remark: Optional[str] = None, parents: Optional[Sequence[str]] = None, parents_chain_index: Optional[Sequence[int]] = None) -> Protein:
    """Assembles a protein from a prediction.

    Args:
      features: Dictionary holding model inputs.
      result: Dictionary holding model outputs.
      b_factors: (Optional) B-factors to use for the protein.
      chain_index: (Optional) Chain indices for multi-chain predictions
      remark: (Optional) Remark about the prediction
      parents: (Optional) List of template names
    Returns:
      A protein instance.
    """
