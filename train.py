#ALL IMPORTS HERE
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import pickle
import sys

#lists for misaliged read qualities.
data_Low=[] #quality score list for misaligned reads

#LOAD QUALITY SCORES FOR MISALIGNED READS
with open("datasets/noisy") as f:
    l=f.readlines()
    l=[i.strip("\n") for i in l]
    l=[i.strip("@[") for i in l]
    l=[i.strip("]") for i in l]
    l=[j.split(",") for j in l]
    
for i in range(len(l)):
    l[i]=[int(j) for j in l[i]]
data_low=l




#lists for correctly aligned read qualities.
data_hi=[] #quality score list for correctly aligned reads

#LOAD QUALITY SCORES FOR CORRECTLY ALIGNED READS
with open("datasets/accurate") as f:
    l=f.readlines()
    l=[i.strip("\n") for i in l]
    l=[i.strip("@[") for i in l]
    l=[i.strip("]") for i in l]
    l=[j.split(",") for j in l]
for i in range(len(l)):
    l[i]=[int(j) for j in l[i]]
data_hi=l



    

X=[] # master list of all unaligned and aligned read's quality scores.
for i in range(len(data_hi)):
    X.append(data_hi[i])
for i in range(len(data_low)):
    X.append(data_low[i])
y=[]# data label
y=[0 for i in data_hi]
for i in range(len(data_low)):
    y.append(1)
    

#train-test split and shuffle.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
pickle.dump( X_test, open( "xtest.p", "wb" ) )
pickle.dump( y_test, open( "ytest.p", "wb" ) )

if sys.argv[1]=="nn":
 #try kNN classifier
 i=int(sys.argv[2])
 classifier = KNeighborsClassifier(n_neighbors=i)
elif sys.argv[1]=='linear':
 classifier = LinearSVC()
classifier.fit(X_train, y_train)
pickle.dump(classifier, open("classifier.p","wb"))
