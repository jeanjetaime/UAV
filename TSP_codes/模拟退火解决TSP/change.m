function new_route = change(route, p_swap, p_reversion, p_insertion)
% ����·����һЩ�ı䣬������·��
n = length(route);
p_roulette = cumsum([p_swap, p_reversion, p_insertion]);
temp_num = rand();
if temp_num < p_roulette(1)
    new_route = swap(route, n);
elseif temp_num < p_roulette(2)
    new_route = reversion(route, n);
else
    new_route = insertion(route, n);
end
end