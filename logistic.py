# load_breast cancer dataset
data = load_breast_cancer()
X = data.data
Y = data.target
# split dataset into training and testing set
X_train,X_test, Y_train, Y_test =train_test_split(X,Y, test_size=0.2, random_state=42)
#Standardize features by removing the mean and scaling to unit variance
scaler =StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#Train logistic regression model
log_reg = logisticRegresssion(max_iter=1000)
log_reg.fit(X_train_scaled, Y_train)
# Make predictions
Y_pred = log_reg.predict(_test_scaled)
# Evaluate model
accuracy =accuracy_score(Y_test, Y_pred)
print("Accuracy:",accuracy)
#classification report
print("c;assification report:")
print(classificaton_report(Y_test, Y_pred, target_names=data.target_names))
