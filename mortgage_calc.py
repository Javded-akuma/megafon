mortgage = 1000000
rate = 10
rate_month = rate/100/12
years = 5
months = years * 12 
#Платеж в месяц
pay = round(mortgage * (rate_month * (1 + rate_month) ** months) / ((1 + rate_month) ** months - 1),2)
#Сумма платежей за 5 лет
all_sum = round((pay * 12) * years, 2)
print(f'Переплата за 5 лет: {round(all_sum - mortgage, 2)} рублей')    