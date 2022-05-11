def mult_callback(a,b):
    return a*b

def add_callback(a,b):
    return a+b

def power_callback(a,b):
    return pow(a, b)

def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1, 10):
        print(i, operateur_str, n, "=", operation_cbk(i, n))

afficher_table(2, "+", add_callback)
print()
afficher_table(2, "^", power_callback)