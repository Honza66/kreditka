card_number = '1051054488597827'
sum_odd_num = 0
sum_even_num = 0

for index, value in enumerate (card_number):
    value = int(value)
    if index % 2 != 0:
        sum_odd_num = sum_odd_num + value
    else:
        value = value*2
        if value >= 10:
            value = str(value)
            first_num = int(value[0])
            second_num = int(value[1])
            sum_even_num = sum_even_num + first_num + second_num
        else:
            sum_even_num  = sum_even_num + value
    

print(sum_odd_num)
print(sum_even_num)
if (sum_even_num + sum_odd_num) % 10 == 0:
    print('Karta je platná')
else:
    print('Karta je neplatná')
