function new_chromo = insertion(chromo, n)
% 基因变异操作中的单点移动，第一个位置是被插入的位置，第二个位置是插入元素的位置
while true
    temp_index = randi([1, n], 1, 2);
    if temp_index(1) ~= temp_index(2) && abs(temp_index(1) - temp_index(2)) > 1
        break; 
    end
end
index1 = temp_index(1);
index2 = temp_index(2);
if index1 < index2
    new_chromo = [chromo(1 : index1), chromo(index2), chromo(index1 + 1 : index2 - 1), chromo(index2 + 1 : end)]; 
else
    new_chromo = [chromo(1 : index2 - 1), chromo(index2 + 1 : index1), chromo(index2), chromo(index1 + 1 : end)];
end
end