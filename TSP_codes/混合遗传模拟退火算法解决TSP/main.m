clc;
close all;
clear;
tic;


%% �����ʼ��
pop = 50;  % ��Ⱥ��Ŀ
gen = 1000;  % ��������
n = 25;  % ������Ŀ
%city_coordinate = unifrnd(0, 100, n, 2);  % ������ɳ�������
city_coordinate = load('citycodi.mat', 'city_coordinate');
city_coordinate = city_coordinate.city_coordinate;
distance_matrix = cal_distance(city_coordinate, n);  % �������
population = init_pop(pop, n);  % ��ʼ����Ⱥ
p_crossover = 0.8;  % �������
p_mutation = 0.2;  % �������
p_swap = 0.2;  % ѡ�񽻻��ĸ���
p_reversion = 0.5;  % ѡ����ת�ĸ���
p_insertion = 1 - p_swap - p_reversion;  % ѡ�����ĸ���
population = object_function(population, distance_matrix, pop, n);  % ����Ⱥ������Ӧ�Ⱥ��������ɸߵ�������
best_chromo = struct('chromo', cell(1, gen), 'fitness', 0);  % ��¼ÿ�������Ÿ���
% ����һ���Ľ�����浽best_chromo��
best_chromo(1).chromo = population(1).chromo;
best_chromo(1).fitness = population(1).fitness;
best.chromo = population(1).chromo;  % ��¼��������Ⱦɫ��
best.fitness = population(1).fitness;  % ��¼����������Ӧ��ֵ
T0 = 10;  % ��ʼ�¶�
lambda = 0.99;  % ��ȴϵ��
inner_iter = 15;  % �ڲ�ѭ������������
T = T0;


%% ����Ŵ�ģ���˻��㷨ѭ��
for iter = 2 : gen
    % ������ѡ��
    population = tournament_selection(population, pop);
    % �������
    population = crossover_pop(population, p_crossover);
    % �������
    population = mutation_pop(population, p_mutation, p_swap, p_reversion, p_insertion);
    % ������Ӧ�Ⱥ���������
    population = object_function(population, distance_matrix, pop, n); 
    % ǰ30%�ĸ������ģ���˻���
    sa_iter = round(pop * 0.4);
    for i = 1 : sa_iter
         [population(i).chromo, population(i).fitness] = sa(population(i).chromo, ...
             population(i).fitness, p_swap, p_reversion, p_insertion, distance_matrix, sa_iter, T, n);
    end
    T = T * lambda;
    % ���¸�����Ӧ��ֵ����
    population = object_function(population, distance_matrix, pop, n);
    % ����Ⱥ������
    best_chromo(iter).chromo = population(1).chromo;
    best_chromo(iter).fitness = population(1).fitness;
    % ������������
    if best.fitness > best_chromo(iter).fitness
        best.fitness = best_chromo(iter).fitness;
        best.chromo = best_chromo(iter).chromo;
    end
    % ���չʾ
    if mod(iter, 20) == 0
        disp(['��' num2str(iter) '�ε�����ȫ������·���ܾ��� = ' num2str(best.fitness)]); 
    end
    figure(1);
    plot_route(best.chromo, city_coordinate);
    pause(0.01);
end


%% �������
figure;
plot([best_chromo.fitness], 'LineWidth', 1);
title('�ܾ�������������仯ͼ');
xlabel('��������');
ylabel('�ܾ���');
toc;

