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
    print('Reminder: ')
    for i in a.s_list:
        print(f'-{i}-  (type {x + 1} to choose)')
        x += 1
    x = 0
    s_choice = int(input('Choose from one of the four problems above: '))
    if s_choice == 1:
        print('Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n')
        print('def make_baab(a, b):\n')
        sone_ans = input()
        add_baab = a.Problem('make_baab', 'Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n','def make_baab(a, b):', '\n\treturn b + a + a + b', [("'Hey'", "'Goodbye'"), ("'Up'", "'Down'")])
        add_baab.test_answer(sone_ans)
    if s_choice == 2:
        print("Given a string, measure the length of a string and splice it in half if its an even number. If the length is an odd number, then return the last two characters.\nExample: 'Player' returns 'yer', 'Armadillo' returns 'lo'")
        stwo_ans = input('def split(text, plac):\n')
        split = a.Problem('split', 'measure the length of a string and splice it in half', 'def split(text, plac):\n', '\tif len(text) % 2 > 0:\n\t\treturn text[len(text) - 2:len(text)]\n\treturn text[len(text) // 2:len(text)]', [("'armadillo'", "'cheat'"), ("'pplllasllllasd'", "'wonder'")])
        split.test_answer(stwo_ans)
elif c_choice.lower() == "l":
    for i in a.l_list:
        print(f'-{i}-  (type {x + 1} to choose)')
        x += 1
    x = 0
    v_choice = int(input('Choose from one of the four problems above: '))
    if v_choice == 1:
        print('Given a list, return True if the first or last number is 6.')
        print('def first_lat6(nums):\n')
        vone_ans = input()
        first_last6 = a.Problem('first_last6', 'Given a list, return True if the first or last number is 6.', 'def first_lat6(nums):', '\n\tif nums[0] == 6 or nums[len(nums) - 1] == 6:\n\t\treturn True\n\treturn False', [(0, 6), (2, 1)])
        first_last6.test_answer(vone_ans)