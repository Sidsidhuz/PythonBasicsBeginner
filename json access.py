import json
jdata = '''
    {
        "people":[
            {
            "name":'Sid',
            'phone : 7907051993,
            'email':'sidharthchandran567@gmail.com',
            'has_license':true
            }
        ]
    }
'''
data = json.loads(jdata)
print(data)