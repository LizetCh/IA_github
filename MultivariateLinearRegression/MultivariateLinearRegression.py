import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
 
# Upload data
data = pd.read_csv('datos_autos.csv')
features = data[['kilometraje', 'edad', 'potencia']].values
prices = data['precio'].values
 
#preprocessing data
# ----- calculate mean of each column ----
median_kilometraje = math.floor(data.kilometraje.median())
median_edad = math.floor(data.edad.median())
median_potencia = math.floor(data.potencia.median())
median_precio = math.floor(data.precio.median())
#fill any gaps inside the data with the mean of that column
data.kilometraje.fillna(median_kilometraje)
data.edad.fillna(median_edad)
data.potencia.fillna(median_potencia)
data.precio.fillna(median_precio)

# Normalize data
mean=np.mean(features, axis=0)
std = np.std(features, axis=0)
features_normalized = (features - mean) / std
 
# Add One Column for Intercept Term
intercept = np.ones((features_normalized.shape[0], 1)) #creates a column full of 1's
X = np.hstack((intercept, features_normalized))
y = prices.reshape(-1, 1) #transform into a column
 
# Initial parameters
theta = np.zeros((X.shape[1], 1)) #column of initial zeros
learning_rate = 0.001
iterations = 1000
 
# Cost Function
def compute_cost(X, y, theta):
	m = len(y) #number of rows in the data
	predictions = X.dot(theta) #calculate predictions (dot product)
	cost = (1/(2*m)) * np.sum(np.square(predictions - y)) #compare predictions to real data
	return cost
 
# Gradient descent
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    cost_history = []
    for i in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        theta -= (learning_rate / m) * X.T.dot(errors)
        cost_history.append(compute_cost(X, y, theta))
        
    return theta, cost_history
 
# Mean Squared Error function
def mse(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))

# Train the model
theta, cost_history = gradient_descent(X, y, theta, learning_rate, iterations)
 
# Show cost based on iterations
plt.plot(cost_history)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Cost Function over Iterations')
plt.show()
 
# Prediction function
def predict(X, theta):
	return X.dot(theta)
 
print("Values of theta: ", theta)

# Predict the price of a new car
new_car = np.array([[45000, 4, 200]]) # example: 45000 km, 4 years, 200 HP
new_car_normalized = (new_car - mean) / std

# new_car_with_intercept = np.hstack(([1], new_car_normalized))
car_intercept = np.ones((new_car_normalized.shape[0], 1))
new_car_with_intercept = np.hstack((car_intercept, new_car_normalized))

predicted_price = predict(new_car_with_intercept, theta)
print("Predicted price of the new car:", predicted_price[0][0])

#print mse
predictions = predict(X,theta)
mse = mse(y,predictions)
print("Mean Squared Error: ", mse)
