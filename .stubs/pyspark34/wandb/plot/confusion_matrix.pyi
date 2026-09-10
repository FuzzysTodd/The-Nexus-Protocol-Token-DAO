from _typeshed import Incomplete
from typing import Sequence
from wandb import util as util

chart_limit: Incomplete

def confusion_matrix(probs: Sequence[Sequence] | None = None, y_true: Sequence | None = None, preds: Sequence | None = None, class_names: Sequence[str] | None = None, title: str | None = None):
    '''Compute a multi-run confusion matrix.

    Arguments:
        probs (2-d arr): Shape [n_examples, n_classes]
        y_true (arr): Array of label indices.
        preds (arr): Array of predicted label indices.
        class_names (arr): Array of class names.

    Returns:
        Nothing. To see plots, go to your W&B run page then expand the \'media\' tab
        under \'auto visualizations\'.

    Example:
        ```
        vals = np.random.uniform(size=(10, 5))
        probs = np.exp(vals)/np.sum(np.exp(vals), keepdims=True, axis=1)
        y_true = np.random.randint(0, 5, size=(10))
        labels = ["Cat", "Dog", "Bird", "Fish", "Horse"]
        wandb.log({\'confusion_matrix\': wandb.plot.confusion_matrix(probs, y_true=y_true, class_names=labels)})
        ```
    '''
