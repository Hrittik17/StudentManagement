import csv
Found=0
    mlist=[]
    newName=input("Please enter the name to be modified")
    for r in csvr:
        if(r(0)==name):
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
def updateData():
    
    File=open("univerisity_records.csv","r")
    csvr=csv.reader(File)
    