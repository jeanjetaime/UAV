function new_chromo = reversion(chromo, n)
% 执行个体反转变异操作
while true
    temp_index = randi([2, n - 1], 1, 2);
    if temp_index(1) ~= temp_index(2)
        break; 
    end
end
index1 = min(temp_index);
index2 = max(temp_index);
new_chromo = [chromo(1 : index1 - 1), chromo(index2 : -1 : index1), chromo(index2 + 1 : end)];
end