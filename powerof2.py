def pow_of_two_rec(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return pow_of_two_rec(n / 2)
    return False