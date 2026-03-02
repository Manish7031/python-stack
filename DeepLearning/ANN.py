import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import make_classification

# data processing
# 'X' contains features and 'y' contains target labels (0 or 1)
overweigth_people = [[99, 89],[119,99],[199,174],[79,99],[39,59]]
fit_people = [[59,174],[89,189],[79,179],[49,139],[29,119]]

people = fit_people+overweigth_people
is_fit = [1,1,1,1,1,0,0,0,0,0]

X = np.array(people)
y = np.array(is_fit)

# data generation
X, y = make_classification(n_features=5, random_state=0)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Standardize the feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Define the model
model = keras.Sequential([
    # Input layer and first hidden layer with 64 neurons and ReLU activation
    layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    # Second hidden layer with 64 neurons and ReLU activation
    layers.Dense(64, activation='relu'),
    # Output layer with 1 neuron and sigmoid activation for binary classification
    layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam', # Optimization algorithm
    loss='binary_crossentropy', # Loss function for binary classification
    metrics=['accuracy'] # Metric to monitor during training
)

# Train the model
history = model.fit(
    X_train, y_train,
    validation_split=0.25, # training data for validation
    epochs=100, # Number of times to iterate over the entire dataset
    batch_size=32 # Number of samples per gradient update
)

# Evaluate model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
print(f'Test accuracy: {test_accuracy}')
