from .. import Options as Options

def backup_Options(): ...
def restore_Options(backup) -> None: ...
def check_global_options(expected_options, white_list=[]):
    '''
    returns error message of "" if check Ok
    '''
