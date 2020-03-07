import numpy as np
import cv2
import numpy as np

img1 = cv2.imread('NL1.jpg',0)
img2 = cv2.imread('NL2.jpg',0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

training_inputs = img1/255

#print(np.info(training_inputs))
training_outputs = img2/255
#print(training_inputs.shape)
#print(training_inputs.ndim)

#print(training_outputs.shape)
#training_inputs = training_inputs.transpose(2,0,1).reshape(3,-1)
print("Training Inputs \n", training_inputs)
print("\n")

#training_outputs = training_outputs.transpose(2,0,1).reshape(3,-1)
print("Expected output \n", training_outputs)
print("\n")

synaptic_weights = 2 * np.random.random((4,4)) - 1


print('Random starting synaptic weights: ')
print(synaptic_weights)
print("\n")

for iteration in range(10000):

    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer.T, synaptic_weights))

    error = training_outputs - outputs
    adjustments = error * sigmoid_derivative(outputs)

    synaptic_weights += np.dot(input_layer.T, adjustments)

#print(outputs.shape)
#print(outputs*100)
print("Predicted ouput")
preimg = (outputs * 255).round()
print(preimg)
cv2.imwrite('preimg.jpg', preimg) 
cv2.imshow('image',preimg)
cv2.waitKey(0)
cv2.destroyAllWindows()