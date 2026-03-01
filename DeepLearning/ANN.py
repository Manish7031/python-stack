import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#from tensorflow import keras
#from tensorflow.keras import layers

# 1. Prepare and Preprocess Data (using a hypothetical dataset)
# Assume 'X' contains features and 'y' contains target labels (0 or 1)
# X, y = load_your_data()

# Example data generation (replace with your data)
from sklearn.datasets import make_classification
X, y = make_classification(n_features=5, random_state=0)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

# Standardize the features (important for neural networks)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 2. Define the model architecture
model = keras.Sequential([
    # Input layer and first hidden layer with 64 neurons and ReLU activation
    layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    # Second hidden layer with 64 neurons and ReLU activation
    layers.Dense(64, activation='relu'),
    # Output layer with 1 neuron and sigmoid activation for binary classification
    layers.Dense(1, activation='sigmoid')
])

# 3. Compile the model
model.compile(
    optimizer='adam', # Optimization algorithm
    loss='binary_crossentropy', # Loss function for binary classification
    metrics=['accuracy'] # Metric to monitor during training
)

# 4. Train the model
history = model.fit(
    X_train, y_train,
    validation_split=0.2, # Use part of training data for validation
    epochs=100, # Number of times to iterate over the entire dataset
    batch_size=32 # Number of samples per gradient update
)

# 5. Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
print(f'Test accuracy: {test_accuracy}')
