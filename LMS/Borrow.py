import Date_Time
import SplitBooks

def borrowBook(): #this function is use to allow the users to borrow books and write a text file with the user's name and books borrowed
    success=False
    while(True): #entering while loop to check validity of name 
        firstname=input("Enter the  first name of the borrower: ")
        if firstname.isalpha():
            break
        print("Dear user, you are requested to input an alphabet from A-Z")
    while(True):
        lastname=input("Enter the Last name of the borrower: ")
        if lastname.isalpha():
            break
        print("Dear user, you are requested to input an alphabet from A-Z")
            
    t="Borrow-"+firstname+".txt" # writes and stores a txt file with borrower's name and books took if any
    with open(t,"w+") as f:
        f.write("              IIC Library Management System  \n")
        f.write("     Borrowed By: "+ firstname+ " " +lastname+"\n") #writes the borrowers name in the text file
        f.write("     Borrowed Date: " + Date_Time.getDate()+"    Time:"+ Date_Time.getTime()+"\n\n") #writes the borrowed date and time in the text file
        f.write("S.N. \t Bookname \t\t\t\t      Authorname \n" )
    
    while success==False: #entering to the while loop
        print("Please select a book show below")
        print()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("          Book ID                  ┃  Book Name")
        for i in range(len(SplitBooks.bookname)): #Display available book names
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Enter\t ┃", i, "\t ┃ to borrow book  ┃", SplitBooks.bookname[i])
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        print("Enter the above mentioned Book ID to borrow the book you want :")
        try:   #exceptional handing as per the requirement 
            a=int(input())
            try:
                if(int(SplitBooks.quantity[a])>0): #checks the book is available or not
                    print("Hey there, Book is available")
                    with open(t,"a") as f:
                        f.write("01. \t\t"+ SplitBooks.bookname[a]+"  \t\t  "+SplitBooks.authorname[a]+"\n")

                    SplitBooks.quantity[a]=int(SplitBooks.quantity[a])-1 #if books is being borrowed it subtracts a quantity of the books from the actual book list text file
                    with open("BookList.txt","w+") as f:
                        for i in range(29):
                            f.write(SplitBooks.bookname[i]+","+SplitBooks.authorname[i]+","+str(SplitBooks.quantity[i])+","+"$"+SplitBooks.cost[i]+"\n")


                    #multiple book borrowing code
                    loop=True 
                    count=1
                    while loop==True: 
                        choice=str(input("Do you want to borrow more books? Hope you will return the books within 10 days. Press 'Y' for yes and 'N' for no."))
                        if(choice.upper()=="Y"): #as asked in choice input function if a user wants to borrow more books same options is displayed to choose books from
                            count=count+1
                            print("Please select a book show below")
                            print()
                            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            print("          Book ID                  ┃  Book Name")
                            for i in range(len(SplitBooks.bookname)): #Display available book names
                                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                                print("Enter\t ┃", i, "\t ┃ to borrow book  ┃", SplitBooks.bookname[i])
                            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            print()
                            print("Enter the above mentioned Book ID to borrow the book you want :")
                            a=int(input())
                            if(int(SplitBooks.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ SplitBooks.bookname[a]+"\t\t  "+SplitBooks.authorname[a]+"\n")

                                SplitBooks.quantity[a]=int(SplitBooks.quantity[a])-1
                                with open("BookList.txt","w+") as f: # opening text file and subtracting quantity of books
                                    for i in range(29):
                                        f.write(SplitBooks.bookname[i]+","+SplitBooks.authorname[i]+","+str(SplitBooks.quantity[i])+","+"$"+SplitBooks.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"): 
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Dear user, please choose as instructed")
                        
                else:
                    print("Sorry, this book is currently out of stock") # in case a book has gone out of stock
                    borrowBook()
                    success=False
            except IndexError:
                print()
                print("Please choose book according to their number.")
        except ValueError:
            print()
            print("Please choose as suggested.")
