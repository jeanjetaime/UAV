function population = object_function(population, distance_matrix, pop, n)
% 计算种群的适应度值，并按照适应度值从大到小排队
for i = 1 : pop
    population(i).fitness = 0;
    for j = 1 : n - 1
        population(i).fitness = population(i).fitness + ...
            distance_matrix(population(i).chromo(j), population(i).chromo(j + 1));
    end
    population(i).fitness = population(i).fitness + distance_matrix...
        (population(i).chromo(n), population(i).chromo(1));
end
[~, index] = sort([population.fitness]);
population = population(index);
end