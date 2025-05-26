import app as a
check = True
# Franko Nava-Islas
# Comp Sci Final
# Strings, Lists, Boolean, Vocabulary

user_name = input("Input a username: ")
print(f'Welcome to Strings, {user_name}.')
x = 0
print('Reminder: You have to manually type in backslash + "n" to add a new line, and backslash + "t" to add a tab.')

while check is True:
    print('\nProblems: ')
    for i in a.s_list:
        print(f'-{i}-  (type {x + 1} to choose)')
        x += 1
    s_choice = int(input('Choose from one of the four problems above: '))
    if s_choice == 1:
        print('Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n')
        sone_ans = input('def make_baab(a, b): ')
        print(sone_ans)
        add_baab = a.Problem('make_baab', 'Given two strings, b and a, return the result of putting them together in the order baab.\nExample: "Hey" and "Goodbye" returns "GoodbyeHeyHeyGoodbye".\n','def make_baab(a, b):\n\t', 'return b + a + a + b', [("'Hey'", "'Goodbye'"), ("'Up'", "'Down'")])
        add_baab.test_answer(sone_ans)
    elif s_choice == 2:
        print("Given a string, measure the length of a string and splice it in half if its an even number. If the length is an odd number, then return the last two characters.\nExample: 'Player' returns 'yer', 'Armadillo' returns 'lo'")
        stwo_ans = input('def split(text): ')
        # Weird cases of the code breaking. These 2 lines of code below works perfectly fine in the app.py file, but it doesn't work once tested here.
        split = a.Problem('split', 'measure the length of a string and splice it in half', 'def split(text, plac):\n',
               '\tif len(text) % 2 > 0:\n\t\treturn text[len(text) - 2:len(text)]\n\treturn text[len(text) // 2:len(text)]',
               [("'armadillo'", "'cheat'"), ("'pplllasllllasd'", "'wonder'")])
        split.test_answer(stwo_ans)
    elif s_choice == 3:
        print('Given a string, return a new string with three copies of the last two places of a string\n For example, "Orange" returns "gegege"')
        sthree_ans = input('def extra3_end(text): ')
        extra3_end = a.Problem('extra3_end', 'Given a string, return a new string with three copies of the last two places of a string\n For example, "Orange" returns "gegege"', 'def extra3_end(text, plac):\n\t','lastc = len(text) - 2\n\treturn text[lastc:] + text[lastc:] + text[lastc:]', [("'Rainbow'", "'Element'"), ("'Science'", "'Multiplication'")])
        extra3_end.test_answer(sthree_ans)
    elif s_choice == 4:
        print('Given a string, return a greeting in the form of "Hello Jake!"')
        sfour_ans = input('def greeting(text): ')
        greeting = a.Problem('greeting', 'Given a string, return a greeting in the form of "Hello Jake!"', 'def greeting(text, plac):\n', 'return "Hello " + text + "!"', [("'Natasha'", "'Bob'"), ("'John'", "'Greg'")])
        greeting.test_answer(sfour_ans)
    else:
        print('Invalid input, try again.')
        s_choice = int(input('Choose from one of the four problems above: '))