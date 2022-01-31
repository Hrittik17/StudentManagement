import csv

def viewAll():
  with open("university_records.csv",'r') as CSVFile:
    csvr = csv.reader(CSVFile)
    for row in csvr:
      print(row)

viewAll()
  
id = input("Enter id: ")

OuterIndex = None
data = None
with open("university_records.csv",'r+') as CSVFile:
    csvr = csv.reader(CSVFile)
    data = list(csvr)

    for row in data:
      if id in row:
        
        OuterIndex = data.index(row)

      


fieldName = input("Enter email: ")
data[OuterIndex][4] = fieldName




with open("university_records.csv",'w') as CSVFile:
  tempfields = ['name', 'branch', 'batch', 'id', 'email', 'password']
  writer = csv.writer(CSVFile)
  #nDATA = {"name":data[OuterIndex][0], "branch":data[OuterIndex][1], "batch":data[OuterIndex][2], "id":data[OuterIndex][3], "email":fieldName, "password":data[OuterIndex][5]}
  writer.writerow(tempfields)
  writer.writerows(data)
    #print(data)





