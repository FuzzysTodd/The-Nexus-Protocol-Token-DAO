from ..wandb_run import Run as LocalRun
from ._private import MEDIA_TMP as MEDIA_TMP
from .base_types.media import BatchableMedia as BatchableMedia, Media as Media
from _typeshed import Incomplete
from typing import Sequence, TextIO
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import runid as runid
from wandb.sdk.lib.paths import LogicalPath as LogicalPath

RDKitDataType: Incomplete

class Molecule(BatchableMedia):
    """Wandb class for 3D Molecular data.

    Arguments:
        data_or_path: (string, io)
            Molecule can be initialized from a file name or an io object.
        caption: (string)
            Caption associated with the molecule for display.
    """
    SUPPORTED_TYPES: Incomplete
    SUPPORTED_RDKIT_TYPES: Incomplete
    def __init__(self, data_or_path: str | TextIO, caption: str | None = None, **kwargs: str) -> None: ...
    @classmethod
    def from_rdkit(cls, data_or_path: RDKitDataType, caption: str | None = None, convert_to_3d_and_optimize: bool = True, mmff_optimize_molecule_max_iterations: int = 200) -> Molecule:
        """Convert RDKit-supported file/object types to wandb.Molecule.

        Arguments:
            data_or_path: (string, rdkit.Chem.rdchem.Mol)
                Molecule can be initialized from a file name or an rdkit.Chem.rdchem.Mol object.
            caption: (string)
                Caption associated with the molecule for display.
            convert_to_3d_and_optimize: (bool)
                Convert to rdkit.Chem.rdchem.Mol with 3D coordinates.
                This is an expensive operation that may take a long time for complicated molecules.
            mmff_optimize_molecule_max_iterations: (int)
                Number of iterations to use in rdkit.Chem.AllChem.MMFFOptimizeMolecule
        """
    @classmethod
    def from_smiles(cls, data: str, caption: str | None = None, sanitize: bool = True, convert_to_3d_and_optimize: bool = True, mmff_optimize_molecule_max_iterations: int = 200) -> Molecule:
        """Convert SMILES string to wandb.Molecule.

        Arguments:
            data: (string)
                SMILES string.
            caption: (string)
                Caption associated with the molecule for display
            sanitize: (bool)
                Check if the molecule is chemically reasonable by the RDKit's definition.
            convert_to_3d_and_optimize: (bool)
                Convert to rdkit.Chem.rdchem.Mol with 3D coordinates.
                This is an expensive operation that may take a long time for complicated molecules.
            mmff_optimize_molecule_max_iterations: (int)
                Number of iterations to use in rdkit.Chem.AllChem.MMFFOptimizeMolecule
        """
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def to_json(self, run_or_artifact: LocalRun | Artifact) -> dict: ...
    @classmethod
    def seq_to_json(cls, seq: Sequence['BatchableMedia'], run: LocalRun, key: str, step: int | str) -> dict: ...
