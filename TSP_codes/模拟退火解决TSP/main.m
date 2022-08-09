clc;
close all;
clear;
tic;


%% 问题初始化
n = 25;  % 城市数目
%city_coordinate = unifrnd(0, 100, n, 2);  % 随机生成城市坐标
city_coordinate = load('citycodi.mat', 'city_coordinate');
city_coordinate = city_coordinate.city_coordinate;
distance_matrix = cal_distance(city_coordinate, n);  % 距离矩阵
p_swap = 0.2;  % 选择交换的概率
p_reversion = 0.5;  % 选择逆转的概率
p_insertion = 1 - p_swap - p_reversion;  % 选择插入的概率  
outer_iter = 300;  % 外循环最大迭代次数
inner_iter = 15;  % 内循环最大迭代次数
T0 = 1;  % 初始温度
lambda = 0.99;  % 冷却系数
solution.route = randperm(n);  % 随机生成初始解
solution.distance = distance(solution.route, distance_matrix);  % 初始解路径长度
best.route = solution.route;  % 全局最优解
best.distance = solution.distance;
T = T0;
iter_solution = zeros(1, outer_iter);  % 记录每代的最优解
iter_solution(1) = best.distance;


%% 模拟退火主循环
for outer = 2 : outer_iter
    for inner = 1 : inner_iter
         new_route = change(solution.route, p_swap, p_reversion, p_insertion);
         new_distance = distance(new_route, distance_matrix);
         if new_distance < solution.distance
             solution.route =  new_route;
             solution.distance = new_distance;
         else
             delta = new_distance - solution.distance;
             if rand() <= exp(-delta / T)  % 进入模拟退火，选择次优解
                 solution.route = new_route;
                 solution.distance = new_distance;
             end
         end
    end
    T = T * lambda;
    if best.distance > solution.distance
        best.route = solution.route;
        best.distance = solution.distance;
    end
    if mod(outer, 20) == 0
        disp(['第' num2str(outer) '次迭代：全局最优路线总距离 = ' num2str(best.distance)]);
    end
    figure(1);
    plot_route(best.route, city_coordinate);
    pause(0.01);
    iter_solution(outer) = best.distance;
end


%% 结果处理
figure;
plot(iter_solution, 'LineWidth', 1);
title('总距离随迭代次数变化图');
xlabel('迭代次数');
ylabel('总距离');
toc;