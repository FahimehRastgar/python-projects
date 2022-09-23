
import urllib.request
import json
import os

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

    personList = []

    for file in os.listdir("./"):
        if file.endswith(".json"):
            name = file.split('.')
            personList.append(name[0])


    personName = ""
    for id, name in enumerate(personList):
         personName = personName + (str(id + 1) + " - " + name) + "\n"

    personId = int(input(f'''
Select file:

{personName}

 What is your file id? '''))

    personId -= 1

    if personId >= len(personList) :
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