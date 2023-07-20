counter = 0

def create_scope(default):
    counter = default * 2
    
    def nonlocal_print():
        nonlocal_counter
        print(f"scoped {counter}) 

    def global_print(): 
        global counter
        print(f"global {counter}")
