import numpy as np
import math

def cal_gradient(start_height, end_height, xy_distance):
    gradient = int(math.degrees(np.arctan((end_height - start_height) / xy_distance)))
    return gradient
