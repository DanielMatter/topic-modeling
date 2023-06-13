import numpy as np
from scipy.stats import entropy


def confusion_loss(confusion_matrix, bias=2):
    G, P = confusion_matrix.shape
    random_entropy = entropy(np.ones(G), base=2)

    loss = 0
    for row in confusion_matrix.T:
        actual_entropy = entropy(row, base=2)
        loss += (actual_entropy / random_entropy) ** bias

    return (loss / P) ** (1 / bias)
