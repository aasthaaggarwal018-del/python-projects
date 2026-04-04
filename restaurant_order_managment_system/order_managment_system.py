# creating a list of orders and dictionary of menu
order_list=[]
menu={
            'pizza':300,
            'burger':150,
            'pasta':200,
            'noddles':250,
            'cold drinks':50,
            'milkshakes':70
        }
print ('--welcome to our restaurant. we hope you like our services and food---' )

while True :
# collecting input to proceeds
    print('\n1. show menu \n2. add order \n3. view orders \n4.total bill amount' \
    '\n5. exit \n')

    choice = int(input('entre your choice here :'))
# shows menu
    if choice==1:
        print('\n---menu---')
        for i,j in menu.items-():
            print(f'{i}:{j}')
# add order
    elif choice==2:
        item = input('entre your item here:')
        if item in menu:
            quantity=int(input('entre no of quantity of order:'))
            price=menu[item]*quantity

            order={
                'item':item,
                'quantity':quantity,
                'price':price
            }
            order_list.append(order)
            print(f'\nyour total bill is {price}')
            print('\norder added successfully!')
        else:
            print('\nitem not available')
# presenting orders
    elif choice==3:
        if len(order_list)==0:
            print('no order yet')
        else:
            count=1
            for i in order_list:
                print(f'item : {i['item']}')
                print(f'quantity : {i['quantity']}')
                print(f'price : {i['price']}')
                count =+1
#calculating total bill
    elif choice==4:
        total_bill=0
        for i in order_list:
            total_bill=total_bill+i['price']
        print(f'\ntotal bill amount is {total_bill}')
# exit 
    elif choice==5:
        print('thanks for visit')
        break
# invalid option
    else:
        print('you entred something wrong')