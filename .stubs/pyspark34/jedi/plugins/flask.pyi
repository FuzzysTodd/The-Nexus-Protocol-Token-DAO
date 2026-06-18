def import_module(callback):
    '''
    Handle "magic" Flask extension imports:
    ``flask.ext.foo`` is really ``flask_foo`` or ``flaskext.foo``.
    '''
