class contact():
    def addcontact(self):
        Name = input("Enter Name :-")
        Number = input("Enter number :-")
        f = open("contacts.txt","a")
        f.write(Name+":"+Number+"\n")
        f.close()
    def searchcontacta(self):
        datil = input("Enter Name or Number :-")
        f=open("contacts.txt","r")
        res = f.readlines()
        for i in res:
            if datil in i:
                print(i)
                break
        else:
            print("No contact found")
        f.close()
    def Removecontact(self):
        num = input("Enter Name or Number :-")
        f=open("contacts.txt","r")
        var = f.readlines()
        for data in var:
            if num in data:
                var.remove(data)
        print(var)
        f.close()
        f=open("contacts.txt","w")
        f.writelines(var)
        f.close()
    def Updatecontact(self):
        f=open('contacts.txt','r')
        lis=f.readlines()
        edit=input("Enter incorrect contact Name or Number  :")
        for j in range(len(lis)):
            if edit in lis[j]:
                lis[j]=input("Enter Name :-")+" : "+str(int(input("Enter Number :-")))+"\n"
                break
        else:
            print("No contact Found")
        f.close()
        f=open("contacts.txt","w")
        f.writelines(lis)
        f.close()
    def Displaydatails(self):
        f=open("contacts.txt","r")
        res = f.read()
        return res
        



 



book=contact()
#book.Displaydatails()
print("press 0 to Exit:\n")
print("press 1 to Add contact :\n")
print("press 2 to Search contact :\n")
print("press 3 to Update contact :\n")
print("press 4 to Delect contact :\n")
print("press 5 to Display All contact:\n")
while True:
    N = input("Press A Number :-")
    if N == '0':
        break
    elif N == '1':
        book.addcontact()
        print ("Contact added successfully....!")
    elif N == '2':
        book.searchcontacta()
        print ("Contact Search for successfully....!")
    elif N == '3':
        book.Updatecontact()
        print ("Contact Updated successfully....!")
    elif N == '4':
        book.Removecontact()
        print ("Contact Delected successfully....!")
    elif N == '5':
        print(book.Displaydatails())
        print (" Your Contact All Displayed successfully....!")
    else:
        print(" & INVALID OPTION TRYAGIN..!")









