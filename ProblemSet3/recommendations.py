
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib notebook')
import numpy as np
import matplotlib.pyplot as plt


# In[7]:

class Recommendation:  
    def __init__(self, file_name='ratings.train.txt', K=20, lamda=0.1, eta=0.02):      
        self.file_name = file_name
        self.K = K
        self.lamda = lamda
        self.eta = eta
        
        item_max = 0
        user_max = 0
        item_set = set()
        user_set = set()        
        with open(file_name, 'r') as file:
            for line in file:
                item, user, _ = Recommendation.parse_line(line)
                if item > item_max:
                    item_max = item
                if user > user_max:
                    user_max = user
                item_set.add(item - 1)
                user_set.add(user - 1) 
            file.close()

        self.q = np.random.uniform(0, np.sqrt(5/K), (item_max, K))
        self.p = np.random.uniform(0, np.sqrt(5/K), (user_max, K))
        self.item_list = list(item_set)
        self.user_list = list(user_set)
    
    @staticmethod
    def parse_line(line):
        u = int(line.split()[0])
        i = int(line.split()[1])
        R = float(line.split()[2])
        return i, u, R
    
    def compute_error(self):
        E = self.lamda * (np.sum(self.q[self.item_list,:]**2) + np.sum(self.p[self.user_list, :]**2))
        with open(self.file_name, 'r') as file:
            for line in file:
                i, u, R = Recommendation.parse_line(line)
                E += np.square(R - self.q[i-1,:].dot(self.p[u-1,:].T))          
            file.close()
        return E
    
    def updates(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                i, u, R = Recommendation.parse_line(line)
                eps = 2*(R - self.q[i-1,:].dot(self.p[u-1,:].T))

                temp_q = self.q[i-1,:] + self.eta * (eps * self.p[u-1,:] - 2 * self.lamda * self.q[i-1,:])
                temp_p = self.p[u-1,:] + self.eta * (eps * self.q[i-1,:] - 2 * self.lamda * self.p[u-1,:])

                self.q[i-1,:] = temp_q
                self.p[u-1,:] = temp_p
            file.close()
            
        error = self.compute_error()  
        return error
    
    def main(self):
        error_list = list()
        for i in range(40):
            error = self.updates()
            error_list.append(error)
            print('iteration {}, error {}'.format(i, error))

        plt.plot(error_list)
        plt.xlabel('iteration')
        plt.ylabel('error')
        plt.show()


# In[8]:

Recommendation_obj = Recommendation()
Recommendation_obj.main()


# In[ ]:



