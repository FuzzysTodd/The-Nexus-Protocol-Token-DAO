import torch
import torch.nn as nn
from ...deepspeed import is_deepspeed_available as is_deepspeed_available
from ...modeling_outputs import ModelOutput as ModelOutput
from ...utils import ContextManagers as ContextManagers, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_scipy_available as is_scipy_available, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_esm import EsmConfig as EsmConfig
from .modeling_esm import ESM_START_DOCSTRING as ESM_START_DOCSTRING, EsmModel as EsmModel, EsmPreTrainedModel as EsmPreTrainedModel
from .openfold_utils import OFProtein as OFProtein, Rigid as Rigid, Rotation as Rotation, atom14_to_atom37 as atom14_to_atom37, chunk_layer as chunk_layer, compute_predicted_aligned_error as compute_predicted_aligned_error, compute_tm as compute_tm, frames_and_literature_positions_to_atom14_pos as frames_and_literature_positions_to_atom14_pos, make_atom14_masks as make_atom14_masks, residue_constants as residue_constants, to_pdb as to_pdb, torsion_angles_to_frames as torsion_angles_to_frames
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union

logger: Incomplete

@dataclass
class EsmForProteinFoldingOutput(ModelOutput):
    """
    Output type of [`EsmForProteinFoldingOutput`].

    Args:
        frames (`torch.FloatTensor`):
            Output frames.
        sidechain_frames (`torch.FloatTensor`):
            Output sidechain frames.
        unnormalized_angles (`torch.FloatTensor`):
            Predicted unnormalized backbone and side chain torsion angles.
        angles (`torch.FloatTensor`):
            Predicted backbone and side chain torsion angles.
        positions (`torch.FloatTensor`):
            Predicted positions of the backbone and side chain atoms.
        states (`torch.FloatTensor`):
            Hidden states from the protein folding trunk.
        s_s (`torch.FloatTensor`):
            Per-residue embeddings derived by concatenating the hidden states of each layer of the ESM-2 LM stem.
        s_z (`torch.FloatTensor`):
            Pairwise residue embeddings.
        distogram_logits (`torch.FloatTensor`):
            Input logits to the distogram used to compute residue distances.
        lm_logits (`torch.FloatTensor`):
            Logits output by the ESM-2 protein language model stem.
        aatype (`torch.FloatTensor`):
            Input amino acids (AlphaFold2 indices).
        atom14_atom_exists (`torch.FloatTensor`):
            Whether each atom exists in the atom14 representation.
        residx_atom14_to_atom37 (`torch.FloatTensor`):
            Mapping between atoms in the atom14 and atom37 representations.
        residx_atom37_to_atom14 (`torch.FloatTensor`):
            Mapping between atoms in the atom37 and atom14 representations.
        atom37_atom_exists (`torch.FloatTensor`):
            Whether each atom exists in the atom37 representation.
        residue_index (`torch.FloatTensor`):
            The index of each residue in the protein chain. Unless internal padding tokens are used, this will just be
            a sequence of integers from 0 to `sequence_length`.
        lddt_head (`torch.FloatTensor`):
            Raw outputs from the lddt head used to compute plddt.
        plddt (`torch.FloatTensor`):
            Per-residue confidence scores. Regions of low confidence may indicate areas where the model's prediction is
            uncertain, or where the protein structure is disordered.
        ptm_logits (`torch.FloatTensor`):
            Raw logits used for computing ptm.
        ptm (`torch.FloatTensor`):
            TM-score output representing the model's high-level confidence in the overall structure.
        aligned_confidence_probs (`torch.FloatTensor`):
            Per-residue confidence scores for the aligned structure.
        predicted_aligned_error (`torch.FloatTensor`):
            Predicted error between the model's prediction and the ground truth.
        max_predicted_aligned_error (`torch.FloatTensor`):
            Per-sample maximum predicted error.
    """
    frames: torch.FloatTensor = ...
    sidechain_frames: torch.FloatTensor = ...
    unnormalized_angles: torch.FloatTensor = ...
    angles: torch.FloatTensor = ...
    positions: torch.FloatTensor = ...
    states: torch.FloatTensor = ...
    s_s: torch.FloatTensor = ...
    s_z: torch.FloatTensor = ...
    distogram_logits: torch.FloatTensor = ...
    lm_logits: torch.FloatTensor = ...
    aatype: torch.FloatTensor = ...
    atom14_atom_exists: torch.FloatTensor = ...
    residx_atom14_to_atom37: torch.FloatTensor = ...
    residx_atom37_to_atom14: torch.FloatTensor = ...
    atom37_atom_exists: torch.FloatTensor = ...
    residue_index: torch.FloatTensor = ...
    lddt_head: torch.FloatTensor = ...
    plddt: torch.FloatTensor = ...
    ptm_logits: torch.FloatTensor = ...
    ptm: torch.FloatTensor = ...
    aligned_confidence_probs: torch.FloatTensor = ...
    predicted_aligned_error: torch.FloatTensor = ...
    max_predicted_aligned_error: torch.FloatTensor = ...
    def __init__(self, frames, sidechain_frames, unnormalized_angles, angles, positions, states, s_s, s_z, distogram_logits, lm_logits, aatype, atom14_atom_exists, residx_atom14_to_atom37, residx_atom37_to_atom14, atom37_atom_exists, residue_index, lddt_head, plddt, ptm_logits, ptm, aligned_confidence_probs, predicted_aligned_error, max_predicted_aligned_error) -> None: ...

ESMFOLD_INPUTS_DOCSTRING: str

def is_fp16_enabled(): ...
def is_deepspeed_initialized(): ...
def collate_dense_tensors(samples: List[torch.Tensor], pad_v: float = 0) -> torch.Tensor:
    """
    Takes a list of tensors with the following dimensions:
        [(d_11, ..., d_1K),
         (d_21, ..., d_2K), ..., (d_N1, ..., d_NK)]
    and stack + pads them into a single tensor of:
    (N, max_i=1,N { d_i1 }, ..., max_i=1,N {diK})
    """
def flatten_final_dims(t: torch.Tensor, no_dims: int): ...
def permute_final_dims(tensor: torch.Tensor, inds: List[int]): ...
def dict_multimap(fn, dicts): ...
def trunc_normal_init_(weights, scale: float = 1.0, fan: str = 'fan_in') -> None: ...
def ipa_point_weights_init_(weights) -> None: ...

class EsmFoldLinear(nn.Linear):
    """
    A Linear layer with built-in nonstandard initializations. Called just like torch.nn.Linear.

    Implements the initializers in 1.11.4, plus some additional ones found in the code.
    """
    init: Incomplete
    init_fn: Incomplete
    def __init__(self, in_dim: int, out_dim: int, bias: bool = True, init: str = 'default', init_fn: Optional[Callable[[torch.Tensor, torch.Tensor], None]] = None) -> None:
        '''
        Args:
            in_dim:
                The final dimension of inputs to the layer
            out_dim:
                The final dimension of layer outputs
            bias:
                Whether to learn an additive bias. True by default
            init:
                The initializer to use. Choose from:

                "default": LeCun fan-in truncated normal initialization "relu": He initialization w/ truncated normal
                distribution "glorot": Fan-average Glorot uniform initialization "gating": Weights=0, Bias=1 "normal":
                Normal initialization with std=1/sqrt(fan_in) "final": Weights=0, Bias=0

                Overridden by init_fn if the latter is not None.
            init_fn:
                A custom initializer taking weight and bias as inputs. Overrides init if not None.
        '''

class EsmFoldLayerNorm(nn.Module):
    c_in: Incomplete
    eps: Incomplete
    weight: Incomplete
    bias: Incomplete
    def __init__(self, c_in, eps: float = 1e-05) -> None: ...
    def forward(self, x): ...

def softmax_no_cast(t: torch.Tensor, dim: int = -1) -> torch.Tensor:
    """
    Softmax, but without automatic casting to fp32 when the input is of type bfloat16
    """

class EsmFoldAttention(nn.Module):
    """
    Standard multi-head attention using AlphaFold's default layer initialization. Allows multiple bias vectors.
    """
    c_q: Incomplete
    c_k: Incomplete
    c_v: Incomplete
    c_hidden: Incomplete
    no_heads: Incomplete
    gating: Incomplete
    linear_q: Incomplete
    linear_k: Incomplete
    linear_v: Incomplete
    linear_o: Incomplete
    linear_g: Incomplete
    sigmoid: Incomplete
    def __init__(self, c_q: int, c_k: int, c_v: int, c_hidden: int, no_heads: int, gating: bool = True) -> None:
        """
        Args:
            c_q:
                Input dimension of query data
            c_k:
                Input dimension of key data
            c_v:
                Input dimension of value data
            c_hidden:
                Per-head hidden dimension
            no_heads:
                Number of attention heads
            gating:
                Whether the output should be gated using query data
        """
    def forward(self, q_x: torch.Tensor, kv_x: torch.Tensor, biases: Optional[List[torch.Tensor]] = None, use_memory_efficient_kernel: bool = False, use_lma: bool = False, lma_q_chunk_size: int = 1024, lma_kv_chunk_size: int = 4096, use_flash: bool = False, flash_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        '''
        Args:
            q_x:
                [*, Q, C_q] query data
            kv_x:
                [*, K, C_k] key data
            biases:
                List of biases that broadcast to [*, H, Q, K]
            use_memory_efficient_kernel:
                Whether to use a custom memory-efficient attention kernel. This should be the default choice for most.
                If none of the "use_<...>" flags are True, a stock PyTorch implementation is used instead
            use_lma:
                Whether to use low-memory attention (Staats & Rabe 2021). If none of the "use_<...>" flags are True, a
                stock PyTorch implementation is used instead
            lma_q_chunk_size:
                Query chunk size (for LMA)
            lma_kv_chunk_size:
                Key/Value chunk size (for LMA)
        Returns
            [*, Q, C_q] attention update
        '''

class EsmFoldTriangleAttention(nn.Module):
    c_in: Incomplete
    c_hidden: Incomplete
    no_heads: Incomplete
    starting: Incomplete
    inf: Incomplete
    layer_norm: Incomplete
    linear: Incomplete
    mha: Incomplete
    def __init__(self, c_in, c_hidden, no_heads, starting: bool = True, inf: float = 1000000000.0) -> None:
        """
        Args:
            c_in:
                Input channel dimension
            c_hidden:
                Overall hidden channel dimension (not per-head)
            no_heads:
                Number of attention heads
        """
    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor] = None, chunk_size: Optional[int] = None, use_memory_efficient_kernel: bool = False, use_lma: bool = False, inplace_safe: bool = False) -> torch.Tensor:
        """
        Args:
            x:
                [*, I, J, C_in] input tensor (e.g. the pair representation)
        Returns:
            [*, I, J, C_in] output tensor
        """

class EsmFoldTriangleMultiplicativeUpdate(nn.Module):
    """
    Implements Algorithms 11 and 12.
    """
    linear_a_p: Incomplete
    linear_a_g: Incomplete
    linear_b_p: Incomplete
    linear_b_g: Incomplete
    linear_g: Incomplete
    linear_z: Incomplete
    layer_norm_in: Incomplete
    layer_norm_out: Incomplete
    sigmoid: Incomplete
    def __init__(self, config, _outgoing: bool = True) -> None: ...
    def forward(self, z: torch.Tensor, mask: Optional[torch.Tensor] = None, inplace_safe: bool = False, _add_with_inplace: bool = False, _inplace_chunk_size: Optional[int] = 256) -> torch.Tensor:
        """
        Args:
            x:
                [*, N_res, N_res, C_z] input tensor
            mask:
                [*, N_res, N_res] input mask
        Returns:
            [*, N_res, N_res, C_z] output tensor
        """

class EsmFoldPreTrainedModel(EsmPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

class EsmFoldSelfAttention(nn.Module):
    embed_dim: Incomplete
    num_heads: Incomplete
    head_width: Incomplete
    proj: Incomplete
    o_proj: Incomplete
    gated: Incomplete
    g_proj: Incomplete
    rescale_factor: Incomplete
    def __init__(self, embed_dim, num_heads, head_width, gated: bool = False) -> None: ...
    def forward(self, x, mask: Incomplete | None = None, bias: Incomplete | None = None, indices: Incomplete | None = None):
        """
        Basic self attention with optional mask and external pairwise bias. To handle sequences of different lengths,
        use mask.

        Inputs:
            x: batch of input sequneces (.. x L x C) mask: batch of boolean masks where 1=valid, 0=padding position (..
            x L_k) bias: batch of scalar pairwise attention biases (.. x Lq x Lk x num_heads)

        Outputs:
          sequence projection (B x L x embed_dim), attention maps (B x L x L x num_heads)
        """

class EsmFoldDropout(nn.Module):
    """
    Implementation of dropout with the ability to share the dropout mask along a particular dimension.
    """
    r: Incomplete
    batch_dim: Incomplete
    dropout: Incomplete
    def __init__(self, r: float, batch_dim: Union[int, List[int]]) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class EsmFoldSequenceToPair(nn.Module):
    layernorm: Incomplete
    proj: Incomplete
    o_proj: Incomplete
    def __init__(self, sequence_state_dim, inner_dim, pairwise_state_dim) -> None: ...
    def forward(self, sequence_state):
        """
        Inputs:
          sequence_state: B x L x sequence_state_dim

        Output:
          pairwise_state: B x L x L x pairwise_state_dim

        Intermediate state:
          B x L x L x 2*inner_dim
        """

class EsmFoldPairToSequence(nn.Module):
    layernorm: Incomplete
    linear: Incomplete
    def __init__(self, pairwise_state_dim, num_heads) -> None: ...
    def forward(self, pairwise_state):
        """
        Inputs:
          pairwise_state: B x L x L x pairwise_state_dim

        Output:
          pairwise_bias: B x L x L x num_heads
        """

class EsmFoldResidueMLP(nn.Module):
    mlp: Incomplete
    def __init__(self, embed_dim, inner_dim, dropout: int = 0) -> None: ...
    def forward(self, x): ...

class EsmFoldTriangularSelfAttentionBlock(nn.Module):
    config: Incomplete
    layernorm_1: Incomplete
    sequence_to_pair: Incomplete
    pair_to_sequence: Incomplete
    seq_attention: Incomplete
    tri_mul_out: Incomplete
    tri_mul_in: Incomplete
    tri_att_start: Incomplete
    tri_att_end: Incomplete
    mlp_seq: Incomplete
    mlp_pair: Incomplete
    drop: Incomplete
    row_drop: Incomplete
    col_drop: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_state, pairwise_state, mask: Incomplete | None = None, chunk_size: Incomplete | None = None, **__kwargs):
        """
        Inputs:
          sequence_state: B x L x sequence_state_dim pairwise_state: B x L x L x pairwise_state_dim mask: B x L boolean
          tensor of valid positions

        Output:
          sequence_state: B x L x sequence_state_dim pairwise_state: B x L x L x pairwise_state_dim
        """

class EsmCategoricalMixture:
    logits: Incomplete
    v_bins: Incomplete
    def __init__(self, param, bins: int = 50, start: int = 0, end: int = 1) -> None: ...
    def log_prob(self, true): ...
    def mean(self): ...

def categorical_lddt(logits, bins: int = 50): ...
def get_axial_mask(mask):
    """
    Helper to convert B x L mask of valid positions to axial mask used in row column attentions.

    Input:
      mask: B x L tensor of booleans

    Output:
      mask: B x L x L tensor of booleans
    """

class EsmFoldRelativePosition(nn.Module):
    bins: Incomplete
    embedding: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, residue_index, mask: Incomplete | None = None):
        """
        Input:
          residue_index: B x L tensor of indices (dytpe=torch.long) mask: B x L tensor of booleans

        Output:
          pairwise_state: B x L x L x pairwise_state_dim tensor of embeddings
        """

class EsmFoldAngleResnetBlock(nn.Module):
    linear_1: Incomplete
    linear_2: Incomplete
    relu: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, a: torch.Tensor) -> torch.Tensor: ...

class EsmFoldAngleResnet(nn.Module):
    """
    Implements Algorithm 20, lines 11-14
    """
    config: Incomplete
    linear_in: Incomplete
    linear_initial: Incomplete
    layers: Incomplete
    linear_out: Incomplete
    relu: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, s: torch.Tensor, s_initial: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            s:
                [*, C_hidden] single embedding
            s_initial:
                [*, C_hidden] single embedding as of the start of the StructureModule
        Returns:
            [*, no_angles, 2] predicted angles
        """

class EsmFoldInvariantPointAttention(nn.Module):
    """
    Implements Algorithm 22.
    """
    config: Incomplete
    hidden_dim: Incomplete
    num_heads: Incomplete
    num_qk_points: Incomplete
    num_v_points: Incomplete
    linear_q: Incomplete
    linear_kv: Incomplete
    linear_q_points: Incomplete
    linear_kv_points: Incomplete
    linear_b: Incomplete
    head_weights: Incomplete
    linear_out: Incomplete
    softmax: Incomplete
    softplus: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, s: torch.Tensor, z: Optional[torch.Tensor], r: Rigid, mask: torch.Tensor, _offload_inference: bool = False, _z_reference_list: Optional[Sequence[torch.Tensor]] = None) -> torch.Tensor:
        """
        Args:
            s:
                [*, N_res, C_s] single representation
            z:
                [*, N_res, N_res, C_z] pair representation
            r:
                [*, N_res] transformation object
            mask:
                [*, N_res] mask
        Returns:
            [*, N_res, C_s] single representation update
        """

class EsmFoldBackboneUpdate(nn.Module):
    """
    Implements part of Algorithm 23.
    """
    linear: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, s: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            [*, N_res, C_s] single representation
        Returns:
            [*, N_res, 6] update vector
        """

class EsmFoldStructureModuleTransitionLayer(nn.Module):
    linear_1: Incomplete
    linear_2: Incomplete
    linear_3: Incomplete
    relu: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, s): ...

class EsmFoldStructureModuleTransition(nn.Module):
    config: Incomplete
    layers: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, s): ...

class EsmFoldStructureModule(nn.Module):
    config: Incomplete
    layer_norm_s: Incomplete
    layer_norm_z: Incomplete
    linear_in: Incomplete
    ipa: Incomplete
    ipa_dropout: Incomplete
    layer_norm_ipa: Incomplete
    transition: Incomplete
    bb_update: Incomplete
    angle_resnet: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, evoformer_output_dict, aatype, mask: Incomplete | None = None, _offload_inference: bool = False):
        '''
        Args:
            evoformer_output_dict:
                Dictionary containing:
                    "single":
                        [*, N_res, C_s] single representation
                    "pair":
                        [*, N_res, N_res, C_z] pair representation
            aatype:
                [*, N_res] amino acid indices
            mask:
                Optional [*, N_res] sequence mask
        Returns:
            A dictionary of outputs
        '''
    def torsion_angles_to_frames(self, r, alpha, f): ...
    def frames_and_literature_positions_to_atom14_pos(self, r, f): ...

class EsmFoldingTrunk(nn.Module):
    config: Incomplete
    pairwise_positional_embedding: Incomplete
    blocks: Incomplete
    recycle_bins: int
    recycle_s_norm: Incomplete
    recycle_z_norm: Incomplete
    recycle_disto: Incomplete
    structure_module: Incomplete
    trunk2sm_s: Incomplete
    trunk2sm_z: Incomplete
    chunk_size: Incomplete
    def __init__(self, config) -> None: ...
    def set_chunk_size(self, chunk_size) -> None: ...
    def forward(self, seq_feats, pair_feats, true_aa, residx, mask, no_recycles):
        """
        Inputs:
          seq_feats: B x L x C tensor of sequence features pair_feats: B x L x L x C tensor of pair features residx: B
          x L long tensor giving the position in the sequence mask: B x L boolean tensor indicating valid residues

        Output:
          predicted_structure: B x L x (num_atoms_per_residue * 3) tensor wrapped in a Coordinates object
        """
    @staticmethod
    def distogram(coords, min_bin, max_bin, num_bins): ...

class EsmForProteinFolding(EsmPreTrainedModel):
    config: Incomplete
    distogram_bins: int
    esm: Incomplete
    esm_feats: Incomplete
    esm_attns: Incomplete
    esm_layers: Incomplete
    esm_s_combine: Incomplete
    esm_s_mlp: Incomplete
    n_tokens_embed: Incomplete
    pad_idx: int
    unk_idx: Incomplete
    mask_idx: Incomplete
    esm_dict_cls_idx: Incomplete
    esm_dict_mask_idx: Incomplete
    esm_dict_eos_idx: Incomplete
    esm_dict_padding_idx: Incomplete
    embedding: Incomplete
    trunk: Incomplete
    distogram_head: Incomplete
    ptm_head: Incomplete
    lm_head: Incomplete
    lddt_bins: int
    lddt_head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor = None, position_ids: Optional[torch.Tensor] = None, masking_pattern: Optional[torch.Tensor] = None, num_recycles: Optional[int] = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, EsmForProteinFolding

        >>> model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1")
        >>> tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
        >>> inputs = tokenizer(["MLKNVQVQLV"], return_tensors="pt", add_special_tokens=False)  # A tiny random peptide
        >>> outputs = model(**inputs)
        >>> folded_positions = outputs.positions
        ```

        '''
    af2_to_esm: Incomplete
    def af2_idx_to_esm_idx(self, aa, mask): ...
    def compute_language_model_representations(self, esmaa: torch.Tensor) -> torch.Tensor: ...
    def bert_mask(self, aa, esmaa, mask, pattern): ...
    def infer(self, seqs: Union[str, List[str]], position_ids: Incomplete | None = None): ...
    @staticmethod
    def output_to_pdb(output: Dict) -> List[str]:
        """Returns the pbd (file) string from the model given the model output."""
    def infer_pdb(self, seqs, *args, **kwargs) -> str:
        """Returns the pdb (file) string from the model given an input sequence."""
    def infer_pdbs(self, seqs: List[str], *args, **kwargs) -> List[str]:
        """Returns the pdb (file) string from the model given an input sequence."""
