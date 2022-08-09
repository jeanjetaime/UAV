function dist = distance(route, distance_matrix)
% ¼ÆËãÂ·¾¶µÄ¾àÀë
dist = 0;
for i = 1 : length(route) - 1
    dist = dist + distance_matrix(route(i), route(i + 1));
end
dist = dist + distance_matrix(route(end), route(1));
end