# Confusion Matrix Loss

To put a firmer grasp on the model's performance, we formalize the notion of a *dominant ground-truth topic* for each predicted topic by introducing an entropy-based loss function $L$:

$$\begin{aligned}
L_\alpha(M) &= ( \frac{1}{-N \log N} \sum_{i = 1}^{N} e(M_i^T)^\alpha )^{-\alpha} \\
e(C) &= -\sum_{j=1}^{K} C_j \log C_j
\end{aligned}$$

$L$ takes as input the confusion matrix $M$. Each column $M_i^T$ of this matrix represents the ground-truth distribution of a predicted topic.
The loss of the overall matrix is the average of the entropy of each column, normalized by the entropy of a uniform distribution over $N$ topics.

The loss of a single column is the entropy of the ground-truth distribution of that predicted topic.