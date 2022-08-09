function new_population = tournament_selection(population, pop)
% 二元锦标赛选择操作
new_population = struct('chromo', cell(1, pop), 'fitness', 0);
for i = 1 : pop
    while true
        temp_index = randi([1, pop], 1, 2);
        if temp_index(1) ~= temp_index(2)
            break; 
        end
    end
    index1 = temp_index(1);
    index2 = temp_index(2);
    if population(index1).fitness <= population(index2).fitness
        new_population(i).chromo = population(index1).chromo;
        new_population(i).fitness = population(index1).fitness;
    else
        new_population(i).chromo = population(index2).chromo;
        new_population(i).fitness = population(index2).fitness;
    end
end
end