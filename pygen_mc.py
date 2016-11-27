"""
pygen_mc.py

Program to generate multiple choice questions by
asking for using input, then storing them in a text file
for pasting into word.

Author: Rick Henderson
Created on: Nov 26, 2016
Updated on: Nov 26, 2016
"""

#TODO:
#	- Allow multiple writes to the same file to continue the numbering system


# Imports
from pygen_functions import append_question, append_answer

# Constants
ANSWER_CODE = "abcd"
#ANSWER_CODE = "ABCD"
#ANSWER_CODE = "1234"
ANSWER_FILE_NAME = "answers_f2016.txt"

# Prime some variables


# Display a welcome banner

print("***** Welcome to the Multiple Choice Exam Generator *****")
print()
file_name = input("Enter the name of the file to create or append to: ")

# Open the file in a+ append mode, which creates
# the file if it didn't exist, or simply appends if it does.
output_file = open(file_name, "a+", encoding="utf-8")

# Open the answer file for storing the answers
answer_file = open(ANSWER_FILE_NAME, "a+", encoding="utf-8")

# Get the priming input from the user
question = input("Type in a question. Enter QUIT to quit: ")
question_number = 1

# Write the question or keep asking until the user enters QUIT
while question != "QUIT":

	# Just ignore accidental blank lines
    if question != "":
		# Prepend the question number to the question
        question = "{}. {}".format(question_number,question)
        append_question(output_file, question)

		# Ask for 4 answers. User can press ENTER to leave the answer blank.
        for answer in ANSWER_CODE:
            answer_text = input("Answer ({:s}): ".format(answer))
            answer_text = "{}) {}".format(answer, answer_text)
            # Write the answer out
            # Could have tab separated answers, but not needed ATM.
            append_answer(output_file, answer_text)

		# Ask which answer was the correct one to write to answer file.
        correct_answer = input("Which choice was the correct answer: ")

        # Store the question # and the answer in the answer file
        correct_answer = "{}. {}".format(question_number, correct_answer)
        append_answer(answer_file, correct_answer)

		# Update the number of questions for the next question
        question_number = question_number + 1

    # Get another question from the user
    print()
    question = input("Type in a question. Enter QUIT to quit: ")

# Exit the program nicely.
print()
print("*** Thank you for using pyGenMC! ***")

# Close the files
output_file.close()
answer_file.close()
