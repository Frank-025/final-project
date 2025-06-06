s_list = ['make_baab', 'split', 'Placeholder', 'Placeholder']

# Coding problem basic solution:
# What makes this not good is the use of exec().
# In the real world, this is extremely dangerous without extensive handling
# to ensure no one can inject their own harmful code. For the purposes of a theoretical project, it's fine.
class Problem:

    def __init__(self, question='', q_desc='', q_code='', q_answer='', test_inputs=[]):
        # We keep the question separate, so we can use it later to call it as a function
        self.question = question

        # Description for printing
        self.q_desc = q_desc

        # Code to run
        self.code = q_code

        # A successful answer
        self.q_answer = q_answer

        # A list of test inputs to run and compare for score
        self.test_inputs = test_inputs

    def test_answer(self, user_input):

        # Creates copies of both the working and users versions of the function/answer
        full_question = self.code + self.q_answer
        user_question = self.code + user_input

        # Variable to keep track of the score
        counter = 0

        # Create a loop to run through the test cases
        for ti in self.test_inputs:

            # Unpack the test variables
            x, y = ti

            # Two dictionaries so we can grab the variables used in the exec() function
            grab1, grab2 = {}, {}

            # Create new copies of the strings for testing
            u_copy, new_str = user_question, full_question

            # Attach the variable we'll be collection in the grab dictionaries, as well as setting up
            # the run. Print statement is there for debugging/ensuring output is desired
            new_str += f"\n\nmain_answer = {self.question}({x}, {y})"
            u_copy += f"\n\nmain_answer = {self.question}({x}, {y})"
            # print(new_str)
            # print(u_copy)

            # Run the problems. Grab dictionaries collect the 'main_answer' variables
            exec(new_str, grab1)
            exec(u_copy, grab2)

            # If the answers are the same, increment the counter by 1
            if grab1['main_answer'] == grab2['main_answer']:
                counter += 1

        if counter == 0:
            print("Incorrect answer, try again.")
        elif counter == 2:
            print("Correct!")

# Test run that works correctly in this file but for some reason doesn't work in the original file.
# demo = Problem('split', 'measure the length of a string and splice it in half', 'def split(text, plac):\n',
#                    '\tif len(text) % 2 > 0:\n\t\treturn text[len(text) - 2:len(text)]\n\treturn text[len(text) // 2:len(text)]',
#                    [("'armadillo'", "'cheat'"), ("'pplllasllllasd'", "'wonder'")])
#
# demo.test_answer('\tif len(text) % 2 > 0:\n\t\treturn text[len(text) - 2:len(text)]\n\treturn text[len(text) // 2:len(text)]')
