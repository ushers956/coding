def missing_no(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr



arr = [2, 3, 4]
print("The missing number IS", missing_no(arr))