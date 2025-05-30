expense = [2345, 2323, 2123, 2567, 2178, 2900]

total = 0

for i in range(len(expense)):
    print("Month:", (i +1), "Expense:", expense[i])

    total = total + expense[i]


print("The total expense is : ", total)

