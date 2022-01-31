# importing the csv module
from ast import FunctionDef
import csv
from msilib.schema import File
from operator import truediv
from unicodedata import name
import pandas as pd

AdminPassword = "12345"
tempfields = ['name', 'branch', 'batch', 'id', 'email', 'password']

with open("university_records.csv", 'a') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=tempfields)
        # writing headers (field names)
 
        writer.writeheader()



def updateData():
    
    File=open("university_records.csv","r")
    csvr=csv.reader(File)
    Found=0
    mlist=[]
    newName=input("Please enter the name to be modified: ")
    for r in csvr:
        if(r[0]==name):
            r[1]=input("Enter the Branch: ")
            r[2]=input("Enter the Batch: ")
            r[3]=input("Enter the Id: ")
            r[4]=input("Enter the email: ")
            print(r)
            Found=1
            mlist.append(r)
        
    f.close()
    
    if(Found==0):
        print("Data Not Found")

    else:
        f=open("univeristy_records.csv","w",newline='')
        csvw=csv.writer(f)
        csvw.writerows(mlist)
        print("File updated Successfully.")
        f.close()
    return


def deleteData():
    
    

    return


def takeInput():
    requiredData = ['name', 'branch', 'batch', 'id', 'email', 'password']
    temptData = {}

    for key in requiredData:
        value = input("{} = ".format(key))
        temptData.update({key: value})
    print("Your Data has been added")
    return temptData


def addData():
    filename = "university_records.csv"
    fields = ['name', 'branch', 'batch', 'id', 'email', 'password']
    newData = takeInput()

    

        
  # now do something here 
  # if first row is the header, then you can do one more next() to get the next row:
  # row2 = next(f)

    with open(filename, 'a') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writing headers (field names)
 
        
        # writing data rows
        writer.writerow(newData)


loginSelection = input("Press: \n1 For Admin\n2 For Student\n")
if(loginSelection == "1"):
    while True:
        mPassword = input("Enter Admin Password : ")
        if(mPassword == AdminPassword):
            while True:
                AdminChoice = input("Welcome Admin\n1. Add Data\n2. Update Data\n3. Delete Data\n4 For Exit\n:")
                if(AdminChoice == "1"):
                    addData()
                elif(AdminChoice == "2"):
                    updateData()
                elif(AdminChoice == "3"):
                    deleteData()
                elif(AdminChoice == "4"):
                    break
                else:
                    print("Please enter the valid choice")

        else:
            exitcase = input("Please Enter Valid Password or press 0 to exit")
            if(exitcase == '0'):
                break


elif(loginSelection == "2"):
    print("Student Portal")
else:
    print("Invalid Input")
