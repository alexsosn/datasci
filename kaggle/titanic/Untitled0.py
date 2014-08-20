
# coding: utf-8

# In[38]:

import csv as csv
import numpy as np

csv_file_obj = csv.reader(open('train.csv', 'rU'))
header = next(csv_file_obj)
print(header)

data = []
for row in csv_file_obj:
    data.append(row)

data = np.array(data)


# In[39]:

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers
print(proportion_survivors)


# In[40]:

women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"


# In[41]:

women_onboard = data[women_only_stats,1].astype(np.float)     
men_onboard = data[men_only_stats,1].astype(np.float)


# In[42]:

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)  
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard) 


# In[43]:

print ('Proportion of women who survived is {}'.format(proportion_women_survived))
print ('Proportion of men who survived is {}'.format(proportion_men_survived))


# In[46]:

test_file = open('test.csv', 'rU')
test_file_obj = csv.reader(test_file)
header = next(test_file_obj)

prediction_file = open('genderbasedmodel.csv', 'wb')
prediction_file_object = csv.writer(prediction_file)


# In[50]:

prediction_file_object.writerow(['PassengerId', 'Survived'])
for row in test_file_obj:
    if row[3] == 'female':
        prediction_file_object.writerow([row[0], '1'])
    else:
        prediction_file_object.writerow([row[0], '0'])
test_file.close()
prediction_file.close()


# In[ ]:



