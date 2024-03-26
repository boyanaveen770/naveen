class Student_Report_Card():
    def __init__(self,schoolname,stuid,stuname,studob,stue_mail,stumarks):
        self.__schoolname=schoolname
        self.__stuid = stuid
        self.__stuname = stuname
        self.__studob=studob
        self.__stue_mail=stue_mail
        self.stumarks=stumarks.split()
        self.marks=[int(marks)for marks in self.stumarks]
        #for marks in stumarks:
        #   marks=int(self.__stumarks)

    def getschoolname(self):
        return self.__schoolname
    def getstuid(self):
        return self.__stuid
    def getstuname(self):
        return self.__stuname
    def getstudob(self):
        return self.__studob
    def getstue_mail(self):
        return self.__stue_mail
    def getstumarks(self):
        return self.stumarks
        
    def Totalmarks(self):
        self.totalmarks=sum(self.marks)
        #print(self.totalmarks)
    def persentage(self):
        self.pers=(self.totalmarks/700)*100
    def Grade(self):
        if 100>self.pers>80:
            self.Grade="A grade"
        elif 80>self.pers>60:   
            self.Grade="B grade"
        elif 60>self.pers>40:
            self.Grade="C grade"
        elif 40>self.pers>35:
            self.Grade="D grade"
        elif 35>self.pers>0:
            self.Grade="Fail"
            
    def display(self):
        print()
        print('\n=-=-=-=-=-==-=-=-==-=-=-=-==-=--==-=-=-=-=-')
        print("         $$$$  REPORT CARD   $$$$          ")
        print('\n===========================================')
        print()
        print("        SCHOOL NAME :-",self.__schoolname)
        print("        STUDENT ID :-",self.__stuid)
        print("        STUDENT NAME:-",self.__stuname)
        print("        STUDENT DATE OF BRITH :-",self.__studob)
        print("        STUDENT E_MAIL :-",self.__stue_mail)
        print("        STUDENT TOTALMARKES :-",self.totalmarks)
        print("        STUDENT PERSENTAGE IS :-",self.pers)
        print("        STUDENT GRADE IS :-",self.Grade)



# obj=Student_Report_Card()
# obj.Totalmarks()
# obj.persentage()
# obj.Grade()
# obj.display()