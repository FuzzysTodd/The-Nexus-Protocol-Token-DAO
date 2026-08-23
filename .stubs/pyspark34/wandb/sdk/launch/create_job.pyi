from typing import List
from wandb.apis.internal import Api as Api
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.internal.job_builder import JobBuilder as JobBuilder
from wandb.sdk.launch.builder.build import get_current_python_version as get_current_python_version
from wandb.sdk.launch.github_reference import GitHubReference as GitHubReference
from wandb.sdk.lib import filesystem as filesystem
from wandb.util import make_artifact_name_safe as make_artifact_name_safe

def create_job(path: str, job_type: str, entity: str | None = None, project: str | None = None, name: str | None = None, description: str | None = None, aliases: List[str] | None = None, runtime: str | None = None, entrypoint: str | None = None, git_hash: str | None = None) -> Artifact | None:
    '''Create a job from a path, not as the output of a run.

    Arguments:
        path (str): Path to the job directory.
        job_type (str): Type of the job. One of "git", "code", or "image".
        entity (Optional[str]): Entity to create the job under.
        project (Optional[str]): Project to create the job under.
        name (Optional[str]): Name of the job.
        description (Optional[str]): Description of the job.
        aliases (Optional[List[str]]): Aliases for the job.
        runtime (Optional[str]): Python runtime of the job, like 3.9.
        entrypoint (Optional[str]): Entrypoint of the job.
        git_hash (Optional[str]): Git hash of a specific commit, when using git type jobs.


    Returns:
        Optional[Artifact]: The artifact created by the job, the action (for printing), and job aliases.
                            None if job creation failed.

    Example:
        ```python
        artifact_job = wandb.create_job(
            job_type="code",
            path=".",
            entity="wandb",
            project="jobs",
            name="my-train-job",
            description="My training job",
            aliases=["train"],
            runtime="3.9",
            entrypoint="train.py",
        )
        # then run the newly created job
        artifact_job.call()
        ```
    '''
