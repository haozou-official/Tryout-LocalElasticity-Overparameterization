# Tryout LocalElasticity and Overparameterization with Neurashed

# Table of Contents
1. [Prior Sequestial Work](#prior-sequential-work)
2. [Additional Useful Repositories](#additional-useful-repositories)

# Prior Sequential Work
| Title | Description | Code |
|-------|-------------|------|
|  [The local elasticity of neural networks](https://arxiv.org/abs/1910.06943) <br> Hangfeng He, Weijie Su     |    <li>Presents a phenomenon called local elasticity</li> <li>Offer a geometric interpretation of local elasticity using the neural tangent kerne</li> <li>Use pairwise similarity measures between feature vectors for clustering in conjunction with K-means</li>   |   [git](https://github.com/HornHehhf/LocalElasticity)   |
|  [Label-Aware Neural Tangent Kernel: Toward Better Generalization and Local Elasticity](https://proceedings.neurips.cc/paper/2020/hash/b6b90237b3ebd1e462a5d11dbc5c4dae-Abstract.html) <br> Shuxiao Chen, Hangfeng He, Weijie Su     |    <li>Introduce a novel approach from the perspective of label-awareness to reduce the gap for generalization ability between NTK and real-world NNs</li> <li>Propose two label-aware kernels</li> <li>Show that the models trained with the proposed kernels better simulate NNs in terms of generalization ability and local elasticity</li>   |   [git](https://github.com/HornHehhf/LANTK)   |
|  [Toward Better Generalization Bounds with Locally Elastic Stability](https://proceedings.mlr.press/v139/deng21b.html) <br> Zhun Deng, Hangfeng He, Weijie Su     |    <li>Uniform stability on=nly considers the worst-case loss change (sensitivity) by removing a single data point</li> <li>There are many cases that the worst-case sensitivity of the loss is much larger than the average sensitivity taken over the single data point that is removed in NNs</li> <li>Show that locally elastic stability implies tighter generalization bounds than those derived based on uniform stability in many situations</li>   |   |
|  [Imitating Deep Learning Dynamics via Locally Elastic Stochastic Differential Equations](https://proceedings.neurips.cc/paper/2021/file/327af0f71f7acdfd882774225f04775f-Paper.pdf) <br> Jiayao Zhang, Hua Wang, Weijie Su     |    <li>Model the evolution of features during deep learning training using a set of stochastic differential equations (SDEs) that each corresponds to a training sampl</li> <li>If the SDEs are locally elastic in the sense that the impact is more significant on samples from the same class as the input, the features of the training data become linearly separable, meaning vanishing training loss; otherwise, the features are not separable, regardless of how long the training time is</li> <li>Show that the emergence of a simple geometric structure called the neural collapse of the features</li>   |   [git](https://github.com/zjiayao/le_sde)   |

# Additional Useful Repositories
* [Exploring Generalization in Deep Learning](https://github.com/bneyshabur/generalization-bounds)
