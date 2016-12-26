from getMatrix import getMatrix
import math
import numpy as np
from mnist_loader import load_data_wrapper
from predict_one import predict
from training import TrainNetwork
from getParameter import getParameter

training_data, validation_data, test_data = load_data_wrapper()

test_matrix, test_result = getMatrix(test_data, "test")

train_matrix, train_result = getMatrix(training_data, "train")

# w1, w2, hid_offset, out_offset = TrainNetwork(train_matrix, train_result)

w1, w2, hid_offset, out_offset = getParameter()

number = len(test_matrix)

# calculate accuracy
count = [0 for i in range(0, 10)]
correct = [0 for i in range(0, 10)]

for i in range(0, number):
    weget = predict(w1, w2, hid_offset, out_offset, test_matrix[i])
    actual = test_result[i]
    #print "weget "+str(weget)+" actual"+str(actual)
    count[actual] = count[actual]+1
    if weget == actual:
        correct[actual] = correct[actual]+1

print "accuracy : "
for i in range(0, 10):
    print "for number "+str(i)+" accuracy is :",
    print "count "+str(count[i])+" correct "+str(correct[i])
    print (1.0*correct[i])/(1.0*count[i])
