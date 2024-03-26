class account:
    def __init__(self,accname,accno,accIFSC,acctype,accpin,cardno,accbal):
        self.__accname = accname
        self.__accno = accno
        self.__accIFSC = accIFSC
        self.__acctype = acctype
        self.__accpin = accpin
        self.__cardno = cardno
        self.__accbal = accbal
    def getaccname(self):
        return self.__accname
    def getaccno(self):
        return self.__accno
    def getaccIFSC(self):
        return self.__accIFSC
    def getacctype(self):
        return self.__acctype
    def getaccpin(self):
        return self.__accpin
    def getcardno(self):
        return self.__cardno
    def getaccbal(self):
        return self.__accbal
    def withdraw(self):
        amount = int(input("Enter amount withdrawn :"))
        if self.__accbal>500:
            self.__accbal -= amount
            print("Amount withdrawn Successfully")
            print("UPdated Account Balance :",self.getaccbal())
        else:
            print('INsufficient Balance, Try Again..')
    def deposit(self):
        amount = int(input("Enter amount deposited :"))
        self.__accbal += amount
        print("UPdated Account Balance :",self.getaccbal())

    def displayaccdetails(self):
        print("Account Name:",self.__accname)
        print("Account Number:",self.__accno)
        print("Account IFS CODE:",self.__accIFSC)
        print("Account Type:",self.__acctype)
        print("Account PIN:",self.__accpin)
        print("Account Balaance:",self.__accbal)
        print()
