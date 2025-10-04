import json
talabalar = 'students.json'
with open(talabalar,'r') as json_talabalar:
    show = json.load(json_talabalar)
    for sikil in show['student']:
        print(f"name:{sikil['name']} fullname:{sikil['lastname']} etap-{sikil['year']}  fakultet:{sikil['faculty']}")