
# coding: utf-8

# In[1]:

import operator
from itertools import combinations


# In[2]:

file_name = 'browsing.txt'
N = 100

def browsing_history():
    with open(file_name, 'r') as f:
        for line in f:
            yield line.rstrip().split(' ')
        f.close()


# In[3]:

def count_history(browsing_reader = browsing_history()):
    count = {}
    frequent_item = set()
    for record in browsing_reader:
        for item in record:
            if item not in count:
                count[item] = 1
            else:
                count[item] += 1
    
    frequent_count = {}
    for item_id, value in count.items():
        if value >= N:
            frequent_item.add(item_id)
            frequent_count[item_id] = value
        
    return frequent_item, frequent_count                     


# In[4]:

def count_pairs(frequent_items, browsing_reader=browsing_history()):
    pairs_count = dict()
    for record in browsing_reader:
        items_in_record = list()
        for item in record:
            if item in frequent_items:
                items_in_record.append(item)  
        
        pair_set = {tuple(sorted(items)) for items in combinations(items_in_record, 2)}
                    
        for pair in pair_set:
            if pair not in pairs_count:
                pairs_count[pair] = 1
            else:
                pairs_count[pair] += 1
                    
    filtered_pair_count = {}       
    for pair, count in pairs_count.items():
        if count >= N: filtered_pair_count[tuple(pair)] = count
                
    return filtered_pair_count         


# In[5]:

frequent_items, frequent_count = count_history()
filtered_pair_count = count_pairs(frequent_items)


# In[6]:

# calculate association rule
association_rule = {}
for pair, count in filtered_pair_count.items():
    association_rule[pair] = count/frequent_count[pair[0]]
    association_rule[pair[::-1]] = count/frequent_count[pair[1]]

# sort association_rule
sorted_association_rule = sorted(association_rule.items(), key=operator.itemgetter(1))
sorted_association_rule.reverse()


# In[7]:

sorted_association_rule


# In[37]:

# construct set of triples
triples = set()
for pair1 in filtered_pair_count.keys():
    for pair2 in filtered_pair_count.keys():
        
        if len(set(pair1).intersection(pair2)) == 1:
            triple = tuple(sorted(list(set(pair1 + pair2))))
            if triple not in triples: triples.add(triple)


# In[38]:

def count_triples(triple_set, frequent_items, browsing_reader=browsing_history()):
    triples_count = dict()
    for triple in triple_set:
        triples_count[triple] = 0
    
    for record in browsing_reader:
        items_in_record = list()
        for item in record:
            if item in frequent_items:
                items_in_record.append(item)
                
        triples_in_record = {tuple(sorted(items)) for items in combinations(items_in_record, 3)}
        for triple in triples_in_record:
            if triple in triple_set: triples_count[triple] += 1
                    
    filtered_triples_count = {}       
    for triple, count in triples_count.items():
        if count >= N: filtered_triples_count[triple] = count
                
    return filtered_triples_count    


# In[39]:

filtered_triples_count = count_triples(triples, frequent_items)


# In[62]:

association_rule_for_triple = {}
for triple, count in filtered_triples_count.items():
    association_rule_for_triple[(tuple(sorted((triple[0], triple[1]))), triple[2])] = count/filtered_pair_count[tuple(sorted([triple[0], triple[1]]))]
    association_rule_for_triple[(tuple(sorted((triple[2], triple[1]))), triple[0])] = count/filtered_pair_count[tuple(sorted([triple[2], triple[1]]))]
    association_rule_for_triple[(tuple(sorted((triple[2], triple[0]))), triple[1])] = count/filtered_pair_count[tuple(sorted([triple[2], triple[0]]))]

# sort association_rule
sorted_association_rule_for_triple = sorted(association_rule_for_triple.items(), key=operator.itemgetter(0))
sorted_association_rule_for_triple = sorted(sorted_association_rule_for_triple, key=operator.itemgetter(1), reverse=True)


# In[63]:

sorted_association_rule_for_triple


# In[42]:

filtered_triples_count[tuple(sorted(['DAI23334', 'ELE92920', 'DAI62779']))]


# In[30]:

filtered_pair_count[tuple(sorted(['DAI23334', 'ELE92920']))]


# In[ ]:



