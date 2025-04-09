#marks how many question is saved
counter = 0

#Ask user for a question or give them the choice to exit
while True:
    question = input('Enter A Question Of Your Choice Or Type "x" To Stop: ')
    if question.lower() == 'x':
        print('Thank You For Using Quiz Crafter \nHave A Great Day!')
        break

    print('Now, What Are The Possible Answers? ')
# ask the user for the choices/possible answers in the question (a-d)
    option_a = input('Option A. ')
    option_b = input('Option B. ')
    option_c = input('Option C. ')
    option_d = input('Option D. ')
    options = ['a', 'b', 'c', 'd']

#ask the user the correct answer and checks if it is in the choices given
    correct_option = input('What option is the correct answer? (a/b/c/d): ').lower()
    
    if correct_option not in options:
        print('Error! Answer Given Is Not On The Choices!')
        continue
    