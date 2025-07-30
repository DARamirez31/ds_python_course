def find_pe_and_pb(price, eps, book_value):
    pe=price/eps
    pb=price/book_value
    return pe, pb #this returns a tuple

pe_ratio, pb_ratio = find_pe_and_pb(100, 5, 20)
print(pe_ratio, pb_ratio)


