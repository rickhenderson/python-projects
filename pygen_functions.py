"""
pygen_functions.py

Functions for the pygen_mc application
for saving multiple choice questions to a file.

Author: Rick Henderson
Created on: Nov 26, 2016
Updated on: Nov 26, 2016
"""

# Constants

# Possible question text prefixes for different output.
QUESTION_PREFIX = ""
#QUESTION_PREFIX = "<li>"
ANSWER_PREFIX = ""

def append_question(file_variable, question_text):
    """
    ==============================================================
        Preconditions:
	        file_variable - a file object open in append+ mode for
						        writing sequential text files. (file)
	        question_text - the text of a question (str)
        -----------------------------------------------------------
        Postconditions:
	        question_text is appended to the file represented by
		        file_variable
        -----------------------------------------------------------
    """

    # Append the question to the file provided
    print("{:s}{:s}".format(QUESTION_PREFIX, question_text), file = file_variable)


def append_answer(file_variable, answer_text):
    """
    ==============================================================
        Preconditions:
	        file_variable - a file object open in append+ mode for
						        writing sequential text files. (file)
	        answer_text - the text of a single answer choice (str)
        -----------------------------------------------------------
        Postconditions:
	        answer_text is appended to the file represented by
		        file_variable
        -----------------------------------------------------------
    """

    # Append the question to the file provided
    print("{:s}{:s}".format(ANSWER_PREFIX, answer_text), file = file_variable)
