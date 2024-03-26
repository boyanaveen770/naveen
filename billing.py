class Bill():
    def __init__(self):
        self.name = None
        self.price = 0
        self.code = None 
        self.totalbill = 0

    def setDetails(self,item):
        self.name=item.get('name')
        self.price=item.get('price')
        self.code=item.get('code')
    def quantity (self):
        quantity=int(input('QUANTITY:'))
        self.totalquantity=self.price*quantity
        print('\nITEM','   QTY','    PRICE','     TOTAL')

        print(self.name,'  ',quantity,'     ',self.price,'       ',self.totalquantity)
        self.totalbill+=self.totalquantity
        return self.totalquantity

    
    def totalbill(self):
        self.totalbill+=self.totalquantity
        return self.totalbill
       

    def display (self):
        print('\n\nMENU')
        print('\nPRESS 1 FOR DOSA')
        print('PRESS 2 FOR ROTI')
        print('PRESS 3 FOR BIRIYANI')
        print('PRESS 4 FOR PALAV')
        print('PRESS 5 FOR IDLY')
        print('PRESS 6 FOR POORI')
        



