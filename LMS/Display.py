#Reads data from BookList.txt and stores data in 2-D list
def path_file(): #function for calling the path which is the actual stock of books txt
    file = open("BookList.txt","r") #opening the file for reading
    lines = file.readlines()
    l = []
    for i in lines:
        l.append(i.replace("\n", " ").split(","))
    file.close() #closing the file
    return l

def read_file(l):
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("{:<45} {:<35} {:<15} {:<10}\n".format("Book Name","  Author"," Quantity"," Cost"))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for item in l:
        print("{:<45} ┃ {:<30} ┃  {:<10} ┃  {:<10} ┃ \n".format(item[0],item[1],item[2],item[3]))
        print("---------------------------------------------------------------------------------------------------------")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    Hope you enjoy our Services    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        