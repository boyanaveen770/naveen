from student import Student_Report_Card
data = [{"schoolname":"Z.PHigh School","stuid":1,"stuname":"Naveen","studob":"13/may/2003",
         "stue_mail":"naveen@gmail.com","stumarks":"50 60 70 80 90 100" },
        {"schoolname":"Z.PHigh School","stuid":2,"stuname":"Sanjay","studob":"28/aug/2002",
         "stue_mail":"sanjay@gmail.com","stumarks":"40 60 70 60 90 100" },
        {"schoolname":"Z.PHigh School","stuid":3,"stuname":"Pavan","studob":"1/jan/2003",
         "stue_mail":"pavan@gmail.com","stumarks":"50 60 30 80 90 100" },
        {"schoolname":"S.N.VM School","stuid":4,"stuname":"prasanth","studob":"15/dec/2001",
         "stue_mail":"prasanth@gmail.com","stumarks":"60 60 70 70 90 100" },
        {"schoolname":"Z.PHigh School","stuid":5,"stuname":"Buden","studob":"22/april/2003",
         "stue_mail":"buden@gmail.com","stumarks":"80 60 70 40 50 100" },
        {"schoolname":"Z.PHigh School","stuid":6,"stuname":"Omkar","studob":"17/jun/2001",
         "stue_mail":"reddy@gmail.com","stumarks":"50 80 30 80 40 100" },
        {"schoolname":"Z.PHigh School","stuid":7,"stuname":"Nani","studob":"25/july/2000",
         "stue_mail":"nani@gmail.com","stumarks":"50 60 30 85 50 100" },
        {"schoolname":"Z.PHigh School","stuid":8,"stuname":"Vijendra","studob":"1/march/2004",
         "stue_mail":"vije@gmail.com","stumarks":"50 62 55 81 70 100" },
        {"schoolname":"Z.PHigh School","stuid":9,"stuname":"vinay","studob":"20/nov/2002",
         "stue_mail":"vinay@gmail.com","stumarks":"54 66 50 89 91 100" }]


print("HI WELCOM OUR SCHOOL")
print()

#stuid = int(input("Enter Your id :"))

while True:
    stuid = int(input("Enter Your id :"))
    for i in data:
        if i["stuid"]==stuid :
            ob = Student_Report_Card(i['schoolname'],i['stuid'],i['stuname'],
            i['studob'],i['stue_mail'],i['stumarks'])
            ob.Totalmarks()
            ob.persentage()
            ob.Grade()
            break
    else:
        print("Your ID is Not Correct Please TRY AGAIN !...")


    ob.display()
    print("please continue...")
    back = input('Y/N: ')
    if back.lower()=='n':break


print("THANK YOU")
print()