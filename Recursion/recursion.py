'''

Recursive function: The function calls itself, breaking down a problem into smaller subproblems.
Base Case: Stops the function from calling itself and returning a result.

'''

#Exemple
def countdown(i):
    # Base Case
    if i <= 0:
        return 0
    # Recursive Case
    else:
        print(i)
        countdown(i-1)



def search_for_the_key(chest):
    stack = main_box.c