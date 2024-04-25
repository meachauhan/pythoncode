from sklearn.datasets import load breast
# Load Iris dataset
iris = load_iris()
X = iris.data
Y = iris.target
#Split dataset into training and testing sets
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
#Standardize features by removing the mean and scaling to unitvariance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#Train KNM classifier
k = 3 # Number of neighbors
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train_scaled, Y_train)
# Make predictions
Y_pred = knn_classifier.predict(X_test_scaled)
# Evaluate model
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:",accuracy)
#classification report
print("classification Report:")
print(classification_report(Y_test, Y_pred, target_names=iris.target_names))
