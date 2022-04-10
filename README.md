# Tryout LocalElasticity and Overparameterization with Neurashed

# Table of Contents
1. [Prior Sequestial Work](#prior-sequential-work)
2. [Additional Useful Repositories](#additional-useful-repositories)

# Prior Sequential Work
## LE and Neurashed
| Title | Description | Code |
|-------|-------------|------|
|  [The local elasticity of neural networks](https://arxiv.org/abs/1910.06943) <br> Hangfeng He, Weijie Su     |    <li>Presents a phenomenon called local elasticity</li> <li>Offer a geometric interpretation of local elasticity using the neural tangent kerne</li> <li>Use pairwise similarity measures between feature vectors for clustering in conjunction with K-means</li>   |   [git](https://github.com/HornHehhf/LocalElasticity)   |
|  [Label-Aware Neural Tangent Kernel: Toward Better Generalization and Local Elasticity](https://proceedings.neurips.cc/paper/2020/hash/b6b90237b3ebd1e462a5d11dbc5c4dae-Abstract.html) <br> Shuxiao Chen, Hangfeng He, Weijie Su     |    <li>Introduce a novel approach from the perspective of label-awareness to reduce the gap for generalization ability between NTK and real-world NNs</li> <li>Propose two label-aware kernels</li> <li>Show that the models trained with the proposed kernels better simulate NNs in terms of generalization ability and local elasticity</li>   |   [git](https://github.com/HornHehhf/LANTK)   |
|  [Toward Better Generalization Bounds with Locally Elastic Stability](https://proceedings.mlr.press/v139/deng21b.html) <br> Zhun Deng, Hangfeng He, Weijie Su     |    <li>Uniform stability only considers the worst-case loss change (sensitivity) by removing a single data point</li> <li>There are many cases that the worst-case sensitivity of the loss is much larger than the average sensitivity taken over the single data point that is removed in NNs</li> <li>Show that locally elastic stability implies tighter generalization bounds than those derived based on uniform stability in many situations</li>   |   |
|  [Imitating Deep Learning Dynamics via Locally Elastic Stochastic Differential Equations](https://proceedings.neurips.cc/paper/2021/file/327af0f71f7acdfd882774225f04775f-Paper.pdf) <br> Jiayao Zhang, Hua Wang, Weijie Su     |    <li>Model the evolution of features during deep learning training using a set of stochastic differential equations (SDEs) that each corresponds to a training sample</li> <li>If the SDEs are locally elastic in the sense that the impact is more significant on samples from the same class as the input, the features of the training data become linearly separable, meaning vanishing training loss; otherwise, the features are not separable, regardless of how long the training time is</li> <li>Show that the emergence of a simple geometric structure called the neural collapse of the features</li>   |   [git](https://github.com/zjiayao/le_sde)   |
|  [Neurashed: A Phenomenological Model for Imitating Deep Learning Training](https://arxiv.org/pdf/2112.09741.pdf) <br> Weijie Su  |   <li>Argue that a future deep learning theory should inherit three characteristics: a hierarchically structured network architecture, parameters iteratively optimized using stochastic gradient-based methods, and information from the data that evolves compressively</li>  <li>Propose Neurashed, a phenomenological model, which enables insights into implicit regularization, infirmation bottleneck, local elasticity</li>  |   |

## Overparameterization
| Title | Description | Code |
|-------|-------------|------|
|  [Towards Understanding the Role of Over-Parametrization in Generalization of Neural Networks](https://arxiv.org/pdf/1811.04918.pdf) <br> Zeyuan Allen-Zhu, Yuanzhi Li, Yingyu Liang 2018     |    <li>Suggest a novel complexity measure based on unit-wise capacities resulting in a tighter generalization bound for two layer ReLU networks.</li> <li>The capacity bound correlates with the behavior of test error with increasing network sizes, and could potentially explain the improvement in generalization with over-parametrization</li>    |   [git](https://github.com/bneyshabur/over-parametrization)   |
|  [Learning and Generalization in Overparameterized Neural Networks, Going Beyond Two Layers](https://arxiv.org/pdf/1805.12076.pdf) <br> Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, Hathan Srebro 2018     |    <li>Prove that overparameterized neural networks can learn some notable concept classes, including two and three-layer networks with fewer parameters and smooth activations.</li> <li>The sample complexity can also be almost independent of the number of parameters in the network.</li>  <li>Establish a new notion of quadratic approximation of the neural network (that can be viewed as a second-order variant of NTK), and connect it to the SGD theory of escaping saddle points.</li>  |    |
|  [Learning Over-Parametrized Two-Layer ReLU Neural Networks beyond NTK](https://arxiv.org/pdf/2007.04596.pdf) <br> Yuanzhi Li, Tengyu Ma, Hongyang Zhang 2020     |    <li>Consider the dynamic of gradient descent for learning a two-layer neural network.</li> <li>Show that an over-parametrized two-layer neural network with ReLU activation, trained by gradient descent from random initialization, can provably learn the ground truth network with population loss at most o(1/d) in polynomial time with polynomial samples.</li>  <li>Prove that any kernel method, including Neural Tangent Kernel, with a
polynomial number of samples in d, has population loss at least Ω(1/d).</li>  |    |

# Additional Useful Repositories
1. [Neural Tangent Kernel](https://github.com/damaru2/ntk/blob/master/readme.md)
2. NTK blogs
* [Understanding the Neural Tangent Kernel](https://rajatvd.github.io/NTK/)
* [Ultra-Wide Deep Nets and Neural Tangent Kernel](http://www.offconvex.org/2019/10/03/NTK/)
3. [Exploring Generalization in Deep Learning](https://github.com/bneyshabur/generalization-bounds)
