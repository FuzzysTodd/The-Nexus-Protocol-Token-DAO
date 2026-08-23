from _typeshed import Incomplete

I18N_DIR: Incomplete
TRANSLATIONS_CACHE: dict

def parse_accept_lang_header(accept_lang):
    """Parses the 'Accept-Language' HTTP header.

    Returns a list of language codes in *ascending* order of preference
    (with the most preferred language last).
    """
def load(language, domain: str = 'nbjs'):
    """Load translations from an nbjs.json file"""
def cached_load(language, domain: str = 'nbjs'):
    """Load translations for one language, using in-memory cache if available"""
def combine_translations(accept_language, domain: str = 'nbjs'):
    """Combine translations for multiple accepted languages.

    Returns data re-packaged in jed1.x format.
    """
