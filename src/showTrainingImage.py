from mnist_loader import load_data_wrapper
from PIL import Image
import numpy as np


# created by Xing

def showImage(num):
	training_data, validation_data, test_data = load_data_wrapper()
	tup = training_data[num]
	size = 28
	imageExample = [[0]*size for i in range(0, size)]
	image = tup[0]

	for i in range(0, size):
		for j in range(0, size):
			imageExample[i][j] = image[i*size+j][0]

	for i in range(0, size):
		for j in range(0, size):
			print "%.4f"%(imageExample[i][j]),
		print


	# print "plot image: "
	image = np.reshape(image, (size, size))
	im = Image.fromarray(image, "I")
	im.show()

	print "actual number: "
	result = tup[1]
	res = 0
	for i in range(0, 10):
		if result[i] == 1:
			res = i
			break
	print res
