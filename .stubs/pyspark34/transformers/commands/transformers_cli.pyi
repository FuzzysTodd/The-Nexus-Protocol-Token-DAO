from .add_new_model import AddNewModelCommand as AddNewModelCommand
from .add_new_model_like import AddNewModelLikeCommand as AddNewModelLikeCommand
from .convert import ConvertCommand as ConvertCommand
from .download import DownloadCommand as DownloadCommand
from .env import EnvironmentCommand as EnvironmentCommand
from .lfs import LfsCommands as LfsCommands
from .pt_to_tf import PTtoTFCommand as PTtoTFCommand
from .run import RunCommand as RunCommand
from .serving import ServeCommand as ServeCommand
from .user import UserCommands as UserCommands

def main() -> None: ...
