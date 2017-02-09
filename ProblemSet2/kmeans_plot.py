
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib notebook')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os


# In[2]:

def Cost_List(output_dir, iteration=20):
    cost = list(range(iteration))
    for i in range(1, iteration+1):
        output_file = os.path.join(output_dir, 'output'+str(i), 'part-r-00000')
        with open(output_file, 'r') as f:
            for line in f:
                if line.split('\t')[0] == 'cost':
                    cost[i-1] = float(line.split('\t')[1].rstrip())
            f.close()
    return cost


# In[3]:

output_dir_1M = "C:\\Users\\Jiajun Sun\\Documents\\cs246\\ProblemSet2\\centroid_M"
output_dir_2M = "C:\\Users\\Jiajun Sun\\Documents\\cs246\\ProblemSet2\\centroid2_M"

output_dir_1L2 = "C:\\Users\\Jiajun Sun\\Documents\\cs246\\ProblemSet2\\centroid_L2"
output_dir_2L2 = "C:\\Users\\Jiajun Sun\\Documents\\cs246\\ProblemSet2\\centroid2_L2"

cost_1M = Cost_List(output_dir_1M)
cost_2M = Cost_List(output_dir_2M)
cost_1L2 = Cost_List(output_dir_1L2)
cost_2L2 = Cost_List(output_dir_2L2)


# In[7]:

def percentage_change(cost):
    return (cost[0] - cost[9])/cost[0]


# In[8]:

print('Euclidean c1.txt', percentage_change(cost_1L2))
print('Euclidean c2.txt', percentage_change(cost_2L2))

print('Manhattan c1.txt', percentage_change(cost_1M))
print('Manhattan c2.txt', percentage_change(cost_2M))


# In[4]:

fig = plt.figure()

line1 = plt.plot(list(range(1, 21)), cost_1L2, 'r', label='c1.txt')
line2 = plt.plot(list(range(1, 21)), cost_2L2, 'b', label='c2.txt')

plt.xlabel('iterations')
plt.ylabel('cost')
plt.title('Euclidean distance')
plt.legend()
plt.show()


# In[5]:

fig2 = plt.figure()

line1 = plt.plot(list(range(1, 21)), cost_1M, 'r', label='c1.txt')
line2 = plt.plot(list(range(1, 21)), cost_2M, 'b', label='c2.txt')

plt.xlabel('iterations')
plt.ylabel('cost')
plt.title('Manhattan distance')
plt.legend()
plt.show()


# In[ ]:



