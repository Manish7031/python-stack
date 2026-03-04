## Artificial neural network for image classification with 2 hidden layer

import numpy as np
import tensorflow as tf
from tensorflow.python.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.layers import LeakyReLU

np.random.seed(42)
tf.random.set_seed(42)

num_samples = 2000
img_height = 28
img_width = 28
num_classes = 10

# Random grayscale images (0-255)
X = np.random.randint(0, 256, size=(num_samples, img_height, img_width))

# Random labels (0-9)
y = np.random.randint(0, num_classes, size=(num_samples,))

# Normalize images (0-1)
X = X / 255.0

# One-hot encode labels
y = to_categorical(y, num_classes)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build ANN Model
model = Sequential([
    
    Flatten(input_shape=(28, 28)),   # Convert 28x28 -> 784
    
    Dense(128, activation='relu'),   # Hidden Layer 1
    
    Dense(64, activation='relu'),    # Hidden Layer 2
    
    Dense(num_classes, activation='softmax')  # Output Layer
])

# Compile Model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train Model
history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Evaluate Model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_accuracy)

# Predictions
predictions = model.predict(X_test[:5])
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test[:5], axis=1)
print("Predicted Classes:", predicted_classes)
print("True Classes:", true_classes)