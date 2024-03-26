from Billclass import Bill
menu=[
    {'name':'POORI','price':35, 'code':6},
    {'name':'DOSA','price':45,'code':1},
    {'name':'ROTI','price':55, 'code':2},
    {'name':'BIRIYANI','price':135, 'code':3},
    {'name':'PALAV','price':65, 'code':4},
    {'name':'IDLY','price':30, 'code':5}
    ]


ob=Bill()
ob.display()
while True:
    n=int(input('\nCHOOSE YOUR ORDER:'))
    for i in menu:
        if i['code']==n:
            ob.setDetails(i)
            print(ob.quantity())
    else:
        if n==0:
            break
print('TOTAL BILL :-', ob.totalbill)
print('\nTHANK YOU')
print('VISIT AGAIN...','\U0001F607')
print()