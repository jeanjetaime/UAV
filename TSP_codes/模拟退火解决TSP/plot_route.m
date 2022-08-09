function plot_route(chromo, city_coordinate)
% Â·¾¶»­Í¼
x = city_coordinate(:, 1);
y = city_coordinate(:, 2);
x = x';
y = y';
route = [chromo, chromo(1)];
plot(x(route), y(route), 'k-o', 'MarkerSize', 10, 'LineWidth', 1.5);
xlabel('x');
ylabel('y');
end