from bankaccount import account



data = [
    {'accname':'Naveen','accno':123,'accIFSC':'00CNB00','acctype':'Savings',
     'accpin':11,'cardno':12,'accbal':10000},
    {'accname':'Sanjay','accno':1234,'accIFSC':'00CNB01','acctype':'Savings',
     'accpin':222,'cardno':123,'accbal':20000},
    {'accname':'Pavan','accno':12345,'accIFSC':'00CNB002','acctype':'Savings',
     'accpin':333,'cardno':1234,'accbal':30000},
    {'accname':'Buden','accno':123456,'accIFSC':'00CNB03','acctype':'Savings',
     'accpin':444,'cardno':12345,'accbal':40000},
    {'accname':'Omkar','accno':12345,'accIFSC':'00CNB04','acctype':'Savings',
     'accpin':555,'cardno':123456,'accbal':50000},
    {'accname':'Nani','accno':12345,'accIFSC':'00CNB05','acctype':'Savings',
     'accpin':666,'cardno':1234567,'accbal':60000},
    {'accname':'prasantha','accno':12345,'accIFSC':'00CNB06','acctype':'Savings',
     'accpin':777,'cardno':12345678,'accbal':70000},
    {'accname':'Vijendra','accno':12345,'accIFSC':'00CNB07','acctype':'Savings',
     'accpin':888,'cardno':123456789,'accbal':80000}]

print("Welcome Your Wish")
print()

print("Your ATM Login")

cardno = int(input("Enter your CardNmber:"))
accpin = int(input("Enter your pinNumber:"))

while True:
    

    for i in data:
        
        if i["cardno"]==cardno and i['accpin']==accpin:
            ob=account(i['accname'],i['accno'],i['accIFSC'],i['acctype'],i['accpin'],i['cardno'],i['accbal'])
            break
    else:
        print("Your Number is Not Correct Please TRY AGAIN !..")
             
    ob.displayaccdetails()
    print("Press 1 For Withdrawn")
    print("Press 2 For Deposit")
    option=int(input("Enter one option:"))
    if option==1:
        ob.withdraw()
    elif option==2:
        ob.deposit()
    else:
        print("Invalid option")


    print("ARE You Next Trasation Continue...")
    back=input('Y/N: ')
    if back.lower()=='n':break
    
print("THANK YOU")
print()



