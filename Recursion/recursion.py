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


# Base Case
'''
1. Build a stack with the boxes that will be analyzed.
2. Pick up a box and look what it has inside.
3. If you find another box inside, add in a new stack to be verified later.
4. If you find the key, its done.
5. Repeat.
'''
def search_for_the_key(main_box):
    stack = main_box.get_boxes() 
    while stack:  
        box = stack.pop()  
        for item in box:  
            if item.is_box():  
                stack.append(item)  
            elif item.is_key():  
                print("I found the key!")  
                return  

# Recursive Case
'''
1. Look whats inside of the box.
2. If you find another box, come back to step 1.
3. If you find the key, its done!
'''
def search_for_the_key(box):
    for item in box:
        if item.is_box():
            search_for_the_key(item)
        elif item.is_key():
            print('I found the key!')
