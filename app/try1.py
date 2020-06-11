print ("import started for numpy -> and some arrays are added")
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
print ("import ended for numpy ")


print ("import started for scikit learn -> gausian naive bayes")
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print ("import ended for sklearn")
print ("predicting the nature of data from numpy dime dataset X, Y")
print(clf.predict([[-0.8, -1]]))

clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))

print(clf_pf.predict([[-0.8, -1]]))
#now dothe same operation on an external dataset

input_file = '../.data/conn.log' 
filedata= []
print ("converting the file into list of elements")
with open(input_file) as f: #closes file after all the lines have been processed
    for line in f: #not using readlines(), as this consumes the memory
        filedata.append(line)
        print("one line appended to list \n")

print ("converting done")
