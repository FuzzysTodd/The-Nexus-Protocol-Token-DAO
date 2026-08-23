from _typeshed import Incomplete
from wandb import sdk as wandb_sdk
from wandb.apis import PublicApi
from wandb.data_types import Audio as Audio, Graph as Graph, Histogram as Histogram, Html as Html, Image as Image, Molecule as Molecule, Object3D as Object3D, Plotly as Plotly, Table as Table, Video as Video
from wandb.sdk.artifacts.artifact_ttl import ArtifactTTL as ArtifactTTL
from wandb.wandb_agent import agent as agent

__all__ = ['__version__', 'init', 'setup', 'save', 'sweep', 'controller', 'agent', 'config', 'log', 'summary', 'join', 'Api', 'Graph', 'Image', 'Plotly', 'Video', 'Audio', 'Table', 'Html', 'Object3D', 'Molecule', 'Histogram', 'ArtifactTTL']

__version__: str
init = wandb_sdk.init
setup = wandb_sdk.setup
watch = wandb_sdk.watch
unwatch = wandb_sdk.unwatch
finish = wandb_sdk.finish
join = finish
login = wandb_sdk.login
helper = wandb_sdk.helper
sweep = wandb_sdk.sweep
controller = wandb_sdk.controller
require = wandb_sdk.require
Artifact = wandb_sdk.Artifact
AlertLevel = wandb_sdk.AlertLevel
Settings = wandb_sdk.Settings
Config = wandb_sdk.Config
Api = PublicApi
config: Incomplete
summary: Incomplete
log: Incomplete
save: Incomplete
restore = wandb_sdk.wandb_run.restore
