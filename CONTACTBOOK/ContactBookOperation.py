#ContactBookOperation.py
import cx_Oracle as orc

def addcontact():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/ORCL")
            cur=con.cursor()
            name=input("Enter Contact Name:")
            phono=int(input("Enter Contact Phone Number:"))
            email=input("Enter Contact Email:")
            address=input("Enter Contact Address:")
            cur.execute("insert into contactbook values('%s',%d,'%s','%s')" %(name,phono,email,address))
            con.commit()
            print("---------------------------------------------------------")
            if(cur.rowcount>0):
                print("Record Inserted in Contact Book Sucessfully--")
            else:
                print("Record Does not Exist")
            print("------------------------------------------------------------")
            ch=input("Do u Want To Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                break
            print("------------------------------------------------------------------")

        except orc.DatabaseError as db:
            print("problem in oracle:",db)
#addcontact()

def viewcontactlist():
    try:
        con = orc.connect("system/tiger@localhost/ORCL")
        cur = con.cursor()
        cur.execute("select * from contactbook")
        print("Contact Information")
        print("----------------------------------------------------------")
        # get the column name
        for colname in [metadata[0] for metadata in cur.description]:
            print("\t{}".format(colname), end="\t")
        print()
        print("----------------------------------------------------------")
        # code for getting the record
        records = cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val), end="\t")
            print()  # Add a newline after printing each record
        print("-----------------------------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle: {}".format(db))
#viewcontactlist()

def searchcontact():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/ORCL")
            cur=con.cursor()
            name=input("Enter Contact Name For View Data:")
            cur.execute("select * from contactbook where name='%s' " %name)
            print("---------------------------------------------------------------")
            #get the colname
            for colname in [metadata[0] for metadata in cur.description]:
                print("\t{}".format(colname),end="\t")
            print()
            print("---------------------------------------------------------------")
            #get the record from cur object
            records=cur.fetchmany(1)
            for record in records:
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            print("-----------------------------------------------------------------")
            ch=input("Do U Want to Search Another Conatct(yes/no):")
            if(ch.lower()=="no"):
                break
            print("------------------------------------------------------------------")
        except orc.DatabaseError as db:
            print("problem in Oracle:",db)
#searchcontact()

def updatecontact():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/ORCL")
            cur=con.cursor()
            phonenumber=int(input("Enter New Phonenumber:"))
            email=input("Enter New Email:")
            address=input("Enter New address:")
            name=input("Enter Name for Updating The Other Deatils:")
            cur.execute("update contactbook set phonenumber=%d,email='%s',address='%s' where name='%s'" %(phonenumber,email,address,name))
            con.commit()
            print("-----------------------------------------------------------------")
            if(cur.rowcount>0):
                print("Update Record of Contact Book sucessfully")
            else:
                print("Table Does not Exist")
            print("-----------------------------------------------------------------")
            ch=input("Do U Want To Update Another Record(yes/no):")
            if(ch.lower()=="no"):
                break
            print("------------------------------------------------------------------")
        except orc.DatabaseError as db:
            print("Problem in Oracle:",db)
#updatecontact()

def deletecontact():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/ORCL")
            cur=con.cursor()
            name=input("Enter Contact Name For Delete The Records:")
            cur.execute("delete from contactbook where name='%s'" %name)
            con.commit()
            print("-------------------------------------------------------")
            if(cur.rowcount>0):
                print("Delete Contact Record sucessfully--")
            else:
                print("Record does not exist")
            print("-------------------------------------------------------")
            ch=input("Do U Want To Delete Another Record(yes/no):")
            if(ch.lower()=="no"):
                break
            print("--------------------------------------------------------")
        except orc.DatabaseError as db:
            print("problem in Oracle:",db)
#deletecontact()













