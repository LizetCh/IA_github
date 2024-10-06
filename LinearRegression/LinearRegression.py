'''
Linear Regression Algorithm
Model that calculates the linear relationship between two variables
'''

#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Upload data from csv
data = pd.read_csv('datos_casas.csv')
X = data['tamano'].values
y = data['precio'].values
 
# Normalize data (bring the values closer together)
Xmean = np.mean(X)
Xstd = np.std(X)
X = (X - Xmean) / Xstd
 
# Initialize parameters (initial values for the )
theta0 = 0 #Intercept
theta1 = 0 #Slope
learning_rate = 0.1
iterations = 1000

print(f"Values after gradient descent: theta0={theta0:.3f}, theta1={theta1:.3f}, learning_rate={learning_rate:.3f}, iterations={iterations:.1f}")

# Cost Function
def compute_cost(X, y, theta0, theta1):
    m = len(y)
    cost = (1/(2*m)) * np.sum((theta0 + theta1*X - y)**2)
    return cost
 
# Gradient descent
def gradient_descent(X, y, theta0, theta1, learning_rate, iterations): 
    m = len(y)
    cost_history = []
    for i in range(iterations):
        predictions = theta0 + theta1*X
        errors = predictions - y
        theta0 -= 2*(learning_rate / m) * np.sum(errors)
        theta1 -= 2*(learning_rate/m) * np.sum(errors * X)
        cost_history.append(compute_cost(X, y, theta0, theta1))

        # Reduce learning rate if the cost is not improving <<<<<<<<<<<< modification (added to have a dynamic learning rate)
        if i > 0 and cost_history[i] >= cost_history[i-1]:
            learning_rate *= 0.9  #reducir un 10%
            print(f"Iteration {i}: Learning rate adjusted to {learning_rate:.7f}")

    return theta0, theta1, cost_history
 
# Train the model
theta0, theta1, cost_history = gradient_descent(X, y, theta0, theta1, learning_rate, iterations)
print(f"Values after gradient descent: theta0={theta0:.3f}, theta1={theta1:.3f}, learning_rate={learning_rate:.3f}, iterations={iterations:.1f}")


# Predict and evaluate
predict = lambda size: (theta0 + theta1 * ((size - Xmean) / Xstd))

predicted_price = predict(620) # Size in square meters

# Show results

print("Price predicted: %.4f" % predicted_price)
 
# Calculate Mean Squared Error (MSE) <<<<<<<<<<<<<<<<<<<<<<<<< modification (added to check the performance of the model)
def mean_squared_error(y_actual, y_pred):
    return np.mean((y_actual - y_pred) ** 2)

# Predict values for all data points
predictions = theta0 + theta1 * X

# Calculate MSE for training set
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse:.4f}')


#Plot graphs 
#Linear Regression Graph <<<<<<<<<<<<<<<<<<< modification (added to visualize the linear regression function calculated)
plt.scatter(X, y, color='blue', label='Data points') 
plt.plot(X, theta0 + theta1 * X, color='red', label='Regression line')
plt.xlabel('Size (normalized)')
plt.ylabel('Price (in thousands of dollars)')
plt.title('Linear Regression Function')
plt.legend()
plt.show()

#Error/Cost grapg
plt.plot(cost_history)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Error/Cost Convergence')
plt.show()

