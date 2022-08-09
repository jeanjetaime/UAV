clc;
close all;
clear;
tic;


%% 问题初始化
pop = 50;  % 种群数目
gen = 1000;  % 迭代次数
n = 25;  % 城市数目
%city_coordinate = unifrnd(0, 100, n, 2);  % 随机生成城市坐标
city_coordinate = load('citycodi.mat', 'city_coordinate');
city_coordinate = city_coordinate.city_coordinate;
distance_matrix = cal_distance(city_coordinate, n);  % 距离矩阵
population = init_pop(pop, n);  % 初始化种群
p_crossover = 0.8;  % 交叉概率
p_mutation = 0.2;  % 变异概率
p_swap = 0.2;  % 选择交换的概率
p_reversion = 0.5;  % 选择逆转的概率
p_insertion = 1 - p_swap - p_reversion;  % 选择插入的概率
population = object_function(population, distance_matrix, pop, n);  % 将种群赋予适应度函数，并由高到低排序
best_chromo = struct('chromo', cell(1, gen), 'fitness', 0);  % 记录每代的最优个体
% 将第一代的结果保存到best_chromo中
best_chromo(1).chromo = population(1).chromo;
best_chromo(1).fitness = population(1).fitness;
best.chromo = population(1).chromo;  % 记录历代最优染色体
best.fitness = population(1).fitness;  % 记录历代最优适应度值
T0 = 10;  % 初始温度
lambda = 0.99;  % 冷却系数
inner_iter = 15;  % 内层循环最大迭代次数
T = T0;


%% 混合遗传模拟退火算法循环
for iter = 2 : gen
    % 锦标赛选择
    population = tournament_selection(population, pop);
    % 交叉操作
    population = crossover_pop(population, p_crossover);
    % 变异操作
    population = mutation_pop(population, p_mutation, p_swap, p_reversion, p_insertion);
    % 赋予适应度函数并排序
    population = object_function(population, distance_matrix, pop, n); 
    % 前30%的个体进入模拟退火步骤
    sa_iter = round(pop * 0.4);
    for i = 1 : sa_iter
         [population(i).chromo, population(i).fitness] = sa(population(i).chromo, ...
             population(i).fitness, p_swap, p_reversion, p_insertion, distance_matrix, sa_iter, T, n);
    end
    T = T * lambda;
    % 重新根据适应度值排序
    population = object_function(population, distance_matrix, pop, n);
    % 更新群体最优
    best_chromo(iter).chromo = population(1).chromo;
    best_chromo(iter).fitness = population(1).fitness;
    % 更新历代最优
    if best.fitness > best_chromo(iter).fitness
        best.fitness = best_chromo(iter).fitness;
        best.chromo = best_chromo(iter).chromo;
    end
    % 结果展示
    if mod(iter, 20) == 0
        disp(['第' num2str(iter) '次迭代：全局最优路线总距离 = ' num2str(best.fitness)]); 
    end
    figure(1);
    plot_route(best.chromo, city_coordinate);
    pause(0.01);
end


%% 结果处理
figure;
plot([best_chromo.fitness], 'LineWidth', 1);
title('总距离随迭代次数变化图');
xlabel('迭代次数');
ylabel('总距离');
toc;

