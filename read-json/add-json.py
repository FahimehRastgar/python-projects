
import json

def getInformation ():

    addPerson = input("Do you want to add a new person (y/n)?")
    if addPerson == 'y':
    
        person = {
            "name": "",
            "last_name": "",
            "birthdate": "",
            "postcode": ""
        }
        
        person['name'] = input("Name: ")
        person["last_name"] = input("Last name: ")
        person["birthdate"] = input("Birthdate (yyyy-mm-dd): ")
        person["postcode"] = input("Postcode: ")

        fileName = (person["name"] + ".json").lower()
        with open(fileName, "w") as jsonFile:
            json.dump(person, jsonFile)
        
        print(person["name"] + " added")
        

getInformation()


