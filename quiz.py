import random

#open the quiz file
with open('quiz.txt', 'r') as file:
    lines = file.readlines()

#formatting of the questions/
questions = []
i = 0
while i < len(lines):

#choosing random questions
#printing the question and choices
#checks if answer is right
#tracking of scores