import random

#open the quiz file and read it
with open('quiz.txt', 'r') as file:
   lines = file.readlines()

#formatting of the questions/choices
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
      questions.append((q,a,b,c,d,correct))
      i += 9
   else:
      i += 1
#choosing random questions
random.shuffle(questions)

#tracking of scores
score = 0

#printing the question and choices
for q in questions:
   print('\n' + q[0])
   print(q[1])
   print(q[2])
   print(q[3])
   print(q[4])

#checks if answer is right
   ans = input('What\'s your answer? (a/b/c/d): ').lower()
   while ans not in ['a','b','c','d']:
      print('Invalid answer,please refer to the choices')
      ans = input('What\'s your answer? (a/b/c/d):'.lower())

   if ans == q[5]:
      print('✅ Correct!')
      score += 1
   else:
      print(f'❌ Wrong! The correct answer is {q[5]}')
      

print(f'Finished! You did a wonderful job! \nYou got {score} out of {len(questions)}')

