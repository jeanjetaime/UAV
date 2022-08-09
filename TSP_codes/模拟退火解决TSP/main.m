clc;
close all;
clear;
tic;


%% �����ʼ��
n = 25;  % ������Ŀ
%city_coordinate = unifrnd(0, 100, n, 2);  % ������ɳ�������
city_coordinate = load('citycodi.mat', 'city_coordinate');
city_coordinate = city_coordinate.city_coordinate;
distance_matrix = cal_distance(city_coordinate, n);  % �������
p_swap = 0.2;  % ѡ�񽻻��ĸ���
p_reversion = 0.5;  % ѡ����ת�ĸ���
p_insertion = 1 - p_swap - p_reversion;  % ѡ�����ĸ���  
outer_iter = 300;  % ��ѭ������������
inner_iter = 15;  % ��ѭ������������
T0 = 1;  % ��ʼ�¶�
lambda = 0.99;  % ��ȴϵ��
solution.route = randperm(n);  % ������ɳ�ʼ��
solution.distance = distance(solution.route, distance_matrix);  % ��ʼ��·������
best.route = solution.route;  % ȫ�����Ž�
best.distance = solution.distance;
T = T0;
iter_solution = zeros(1, outer_iter);  % ��¼ÿ�������Ž�
iter_solution(1) = best.distance;


%% ģ���˻���ѭ��
for outer = 2 : outer_iter
    for inner = 1 : inner_iter
         new_route = change(solution.route, p_swap, p_reversion, p_insertion);
         new_distance = distance(new_route, distance_matrix);
         if new_distance < solution.distance
             solution.route =  new_route;
             solution.distance = new_distance;
         else
             delta = new_distance - solution.distance;
             if rand() <= exp(-delta / T)  % ����ģ���˻�ѡ����Ž�
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
        disp(['��' num2str(outer) '�ε�����ȫ������·���ܾ��� = ' num2str(best.distance)]);
    end
    figure(1);
    plot_route(best.route, city_coordinate);
    pause(0.01);
    iter_solution(outer) = best.distance;
end


%% �������
figure;
plot(iter_solution, 'LineWidth', 1);
title('�ܾ�������������仯ͼ');
xlabel('��������');
ylabel('�ܾ���');
toc;