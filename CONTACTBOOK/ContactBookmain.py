from ContactBookMenu import menu
from ContactBookOperation import addcontact,viewcontactlist,searchcontact,updatecontact,deletecontact
def main():
    while(True):
        menu()
        try:
            ch=int(input("Enter u are Choice:"))
            match(ch):
                case 1:
                    print("--------------------------------------------")
                    print("Add Contact")
                    print("--------------------------------------------")
                    addcontact()
                case 2:
                    print("--------------------------------------------")
                    print("View Contact List")
                    print("--------------------------------------------")
                    viewcontactlist()
                case 3:
                    print("--------------------------------------------")
                    print("Search Contact Record")
                    print("--------------------------------------------")
                    searchcontact()
                case 4:
                    print("--------------------------------------------")
                    print("Update Contact Record")
                    print("--------------------------------------------")
                    updatecontact()
                case 5:
                    print("--------------------------------------------")
                    print("Delete Contact record")
                    print("--------------------------------------------")
                    deletecontact()
                case 6:
                    print("Thanks For Using Program")
                case _:
                    print("U are enter Wrong Choice---Try again")
        except ValueError:
            print("Don't Enter alphunm and str and special symbol for Enter u are Choice")
#main program
main()