# importing the csv module
import csv
import email
from operator import truediv
import pandas as pd
import re





AdminPassword = "12345"
tempfields = ['name', 'branch', 'batch', 'id', 'email', 'password']

with open("university_records.csv", 'a') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=tempfields)
        # writing headers (field names)
 
        writer.writeheader()

#Email Validation
def EmailValidation(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def updateData():
    return


def deleteData():
    return


def takeInput():
    requiredData = ['name', 'branch', 'batch', 'id', 'email', 'password']
    temptData = {}

    for key in requiredData:
        value = input("{} = ".format(key))
        if(key=="email" and (not EmailValidation(value))):
            while True:
                print("Invalid Email")
                emailNew = input("Enter valid email address: ")
                if(EmailValidation(emailNew)):
                    temptData.update({key: value})
                    break
        else:
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
                AdminChoice = input("Welcome Admin\n1. Add Data\n2. Update Data\n3. Delete Data\n4 Enter Marks of Students.\n5. For Exit\n:")
                if(AdminChoice == "1"):
                    addData()
                elif(AdminChoice == "2"):
                    updateData()
                elif(AdminChoice == "3"):
                    deleteData()
                elif(AdminChoice == "5"):
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




