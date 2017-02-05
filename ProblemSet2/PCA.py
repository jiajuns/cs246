#%%
import numpy as np
from scipy import linalg

## initialize M
#%%
M = np.array([[1, 2, 3, 4], [2, 1, 4, 3]])


## SVD of M
#%%
U, s, Vh = linalg.svd(np.transpose(M))
print('U: ', U)
print('s: ', s)
print('Vh ', Vh)


## eigenvalue decomposition of M^TM
#%%
Evals, Evcts = linalg.eigh(np.dot(M, np.transpose(M)))
print('eigenvalues: ', Evals)
print('eigenvectors: ', Evcts)