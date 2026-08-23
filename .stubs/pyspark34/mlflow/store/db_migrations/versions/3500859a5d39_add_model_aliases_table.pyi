from _typeshed import Incomplete
from mlflow.store.model_registry.dbmodels.models import SqlRegisteredModelAlias as SqlRegisteredModelAlias

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete

def get_existing_tables(): ...
def upgrade() -> None: ...
def downgrade() -> None: ...
