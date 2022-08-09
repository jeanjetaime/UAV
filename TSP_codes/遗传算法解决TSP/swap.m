function chromo = swap(chromo, n)
% 执行两点互换的变异操作
while true
    temp_index = randi([1, n], 1, 2);
    if temp_index(1) ~= temp_index(2)
        break; 
    end
end
index1 = min(temp_index);
index2 = max(temp_index);
value1 = chromo(index1);
value2 = chromo(index2);
chromo(index1) = value2;
chromo(index2) = value1;
end