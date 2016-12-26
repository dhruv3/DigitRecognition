from mnist_loader import load_data_wrapper
import types

# created by Xing

size = 28

def getMatrix(training_data, type):

    # parse training_data
    training_row = len(training_data)
    training_matrix = []
    training_result = []

    for i in range(0, training_row):
        one_matirx, res = getOne(training_data[i], type)
        training_matrix.append(one_matirx)
        training_result.append(res)
    return (training_matrix, training_result)


def getOne(training_data_one, type):
    x = training_data_one[0]
    result = training_data_one[1]
    one_matrix = [0 for i in range(0, len(x))]
    for i in range(0, len(x)):
        one_matrix[i] = x[i][0]
    res = 0

    if type == "test":
        res = int(result)
        return (one_matrix, res)

    for i in range(0, 10):
		if result[i] == 1:
			res = i
			break

    return (one_matrix, res)
