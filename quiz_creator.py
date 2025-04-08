while True:
    question = input('Enter A Question Of Your Choice: ')
    print('Now, What Are The Possible Answers? ')
    option_a = input('Option A. ')
    option_b = input('Option B. ')
    option_c = input('Option C. ')
    option_d = input('Option D. ')
    options = [option_a , option_b , option_c , option_d]
    correct_option = input('What option is the correct answer? ')
    if correct_option not in options:
        print('Error! Answer Given Is Not On The Choices!')
        break
    