from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
iris = load_iris()
  
X = iris.data
y = iris.target
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
  
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
  
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
print(metrics.confusion_matrix(y_test,y_pred))
print("\n Precision score is:", metrics.precision_score(y_test, y_pred, average='macro'))
print("\n Precision score is:", metrics.precision_score(y_test, y_pred, average='micro'))