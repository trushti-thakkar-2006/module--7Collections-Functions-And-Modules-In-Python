my_list = [10, 20, 30, 40, 50]

popped_element = my_list.pop()
print("After pop():", my_list)
print("Popped element:", popped_element)

popped_element_at_index = my_list.pop(1)  
print("After pop(1):", my_list)
print("Popped element at index 1:", popped_element_at_index)

my_list.remove(30)  
print("After remove(30):", my_list)
