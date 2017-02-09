
# coding: utf-8

# In[1]:

import numpy as np

N = 100
iteration = 40


# In[2]:

# get count from txt file
def edge_counter(file_name = 'graph.txt', count_matrix = np.zeros((N, N))):
    with open(file_name) as fp:
        for line in fp:
            source_node, dest_node = line.split() # node number is 1-based
            if count_matrix[int(dest_node)-1, int(source_node)-1] < 1:  
                count_matrix[int(dest_node)-1, int(source_node)-1] += 1
        fp.close()
        
    return count_matrix


# In[3]:

# generate matrix M
def M_matrix(count_matrix=edge_counter()):
    M = count_matrix / np.sum(count_matrix, axis=0)
    return M


# In[4]:

## page rank
r = np.array([1./N for _ in range(N)]).reshape(N, 1)
beta = 0.8
M = M_matrix()

for _ in range(iteration):
    r = np.array([(1-beta)/N for _ in range(N)]).reshape(N, 1) + beta * M.dot(r)
    
print('top 5 nodes: ', sorted(range(1, len(r)+1), key=lambda i: r[i-1])[-5:][::-1])
print('bottom 5 nodes: ', sorted(range(1, len(r)+1), key=lambda i: r[i-1])[:5])


# In[5]:

## HITS 

L = np.transpose(edge_counter())
lambbda = 1
mu = 1

h = np.array([1 for _ in range(N)]).reshape(N, 1)

a = L.T.dot(h)
a = a/np.max(a)

h = L.dot(a)
h = h/np.max(h)

for _ in range(iteration):
    a = lambbda * L.T.dot(h)
    a = a/np.max(a)
    h = mu * L.dot(a)
    h = h/np.max(h)


# In[6]:

print('top 5 hubbiness nodes: ', sorted(range(1, len(r)+1), key=lambda i: h[i-1])[-5:][::-1])
print('bottom 5 hubbiness nodes: ', sorted(range(1, len(r)+1), key=lambda i: h[i-1])[:5])
print('top 5 authority nodes: ', sorted(range(1, len(r)+1), key=lambda i: a[i-1])[-5:][::-1])
print('bottom 5 authority nodes: ', sorted(range(1, len(r)+1), key=lambda i: a[i-1])[:5])


# In[ ]:



