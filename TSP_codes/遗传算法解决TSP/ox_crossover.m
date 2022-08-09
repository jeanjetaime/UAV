function [new_chromo1, new_chromo2] = ox_crossover(chromo1, chromo2, n)
% 个体OX交叉操作
while true
    temp_index = randi([2, n - 1], 1, 2);
    if temp_index(1) ~= temp_index(2)
        break; 
    end
end
index1 = min(temp_index);
index2 = max(temp_index);
chromo1_part1 = zeros(1, index1 - 1);
chromo1_part2 = chromo1(index1 : index2);
chromo1_part3 = zeros(1, n - index2);
chromo2_part1 = zeros(1, index1 - 1);
chromo2_part2 = chromo2(index1 : index2);
chromo2_part3 = zeros(1, n - index2);
index = 1;
for i = 1 : n
    if ~ismember(chromo2(i), chromo1_part2)
         if index <= index1 - 1
             chromo1_part1(index) = chromo2(i);
         else
             chromo1_part3(index - index1 + 1) = chromo2(i);
         end
         index = index + 1;
    end
end
index = 1;
for i = 1 : n
    if ~ismember(chromo1(i), chromo2_part2)
         if index <= index1 - 1
             chromo2_part1(index) = chromo1(i);
         else
             chromo2_part3(index - index1 + 1) = chromo1(i);
         end
         index = index + 1;
    end
end
new_chromo1 = [chromo1_part1, chromo1_part2, chromo1_part3];
new_chromo2 = [chromo2_part1, chromo2_part2, chromo2_part3];
end