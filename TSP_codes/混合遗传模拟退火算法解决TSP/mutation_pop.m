function population = mutation_pop(population, p_mutation, p_swap, p_reversion, p_insertion)
% 执行群体的变异操作
pop = length(population);
p_roulette = cumsum([p_swap, p_reversion, p_insertion]);
n = length(population(1).chromo);
for i = 1 : pop
    if rand() < p_mutation
         temp_num = rand();
         if temp_num < p_roulette(1)  % 执行轮盘赌操作
             population(i).chromo = swap(population(i).chromo, n);
         elseif temp_num < p_roulette(2)
             population(i).chromo = reversion(population(i).chromo, n);
         else
             population(i).chromo = insertion(population(i).chromo, n); 
         end
    end
end
end