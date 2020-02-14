from database import JSONDatabase

db = JSONDatabase("Databases")

#db.checkExistDatabase("HejMedDig")

#db.createDatabase("TestDatabase")

#db.checkExistTable("TestDatabase", "TableName")

db.createTable("TestDatabase", "Table_2", "Hej-String", "Med-Int", "Dig-Bool")

#import json

"""f = open("test.json", "r")

y = json.loads(f.read())

print(y['Database Name']['Rows'])

print(len(y['Database Name']['Rows']))"""

"""f = open("test.json", "r")

y = json.loads(f.read())

new_key = {"Column name 2": "String"}

y['Database Name']['Column Structure'].update(new_key)

with open('test.json', 'w') as f:
    json.dump(y, f)"""