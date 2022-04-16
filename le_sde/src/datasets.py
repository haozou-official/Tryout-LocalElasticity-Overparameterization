import numpy as np
import skimage.draw as skd
import scipy.ndimage as simg
import torch

def get_random_smps(x_tr, y_tr, x_va, y_va, n_tr, n_va, n_tot_tr, n_tot_va, n_c):
    tridxs = [np.random.choice(n_tot_tr, n_tr) for _ in range(n_c)]
    vaidxs = [np.random.choice(n_tot_va, n_va) for _ in range(n_c)]
    Xtr = torch.vstack([x_tr[y_tr==k][tridxs[k]] for k in range(n_c)])
    Ytr = np.repeat(np.arange(n_c), n_tr) 
    Xva = torch.vstack([x_va[y_va==k][vaidxs[k]] for k in range(n_c)])
    Yva = np.repeat(np.arange(n_c), n_va) 
    
    return Xtr, Ytr, Xva, Yva

####
# CIFAR10
####
def load_cifar10(path):
    import torchvision
    import torchvision.transforms as transforms
    transform = transforms.Compose( [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    return [torchvision.datasets.CIFAR10(root=str(path),
	    train=True, download=True, transform=transform), 
	    torchvision.datasets.CIFAR10(root=str(path),
		train=False, download=True, transform=transform)]

def cifar_unpack(dt, clss=None):
    xs = torch.stack([xx[0] for xx in dt])
    ys = np.array([xx[1] for xx in dt])
    if clss is not None:
        sel = np.zeros(ys.shape)
        for cr in cls:
            sel |= (sel == cr)
        xs = xs[sel]
        ys = ys[sel]
    return xs, ys

def get_cifar10(cifar10_data):
    cifar10_tr = list(cifar10_data[0])
    cifar10_va = list(cifar10_data[1])
    cifar10_xtr, cifar10_ytr = cifar_unpack(cifar10_tr)
    cifar10_xva, cifar10_yva = cifar_unpack(cifar10_va)
    return [cifar10_xtr, cifar10_ytr, cifar10_xva, cifar10_yva]
