#ALL IMPORTS HERE
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import pickle


X_test = pickle.load( open( "xtest.p", "rb" ) )
y_test = pickle.load( open( "ytest.p", "rb" ) )
classifier = pickle.load( open( "classifier.p", "rb" ) )

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
