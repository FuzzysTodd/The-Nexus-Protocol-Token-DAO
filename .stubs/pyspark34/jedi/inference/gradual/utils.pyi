from jedi.inference.gradual.typeshed import TYPESHED_PATH as TYPESHED_PATH, create_stub_module as create_stub_module

def load_proper_stub_module(inference_state, grammar, file_io, import_names, module_node):
    """
    This function is given a random .pyi file and should return the proper
    module.
    """
