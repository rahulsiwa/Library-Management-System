import SplitBooks
import Date_Time
def returnBook(): # this function is used to take back the return books from the borrowers and create a text file for each transaction
    name=input("Enter first name of borrower: ") #Entering first name of the borrower
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower's name is incorrect")
        returnBook()

    b="Return-"+name+".txt"  #generating  a return text file with the name of the borrower
    with open(b,"w+")as f:
        f.write("IIC Library Management System \n")
        f.write("Returned By: "+ name+"\n") #writes name of the person who has returned the book
        f.write("Returned Date: " + Date_Time.getDate()+"    Time:"+ Date_Time.getTime()+"\n\n") #writes the book returned date and time in the return text file
        f.write("S.N.\tBookname\t\tCost\n") #writes returned date and time in the return text file


    total=0.0 #total payment of the book without reading the BookList text file
    for i in range(29):
        if SplitBooks.bookname[i] in data: 
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+SplitBooks.bookname[i]+"\t\t$"+SplitBooks.cost[i]+"\n")
                SplitBooks.quantity[i]=int(SplitBooks.quantity[i])+1 #Adds quantity of books in the pathfile i.e. BookList.txt when a user returns book
            total+=float(SplitBooks.cost[i]) #function to read the books cost from the main txt file
    print()       
    print("Total Payment\t\t\t"+"$"+str(total))
    print()
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"): #if statement is invoked to ask the user total return period
        print("In how many days you are returning the book? ")
        day=int(input()) 
        if day >= 10: #
            fine = (day-10)*1 # fine is calculated as $1 per late days
        with open(b,"a")as f: #opening the return txt file after reading the original cost and add the fine amount also 
            f.write("\t\t\t\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total with fine: "+ "$"+str(total))  
    with open(b,"a")as f:
        f.write("\t\t\t\t\t\t\t\ttTotal Payment: $"+ str(total))
    
        
    with open("BookList.txt","w+") as f:
            for i in range(29):
                f.write(SplitBooks.bookname[i]+","+SplitBooks.authorname[i]+","+str(SplitBooks.quantity[i])+","+"$"+SplitBooks.cost[i]+"\n")
