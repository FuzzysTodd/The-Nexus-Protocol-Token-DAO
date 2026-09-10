from nltk.metrics.agreement import AnnotationTask as AnnotationTask
from nltk.metrics.aline import align as align
from nltk.metrics.association import BigramAssocMeasures as BigramAssocMeasures, ContingencyMeasures as ContingencyMeasures, NgramAssocMeasures as NgramAssocMeasures, QuadgramAssocMeasures as QuadgramAssocMeasures, TrigramAssocMeasures as TrigramAssocMeasures
from nltk.metrics.confusionmatrix import ConfusionMatrix as ConfusionMatrix
from nltk.metrics.distance import binary_distance as binary_distance, custom_distance as custom_distance, edit_distance as edit_distance, edit_distance_align as edit_distance_align, fractional_presence as fractional_presence, interval_distance as interval_distance, jaccard_distance as jaccard_distance, masi_distance as masi_distance, presence as presence
from nltk.metrics.paice import Paice as Paice
from nltk.metrics.scores import accuracy as accuracy, approxrand as approxrand, f_measure as f_measure, log_likelihood as log_likelihood, precision as precision, recall as recall
from nltk.metrics.segmentation import ghd as ghd, pk as pk, windowdiff as windowdiff
from nltk.metrics.spearman import ranks_from_scores as ranks_from_scores, ranks_from_sequence as ranks_from_sequence, spearman_correlation as spearman_correlation
