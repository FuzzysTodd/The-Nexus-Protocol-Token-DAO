from . import measures as measures, methods as methods
from .. import __version__ as __version__

def runtime(X, y, model_generator, method_name):
    ''' Runtime (sec / 1k samples)
    transform = "negate_log"
    sort_order = 2
    '''
def local_accuracy(X, y, model_generator, method_name):
    ''' Local Accuracy
    transform = "identity"
    sort_order = 0
    '''
def consistency_guarantees(X, y, model_generator, method_name):
    ''' Consistency Guarantees
    transform = "identity"
    sort_order = 1
    '''
def keep_positive_mask(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Positive (mask)
    xlabel = "Max fraction of features kept"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 4
    '''
def keep_negative_mask(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Negative (mask)
    xlabel = "Max fraction of features kept"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 5
    '''
def keep_absolute_mask__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Absolute (mask)
    xlabel = "Max fraction of features kept"
    ylabel = "R^2"
    transform = "identity"
    sort_order = 6
    '''
def keep_absolute_mask__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Absolute (mask)
    xlabel = "Max fraction of features kept"
    ylabel = "ROC AUC"
    transform = "identity"
    sort_order = 6
    '''
def remove_positive_mask(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Positive (mask)
    xlabel = "Max fraction of features removed"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 7
    '''
def remove_negative_mask(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Negative (mask)
    xlabel = "Max fraction of features removed"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 8
    '''
def remove_absolute_mask__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Absolute (mask)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - R^2"
    transform = "one_minus"
    sort_order = 9
    '''
def remove_absolute_mask__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Absolute (mask)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - ROC AUC"
    transform = "one_minus"
    sort_order = 9
    '''
def keep_positive_resample(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Positive (resample)
    xlabel = "Max fraction of features kept"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 10
    '''
def keep_negative_resample(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Negative (resample)
    xlabel = "Max fraction of features kept"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 11
    '''
def keep_absolute_resample__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Absolute (resample)
    xlabel = "Max fraction of features kept"
    ylabel = "R^2"
    transform = "identity"
    sort_order = 12
    '''
def keep_absolute_resample__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Absolute (resample)
    xlabel = "Max fraction of features kept"
    ylabel = "ROC AUC"
    transform = "identity"
    sort_order = 12
    '''
def remove_positive_resample(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Positive (resample)
    xlabel = "Max fraction of features removed"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 13
    '''
def remove_negative_resample(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Negative (resample)
    xlabel = "Max fraction of features removed"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 14
    '''
def remove_absolute_resample__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Absolute (resample)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - R^2"
    transform = "one_minus"
    sort_order = 15
    '''
def remove_absolute_resample__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Absolute (resample)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - ROC AUC"
    transform = "one_minus"
    sort_order = 15
    '''
def keep_positive_impute(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Positive (impute)
    xlabel = "Max fraction of features kept"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 16
    '''
def keep_negative_impute(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Negative (impute)
    xlabel = "Max fraction of features kept"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 17
    '''
def keep_absolute_impute__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Absolute (impute)
    xlabel = "Max fraction of features kept"
    ylabel = "R^2"
    transform = "identity"
    sort_order = 18
    '''
def keep_absolute_impute__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Absolute (impute)
    xlabel = "Max fraction of features kept"
    ylabel = "ROC AUC"
    transform = "identity"
    sort_order = 19
    '''
def remove_positive_impute(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Positive (impute)
    xlabel = "Max fraction of features removed"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 7
    '''
def remove_negative_impute(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Negative (impute)
    xlabel = "Max fraction of features removed"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 8
    '''
def remove_absolute_impute__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Absolute (impute)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - R^2"
    transform = "one_minus"
    sort_order = 9
    '''
def remove_absolute_impute__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Absolute (impute)
    xlabel = "Max fraction of features removed"
    ylabel = "1 - ROC AUC"
    transform = "one_minus"
    sort_order = 9
    '''
def keep_positive_retrain(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Positive (retrain)
    xlabel = "Max fraction of features kept"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 6
    '''
def keep_negative_retrain(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Keep Negative (retrain)
    xlabel = "Max fraction of features kept"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 7
    '''
def remove_positive_retrain(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Positive (retrain)
    xlabel = "Max fraction of features removed"
    ylabel = "Negative mean model output"
    transform = "negate"
    sort_order = 11
    '''
def remove_negative_retrain(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Remove Negative (retrain)
    xlabel = "Max fraction of features removed"
    ylabel = "Mean model output"
    transform = "identity"
    sort_order = 12
    '''
def batch_remove_absolute_retrain__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Batch Remove Absolute (retrain)
    xlabel = "Fraction of features removed"
    ylabel = "1 - R^2"
    transform = "one_minus"
    sort_order = 13
    '''
def batch_keep_absolute_retrain__r2(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Batch Keep Absolute (retrain)
    xlabel = "Fraction of features kept"
    ylabel = "R^2"
    transform = "identity"
    sort_order = 13
    '''
def batch_remove_absolute_retrain__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Batch Remove Absolute (retrain)
    xlabel = "Fraction of features removed"
    ylabel = "1 - ROC AUC"
    transform = "one_minus"
    sort_order = 13
    '''
def batch_keep_absolute_retrain__roc_auc(X, y, model_generator, method_name, num_fcounts: int = 11):
    ''' Batch Keep Absolute (retrain)
    xlabel = "Fraction of features kept"
    ylabel = "ROC AUC"
    transform = "identity"
    sort_order = 13
    '''
def human_and_00(X, y, model_generator, method_name):
    ''' AND (false/false)

    This tests how well a feature attribution method agrees with human intuition
    for an AND operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever and cough: +6 points

    transform = "identity"
    sort_order = 0
    '''
def human_and_01(X, y, model_generator, method_name):
    ''' AND (false/true)

    This tests how well a feature attribution method agrees with human intuition
    for an AND operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever and cough: +6 points

    transform = "identity"
    sort_order = 1
    '''
def human_and_11(X, y, model_generator, method_name):
    ''' AND (true/true)

    This tests how well a feature attribution method agrees with human intuition
    for an AND operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever and cough: +6 points

    transform = "identity"
    sort_order = 2
    '''
def human_or_00(X, y, model_generator, method_name):
    ''' OR (false/false)

    This tests how well a feature attribution method agrees with human intuition
    for an OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough: +6 points

    transform = "identity"
    sort_order = 0
    '''
def human_or_01(X, y, model_generator, method_name):
    ''' OR (false/true)

    This tests how well a feature attribution method agrees with human intuition
    for an OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough: +6 points

    transform = "identity"
    sort_order = 1
    '''
def human_or_11(X, y, model_generator, method_name):
    ''' OR (true/true)

    This tests how well a feature attribution method agrees with human intuition
    for an OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough: +6 points

    transform = "identity"
    sort_order = 2
    '''
def human_xor_00(X, y, model_generator, method_name):
    ''' XOR (false/false)

    This tests how well a feature attribution method agrees with human intuition
    for an eXclusive OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough but not both: +6 points

    transform = "identity"
    sort_order = 3
    '''
def human_xor_01(X, y, model_generator, method_name):
    ''' XOR (false/true)

    This tests how well a feature attribution method agrees with human intuition
    for an eXclusive OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough but not both: +6 points

    transform = "identity"
    sort_order = 4
    '''
def human_xor_11(X, y, model_generator, method_name):
    ''' XOR (true/true)

    This tests how well a feature attribution method agrees with human intuition
    for an eXclusive OR operation combined with linear effects. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points
    if fever or cough but not both: +6 points

    transform = "identity"
    sort_order = 5
    '''
def human_sum_00(X, y, model_generator, method_name):
    ''' SUM (false/false)

    This tests how well a feature attribution method agrees with human intuition
    for a SUM operation. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points

    transform = "identity"
    sort_order = 0
    '''
def human_sum_01(X, y, model_generator, method_name):
    ''' SUM (false/true)

    This tests how well a feature attribution method agrees with human intuition
    for a SUM operation. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points

    transform = "identity"
    sort_order = 1
    '''
def human_sum_11(X, y, model_generator, method_name):
    ''' SUM (true/true)

    This tests how well a feature attribution method agrees with human intuition
    for a SUM operation. This metric deals
    specifically with the question of credit allocation for the following function
    when all three inputs are true:
    if fever: +2 points
    if cough: +2 points

    transform = "identity"
    sort_order = 2
    '''
