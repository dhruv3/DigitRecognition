import numpy as np
import math

# load w1,w2,hid_offset,out_offset

def get(x):
    act_vec=[]
    for i in x:
        act_vec.append(1/(1+math.exp(-i)))
    act_vec=np.array(act_vec)
    return act_vec

def predict(w1, w2, hid_offset, out_offset, image):
    # image is 1 x 784
    hid_value=np.dot(image, w1)+hid_offset #
    hid_act=get(hid_value)                 #
    out_value=np.dot(hid_act, w2)+out_offset
    out_act=get(out_value)
    index = 0
    max = out_act[index]
    for i in range(1, 10):
        if out_act[i] > max:
            index = i
            max = out_act[i]
    return index
