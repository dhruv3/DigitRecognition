# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:24:18 2016

@author: Dhruv
"""
def getParameter():
    f = open('parameter.txt', 'r')
    lines = f.read().split('####')
    w1 = lines[1].replace("\n", " ").replace("] [", "],[").split('],[')
    for index in range(len(w1)):
        w1[index] = w1[index].replace('[', '').replace(']', '').replace(' ', ',').split(',')
        w1[index] = filter(None, w1[index])
        w1[index] = map(float, w1[index])

    w2 = lines[2].replace("\n", " ").replace("] [", "],[").split('],[')
    for index in range(len(w2)):
        w2[index] = w2[index].replace('[', '').replace(']', '').replace(' ', ',').split(',')
        w2[index] = filter(None, w2[index])
        w2[index] = map(float, w2[index])

    hid_offset  = lines[3].replace("\n", ",").split(',')
    hid_offset = filter(None, hid_offset)
    hid_offset = map(float, hid_offset)

    out_offset = lines[4].replace("\n", ",").split(',')
    out_offset = filter(None, out_offset)
    out_offset = map(float, out_offset)

    f.close()

    return (w1, w2, hid_offset, out_offset)
