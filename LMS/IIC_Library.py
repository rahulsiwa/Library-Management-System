import Return  #importing Return module to call its function
import SplitBooks #importing Slitlist module to call its function
import Date_Time #importing Date_Time module to call its function
import Borrow   #importing Borrow module to call its function
from Display import read_file, path_file # calling Display to import it's functions to display book list

def start():
    while(True):
        print()
        print()
        print("                                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("                                 ┃    Welcome to the IIC Library Management System     ┃")
        print("                                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("                                 ┃            Enter 1. ┃       View Book List          ┃")
        print("                                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("                                 ┃            Enter 2. ┃       Borrow Books            ┃")
        print("                                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("                                 ┃            Enter 3. ┃       Return Books            ┃")
        print("                                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("                                 ┃            Enter 4. ┃       Exit                    ┃")
        print("                                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print()
        print(" Note : Borrowers are requested to return book with in 10 days ")
        print("        In case one fails to return the books with in 10 days he/she will be penalized with $1 per additional day")
        print()
        print()
        
        try:
            a=int(input("Dear user, please enter the number as per required service from 1-4: ")) #taking input from user within limitation of 1-4
            print()
            if(a==1):
                read_file(path_file()) #calling the function from Display.py module to display book lits
            elif(a==2):
                SplitBooks.splitBooks()
                Borrow.borrowBook() #calling the function from Borrow.py module to borrow books
            elif(a==3):
                SplitBooks.splitBooks()
                Return.returnBook() # calling the function from Return.py module to return books
            elif(a==4):
                print("Thank you for using library management system")
                break    # the program stops here
            else:
                print("Dear user, please enter a valid choice from 1-4") # in case user inputs alphabet
        except ValueError:
            print("Dear user, please input as suggested.") #exceptional handling if a user inputs number except from 1-4
start()
