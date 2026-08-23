from tensorboard.summary.v2 import audio as audio, histogram as histogram, image as image, scalar as scalar, text as text

def reexport_tf_summary() -> None:
    '''Re-export all symbols from the original tf.summary.

    This function finds the original tf.summary V2 API and re-exports all the
    symbols from it within this module as well, so that when this module is
    patched into the TF API namespace as the new tf.summary, the effect is an
    overlay that just adds TensorBoard-provided symbols to the module.

    Finding the original tf.summary V2 API module reliably is a challenge, since
    this code runs *during* the overall TF API import process and depending on
    the order of imports (which is subject to change), different parts of the API
    may or may not be defined at the point in time we attempt to access them. This
    code also may be inserted into two places in the API (tf and tf.compat.v2)
    and may be re-executed multiple times even for the same place in the API (due
    to the TF module import system not populating sys.modules properly), so it
    needs to be robust to many different scenarios.

    The one constraint we can count on is that everywhere this module is loaded
    (via the component_api_helper mechanism in TF), it\'s going to be the \'summary\'
    submodule of a larger API package that already has a \'summary\' attribute
    that contains the TF-only summary API symbols we need to re-export. This
    may either be the original TF-only summary module (the first time we load
    this module) or a pre-existing copy of this module (if we\'re re-loading this
    module again). We don\'t actually need to differentiate those two cases,
    because it\'s okay if we re-import our own TensorBoard-provided symbols; they
    will just be overwritten later on in this file.

    So given that guarantee, the approach we take is to first attempt to locate
    a TF V2 API package that already has a \'summary\' attribute (most likely this
    is the parent package into which we\'re being imported, but not necessarily),
    and then do the dynamic version of "from tf_api_package.summary import *".

    Lastly, this logic is encapsulated in a function to avoid symbol leakage.
    '''
