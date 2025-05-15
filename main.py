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
        sone_ans = input('Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n')
        add_baab = a.Problem('make_baab', 'Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n','def make_baab(a, b):', '\n\treturn b + a + a + b', ["'Hey'", "'Bye'"])
        add_baab.test_answer(sone_ans)
    if s_choice == 2:
        stwo_ans = input("Given a string, measure the length of a string and splice it in half if its an even number. If the length is an odd number, then return the last two characters.\nExample: 'Player' returns 'yer', 'Armadillo' returns 'lo'")
        split = a.Problem('split', 'measure the length of a string and splice it in half', 'def splice(text):\n', '\tif len(text) % 2 > 0:\n\t\treturn text[len(text) - 2:len(text)]\n\treturn text[len(text) // 2:len(text)]', ["'armadillo'", "'cheat'"])
        split.test_answer(stwo_ans)
