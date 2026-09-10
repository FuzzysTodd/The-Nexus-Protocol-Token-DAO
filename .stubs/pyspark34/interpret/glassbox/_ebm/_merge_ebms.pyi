from ._utils import convert_categorical_to_continuous as convert_categorical_to_continuous, deduplicate_bins as deduplicate_bins, generate_term_names as generate_term_names, order_terms as order_terms, process_terms as process_terms, remove_unused_higher_bins as remove_unused_higher_bins

def merge_ebms(models):
    """Merging multiple EBM models trained on the same dataset.
    Args:
        models: List of EBM models to be merged.
    Returns:
        An EBM model with averaged mean and standard deviation of input models.
    """
