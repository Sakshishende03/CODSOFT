#AopMain.py
from AopMenu import menu
from AopOperation import addop,subop,mulop,divop,moddiv,Frdivop,Expop
def mainop():
    while(True):
        try:
            menu()
            ch=int(input("Enter U r Choice:"))
            print("-----------------------------------------------")
            match(ch):
                        case 1:
                            addop()
                        case 2:
                            subop()
                        case 3:
                            mulop()
                        case 4:
                            divop()
                        case 5:
                            moddiv()
                        case 6:
                            Frdivop()
                        case 7:
                            Expop()
                        case 8:
                             print("Thanks For Using Program")
                        case _:
                            print("You Are Enter Wrong Choice-- Try Again")
        except ValueError:
            print("Don't Enter alphnum and str and special symbol for Enter u are choice")


#main program
mainop()

