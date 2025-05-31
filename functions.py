toms_exp_list = [1200, 3456, 2345, 3452]
joe_exp_list = [200, 500, 700]

def calculate_total(exp):
    total = 0 
    for item in exp:
        total = item + total
    return total

toms_total = calculate_total(toms_exp_list)
joes_total = calculate_total(joe_exp_list)

print("Tom's total expenses", toms_total)
print("Joe's total expense", joes_total)
