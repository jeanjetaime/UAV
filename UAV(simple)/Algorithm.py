import sys
# import matplotlib
# matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qt_material import apply_stylesheet
import random
import math
import copy
from cal_gradient import cal_gradient


def cal_distance(coordinate):
    """
    计算距离矩阵
    :param coordinate: 坐标
    :return: distance_matrix
    """
    distance_matrix = []
    for i in range(len(coordinate)):
        distance_matrix.append([])
        for j in range(len(coordinate)):
            distance_matrix[i].append(math.sqrt((coordinate[i][0] - coordinate[j][0]) ** 2 +
                                                (coordinate[i][1] - coordinate[j][1]) ** 2))
    return distance_matrix


def distance(route, distance_matrix):
    """
    计算路径route的距离
    :param route: route
    :param distance_matrix: distance metrix
    :return: distance
    """
    dist = 0
    # if len(route) > 3:
    #     for i in range(3):
    #         dist += distance_matrix[route[i]][route[i + 1]]
    #     dist += distance_matrix[route[2]][route[0]]
    #     for i in range(len(route) - 3):
    #         dist += distance_matrix[route[i + 3]][route[i + 3 + 1]]
    #     dist += distance_matrix[route[-1]][route[3]]
    # else:
    for i in range(len(route) - 1):
        dist += distance_matrix[route[i]][route[i + 1]]
    dist += distance_matrix[route[-1]][route[0]]
    return dist


def swap(route):
    """
    执行两点互换操作
    :param route:
    :return:
    """
    new_route = copy.deepcopy(route)
    index = copy.deepcopy(route)
    random.shuffle(index)
    index1 = max(index[0], index[1])
    index2 = min(index[0], index[1])
    temp_value = route[index1]
    route[index1] = route[index2]
    route[index2] = temp_value
    return new_route


def insertion(route):
    """
    基因变异操作中的单点移动，第一个位置是被插入位置，第二个位置是插入元素的位置
    :param route:
    :return:
    """
    new_route = copy.deepcopy(route)
    index = copy.deepcopy(route)
    random.shuffle(index)
    index1 = max(index[0], index[1])
    index2 = min(index[0], index[1])
    new_route.remove(route[index1])
    new_route.insert(index2, route[index1])
    return new_route


def reversion(route):
    """
    执行个体反转变异操作
    :param route:
    :return:
    """
    new_route = []
    index = copy.deepcopy(route)
    random.shuffle(index)
    index1 = min(index[0], index[1], 1)
    index2 = max(index[0], index[1], len(index) - 2)
    for i in range(index1):
        new_route.append(route[i])
    for i in range(index2 - 1, index1 - 1, -1):
        new_route.append(route[i])
    for i in range(index2, len(route)):
        new_route.append(route[i])
    return new_route


def change(route, p_swap, p_reversion, p_insertion):
    """
    对旧路径进行变异，生成新路径
    :param route:
    :param p_swap:
    :param p_reversion:
    :param p_insertion:
    :return:
    """
    p_roulette = [p_swap, p_swap + p_reversion, 1]
    temp_num = random.random()
    if temp_num < p_roulette[0]:
        new_route = swap(route)
    elif temp_num < p_roulette[1]:
        new_route = reversion(route)
    else:
        new_route = insertion(route)
    return new_route


def main(coordinate):
    """
    模拟退火求解TSP主函数
    :param coordinate: 坐标，二维数组，第一个坐标为起点(终点)
    :return:
    """
    # 参数定义
    n = len(coordinate)  # 点的个数
    distance_matrix = cal_distance(coordinate)  # 距离矩阵
    p_swap = 0.2  # 选择交换的概率
    p_reversion = 0.5  # 选择逆转的概率
    p_insertion = 1 - p_reversion - p_swap  # 选择插入的概率
    outer_iter = 300  # 外循环最大迭代次数
    inner_iter = 15  # 内循环最大迭代次数
    T0 = 1  # 初始温度
    lambda1 = 0.99  # 冷却系数
    solution_route = [i for i in range(n)]  # 生成初始解
    random.shuffle(solution_route)
    solution_dist = distance(solution_route, distance_matrix)  # 初始解长度
    best_solution = copy.deepcopy(solution_route)  # 全局最优解
    best_dist = solution_dist  # 全局最短路径长度
    iter_solution = [best_dist]  # 记录每代的最优解
    T = T0  # 初始温度

    # 模拟退火算法主循环
    for outer in range(1, outer_iter):
        for inner in range(inner_iter):
            new_route = change(solution_route, p_swap, p_reversion, p_insertion)
            new_distance = distance(new_route, distance_matrix)
            if new_distance < solution_dist:
                solution_route = copy.deepcopy(new_route)
                solution_dist = new_distance
            else:
                delta = new_distance - solution_dist
                if random.random() <= math.exp(-delta / T):
                    solution_route = copy.deepcopy(new_route)
                    solution_dist = new_distance
        T = T * lambda1
        if best_dist > solution_dist:
            best_solution = copy.deepcopy(solution_route)
            best_dist = solution_dist
        iter_solution.append(solution_dist)
    return best_solution


def lonlat2meter(coordinate):
    """
    经纬度转换成米
    :param coordinate:
    :return:
    """
    new_coordinate = [[0, 0]]
    for i in range(1, len(coordinate)):
        new_coordinate.append([
            (coordinate[i][0] - coordinate[0][0]) * 111194.926644558727,
            (coordinate[i][1] - coordinate[0][1]) * 111194.926644558737 * math.cos(coordinate[0][1])
        ])
    return new_coordinate