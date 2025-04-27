import numpy as np

def construct_matrix(first_array, second_array):
    return np.array([first_array, second_array]).reshape((first_array.shape[0], 2)) # <- your first right code here

