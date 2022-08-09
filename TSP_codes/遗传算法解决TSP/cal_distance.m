function distance_matrix = cal_distance(city_coordinate, n)
% 根据城市坐标计算距离矩阵
distance_matrix = zeros(n);
for i = 1 : n
    for j = 1 : n
        distance_matrix(i, j) = norm(city_coordinate(i, : ) - city_coordinate(j, : )); 
    end
end
end