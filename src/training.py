from getMatrix import getMatrix
import math
import numpy as np
from mnist_loader import load_data_wrapper

"""
# define parameter
# sample number 50000
samp_num = len(train_result)
# input parameter number, 784
in_num = len(train_matrix[0])
# output paramter number
out_num = 10
# hidden number, only one layer
hid_num = 25
"""
"""
w1 = 0.2*np.random.random((in_num, hid_num))- 0.1
w2 = 0.2*np.random.random((hid_num, out_num))- 0.1   #
hid_offset = np.zeros(hid_num)     #
out_offset = np.zeros(out_num)     #
inp_lrate = 0.3             #
hid_lrate = 0.3             #
err_th = 0.01                #
"""


def MatrixToTxt(w, f):
    for i in range(0, len(w)):
        f.write(str(w[i]))
        f.write('\n')

# define Sigmoid function
def get(x):
    act_vec=[]
    for i in x:
        act_vec.append(1/(1+math.exp(-i)))
    act_vec=np.array(act_vec)
    return act_vec

def TrainNetwork(sample,label):
    # sample is 50 000 x 784
    # label is 50 000 x 1, each row corresponds to a integer from 0 to 9
    sample_num = len(sample)
    sample_len = len(sample[0])
    out_num = 10
    hid_num = 25
    w1 = 0.2 * np.random.random((sample_len, hid_num)) - 0.1
    #print "w1 size: "+str(len(w1))+" "+str(len(w1[0]))
    w2 = 0.2 * np.random.random((hid_num, out_num)) - 0.1
    #print "w2 size: "+str(len(w2))+" "+str(len(w2[0]))
    hid_offset = np.zeros(hid_num)
    out_offset = np.zeros(out_num)
    input_learnrate = 0.2
    hid_learnrate = 0.2
    for i in range(0,len(sample)):
        print "training sample "+str(i)
        t_label=np.zeros(out_num)
        t_label[label[i]]=1

        # front
        hid_value=np.dot(sample[i], w1)+hid_offset #
        hid_act=get(hid_value)                 #
        out_value=np.dot(hid_act, w2)+out_offset
        out_act=get(out_value)    #

        # back
        err=t_label-out_act
        out_delta=err*out_act*(1-out_act) #
        hid_delta = hid_act*(1 - hid_act) * np.dot(w2, out_delta)
        for j in range(0,out_num):
            w2[:,j]+=hid_learnrate*out_delta[j]*hid_act
        for k in range(0,hid_num):
            for row in range(0, len(w1)):
                w1[row, k]+=input_learnrate*hid_delta[k]*sample[i][row]

        out_offset += hid_learnrate * out_delta   #
        hid_offset += input_learnrate * hid_delta

    f = open('parameter.txt', 'w')

    f.write("w1\n")
    MatrixToTxt(w1, f)

    f.write("w2\n")
    MatrixToTxt(w2, f)

    f.write("hid_offset\n")
    MatrixToTxt(hid_offset, f)

    f.write("out_offset\n")
    MatrixToTxt(out_offset, f)

    f.close()

    return w1,w2,hid_offset,out_offset

"""
training_data, validation_data, test_data = load_data_wrapper()

train_matrix, train_result = getMatrix(training_data, "train")

print "get data"

w1,w2,hid_offset,out_offset = TrainNetwork(train_matrix, train_result)

"""
