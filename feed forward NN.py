import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.random.rand(1, self.hidden_size)
        
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.random.rand(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        # Forward pass
        hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        hidden_output = self.sigmoid(hidden_input)
        
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_hidden_output
        predicted_output = self.sigmoid(output_input)
        
        return predicted_output

# Example usage:
input_size = 2
hidden_size = 3
output_size = 1

# Create a neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Input values
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Get predictions
predictions = nn.forward(inputs)
print("Predictions:")
print(predictions)
