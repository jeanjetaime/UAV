function new_chromo = insertion(chromo, n)
% �����������еĵ����ƶ�����һ��λ���Ǳ������λ�ã��ڶ���λ���ǲ���Ԫ�ص�λ��
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