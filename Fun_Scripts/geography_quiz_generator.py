import random, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

quizPath = 'C:\\Users\\Alex\\Dropbox\\Programming\\Test\\QuizFiles'

os.makedirs(quizPath, exist_ok=True)
for quiz in range(10):
    # TODO: Create quiz and answer key files
    quizFile = open(os.path.join(quizPath, 'capitalsquiz%s.txt' % (quiz + 1)), 'w')
    answerFile = open(os.path.join(quizPath, 'capitalsquiz_answer%s.txt' % (quiz + 1)), 'w')

    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\nDate:\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz + 1))
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # TODO: Loop through all 50 states, making a question for each.
    for x, i in enumerate(states):  # x is the count, i is the value
        correctAnswer = capitals[i]  # Gets the state capital for each iteration
        wrongAnswers = [capitals.get(i) for i in capitals if capitals.get(i) not in str.split(correctAnswer, maxsplit=0)]  # Makes a list of wrong capitals
        number = str(x+1)  # To get question number for writing in txt file
        quizFile.write(number + '. What is the capital of ' + i + '?' + '\n')  # '1. What is the capital of Alabama?'
        correctLetter = random.choice('ABCD')
        for i in 'ABCD':  # There must be a better way to do this than iterate through the ABCD string
            if i in correctLetter:
                quizFile.write(i + ':' + correctAnswer + '\n')  # Writes one instance of the correct answer
            elif i not in correctLetter:
                quizFile.write(i + ':' + random.choice(wrongAnswers) + '\n')  # Writes three instances of the wrong answer  # TODO: Stop repeating the same wrong answers
        quizFile.write('\n')
        answerFile.write(number + ': ' + correctAnswer + '\n')
    quizFile.close()
    answerFile.close()
