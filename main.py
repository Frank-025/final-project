import app as a
x = 0
# Franko Nava-Islas
# Comp Sci Final
# Strings, Lists, Boolean, Vocabulary

user_name = input("Input a username: ")
print(f'Welcome to Butterfly, {user_name}.\nCategories:')

for i in a.categories:
    print(f'--{i}--  (type {a.categories[x][0]} to choose)')
    x += 1
x = 0

c_choice = input('Choose from one of the four categories above: ')
print('\nProblems:')
if c_choice.lower() == "s":
    for i in a.s_list:
        print(f'--{i}--  (type {x + 1} to choose)')
        x += 1
    s_choice = input('Choose from one of the four categories above: ')
    if s_choice.lower() == "1":
        pass