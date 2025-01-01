def main():
    number = 5
    extra = 2
    add = 5
    double(number, extra)
    addition(number, add)
    
def double(n, e):
    new_number = n * e
    print_double(new_number)
    
def print_double(new_number):
    print(f"This is double {new_number}")
    
    
def addition(n, a):
    new_addition = n + a
    print_addition(new_addition)
    
def print_addition(new_addition):
    print(f"This is with 5 added {new_addition}")
    
    
main()
    

    
    