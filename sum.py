def sum_gr_100(arr):
    sum = 0
    for el in arr:
        sum = sum + el
    if sum > 100:
        return sum
    else:
        return False
