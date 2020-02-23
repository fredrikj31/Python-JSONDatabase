import sys
import os
import json
import datetime

class JSONDatabase:

	DatabaseLoc = "./Databases/"
	def __init__(self, databaseLoc):
		self.DatabaseLoc = "./" + databaseLoc + "/"

		self.TableStructure = {
				"Database Name": {
					"Details": {},
					"Column Structure": {},
					"Rows": {}
				}
			}

		self.validTypes = ["String", "Int", "Bool"]
		

	def createDefaultFile(self, Name):
		time = datetime.datetime.now()

		defaultFileContent = {
			"Database Name": Name,
			"Details": {
				"Created At": time.strftime("%d/%m/%Y - %H:%M:%S")
			},
			"Column Structure": {

			},
			"Rows": {
				
			}
		}

		result = json.dumps(defaultFileContent)

		return result

	#Check if database exists
	def checkExistDatabase(self, Name):
		fileName = self.DatabaseLoc + Name + "/" + Name + ".json"
		try:
			#Tries to open the (DatabaseName).json file
			f = open(fileName, "r")
			f.close()

		except IOError:
			print("A database with the name ({}) was not found!".format(Name))
			return False
		else:
			print("A database with the name ({}) was found!".format(Name))
			return True

	
	#Check if table exists
	def checkExistTable(self, dbName, tableName):
		tableFile = self.DatabaseLoc + dbName + "/" + tableName + ".json"
		try:
			f = open(tableFile, "r")

			f.close()
		except IOError:
			return False
		else:
			return True


	#Check Database & Table Name for spaces
	def checkSpaces(self, enterName):
		if enterName.isspace() == True:	
			return True
		else:
			return False


	#Create database
	def createDatabase(self, Name):
		result = self.checkExistDatabase(Name)
		if result == False:
			#Checks if name contains spaces
			result = self.checkSpaces(Name)
			if result == False:
				databaseFolder = self.DatabaseLoc + Name
				try:
					#Creates the database folder
					os.mkdir(databaseFolder)

					#Creates the default database file
					fileName = self.DatabaseLoc + Name + "/" + Name + ".json"
					defaultFile = self.createDefaultFile(Name)
					f = open(fileName, "w")
					f.write(defaultFile)

					#Closes the file !IMPORTANT!
					f.close()

				except OSError:
					print ("Creation of the directory {} failed".format(databaseFolder))
					return False
				else:
					print("A database with the name ({}) was created".format(databaseFolder))
					return True
			
			else:
				print("Your database name cannot contain spaces! You can use (-) and (_)")
				return False
		else:
			print("A database with that name already exist!")
			return False

	
	#Create table
	def createTable(self, dbName, Name, *columnNames):
		#Tries if the arguments is set
		try:
			dbName
			Name
			columnNames
		except NameError:
			print("well, it WASN'T defined after all!")
			return False
		else:
			result1 = self.checkSpaces(dbName)
			result2 = self.checkSpaces(Name)
			if result1 and result2 == False:
				checkTableExists = self.checkExistTable(dbName, Name)

				if checkTableExists == False:
					
					f = open(self.DatabaseLoc + dbName + "/" + Name + ".json", "w")
					f.write(self.TableStructure)
					f.close()
					print("Table was created!")
					print("Added details and columns")

					f = open(self.DatabaseLoc + dbName + "/" + Name + ".json", "r")
					data = json.loads(f.read())

					f.close()
					# Setting the column and their type
					for column in columnNames:
						columnText = column.split("-")
						if columnText[1] in self.validTypes:
							new_column = {columnText[0]: columnText[1]}
							data['Database Name']['Column Structure'].update(new_column)
						else:
							print("You did not insert a valid data type. Fix your error and try again")
							return False
							exit()

					with open(self.DatabaseLoc + dbName + "/" + Name + ".json", 'w') as f:
						json.dump(data, f)
					
					return True

				else:
					print("There is already a table with that name!")
					return False
			else:
				print("No spaces allows in database and table names")
				return False