import numpy as np
from scipy.stats import entropy


def confusion_loss(confusion_matrix, alpha=2):
    G, P = confusion_matrix.shape
    random_entropy = entropy(np.ones(G), base=2)

    loss = 0
    for row in confusion_matrix.T:
        actual_entropy = entropy(row, base=2)
        loss += (actual_entropy / random_entropy) ** alpha

    return (loss / P) ** (1 / alpha)


def confusion_loss_from_labels(labels, predictions, alpha=2):
    """Helper function to compute confusion loss from labels and predictions."""

    labels_map = {l: i for i, l in enumerate(set(labels))}
    predictions_map = {p: i for i, p in enumerate(set(predictions))}

    confusion_matrix = np.zeros((len(labels_map), len(predictions_map)))
    for l, p in zip(labels, predictions):
        l_idx = labels_map[l]
        p_idx = predictions_map[p]
        confusion_matrix[l_idx, p_idx] += 1

    return confusion_loss(confusion_matrix, alpha), confusion_matrix
