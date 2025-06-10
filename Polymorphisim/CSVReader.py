'''
Duck typing - in other way
'''
class CSVReader:
    def read(self):
        print("Reading data from CSV")

class APIReader:
    def read(self):
        print("Reading data from API")

class SQLReader:
    def read(self):
        print("Reading data from SQL Database")

#Here reader is placeholder name. It can be CSVReader, APIReader and SQLReader.
#Python sees that the object passed has a .read() method, and it calls it. That's duck typing.
def run_pipeline(reader):
    #Duck Typing: Any object with a 'read()' method works
    reader.read()

run_pipeline(CSVReader())
run_pipeline(APIReader())
run_pipeline(SQLReader())

