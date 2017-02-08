#%%
import numpy as np
from numpy import linalg

## initialize M
#%%
M = np.array([[1, 2, 3, 4], [2, 1, 4, 3]])


## SVD of M
#%%
U, s, Vh = linalg.svd(np.transpose(M), full_matrices=False)
print('U: ', U)
print('s: ', s)
print('Vh ', Vh)


## eigenvalue decomposition of M^TM
#%%
Evals, Evcts = linalg.eig(np.dot(M, np.transpose(M)))
print('eigenvalues: ', Evals)
print('eigenvectors: ', Evcts)