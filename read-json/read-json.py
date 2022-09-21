import json


x = int(input('''
Select file:
1 - Mohammad
2 - Fahim

What is your file id? '''))

file_names = {
    1: 'mohammad',
    2: 'fahim'
}
if x not in file_names :
    print('g f y')
else:
    file_name = (file_names[x] + '.json')

    with open(file_name, 'r') as file2 :
        data2 = json.load(file2) 



    splited_birth= data2['birthdate'].split('-')
    year= int(splited_birth[0])
    age_cal= 2022 - year

    print(f'''Full name: {data2['name']} {data2['last_name']}''')
    print(f'''Age: {age_cal} ''')
    print(f'''Postcode: {data2['postcode']} ''')

