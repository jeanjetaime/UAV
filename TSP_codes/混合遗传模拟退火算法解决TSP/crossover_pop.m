function population = crossover_pop(population, p_crossover)
% 执行群体的交叉操作
len = length(population);
n = length(population(1).chromo);
crossover_index = randperm(len);
for i = 1 : len / 2
    father = population(crossover_index(i * 2 - 1)).chromo;
    mother = population(crossover_index(i * 2)).chromo;
    if rand() < p_crossover
        [population(crossover_index(i * 2 - 1)).chromo, population(crossover_index(i * 2)).chromo] = ox_crossover(father, mother, n);
    end
end
end