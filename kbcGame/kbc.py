from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if question['answer']==answer else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''

'''
    correctoption = ques['answer']
    #option
    optionDelete1 = 0
    optiondelete2 = 0

    if(correctoption=1):
        optionDelete1 = 3
        optiondelete2 = 4
    elif(correctoption=2):
        optionDelete1 = 3
        optiondelete2 = 4
    elif(correctoption=3):
        optionDelete1 = 1
        optiondelete2 = 2
    elif (correctoption=4):
        optionDelete1 = 1
        optiondelete2 = 2
        
    del.ques['optiob{}'.format(optionDelete1)]
    del.ques['optiob{}'.format(optionDelete1)]
'''

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    welcome = False

    print("Welcome to Kon Banega Crorepati")


    #  For each question, display the prize won until now and available life line.
    lifeline=1
    price_won=0
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
game_play = True
i=0
while game_play:
    print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
    print(f'\t\tOptions:')
    print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
    print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
    print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
    print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
    ans = input('Your choice ( 1-4 ) : ')
    if ans.lower()=='quit':
        game_play=False
    # check for the input validations

    if isAnswerCorrect(QUESTIONS[0], int(ans) ):
        # print the total money won.
        print('Total amount won is',QUESTIONS[i]['money'])
        # See if the user has crossed a level, print that if yes
        print('\nCorrect !')
        i+=1

    else:
        # end the game now.
        # also print the correct answer
        print('\nIncorrect !')
        print(f"The correct answer was, {QUESTIONS[i]['answer']}")
        game_play=False

    # print the total money won in the end.


kbc()