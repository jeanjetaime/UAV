function population = init_pop(pop, n)
% 随机初始化种群
population = struct('chromo', cell(1, pop), 'fitness', 0);
for i = 1 : pop
    population(i).chromo = randperm(n);
end
end