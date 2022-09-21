
import urllib.request
import json


def calculateAge(birthdate):

    dateSplit = birthdate.split('-')
    birthYear = int(dateSplit[0])
    age = 2022 - birthYear

    return age

def getUpcomingPost(postCode):

    with urllib.request.urlopen(f"https://portal.postnord.com/api/sendoutarrival/closest?postalCode=" + postCode) as postData:
        jsonPostData = json.load(postData)

    return jsonPostData


def init():

    personId = int(input('''
Select file:

    1 - Mohammad
    2 - Fahim
    3 - Ali
    

 What is your file id? '''))

    personList = {
        1: 'mohammad',
        2: 'fahim', 
        3: 'ali', 
    }

    if personId not in personList :
        print('g f y')
    else:
        fileName = (personList[personId] + '.json')

        with open(fileName, 'r') as fileData :
            person = json.load(fileData) 

        age = calculateAge(person['birthdate'])
        postData = getUpcomingPost(person['postcode'])

        print(f'''\nFull name: {person['name']} {person['last_name']}''')
        print(f'''Age: {age} ''')
        print(f'''Postcode: {person['postcode']} ''')
        print(f'''City: {postData['city']}''')
        print(f'''Upcoming Delivery: {postData['upcoming']}\n\n''')


init()