import random

OBJECT_PRO = ['Her', 'Him', 'Them']
POSS_PRO = ['Her', 'His', 'Their']
PERS_PRO = ['She', 'He','They']
STATES = ['Alabama', 'Arizona', 'Florida', 'Georgia', 'Indiana', 'Kentucky', 'Mississippi', 'Nevada', 'Ohio', 'Oklahoma', 'Texas', 'West Virginia']
NOUNS = ['Essential Oil', 'Umbrella', 'Plastic Straw', 'Video Game', 'Zero Calorie Sweetener', 'Pet Rock']
PLACES = ['Home Office', 'Dog Park', 'Fallout Shelter', 'Laundromat', 'Tree House', '4-Star Restaurant', 'Motel 6']
WHEN = ['Next Week', 'Tomorrow', 'Immediately', 'In Under 20 Minutes', 'On Your Only Day Off This Week']
PEOPLE = ['Mother of 12', 'Former Golf Caddy', 'Palentologist', 'Self-Identified Extrovert']



def main():
        print('Clickbait Headline Generator')
        print('Adapted from Al Sweigart project')
        print()

        while True:
                print ('How many clickbait headlines should we generate?')
                response = input('> ')
                if not response.isdecimal():
                    print('Please enter a number. ')
                else:
                    numberOfHeadlines=int(response)
                    break
                
        for i in range(numberOfHeadlines):
            clickbaitType = random.randint(1,8)

            if clickbaitType == 1:
                headline = generateAreMillenialsKillingHeadline()
            elif clickbaitType == 2:
                headline = generateWhatYouDontKnowHeadline()
            elif clickbaitType == 3:
                headline = generateBigCompaniesHateHerHeadline()
            elif clickbaitType == 4:
                headline = generateYouWontBelieveHeadline()
            elif clickbaitType == 5:
                headline = generateDontWantYouToKnowHeadline()
            elif clickbaitType == 6:
                headline = generateGiftIdeaHeadline()
            elif clickbaitType == 7:
                headline = generateReasonsWhyHeadline()
            elif clickbaitType == 8:
                headline = generateJobAutomatedHeadline()
            
            print(headline)
        print()

def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun=random.choice(NOUNS)
    pluralNoun =random.choice(NOUNS)+'s '
    when = random.choice(WHEN)
    return 'Without This {}. {} Could Kill You {}'.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    state = random.choice(STATES)
    person= random.choice(PEOPLE)
    noun = random.choice(NOUNS)
    return 'Big Companies Hate to See It! See How This {} {} Invented a Cheaper {}'.format(state, person, noun)

def generateYouWontBelieveHeadline():
    state= random.choice(STATES)
    person=random.choice(PEOPLE)
    pronoun=random.choice(POSS_PRO)
    place =random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, person, pronoun, place)

def generateDontWantYouToKnowHeadline():
    pluralNoun1=random.choice(NOUNS)+ 's'
    pluralNoun2=random.choice(NOUNS)+ 's'
    return 'What {} Don\'t Want You to Know About {}'.format(pluralNoun1, pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7,15)
    person = random.choice(PEOPLE)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give your {} From {}'.format(number,person,state)

def generateReasonsWhyHeadline():
    number1 =random.randint(3,19)
    pluarlNoun = random.choice(NOUNS)+'s'
    number2 =random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting than You Think (Number {} Will Surprise You!)'.format(number1,pluarlNoun,number2)

def generateJobAutomatedHeadline():
    state=random.choice(STATES)
    person= random.choice(PEOPLE)

    i =random.randint(0,2)
    pronoun1=POSS_PRO[i]
    pronoun2=PERS_PRO[i]
    if pronoun1== 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, person, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, person, pronoun1, pronoun2)

if __name__ == '__main__':
    main()