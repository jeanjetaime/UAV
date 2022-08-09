function [chromo, dist] = sa(chromo, dist, p_swap, p_reversion, p_insertion, distance_matrix, sa_iter, T, n)
% 执行单一chromo的模拟退火操作
for i = 1 : sa_iter
    new_chromo = change(chromo, p_swap, p_reversion, p_insertion, n);
    new_distance = distance(new_chromo, distance_matrix);
    if new_distance < dist
         chromo = new_chromo;
         dist = new_distance;
    else
        delta = new_distance - dist;
        if rand() <= exp(-delta / T)
            chromo = new_chromo;
            dist = new_distance;
        end
    end
end
end