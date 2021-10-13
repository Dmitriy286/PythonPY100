# Напишите ваше решение
TAX = 0.13

salary = int(input("Enter salary amount: "))

tax = (salary / 1.13) * TAX

net_sal = salary - tax

print(tax, net_sal)