header = '\n' + '-'*30 + '\n'
game_levels = ['1 - Easy', '2 - Medium', '3 - Hard']

#####################################################################
# Questions and answers
# Easy
question1 = 'In order to access a web page your computer needs to run a web __1__. The __1__ will make requests to __2__s using the __3__. This requests use a protocol called HTTP, or __4__ Transfer Protocol. The __2__s responds with files that the __1__ displays.'
blanks1 = ['__1__', '__2__', '__3__', '__4__']
answers1 = ['browser', 'server', 'Internet', 'HyperText']
#######################
# Medium
question2 = 'HTML (__1__ Language) is the standard language for creating web pages. It describes the structure of the page, while the CSS (__2__ Sheets) sets its visual style. HTML and CSS, together with the programming language __3__, are the three core technologies for building web pages, and are well known, if not mastered, by any good __4__ Web Developer.'
blanks2 = ['__1__', '__2__', '__3__', '__4__']
answers2 = ['HyperText Markup', 'Cascading Style', 'JavaScript', 'Front-End']
#######################
# Hard
question3 = '__1__s are responsible for making server, application and __2__ communicate with each other. For that, they use __3__ languages, like Python, Ruby and Java and may use __4__s like Django and Ruby on Rails to make the development faster and easier. __1__s also need know their way with __2__ tools like MySQL and Oracle and its __4__s.'
blanks3 = ['__1__', '__2__', '__3__', '__4__']
answers3 = ['Back-End Developer', 'database', 'server-side', 'framework']
#####################################################################

def name_asker():
    # Asks the player's name and makes it global
    print "\nBefore we start, what's your name?\n"
    global name
    name = raw_input()
    if name == '' or name == ' ':
        print 'A mysterious one, right?'
        name = 'Mysterious Player'

def game_intro():
    # Presents the game intro and tells user to choose a level
    print header
    print 'So ' + name + ', what level would you like to play?\n'
    for level in game_levels:
        print level
    chosen_level = raw_input('\n').lower()
    if chosen_level == '1' or chosen_level == 'easy':
        global_tries = choose_tries()
        play_game(question1, blanks1, answers1, global_tries)
    elif chosen_level == '2' or chosen_level == 'medium':
        global_tries = choose_tries()
        play_game(question2, blanks2, answers2, global_tries)
    elif chosen_level == '3' or chosen_level == 'hard':
        global_tries = choose_tries()
        play_game(question3, blanks3, answers3, global_tries)
    else:
        game_intro()

def choose_tries():
    # Asks user to choose number of tries between 0 and 10
    tries = ''
    number_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    while tries not in number_range:
        print header
        print 'And how many tries per question you would like to have? (1 - 10)\n'
        tries = raw_input()
    return int(tries)

def play_again():
    # Asks if the player wants to play again or not
    positive = ['yes', 'y', 'ok', 'yup']
    negative = ['no', 'n', 'nah', 'nope']
    answer = ''
    while answer not in positive or answer not in negative:
        print header
        print 'Wanna play again? [y/n]\n'
        answer = raw_input().lower()
        if answer in positive:
            print '\nGreat!'
            game_intro()
        if answer in negative:
            print '\nUntil next time!'
            break

def word_replacer(word, blank, answer):
    # Checks if a word contains the answer and replaces the blank with it, including other characters like dots, commas, parentheses and plurals.
    # Based on Mad Libs Generator, by Sean @ Udacity
    replaced = []
    for letter in word:
        if letter not in blank:
            replaced.append(letter)
        elif letter in list(['1', '2', '3', '4', '5']):
            replaced.append(answer)
    replaced = ''.join(replaced)
    return replaced

def cut_join(question, blank, answer):
    # Splits a string into a list, calls the word_replacer() and joins it again into a string
    answered = []
    question = question.split()
    for word in question:
        if blank in word:
            word = word_replacer(word, blank, answer)
        answered.append(word)
    answered = ' '.join(answered)
    return answered

def answer_checker(question, blank, answer, tries):
    # Checks the answer and runs the next if correct or stops if out of tries
    outof_tries = 0
    while tries > outof_tries:
        print header
        print question
        print '\nTries left: ' + str(tries)
        print "What's the answer for " + blank + '?'
        guess = raw_input('\n')
        if guess.lower() == answer.lower():
            print "\nThat's right, " + name + "!"
            question = cut_join(question, blank, answer)
            break
        else:
            print "\nWrong!"
            tries -= 1
    return question, tries

def play_game(question, blanks, answers, global_tries):
    # Plays each level
    index = 0
    outof_tries = 0
    print "\nAlright, so let's do this!"
    for each in blanks:
        question, tries = answer_checker(question, blanks[index], answers[index], global_tries)
        if tries == outof_tries:
            print '\nYou lose! Better luck next time, ' + name + '.'
            return
        index += 1
    print '\n' + question
    print '\nYou win! Good job, ' + name + '!'

print '##### Welcome to the Ultimate Web Development Quiz #####'
name_asker()
game_intro()
play_again()
