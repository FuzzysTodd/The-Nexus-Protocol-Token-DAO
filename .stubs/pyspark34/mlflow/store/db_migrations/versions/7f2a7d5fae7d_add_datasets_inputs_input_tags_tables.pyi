from _typeshed import Incomplete
from mlflow.store.tracking.dbmodels.models import SqlDataset as SqlDataset, SqlInput as SqlInput, SqlInputTag as SqlInputTag

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete

def upgrade() -> None: ...
def downgrade() -> None: ...
