function chromo = change(chromo, p_swap, p_reversion, p_insertion, n)
% ģ���˻����ı�
p_roulette = cumsum([p_swap, p_reversion, p_insertion]);
temp_num = rand();
if temp_num < p_roulette(1)
    chromo = swap(chromo, n);
elseif temp_num < p_roulette(2)
    chromo = reversion(chromo, n);
else
    chromo = insertion(chromo, n);
end
end