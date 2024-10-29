global_var = "I am global!"
def print_variables():
    print(global_var)
    local_var = "I am local!"
    print(local_var)
# print(local_var) This will break the code as it is not defined outside the function.
print_variables()