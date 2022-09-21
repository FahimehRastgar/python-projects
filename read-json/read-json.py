from fileinput import filename
import json


def calculateAge(birthdate):

    dateSplit = birthdate.split('-')
    birthYear = int(dateSplit[0])
    age = 2022 - birthYear

    return age


def init():

    personId = int(input('''
    Select file:
    1 - Mohammad
    2 - Fahim

    What is your file id? '''))

    personList = {
        1: 'mohammad',
        2: 'fahim'
    }
    if personId not in personList :
        print('g f y')
    else:
        fileName = (personList[personId] + '.json')

        with open(fileName, 'r') as fileData :
            person = json.load(fileData) 

        age = calculateAge(person['birthdate'])

        print(f'''Full name: {person['name']} {person['last_name']}''')
        print(f'''Age: {age} ''')
        print(f'''Postcode: {person['postcode']} ''')


init()
