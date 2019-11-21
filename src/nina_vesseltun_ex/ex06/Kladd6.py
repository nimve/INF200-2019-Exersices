from math import exp

def sigmoid(z):
    for idx, z_element in enumerate(z):
        z[idx] = 1 / (1 + exp(-float(z_element)))
    return z

