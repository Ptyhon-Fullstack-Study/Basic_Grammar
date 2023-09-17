def get_total_page(m, n):
    total_page = 0
    if m % n == 0:
        total_page = m // n
    else:
        total_page = m // n + 1
    return total_page

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))