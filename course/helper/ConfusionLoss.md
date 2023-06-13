# Loss from a Confusion Matrix

To put a firmer grasp on the model's performance, we formalize the notion of a *dominant ground-truth topic* for each predicted topic by introducing an entropy-based loss function:

$$
L(M) = \frac{1}{N} \sum_{i = 1}^{N} \frac{e(M_i)}{\hat{e}_N} \\
e(R) = -\sum_{j=1}^{K} M_j \log M_j \\
\hat{e}_N = \log \frac{1}{N}
$$