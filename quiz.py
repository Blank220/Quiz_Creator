import random

#open the quiz file and read it
with open('quiz.txt', 'r') as file:
    lines = file.readlines()

#formatting of the questions/
questions = []
i = 0
while i < len(lines):
    if lines[i].startswith('#QUESTIONS'):
      q = lines[i + 1].strip()
      a = lines[i + 3].strip()
      b = lines[i + 4].strip()
      c = lines[i + 5].strip()
      d = lines[i + 6].strip()
      correct = lines[i + 7].strip()[-1]
      questions.append((q,a,b,c,d))
#choosing random questions
#shapol
#printing the question and choices
#checks if answer is right
#tracking of scores

