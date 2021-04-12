string = input()
lists = list([val for val in string if val.isalpha()])
alpha_string = "".join(lists)
print(alpha_string)

