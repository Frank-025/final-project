import app as a

# Franko Nava-Islas
# Comp Sci Final
# Strings, Lists, Boolean, Vocabulary

user_name = input("Input a username: ")
print(f'Welcome to Butterfly, {user_name}.\nCategories:')

x = 0
for i in a.categories:
    print(f'--{i}--  (type {a.categories[x][0]} to choose)')
    x += 1

c_choice = input('Choose from one of the four categories above.')