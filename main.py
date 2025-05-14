import app as a
from simple_colors import *
x = 0
# Franko Nava-Islas
# Comp Sci Final
# Strings, Lists, Boolean, Vocabulary

user_name = input("Input a username: ")
print(f'Welcome to Butterfly, {user_name}.\n\nCategories:')

for i in a.categories:
    print(f'--{i}--  (type {a.categories[x][0]} to choose)')
    x += 1
x = 0

c_choice = input('Choose from one of the four categories above: ')
print('\nProblems:')
if c_choice.lower() == "s":
    for i in a.s_list:
        print(f'-{i}-  (type {x + 1} to choose)')
        x += 1
    s_choice = int(input('Choose from one of the four problems above: '))
    if s_choice == 1:
        s_answer = input('Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n')
        test_one = a.Problem('make_baab', 'Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n','def make_baab(a, b):', '\n\treturn b + a + a + b', ["'Hey'", "'Bye'"])
        test_one.test_answer(s_answer)