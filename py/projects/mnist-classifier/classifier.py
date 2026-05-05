# =============================================================================
# PROJECT: MNIST Classifier from Scratch (NumPy only)
# =============================================================================
# Roadmap: AI/ML Mini — "MNIST classifier from scratch (NumPy only)"
# Architecture: 784 → 128 → 64 → 10 (softmax output)
#
# TODO 1: Data loading
#   pip install mnist  OR  use: from sklearn.datasets import load_digits (8x8 subset)
#   - Normalize pixels to [0, 1]
#   - One-hot encode labels
#   - Split: 80% train, 10% val, 10% test
#
# TODO 2: Forward pass
#   - Linear: Z = X @ W + b
#   - ReLU:   A = max(0, Z)
#   - Softmax: exp(Z - max(Z)) / sum(...)  ← numerical stability
#
# TODO 3: Loss — categorical cross-entropy
#   L = -mean(sum(y_true * log(y_pred + 1e-8), axis=1))
#
# TODO 4: Backward pass (manual backprop)
#   - dL/dZ (softmax + cross-entropy combined derivative = y_pred - y_true)
#   - dL/dW = X.T @ dZ / N
#   - dL/db = mean(dZ, axis=0)
#   - dL/dX = dZ @ W.T (pass to previous layer)
#
# TODO 5: Training loop
#   - Mini-batch SGD (batch_size=32)
#   - Learning rate: 0.01 with step decay every 10 epochs
#   - Track train/val loss + accuracy each epoch
#   - Print: "Epoch 5/50 — loss: 0.312 — val_acc: 0.923"
#
# TODO 6: Evaluation
#   - Test accuracy on held-out set (target: >95%)
#   - Confusion matrix (matplotlib)
#   - Show 9 misclassified examples in a 3x3 grid
#
# TODO 7: Extensions
#   - Momentum (v = beta*v - lr*grad; W += v)
#   - Dropout (randomly zero activations during training)
#   - He initialization (std = sqrt(2 / fan_in))
#
# Run: python classifier.py
# Install: pip install numpy matplotlib
# =============================================================================

import numpy as np

def relu(Z: np.ndarray) -> np.ndarray:
    return np.maximum(0, Z)

def relu_grad(Z: np.ndarray) -> np.ndarray:
    return (Z > 0).astype(float)

def softmax(Z: np.ndarray) -> np.ndarray:
    exp = np.exp(Z - Z.max(axis=1, keepdims=True))
    return exp / exp.sum(axis=1, keepdims=True)

def cross_entropy(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    # TODO: implement — return scalar loss
    return 0.0

class NeuralNetwork:
    def __init__(self, layer_sizes: list[int]):
        """He initialization for weights."""
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            fan_in = layer_sizes[i]
            # TODO: W = np.random.randn(fan_in, fan_out) * sqrt(2/fan_in)
            # TODO: b = np.zeros((1, fan_out))
            pass

    def forward(self, X: np.ndarray) -> np.ndarray:
        """TODO: implement forward pass, cache activations for backprop"""
        return X

    def backward(self, y_true: np.ndarray) -> list[tuple]:
        """TODO: implement backprop, return list of (dW, db) per layer"""
        return []

    def update(self, grads: list[tuple], lr: float):
        """TODO: gradient descent update"""
        pass

    def fit(self, X_train, y_train, X_val, y_val,
            epochs=50, batch_size=32, lr=0.01):
        """TODO: implement training loop with progress printing"""
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """TODO: return predicted class indices"""
        return np.zeros(len(X), dtype=int)
