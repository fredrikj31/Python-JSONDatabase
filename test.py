#from database import JSONDatabase

#db = JSONDatabase("Databases")

#db.checkExistDatabase("HejMedDig")

#db.createDatabase("TestDatabase")

#db.checkExistTable("TestDatabase", "TableName")

import json

f = open("test.json", "r")

y = json.loads(f.read())

print(y['Database Name']['Rows'])

print(len(y['Database Name']['Rows']))