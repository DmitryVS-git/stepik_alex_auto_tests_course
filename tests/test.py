price1 = '$29.99'
price2 = '$11.01'

prices = [price1, price2]

a = sum(map(float, [i.lstrip('$') for i in prices]))
print(a)